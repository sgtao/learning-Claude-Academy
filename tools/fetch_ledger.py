#!/usr/bin/env python3
"""台帳にある ID のページを取得し、薄い判定と README を作る（既に台帳に行があるページ用）。

使い方:  python3 tools/fetch_ledger.py <ID> [--url <別の URL>]
add_page.py は「台帳に無い URL」を足す。こちらは「台帳に既にある行」の原本を取る（取得から状態の更新まで）。
状態: 取得して本文 300 字以上 → 取得済（解説は別に作る）／300 字未満 → 薄いページ／取得できない → 失敗（--force は使わない）
終了コード: 0＝取得して記録／1＝取得できない（失敗として記録）／2＝引数の誤り
"""
import re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, read_ledger, write_ledger, body_text_chars, find_ced, today
from page_readme import render


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    rid = a[0]
    url_override = a[a.index("--url") + 1] if "--url" in a else None
    cols, rows = read_ledger()
    hit = [r for r in rows if r["id"] == rid]
    if not hit:
        print("その ID は台帳にありません"); sys.exit(2)
    r = hit[0]
    page = ROOT / r["page_dir"]
    url = url_override or r["url"]
    slug = r["slug"]
    (page / "00_originals").mkdir(parents=True, exist_ok=True)
    raw = page / "00_originals" / f".{slug}.body.md"
    orig = page / "00_originals" / f"{slug}.md"
    fetch = find_ced("fetch_convert.py"); addfm = find_ced("add_frontmatter.py")
    f = subprocess.run(["uv", "run", "--python", "3.12", fetch, url, "-o", str(raw)], capture_output=True, text=True)
    if f.returncode != 0 or not raw.exists():
        last = (f.stderr.strip().splitlines() or ["?"])[-1]
        r["status"] = "失敗"; r["note"] = f"取得できない: {last[:120]}"
        (page / "README.md").write_text(render(r, page, "failed", last), encoding="utf-8")
        write_ledger(rows)
        print(f"[stop] {last}"); sys.exit(1)
    fm = "html" if "--format-html" in a or True else "html"
    g = subprocess.run(["uv", "run", "--python", "3.12", addfm, str(raw), "--url", url, "--format", "html", "--conversion", "direct", "-o", str(orig)], capture_output=True, text=True)
    raw.unlink(missing_ok=True)
    if g.returncode != 0:
        print("[stop] frontmatter: " + g.stderr.strip()[-200:]); sys.exit(1)
    chars = body_text_chars(orig)
    thin = chars < 300
    r["status"] = "薄いページ" if thin else "取得済"
    r["note"] = f"本文 {chars} 字（{'薄いページ。解説は作らない' if thin else '解説はこれから作る'}）"
    (page / "README.md").write_text(render(r, page, "thin" if thin else "pending", f"本文 {chars} 字"), encoding="utf-8")
    write_ledger(rows)
    print(f"{rid}\t{r['status']}\t本文 {chars} 字\t{page.relative_to(ROOT)}")
    sys.exit(0)


if __name__ == "__main__":
    main()
