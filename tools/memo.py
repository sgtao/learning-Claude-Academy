#!/usr/bin/env python3
"""解説メモを引くための参照ツール（読むだけ。何も書き換えない）。標準ライブラリのみ。Python 3.9 以上。

構造は、いつも「ステップ／まとまり／ページ」の 3 段:
  step1_basics/01_academy-courses-claude-101/07_working-with-skills/

使い方（リポジトリのトップ 03_outputs/ から）:
  python3 tools/memo.py groups [STEP]            ステップごとの「まとまり」の一覧（STEP を省くと全ステップ）
  python3 tools/memo.py pages [STEP] GROUP       まとまりの中のページ（解説メモ）の一覧
  python3 tools/memo.py pages -a [STEP]          全ページの一覧（STEP を付けるとそのステップだけ）
  python3 tools/memo.py info PAGE [--json]       解説メモの README のフロントマター（題名・URL・取得日など）
  python3 tools/memo.py show PAGE [--only ...]   README・out/09_input-memo.md・12_LLM_prompts_as_guide.md を表示
                                                 （out か 12 が無いページは README と 01_source を表示）

指定のしかた:
  STEP   1 / step1 / step1_basics / basics
  GROUP  01 / 01_academy-courses-claude-101 / claude-101（STEP の中、または STEP を省いて全体から探す）
  PAGE   台帳の ID（1-7）/ ページのフォルダ名（07_working-with-skills）/ slug（working-with-skills）/
         step1_basics/01_academy-courses-claude-101/07_working-with-skills / 題名や名前の一部（1 件に決まるとき）
         複数に当たるときは候補を出して終了コード 2 で止まる。

表示の題名は「<ステップ名>_<まとまり名>_<解説メモの題名>」。
終了コード: 0＝成功 / 2＝指定の誤り（見つからない・複数に当たる）
"""
import argparse, csv, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common

ROOT = common.ROOT
STEP_RE = re.compile(r"^step\d+_")
SKIP = {"tools", "catalog", "__pycache__"}
MEMO_REL = "out/09_input-memo.md"
PROMPT_NAME = "12_LLM_prompts_as_guide.md"
SECTION_KEYS = ("readme", "input", "prompt", "source")


class UserError(Exception):
    """指定の誤り（終了コード 2）。"""


# ---------------------------------------------------------------- 走査

def _dirs(p):
    return sorted(d for d in p.iterdir() if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP)


def _read_ledger(root):
    f = root / "ledger.csv"
    if not f.exists():
        return {}
    with open(f, encoding="utf-8", newline="") as fh:
        return {r["page_dir"]: r for r in csv.DictReader(fh)}


def scan(root=ROOT):
    """全ページ（ステップ／まとまり／ページの 3 段）を、並んだ順に返す。隠しフォルダ（.work など）は見ない。"""
    root = Path(root)
    ledger = _read_ledger(root)
    pages = []
    for sd in _dirs(root):
        if not STEP_RE.match(sd.name):
            continue
        for gd in _dirs(sd):
            for pd in _dirs(gd):
                rel = f"{sd.name}/{gd.name}/{pd.name}"
                ex = next((d for d in _dirs(pd) if d.name.endswith("_explained")), None)
                row = ledger.get(rel, {})
                pages.append({"step": sd.name, "group": gd.name, "name": pd.name, "rel": rel, "path": pd,
                              "explained": ex, "id": row.get("id", ""), "status": row.get("status", ""),
                              "ledger_title": row.get("title", "")})
    return pages


# ---------------------------------------------------------------- フロントマター・題名

_BULLET = re.compile(r"^-\s+`([^`]+)`:\s*(.*)$")
_YAML = re.compile(r"^([A-Za-z0-9_\-]+):\s*(.*)$")


def _unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def parse_frontmatter(text):
    """YAML 形式（--- で囲む）か、解説メモの README の形式（- `キー`: 値 が見出しの下に並ぶ）を読む。"""
    lines = text.split("\n")
    out = {}
    if lines and lines[0].strip() == "---":
        for ln in lines[1:]:
            if ln.strip() == "---":
                break
            m = _YAML.match(ln)
            if m:
                out[m.group(1)] = _unquote(m.group(2))
        return out
    for ln in lines:
        if ln.startswith("-----"):          # 区切り線から先は本文
            break
        m = _BULLET.match(ln)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def originals_md(page):
    d = page["path"] / "00_originals"
    if not d.is_dir():
        return None
    mds = sorted(p for p in d.glob("*.md") if not p.name.endswith(".raw.md"))
    return mds[0] if mds else None


def frontmatter_of(page):
    """(辞書, 読んだファイルの相対パス)。解説メモの README を先に、無ければ原本の frontmatter を読む。"""
    root_of = page["path"].parent.parent.parent
    cands = []
    if page["explained"] is not None:
        cands.append(page["explained"] / "README.md")
    o = originals_md(page)
    if o is not None:
        cands.append(o)
    for f in cands:
        if f.is_file():
            fm = parse_frontmatter(f.read_text(encoding="utf-8"))
            if fm:
                return fm, str(f.relative_to(root_of))
    return {}, None


