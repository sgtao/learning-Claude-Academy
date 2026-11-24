#!/usr/bin/env python3
"""README のコマンド例が、そのまま貼り付けて動くかの検査（標準ライブラリのみ）。

zsh は、対話シェルでは `#` をコメントとして扱わないことがある。`npm run docs:dev  # 説明` を貼ると、`#` 以降が
引数になり、VitePress が「プロジェクトのルートが # というフォルダ」と解釈して、ページが表示されない（実際に起きた）。
そこで、(1) コード例の行末にコメントを付けない（コメントは別の行に書く）、(2) npm スクリプトはルート（.）を明示する。

使い方:  python3 tools/test_docs.py
"""
import json, re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ["README.md", "tools/README.md"]
TRAIL = re.compile(r"\s#\s")


def code_lines(text):
    inb = False
    for n, ln in enumerate(text.split("\n"), 1):
        if ln.startswith("```"):
            inb = not inb
            continue
        if inb:
            yield n, ln


class DocsTests(unittest.TestCase):
    def test_no_trailing_comments_in_command_blocks(self):
        for d in DOCS:
            text = (ROOT / d).read_text(encoding="utf-8")
            for n, ln in code_lines(text):
                if ln.lstrip().startswith("#") or "'" in ln or '"' in ln:
                    continue                                   # コメントだけの行・引用符を含む行（# が文字列かもしれない）は見ない
                self.assertIsNone(TRAIL.search(ln), f"{d}:{n} 行末にコメントがある（別の行に書く）: {ln}")

    def test_no_leading_spaces_in_command_blocks(self):
        for d in DOCS:
            for n, ln in code_lines((ROOT / d).read_text(encoding="utf-8")):
                if re.match(r"^ +(npm|python3|bash|gh|git) ", ln):
                    self.fail(f"{d}:{n} コマンドの行頭に空白がある: {ln!r}")

    def test_npm_scripts_name_the_root_explicitly(self):
        scripts = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))["scripts"]
        for k, v in scripts.items():
            if v.startswith("vitepress "):
                self.assertTrue(v.endswith(" ."), f"{k}: {v!r}（余計な引数がルートと解釈されないよう、末尾に . を付ける）")


if __name__ == "__main__":
    unittest.main(verbosity=2)
