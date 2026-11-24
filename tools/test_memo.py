#!/usr/bin/env python3
"""memo.py の検査。見本の木（一時フォルダ）で動きと失敗系を確かめ、最後に実物の木も通す。

使い方:  python3 tools/test_memo.py            （標準ライブラリの unittest）
"""
import io, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import memo

REAL_ROOT = Path(__file__).resolve().parent.parent


def w(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_tree(root):
    """見本の木。alpha=完全／beta=out が無い／gamma=解説メモが無い／.work=無視される。"""
    g = root / "step1_basics" / "01_grpA"
    # alpha: すべてそろっている
    a = g / "07_alpha"
    w(a / "README.md", "PAGE-README-ALPHA")
    w(a / "alpha_explained/README.md",
      "###### [toTopPage](./README.md)\n# 資料：アルファ題\n- `title`: アルファ題\n- `url`: https://example.com/alpha\n"
      "- `retrieved_at`: 2026-11-15\n\n-----\n## 概要\nEXPLAINED-README-ALPHA\n")
    w(a / "alpha_explained/01_source.md", "SOURCE-ALPHA")
    w(a / "alpha_explained/12_LLM_prompts_as_guide.md", "PROMPT-ALPHA")
    w(a / "alpha_explained/out/09_input-memo.md", "INPUTMEMO-ALPHA")
    # beta: out/09 が無い（12 はある）
    b = g / "08_beta"
    w(b / "README.md", "PAGE-README-BETA")
    w(b / "beta_explained/README.md", "# 資料：ベータ題\n- `title`: ベータ題\n- `url`: https://example.com/beta\n\n-----\nEXPLAINED-README-BETA\n")
    w(b / "beta_explained/01_source.md", "SOURCE-BETA")
    w(b / "beta_explained/12_LLM_prompts_as_guide.md", "PROMPT-BETA")
    # gamma: 解説メモなし（薄いページ）。原本だけ
    c = g / "09_gamma"
    w(c / "README.md", "# 1-9 ガンマ\nPAGE-README-GAMMA")
    w(c / "00_originals/gamma.md", "---\ntitle: ガンマ題\nsource_url: \"https://example.com/gamma\"\nretrieved_at: 2026-11-24\n---\nORIGINAL-GAMMA\n")
    w(c / "00_originals/gamma.raw.txt", "RAW-GAMMA")
    # 別ステップに同じ slug（曖昧さの検査用）
    d = root / "step2_tools" / "01_grpB" / "01_alpha"
    w(d / "README.md", "PAGE-README-ALPHA2")
    w(d / "alpha_explained/README.md", "# 資料：別のアルファ\n- `title`: 別のアルファ\n\n-----\n")
    w(d / "alpha_explained/01_source.md", "SOURCE-ALPHA2")
    # フロントマターが無いページ（重複ページなど）
    w(root / "step2_tools/01_grpB/02_nofm/README.md", "# 2-2 plain page\nPAGE-README-NOFM")
    # 無視される場所
    w(root / "step9_added/01_added/01_x/.work/aborted/x_explained/README.md", "HIDDEN")
    w(root / "step9_added/01_added/01_x/README.md", "PAGE-README-X")
    w(root / "step9_added/01_added/.work/tmp/README.md", "HIDDEN2")           # まとまりの階層の隠しフォルダ
    w(root / "step9_added/.cache/g/p/README.md", "HIDDEN3")                   # ステップの階層の隠しフォルダ
    # ledger（ID と状態）
    w(root / "ledger.csv",
      "id,step,group,page_dir,slug,title,minutes,kind,fetch,url,status,memo,slides,learned_on,note\n"
      "1-7,1,01_grpA,step1_basics/01_grpA/07_alpha,alpha,アルファ(台帳),15,k,A,u,完了,,,,\n"
      "1-8,1,01_grpA,step1_basics/01_grpA/08_beta,beta,ベータ(台帳),15,k,A,u,完了,,,,\n"
      "1-9,1,01_grpA,step1_basics/01_grpA/09_gamma,gamma,ガンマ(台帳),15,k,A,u,薄いページ,,,,\n"
      "2-1,2,01_grpB,step2_tools/01_grpB/01_alpha,alpha,アルファ2(台帳),15,k,A,u,完了,,,,\n")


def run(root, *argv):
    out, err = io.StringIO(), io.StringIO()
    code = memo.main(list(argv), root=root, out=out, err=err)
    return code, out.getvalue(), err.getvalue()


class FixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._td = tempfile.TemporaryDirectory()
        cls.root = Path(cls._td.name)
        make_tree(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    # --- 1. step ごとのまとまり一覧
    def test_groups_all_steps(self):
        code, out, _ = run(self.root, "groups")
        self.assertEqual(code, 0)
        for s in ("step1_basics", "step2_tools", "step9_added", "01_grpA", "01_grpB", "01_added"):
            self.assertIn(s, out)

    def test_groups_shows_names_only(self):
        code, out, _ = run(self.root, "groups")
        self.assertEqual(out.split("\n")[:-1],
                         ["step1_basics", "  01_grpA", "step2_tools", "  01_grpB", "step9_added", "  01_added"])

    def test_groups_one_step_only(self):
        code, out, _ = run(self.root, "groups", "1")
        self.assertEqual(code, 0)
        self.assertIn("01_grpA", out)
        self.assertNotIn("01_grpB", out)

    def test_groups_unknown_step_fails(self):
        code, _, err = run(self.root, "groups", "77")
        self.assertEqual(code, 2)
        self.assertIn("not found", err)

    # --- 2. まとまり配下のメモ一覧
    def test_pages_lists_all_pages_of_group(self):
        code, out, _ = run(self.root, "pages", "1", "01")
        self.assertEqual(code, 0)
        for s in ("07_alpha", "08_beta", "09_gamma", "1-7", "1-9"):
            self.assertIn(s, out)
        self.assertNotIn("01_alpha", out)           # 別ステップのページは出ない

    def test_pages_all(self):
        code, out, _ = run(self.root, "pages", "-a")
        self.assertEqual(code, 0)
        for s in ("# step1_basics / 01_grpA (3 pages)", "# step2_tools / 01_grpB", "# step9_added / 01_added",
                  "07_alpha", "09_gamma", "01_alpha", "02_nofm", "01_x"):
            self.assertIn(s, out)
        self.assertNotIn("aborted", out)
        self.assertNotIn(".work", out)
        # 数え合わせ：ページの行の数が scan の件数と一致
        rows = [l for l in out.split("\n") if "\t" in l and not l.startswith("id\t")]
        self.assertEqual(len(rows), len(memo.scan(self.root)))

    def test_pages_all_one_step(self):
        code, out, _ = run(self.root, "pages", "-a", "1")
        self.assertEqual(code, 0)
        self.assertIn("07_alpha", out)
        self.assertNotIn("step2_tools", out)

    def test_pages_all_long_option_and_bad_args(self):
        self.assertEqual(run(self.root, "pages", "--all")[0], 0)
        code, _, err = run(self.root, "pages", "-a", "1", "01")
        self.assertEqual(code, 2)
        code, _, err = run(self.root, "pages")
        self.assertEqual(code, 2)
        self.assertIn("-a", err)

    def test_pages_hides_work_dirs(self):
        code, out, _ = run(self.root, "pages", "9", "01_added")
        self.assertEqual(code, 0)
        self.assertIn("01_x", out)
        self.assertNotIn("aborted", out)
        self.assertNotIn("HIDDEN", out)
        self.assertNotIn(".work", out)
        code, out, _ = run(self.root, "groups", "9")
        self.assertNotIn(".cache", out)
        self.assertNotIn(".work", out)

    def test_pages_group_unknown_fails(self):
        code, _, err = run(self.root, "pages", "1", "nothing")
        self.assertEqual(code, 2)

    # --- 3. メモの情報（README のフロントマター）
    def test_info_prints_frontmatter_and_title(self):
        code, out, _ = run(self.root, "info", "1-7")
        self.assertEqual(code, 0)
        self.assertIn("step1_basics_01_grpA_アルファ題", out)
        self.assertIn("title: アルファ題", out)
        self.assertIn("url: https://example.com/alpha", out)
        self.assertIn("retrieved_at: 2026-11-15", out)
        self.assertNotIn("EXPLAINED-README-ALPHA", out)   # 本文は出さない

    def test_info_falls_back_to_originals_yaml_frontmatter(self):
        code, out, _ = run(self.root, "info", "1-9")
        self.assertEqual(code, 0)
        self.assertIn("step1_basics_01_grpA_ガンマ題", out)
        self.assertIn("source_url: https://example.com/gamma", out)
        self.assertNotIn("ORIGINAL-GAMMA", out)

    def test_info_without_frontmatter(self):
        code, out, _ = run(self.root, "info", "02_nofm")
        self.assertEqual(code, 0)
        self.assertIn("(no frontmatter)", out)
        self.assertIn("frontmatter_from: (none)", out)

    def test_info_json(self):
        import json
        code, out, _ = run(self.root, "info", "1-7", "--json")
        self.assertEqual(code, 0)
        d = json.loads(out)
        self.assertEqual(d["title"], "step1_basics_01_grpA_アルファ題")
        self.assertEqual(d["frontmatter"]["url"], "https://example.com/alpha")
        self.assertEqual(d["id"], "1-7")

    # --- 4. 本文の表示
    def test_show_full_set(self):
        code, out, _ = run(self.root, "show", "1-7")
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("# step1_basics_01_grpA_アルファ題"))
        for s in ("EXPLAINED-README-ALPHA", "INPUTMEMO-ALPHA", "PROMPT-ALPHA"):
            self.assertIn(s, out)
        self.assertNotIn("SOURCE-ALPHA", out)              # 01_source は出さない
        self.assertLess(out.index("EXPLAINED-README-ALPHA"), out.index("INPUTMEMO-ALPHA"))
        self.assertLess(out.index("INPUTMEMO-ALPHA"), out.index("PROMPT-ALPHA"))

    def test_show_falls_back_when_out_missing(self):
        code, out, _ = run(self.root, "show", "1-8")
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("# step1_basics_01_grpA_ベータ題"))
        self.assertIn("EXPLAINED-README-BETA", out)
        self.assertIn("SOURCE-BETA", out)
        self.assertNotIn("PROMPT-BETA", out)               # 12 があっても、out が無ければ代替の形
        self.assertIn("out/09_input-memo.md not created", out)   # 無いものを注記する

    def test_show_page_without_explained_dir(self):
        code, out, _ = run(self.root, "show", "1-9")
        self.assertEqual(code, 0)
        self.assertIn("PAGE-README-GAMMA", out)
        self.assertIn("ORIGINAL-GAMMA", out)               # 01_source の代わりに原本
        self.assertNotIn("RAW-GAMMA", out)
        self.assertIn("no explanation memo", out)

    def test_show_only_option(self):
        code, out, _ = run(self.root, "show", "1-7", "--only", "prompt")
        self.assertEqual(code, 0)
        self.assertIn("PROMPT-ALPHA", out)
        self.assertNotIn("INPUTMEMO-ALPHA", out)

    # --- ページの指定のしかた
    def test_resolve_by_id_dir_name_slug_and_path(self):
        for q in ("1-7", "07_alpha", "step1_basics/01_grpA/07_alpha", "step1_basics/01_grpA/07_alpha/README.md",
                  "08_beta"):
            code, out, err = run(self.root, "info", q)
            self.assertEqual(code, 0, (q, err))

    def test_resolve_unique_substring(self):
        code, out, _ = run(self.root, "info", "gamma")
        self.assertEqual(code, 0)
        self.assertIn("ガンマ題", out)

    def test_ambiguous_query_fails_and_lists_candidates(self):
        code, out, err = run(self.root, "show", "alpha")
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("step1_basics/01_grpA/07_alpha", err)
        self.assertIn("step2_tools/01_grpB/01_alpha", err)

    def test_unknown_page_fails(self):
        code, out, err = run(self.root, "show", "9-99")
        self.assertEqual(code, 2)
        self.assertIn("not found", err)

    def test_no_command_fails(self):
        code, _, _ = run(self.root)
        self.assertEqual(code, 2)


