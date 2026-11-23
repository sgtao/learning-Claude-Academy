#!/usr/bin/env python3
"""スライド MD の数字が、原本か解説メモにあるかを確かめる（無い数字を表示。合格条件 4）。

使い方:  python3 tools/check_numbers.py <ページのフォルダ> [--slide <別のスライド MD>]
終了コード: 0＝出典の無い数字 0 件 / 1＝あり / 2＝入力の誤り
URL の中の数字と、解説メモの参照番号（out/03、「03」「06 総括」のような、0 から始まる 2 桁）は数えない。
"""
import re, sys
from pathlib import Path


def missing_numbers(page, slide_text=None):
    page = Path(page)
    orig = sorted((page / "00_originals").glob("*.md"))
    expl = sorted(page.glob("*_explained"))
    slides = sorted(page.glob("*-explained-slides.md"))
    if not orig or not slides:
        raise FileNotFoundError("00_originals/*.md か *-explained-slides.md が無い")
    src = "".join(p.read_text(encoding="utf-8") for p in orig)
    for e in expl:
        src += "".join(p.read_text(encoding="utf-8") for p in e.glob("*.md"))
    text = slide_text if slide_text is not None else slides[0].read_text(encoding="utf-8")
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\bout/\d+\b", "", text)
    nums = sorted(set(n for n in re.findall(r"\d[\d,\.]*\d|\d", text) if not re.fullmatch(r"0\d", n)))
    return nums, [n for n in nums if n not in src]


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    text = None
    if "--slide" in args:
        i = args.index("--slide"); text = Path(args[i + 1]).read_text(encoding="utf-8")
    try:
        nums, miss = missing_numbers(args[0], text)
    except FileNotFoundError as e:
        print("入力の誤り:", e); sys.exit(2)
    print(f"slide numbers: {len(nums)} | not in source/memo: {miss}")
    sys.exit(1 if miss else 0)


if __name__ == "__main__":
    main()
