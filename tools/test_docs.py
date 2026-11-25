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


# 冒頭の戻るリンク（全ページのファイルで同じ規則）
#   toTopPage＝1 つ上のフォルダの README（ページのフォルダから見て ../README.md）
#   toREADME ＝そのファイルと同じフォルダの README（README 自身も ./README.md）
# 作業ログ（.work/working-log.md）は .work/ の中にあるので、ページのフォルダ（../README.md）と 1 つ上（../../README.md）を指す。
NAV_HEAD = re.compile(r"\A###### \[toTopPage\]\(([^)]*)\)\n###### \[toREADME\]\(([^)]*)\)")


def expected_nav(rel):
    parts = rel.parts
    if len(parts) == 5 and parts[3] == ".work" and parts[4] == "working-log.md":
        return ("../../README.md", "../README.md")
    if parts[0].startswith("step") and len(parts) in (2, 3, 4):     # step / まとまり / ページ（と、その中のファイル）
        return ("../README.md", "./README.md")
    return None


class NavLinkTests(unittest.TestCase):
    def test_every_nav_header_follows_the_rule(self):
        bad, seen = [], 0
        for p in sorted(ROOT.rglob("*.md")):
            rel = p.relative_to(ROOT)
            if any(x in rel.parts for x in ("node_modules", ".git", ".vitepress", "aborted")):
                continue
            head = NAV_HEAD.match(p.read_text(encoding="utf-8"))
            if not head:
                continue
            seen += 1
            want = expected_nav(rel)
            if want is None or (head.group(1), head.group(2)) != want:
                bad.append(f"{rel}: {head.group(1)} / {head.group(2)} （期待 {want}）")
        self.assertGreater(seen, 400, "戻るリンクの見つかった数が少なすぎる（検査の対象を取れていない）")
        self.assertEqual(bad, [], "\n".join(bad[:20]) + (f"\n...ほか {len(bad) - 20} 件" if len(bad) > 20 else ""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