def _h1(path):
    if path.is_file():
        for ln in path.read_text(encoding="utf-8").split("\n"):
            if ln.startswith("# "):
                return ln[2:].strip()
    return ""


def memo_title(page, fm=None):
    fm = frontmatter_of(page)[0] if fm is None else fm
    t = fm.get("title") or page["ledger_title"] or _h1(page["path"] / "README.md") or page["name"]
    return " ".join(t.split())


def full_title(page, fm=None):
    """<ステップ名>_<まとまり名>_<解説メモの題名>"""
    return f"{page['step']}_{page['group']}_{memo_title(page, fm)}"


# ---------------------------------------------------------------- 指定の解決

def _pick(tiers, label, q, show):
    for found in tiers:
        found = list(found)
        if len(found) == 1:
            return found[0]
        if len(found) > 1:
            lines = "\n".join("  " + show(x) for x in found)
            raise UserError(f"{label} '{q}' is ambiguous ({len(found)} matches). Be more specific:\n{lines}")
    raise UserError(f"{label} '{q}' not found")


def resolve_step(pages, q):
    names = sorted({p["step"] for p in pages})
    ql = q.strip().lower()
    tiers = [
        [n for n in names if n.lower() == ql or n.split("_")[0].lower() == ql or (ql.isdigit() and n.startswith(f"step{int(ql)}_"))],
        [n for n in names if ql in n.lower()],
    ]
    return _pick(tiers, "step", q, lambda x: x)


def resolve_group(pages, q, step=None):
    pairs = sorted({(p["step"], p["group"]) for p in pages if step is None or p["step"] == step})
    ql = q.strip().lower()
    tiers = [
        [x for x in pairs if x[1].lower() == ql],
        [x for x in pairs if ql.isdigit() and x[1].split("_")[0] == ql.zfill(2)],
        [x for x in pairs if ql in x[1].lower()],
    ]
    return _pick(tiers, "group", q, lambda x: f"{x[0]}/{x[1]}")


def _normalize_page_query(q):
    q = q.strip().replace("\\", "/")
    while q.startswith("./"):
        q = q[2:]
    q = q.replace("03_outputs/", "", 1) if q.startswith("03_outputs/") else q
    parts = [x for x in q.split("/") if x]
    if len(parts) >= 3 and STEP_RE.match(parts[0]):
        return "/".join(parts[:3])          # README.md や 01_source.md まで書いてあっても、ページに戻す
    return q.rstrip("/")


def resolve_page(pages, q):
    nq = _normalize_page_query(q)
    ql = nq.lower()
    titles = {p["rel"]: memo_title(p) for p in pages}

    def slug(p):
        return re.sub(r"^\d+_", "", p["name"]).lower()

    tiers = [
        [p for p in pages if p["id"] and p["id"].lower() == ql],
        [p for p in pages if p["rel"].lower() == ql],
        [p for p in pages if p["name"].lower() == ql or slug(p) == ql or p["rel"].lower().endswith("/" + ql)],
        [p for p in pages if ql in p["rel"].lower() or ql in titles[p["rel"]].lower() or ql in p["ledger_title"].lower()],
    ]
    return _pick(tiers, "page", q, lambda p: f"{p['rel']}  [{p['id'] or '-'}]  {titles[p['rel']]}")


# ---------------------------------------------------------------- 表示する中身

def show_plan(page):
    """(注記, [(キー, 表示名, ファイル)])。out/09 と 12 の両方があれば通常の 3 つ、無ければ README と 01_source。"""
    root_of = page["path"].parent.parent.parent
    ex = page["explained"]
    memo = ex / MEMO_REL if ex else None
    prompt = ex / PROMPT_NAME if ex else None
    if ex and memo.is_file() and prompt.is_file():
        return None, [("readme", "README.md", ex / "README.md"),
                      ("input", MEMO_REL, memo),
                      ("prompt", PROMPT_NAME, prompt)]
    if ex is None:
        note = "no explanation memo (thin / failed / duplicate page); showing the page README and the original"
        readme, source = page["path"] / "README.md", originals_md(page)
        source_label = "00_originals (original)"
    else:
        missing = [n for n, f in ((MEMO_REL, memo), (PROMPT_NAME, prompt)) if not f.is_file()]
        note = f"{' and '.join(missing)} not created; showing README and 01_source"
        readme, source = ex / "README.md", ex / "01_source.md"
        source_label = "01_source.md"
    plan = []
    if readme.is_file():
        plan.append(("readme", "README.md", readme))
    if source is not None and source.is_file():
        plan.append(("source", source_label, source))
    return note, plan


# ---------------------------------------------------------------- コマンド

