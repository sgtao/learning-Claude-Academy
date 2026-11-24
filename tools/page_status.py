#!/usr/bin/env python3
"""1 ページ分の検査結果をまとめて返す（台帳の memo・slides・状態を決めるのに使う）。

使い方:  python3 tools/page_status.py <ページのフォルダ>      （JSON を表示）
見るもの: 解説メモ（check_docs の PASS 数。直下の 5 本を --out-dir .work/intermediate で検査）／スライド（docs/）（mdss-convert の枚数と lint）／
          数字の照合／リンク／原本の本文の長さ（300 字未満なら thin）
"""
import json, re, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import body_text_chars, find_checker, run_py, has_memo, intermediate_dir, slide_mds, slide_htmls
from check_numbers import missing_numbers
from check_links import broken_links


def page_status(page):
    page = Path(page)
    s = {"page": str(page), "has_dir": page.is_dir()}
    if not page.is_dir():
        return s
    orig = sorted((page / "00_originals").glob("*.md"))
    s["has_original"] = bool(orig)
    s["thin"] = bool(orig) and body_text_chars(orig[0]) < 300
    s["body_chars"] = body_text_chars(orig[0]) if orig else None
    s["memo"] = ""
    if has_memo(page):                       # 解説メモ 5 本はページのフォルダの直下。中間ファイルは .work/intermediate/
        chk = find_checker()
        if chk:
            r = run_py(chk, page, "--out-dir", intermediate_dir(page))
            m = re.search(r"結果: (\d+) PASS / (\d+) FAIL", r.stdout)
            s["memo"] = f"{m.group(1)} PASS" + (f"／{m.group(2)} FAIL" if m and m.group(2) != "0" else "") if m else "検査不能"
        else:
            s["memo"] = "未実施（check_docs が無い）"
    slides = slide_mds(page)                 # スライドは docs/
    s["slides"] = ""
    s["html"] = bool(slide_htmls(page))
    if slides:
        if shutil.which("mdss-convert"):
            r = subprocess.run(["mdss-convert", str(slides[0]), "--json-only", "--quiet"], capture_output=True, text=True)
            try:
                j = json.loads(r.stdout)
                s["slides"] = f"{j['slideCount']} 枚／lint {len(j.get('lint', []))}"
                s["lint"] = len(j.get("lint", []))
            except Exception:
                s["slides"] = "検査不能"
        else:
            s["slides"] = "未実施（mdss-convert が無い）"
    try:
        _, miss = missing_numbers(page)
        s["numbers_missing"] = miss
    except FileNotFoundError:
        s["numbers_missing"] = None
    s["links_broken"] = len(broken_links(page))
    return s


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    print(json.dumps(page_status(sys.argv[1]), ensure_ascii=False, indent=1))
