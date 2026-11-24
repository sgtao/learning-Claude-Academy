#!/usr/bin/env python3
"""フォルダの中の Markdown の相対リンクが、存在するファイルを指すかを確かめる（合格条件 5）。

使い方:  python3 tools/check_links.py [<フォルダ。既定は 03_outputs 全体>]
終了コード: 0＝切れ 0 件 / 1＝あり
http・mailto・claude:// などのスキーム付きと、ページ内の # は対象外。.work/（中間ファイルと working-log.md）・out/・node_modules/・.vitepress/ の中は見ない。
"""
import re, sys
from pathlib import Path

LINK = re.compile(r"\]\((?![a-zA-Z][a-zA-Z0-9+.-]*:|#)([^)\s]+)\)")


def broken_links(root):
    bad = []
    for f in sorted(Path(root).rglob("*.md")):
        parts = f.as_posix()
        if any(x in parts for x in ("/out/", "/.work/", "/.git/", "/node_modules/", "/.vitepress/")):
            continue
        in_code = False
        for ln, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            for m in LINK.finditer(line):
                p = m.group(1).split("#")[0]
                if p and not (f.parent / p).resolve().exists():
                    bad.append((f, ln, m.group(1)))
    return bad


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    bad = broken_links(root)
    for f, ln, t in bad:
        print(f"BROKEN: {f}:{ln} -> {t}")
    print(f"broken links: {len(bad)}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