class AsciiOutputTests(unittest.TestCase):
    """ツール自身の文言（見出し・ラベル・注記・エラー）は ASCII。本文・題名・台帳の値は日本語のまま出る。"""

    @classmethod
    def setUpClass(cls):
        cls._td = tempfile.TemporaryDirectory()
        cls.root = Path(cls._td.name)
        make_tree(cls.root)
        # 日本語の題名・状態・本文を、ASCII の枠だけ残して消した出力にして比べる
        cls.jp = ["アルファ題", "ベータ題", "ガンマ題", "別のアルファ", "完了", "薄いページ",
                  "アルファ(台帳)", "ベータ(台帳)", "ガンマ(台帳)", "アルファ2(台帳)", "資料", "概要"]

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def frame(self, text):
        import re
        for j in self.jp:
            text = text.replace(j, "")
        return text

    def test_frames_are_ascii(self):
        cases = [("groups",), ("groups", "1"), ("pages", "1", "01"), ("info", "1-7"), ("info", "1-9"),
                 ("show", "1-7"), ("show", "1-8"), ("show", "1-9"), ("show", "1-7", "--only", "source"),
                 ("info", "02_nofm"), ("show", "02_nofm")]
        for argv in cases:
            code, out, err = run(self.root, *argv)
            self.assertEqual(code, 0, argv)
            for line in self.tool_lines(out):
                f = self.frame(line)
                self.assertTrue(f.isascii(), (argv, line))

    @staticmethod
    def tool_lines(out):
        """ツールが書いた行だけ。show の各区間は、最初の『(パス)』の行までがツールの行で、その後ろはファイルの内容。"""
        lines = []
        for i, part in enumerate(out.split("\n---\n")):
            for ln in part.split("\n"):
                lines.append(ln)
                if i > 0 and ln.startswith("(") and ln.endswith(")"):
                    break
        return lines

    def test_errors_are_ascii(self):
        for argv in (("show", "alpha"), ("show", "9-99"), ("groups", "77"), ("pages", "1", "nothing")):
            code, out, err = run(self.root, *argv)
            self.assertEqual(code, 2)
            self.assertTrue(self.frame(err.replace("\n", " ")).isascii(), (argv, err))


