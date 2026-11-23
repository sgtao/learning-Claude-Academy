#!/usr/bin/env python3
"""URL 1 件を、取得から台帳の追加まで行う（合格条件 10 の前半）。

使い方:
  python3 tools/add_page.py <URL> [--step 9] [--group 01_added] [--kind 技術・ハウツー|学習・ビジネス] [--minutes 10]

やること（順に。失敗したら止まって理由を出す）:
  1. URL が academy.claude.com の日本語版（/ja/）か確かめる。英語版しかないときは止まる（人が決める）
  2. 同じ URL が台帳に無いか確かめる（あれば止まる。重複は人が決める）
  3. fetch_convert.py で原本を取る → 00_originals/<slug>.md。add_frontmatter.py で frontmatter を付ける
  4. 本文の字数を数える。300 字未満なら「薄いページ」。README だけ置く（tools/page_readme.py）
  5. 台帳に 1 行足す（状態は 取得済 か 薄いページ）。ledger.py refresh で検査し直す準備はここまで
解説メモとスライドは、このあと人（または Claude）が ced-craft-explanation-docs と ced-websearch-slide-ja で作る。
その後は `python3 tools/ledger.py refresh && python3 tools/build_index.py && python3 tools/check_index.py`。
終了コード: 0＝取得して台帳に入った（薄いページを含む） / 1＝止まった（理由を表示） / 2＝引数の誤り
"""
import re, subprocess, sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, LEDGER, STEPS, read_ledger, write_ledger, body_text_chars, find_ced, today
from page_readme import render

JA = re.compile(r"^https://academy\.claude\.com/ja/(courses|tutorials|use-cases)/([^/?#]+)$")


def stop(msg, code=1):
    print(f"[stop] {msg}")
    sys.exit(code)


def run(args):
    return subprocess.run(args, capture_output=True, text=True)


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        print(__doc__); sys.exit(2)
    url = a[0]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    step = opt("--step", "9"); group = opt("--group", "01_added")
    kind = opt("--kind", "学習・ビジネス"); minutes = opt("--minutes", "")
    if step not in STEPS:
        stop(f"ステップ {step} は無い", 2)
    m = JA.match(url)
    if not m:
        stop("対象外の URL の形。受け付けるのは https://academy.claude.com/ja/courses/<コース>・/ja/tutorials/<slug>・/ja/use-cases/<slug> の 1 段の slug だけ（レッスン・英語版・他のホストは人が決める）", 2)
    kindpath, slug = m.group(1), m.group(2)
    _, rows = read_ledger()
    if any(url == r.get("url") for r in rows):
        stop("この URL は台帳に既にある（重複は人が決める）")
    fetch = find_ced("fetch_convert.py"); addfm = find_ced("add_frontmatter.py")
    if not fetch or not addfm:
        stop("ced-url-to-md のスクリプトが見つからない（~/.claude/plugins/cache/ced-skills/）", 1)
    n = len(rows)
    base = ROOT / STEPS[step][0] / group
    base.mkdir(parents=True, exist_ok=True)
    existing = sorted(p.name for p in base.glob("*/"))
    idx = len(existing) + 1
    folder = base / f"{idx:02d}_{slug}"
    (folder / "00_originals").mkdir(parents=True, exist_ok=True)
    orig = folder / "00_originals" / f"{slug}.md"
    raw = folder / "00_originals" / f".{slug}.body.md"
    r = run(["uv", "run", "--python", "3.12", fetch, url, "-o", str(raw)])
    if r.returncode != 0 or not raw.exists():
        (folder / "README.md").write_text(f"# {slug}\n- 元ページ: {url}\n- 状態: 失敗\n- 理由: 取得できなかった（fetch_convert の出力: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else '不明'}）\n", encoding="utf-8")
        rows.append(_row(n, step, group, folder, slug, url, kind, minutes, "失敗", "取得できなかった"))
        write_ledger(rows)
        stop(f"取得に失敗。README と台帳（失敗）に記録した: {r.stderr.strip().splitlines()[-1:] or ['']}", 1)
    r2 = run(["uv", "run", "--python", "3.12", addfm, str(raw), "--url", url, "--format", "html", "--conversion", "direct", "-o", str(orig)])
    if r2.returncode != 0:
        stop("frontmatter を付けられなかった: " + r2.stderr.strip()[-200:])
    raw.unlink(missing_ok=True)
    chars = body_text_chars(orig)
    thin = chars < 300
    row = _row(n, step, group, folder, slug, url, kind, minutes, "薄いページ" if thin else "取得済",
               f"本文 {chars} 字（{'薄いページ。解説は作らない' if thin else '解説メモとスライドは未作成'}）")
    rows.append(row)
    write_ledger(rows)
    (folder / "README.md").write_text(render(row, folder, "thin" if thin else "pending", f"本文 {chars} 字"), encoding="utf-8")
    print(json.dumps({"id": row["id"], "folder": str(folder.relative_to(ROOT)), "chars": chars,
                      "status": row["status"]}, ensure_ascii=False))
    print("次: " + ("（薄いページのため、ここで終わり）" if thin else "ced-craft-explanation-docs で解説メモ、ced-websearch-slide-ja でスライドを作り、ledger.py refresh"))
    sys.exit(0)


def _row(n, step, group, folder, slug, url, kind, minutes, status, note):
    return {"id": f"{step}-add-{n + 1:03d}", "step": step, "group": group,
            "page_dir": folder.relative_to(ROOT).as_posix(), "slug": slug, "title": slug,
            "minutes": minutes, "kind": kind, "fetch": "A", "url": url, "status": status,
            "memo": "", "slides": "", "learned_on": "", "note": note}


if __name__ == "__main__":
    main()
