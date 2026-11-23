"""台帳・索引・ページ検査で共通に使うもの（標準ライブラリのみ。Python 3.9 以上）。"""
import csv, re, subprocess, shutil, glob, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # 03_outputs/
LEDGER = ROOT / "ledger.csv"
INDEX = ROOT / "00_index.md"
COLS = ["id", "step", "group", "page_dir", "slug", "title", "minutes", "kind", "fetch", "url",
        "status", "memo", "slides", "learned_on", "note"]
STATUSES = ["未着手", "取得済", "作成中", "完了", "薄いページ", "重複", "失敗", "要確認"]
STEPS = {
    "0": ("step0_intro", "入口"),
    "1": ("step1_basics", "基礎（Claude 101）"),
    "2": ("step2_tools", "道具を整える"),
    "3": ("step3_roles", "職種で習熟"),
    "4": ("step4_advanced", "発展"),
    "9": ("step9_added", "追加（台帳の対象外で、URL を渡して作ったもの）"),
}


def read_ledger():
    with open(LEDGER, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        return list(rd.fieldnames or []), list(rd)


def write_ledger(rows):
    with open(LEDGER, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})


def body_of(md_path):
    """frontmatter を除いた本文。"""
    t = Path(md_path).read_text(encoding="utf-8")
    if t.startswith("---"):
        parts = t.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return t


def find_checker():
    """ced-craft-explanation-docs の check_docs.py の、いちばん新しい版を探す。"""
    c = sorted(glob.glob(str(Path.home() / ".claude/plugins/cache/ced-skills/ced-skills/*/ced-craft-explanation-docs/scripts/check_docs.py")))
    return c[-1] if c else None


def run_py(script, *args):
    """uv があれば Python 3.12、なければ python3 で script を動かす。"""
    base = ["uv", "run", "--python", "3.12"] if shutil.which("uv") else ["python3"]
    return subprocess.run(base + [str(script)] + [str(a) for a in args],
                          capture_output=True, text=True)


def find_ced(name):
    """ced-url-to-md の scripts/<name>（いちばん新しい版）。"""
    c = sorted(glob.glob(str(Path.home() / f".claude/plugins/cache/ced-skills/ced-skills/*/ced-url-to-md/scripts/{name}")))
    return c[-1] if c else None


def today():
    import datetime
    return datetime.date.today().isoformat()


_NAV = re.compile(r"^\s*(\*|-|\d+\.)?\s*\[[^\]]*\]\([^)]*\)\s*$")          # リンクだけの行（ナビ・一覧）
_NOISE = re.compile(r"^\s*(読み込み中|視聴|言語\s*日本語|!\[.*\]\(.*\)|\s*)$")


def body_text_chars(md_path):
    """本文の字数（空白除く）。ナビ・リンクだけの行・画像・フッターを除く。

    薄いページの判定（P-2）に使う。『© 』の行より後ろは、フッターとして数えない。
    """
    lines = body_of(md_path).split("\n")
    # Academy の共通ナビ（「AIについて学ぶ」などの見出しから、フッターまで）は本文ではない
    nav_heads = ("## AIについて学ぶ", "## 対象者別", "## 種類別", "## 製品別", "## ヘルプとドキュメント")
    kept = []
    skip = False
    for ln in lines:
        if ln.strip() in nav_heads:
            skip = True
        if ln.lstrip().startswith("©"):
            skip = False
            break
        if skip:
            continue
        if _NAV.match(ln) or _NOISE.match(ln):
            continue
        kept.append(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", ln))   # 本文中のリンクは文字だけ残す
    return len(re.sub(r"\s", "", "\n".join(kept)))