def cmd_groups(pages, args, out):
    steps = [resolve_step(pages, args.step)] if args.step else sorted({p["step"] for p in pages})
    for s in steps:
        out.write(f"{s}\n")
        for g in sorted({p["group"] for p in pages if p["step"] == s}):
            out.write(f"  {g}\n")
    return 0


def _write_group_pages(gp, s, g, out):
    out.write(f"# {s} / {g} ({len(gp)} pages)\n\n")
    out.write("id\tpage\tmemo\tstatus\ttitle\n")
    for p in gp:
        has = "yes" if show_plan(p)[0] is None else ("partial" if p["explained"] else "no")
        out.write(f"{p['id'] or '-'}\t{p['name']}\t{has}\t{p['status'] or '-'}\t{memo_title(p)}\n")


def cmd_pages(pages, args, out):
    if args.all:
        # -a: every group (of one step, if STEP is given)
        if args.second:
            raise UserError("with -a give at most one argument (STEP)")
        step = resolve_step(pages, args.first) if args.first else None
        pairs = sorted({(p["step"], p["group"]) for p in pages if step is None or p["step"] == step})
        for n, (s, g) in enumerate(pairs):
            if n:
                out.write("\n")
            _write_group_pages([p for p in pages if p["step"] == s and p["group"] == g], s, g, out)
        return 0
    if not args.first:
        raise UserError("give [STEP] GROUP, or use -a to list all pages")
    step = resolve_step(pages, args.first) if args.second else None
    group_q = args.second or args.first
    s, g = resolve_group(pages, group_q, step)
    _write_group_pages([p for p in pages if p["step"] == s and p["group"] == g], s, g, out)
    return 0


def cmd_info(pages, args, out):
    p = resolve_page(pages, args.page)
    fm, src = frontmatter_of(p)
    title = full_title(p, fm)
    if args.json:
        out.write(json.dumps({"title": title, "id": p["id"], "status": p["status"], "page": p["rel"],
                              "frontmatter_from": src, "frontmatter": fm}, ensure_ascii=False, indent=2) + "\n")
        return 0
    out.write(f"# {title}\n\n")
    out.write(f"- page: {p['rel']}\n")
    out.write(f"- id: {p['id'] or '-'}\n- status: {p['status'] or '-'}\n")
    out.write(f"- frontmatter_from: {src or '(none)'}\n\n")
    for k, v in fm.items():
        out.write(f"{k}: {v}\n")
    if not fm:
        out.write("(no frontmatter)\n")
    return 0


def cmd_show(pages, args, out):
    p = resolve_page(pages, args.page)
    root_of = p["path"].parent.parent.parent
    note, plan = show_plan(p)
    if args.only:
        want = set(args.only)
        plan = [x for x in plan if x[0] in want]
    out.write(f"# {full_title(p)}\n\n")
    out.write(f"- path: {p['rel']}\n- id: {p['id'] or '-'}  status: {p['status'] or '-'}\n")
    if note:
        out.write(f"- note: {note}\n")
    if not plan:
        out.write("\n(nothing to show for this selection)\n")
    for i, (key, label, f) in enumerate(plan, 1):
        # 区切りは「[n/N]」付きにして、本文の中の見出し（## 概要 など）と見分けられるようにする
        out.write(f"\n---\n\n## [{i}/{len(plan)}] {label}\n\n({f.relative_to(root_of)})\n\n")
        out.write(f.read_text(encoding="utf-8").rstrip("\n") + "\n")
    return 0


def build_parser():
    ap = argparse.ArgumentParser(prog="memo.py", description="Look up explanation memos (read-only)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("groups", help="list groups per step")
    g.add_argument("step", nargs="?", help="step (omit for all steps)")
    pg = sub.add_parser("pages", help="list pages in a group")
    pg.add_argument("first", nargs="?", help="step (when two args are given) or group; with -a, the step")
    pg.add_argument("second", nargs="?", help="group")
    pg.add_argument("-a", "--all", action="store_true", help="list all pages (of one step if STEP is given)")
    i = sub.add_parser("info", help="show the README frontmatter")
    i.add_argument("page")
    i.add_argument("--json", action="store_true")
    s = sub.add_parser("show", help="show README, input memo and LLM prompt")
    s.add_argument("page")
    s.add_argument("--only", nargs="+", choices=SECTION_KEYS, help="parts to show")
    return ap


def main(argv=None, root=ROOT, out=None, err=None):
    out = out or sys.stdout
    err = err or sys.stderr
    try:
        args = build_parser().parse_args(argv)
    except SystemExit as e:
        return 2 if e.code else 0
    try:
        pages = scan(root)
        return {"groups": cmd_groups, "pages": cmd_pages, "info": cmd_info, "show": cmd_show}[args.cmd](pages, args, out)
    except UserError as e:
        err.write(f"error: {e}\n")
        return 2


if __name__ == "__main__":
    sys.exit(main())