class RealTreeTests(unittest.TestCase):
    """実物の木：すべてのページが、見つかり・表示でき・題名が付く。"""

    @unittest.skipUnless((REAL_ROOT / "ledger.csv").exists(), "実物の木が無い")
    def test_every_real_page_shows(self):
        pages = memo.scan(REAL_ROOT)
        self.assertGreaterEqual(len(pages), 70)
        for p in pages:
            code, out, err = run(REAL_ROOT, "show", p["rel"])
            self.assertEqual(code, 0, (p["rel"], err))
            self.assertTrue(out.startswith(f"# {p['step']}_{p['group']}_"), p["rel"])
            self.assertGreater(len(out), 200, p["rel"])
            code, out, err = run(REAL_ROOT, "info", p["rel"])
            self.assertEqual(code, 0, (p["rel"], err))

    @unittest.skipUnless((REAL_ROOT / "ledger.csv").exists(), "実物の木が無い")
    def test_every_ledger_page_with_dir_is_scanned(self):
        rels = {p["rel"] for p in memo.scan(REAL_ROOT)}
        _, rows = memo.common.read_ledger()
        for r in rows:
            if (REAL_ROOT / r["page_dir"]).is_dir():
                self.assertIn(r["page_dir"], rels)


if __name__ == "__main__":
    unittest.main(verbosity=2)
