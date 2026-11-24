#!/usr/bin/env python3
"""構造の移行（.work/migrate-page-structure.sh）と、表紙・作業ログの更新（page_readme.py）の検査。

使い方:  python3 tools/test_structure.py        （標準ライブラリの unittest。bash が要る）
"""
import os, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page_readme

REAL_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REAL_ROOT / ".work" / "migrate-page-structure.sh"
SEP = "-----\n[toTop](#totoppage)"


def w(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def old_page(root, name="07_alpha", slug="alpha"):
    """旧構造のページ。ページ README／<slug>_explained/（5 本と out/）／スライド（直下）。"""
    p = root / "step1_basics" / "01_grp" / name
    w(p / "README.md", "###### [toTopPage](../../../README.md)\n###### [toREADME](../README.md)\n# 1-7 アルファ\n\n## 成果物\n"
      f"| 解説メモ | [{slug}_explained/README.md](./{slug}_explained/README.md) |\n"
      f"| スライド | [{slug}-explained-slides.html](./{slug}-explained-slides.html) |\n"
      f"| 原本 | [00_originals/{slug}.md](./00_originals/{slug}.md) |\n\n## 確認していないこと\n- 動画の中身（字幕なし）\n- 画像\n")
    w(p / f"00_originals/{slug}.md", "---\ntitle: アルファ題\n---\nORIGINAL\n")
    e = p / f"{slug}_explained"
    for n in ("README.md", "01_source.md", "02_explanation_memo.md", "11_question_and_answer.md", "12_LLM_prompts_as_guide.md"):
        w(e / n, f"{n}-BODY\n" + (f"-----\n[toTop](#totoppage)\n" if n == "README.md" else ""))
    w(e / "out/09_input-memo.md", "INPUTMEMO")
    w(e / "out/00_manifest.json", "{}")
    w(p / f"{slug}-explained-slides.md", f"# s\n- [解説メモ](./{slug}_explained/README.md)\n- [FAQ]({slug}_explained/11_question_and_answer.md)\n- [外](https://x.example/{slug}_explained/a)\n")
    w(p / f"{slug}-explained-slides.html", f"<html>[解説メモ](./{slug}_explained/02_explanation_memo.md)</html>")
    return p


def sh(root, *args):
    # LANG=C でも動くこと（全角文字の直前の変数名の誤読を防ぐ）。出力は UTF-8 として読む
    env = {**os.environ, "LANG": "C", "LC_ALL": "C"}
    return subprocess.run(["bash", str(SCRIPT), "--root", str(root), "--no-status", *args], capture_output=True, env=env,
                          encoding="utf-8", errors="strict")


def tree(p):
    return sorted(str(x.relative_to(p)) for x in p.rglob("*") if x.is_file())


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        w(self.root / ".gitignore", "**/.work/*\n!**/.work/working-log.md\n")
        self.page = old_page(self.root)
        w(self.root / "step1_basics/01_grp/README.md",
          "| [スライド](./07_alpha/alpha-explained-slides.html) | [メモ](./07_alpha/alpha_explained/02_explanation_memo.md) | [表紙](07_alpha/README.md) |\n")
        # 解説メモが無いページ（触られない）
        w(self.root / "step1_basics/01_grp/08_thin/README.md", "THIN")
        w(self.root / "step1_basics/01_grp/08_thin/00_originals/thin.md", "x")

    def tearDown(self):
        self._td.cleanup()

    def test_dry_run_changes_nothing(self):
        before = tree(self.root)
        r = sh(self.root)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(tree(self.root), before)
        self.assertIn("試し", r.stdout)

    def test_apply_moves_everything(self):
        r = sh(self.root, "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        p = self.page
        self.assertEqual(tree(p), sorted([
            ".work/intermediate/00_manifest.json", ".work/intermediate/09_input-memo.md", ".work/working-log.md",
            "00_originals/alpha.md", "01_source.md", "02_explanation_memo.md", "11_question_and_answer.md",
            "12_LLM_prompts_as_guide.md", "README.md",
            "docs/alpha-explained-slides.html", "docs/alpha-explained-slides.md"]))
        self.assertFalse((p / "alpha_explained").exists())
        self.assertIn("README.md-BODY", (p / "README.md").read_text(encoding="utf-8"))     # 表紙は解説メモの README
        self.assertEqual((p / "01_source.md").read_text(encoding="utf-8"), "01_source.md-BODY\n")   # 本文は変えない

    def test_old_readme_becomes_working_log_with_links_rebased(self):
        sh(self.root, "--apply")
        log = (self.page / ".work/working-log.md").read_text(encoding="utf-8")
        self.assertIn("## 確認していないこと\n- 動画の中身（字幕なし）\n- 画像", log)       # 本文はそのまま（見出しも変えない）
        self.assertIn("# 1-7 アルファ", log)
        for link in ("](../../../../README.md)", "](../../README.md)", "](../README.md)",
                     "](../docs/alpha-explained-slides.html)", "](../00_originals/alpha.md)"):
            self.assertIn(link, log)
        import re
        for target in re.findall(r"\]\(([^)]*)\)", log):
            self.assertNotIn("_explained", target)                                     # リンク先に旧パスは残さない（表示文字はそのまま）
        # .work/ から辿って、リンク先が実在する
        for rel in ("../README.md", "../docs/alpha-explained-slides.html", "../00_originals/alpha.md"):
            self.assertTrue((self.page / ".work" / rel).exists(), rel)

    def test_slide_links_rewritten(self):
        sh(self.root, "--apply")
        md = (self.page / "docs/alpha-explained-slides.md").read_text(encoding="utf-8")
        self.assertIn("](../README.md)", md)
        self.assertIn("](../11_question_and_answer.md)", md)                               # ./ なしの形も
        self.assertIn("https://x.example/alpha_explained/a", md)                          # 外部の URL は触らない
        self.assertIn("](../02_explanation_memo.md)", (self.page / "docs/alpha-explained-slides.html").read_text(encoding="utf-8"))
        for rel in ("../README.md", "../11_question_and_answer.md"):
            self.assertTrue((self.page / "docs" / rel).exists(), rel)

    def test_group_readme_links_rewritten(self):
        sh(self.root, "--apply")
        t = (self.root / "step1_basics/01_grp/README.md").read_text(encoding="utf-8")
        self.assertIn("](./07_alpha/docs/alpha-explained-slides.html)", t)
        self.assertIn("](./07_alpha/02_explanation_memo.md)", t)
        self.assertIn("](07_alpha/README.md)", t)
        self.assertNotIn("docs/docs", t)

    def test_idempotent(self):
        sh(self.root, "--apply")
        after1 = {f: (self.root / f).read_bytes() for f in tree(self.root)}
        r = sh(self.root, "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual({f: (self.root / f).read_bytes() for f in tree(self.root)}, after1)
        self.assertIn("移した: 0", r.stdout)

    def test_pages_without_memo_untouched(self):
        sh(self.root, "--apply")
        self.assertEqual((self.root / "step1_basics/01_grp/08_thin/README.md").read_text(encoding="utf-8"), "THIN")
        self.assertFalse((self.root / "step1_basics/01_grp/08_thin/.work").exists())

    def test_unexpected_file_stops_that_page_only(self):
        w(self.page / "alpha_explained/notes.txt", "x")
        p2 = old_page(self.root, "09_beta", "beta")
        before = tree(self.page)
        r = sh(self.root, "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("想定外のファイル: notes.txt", r.stdout)
        self.assertEqual(tree(self.page), before)                                        # 止めたページは 1 つも動かさない
        self.assertTrue((p2 / "docs/beta-explained-slides.md").exists())                 # ほかのページは移る

    def test_destination_collision_stops(self):
        w(self.page / "01_source.md", "ALREADY")
        r = sh(self.root, "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("移し先に 01_source.md が既にある", r.stdout)
        self.assertTrue((self.page / "alpha_explained/01_source.md").exists())

    def test_existing_log_or_intermediate_stops(self):
        for existing, msg in ((".work/working-log.md", "working-log.md が既にある"), (".work/intermediate/x.md", ".work/intermediate が既にある"),
                              ("docs/alpha-explained-slides.md", "docs/alpha-explained-slides.md が既にある")):
            with self.subTest(existing=existing):
                w(self.page / existing, "ALREADY")
                r = sh(self.root, "--apply")
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn(msg, r.stdout)
                self.assertTrue((self.page / "alpha_explained/README.md").exists())
                (self.page / existing).unlink()
                shutil.rmtree(self.page / ".work", ignore_errors=True)

    def test_missing_memo_file_stops(self):
        (self.page / "alpha_explained/11_question_and_answer.md").unlink()
        r = sh(self.root, "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertTrue((self.page / "alpha_explained/README.md").exists())

    def test_ds_store_is_tolerated(self):
        w(self.page / "alpha_explained/.DS_Store", "junk")
        r = sh(self.root, "--apply")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertFalse((self.page / "alpha_explained").exists())

    def test_only_one_page(self):
        p2 = old_page(self.root, "09_beta", "beta")
        r = sh(self.root, "--apply", "--page", "step1_basics/01_grp/09_beta")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertTrue((p2 / "docs").exists())
        self.assertTrue((self.page / "alpha_explained").exists())                        # 指定しなかったページは動かない

    def test_unknown_option_and_page(self):
        self.assertEqual(sh(self.root, "--nope").returncode, 2)
        self.assertEqual(sh(self.root, "--page", "step1_basics/01_grp/99_none").returncode, 2)


class CoverTests(unittest.TestCase):
    """表紙末尾の「状態と関連資料」と作業ログの「検査の結果」。検査（page_status）は固定の値に差し替える。"""

    FAKE = {"memo": "12 PASS", "slides": "10 枚／lint 0", "numbers_missing": [], "links_broken": 0}

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.page = Path(self._td.name) / "step1_basics/01_g/07_alpha"
        w(self.page / "README.md", "# 資料：アルファ\n- `title`: アルファ\n\n-----\n[toTop](#totoppage)\n## 概要\nOVERVIEW\n\n" + SEP + "\n")
        for n in ("01_source.md", "02_explanation_memo.md", "11_question_and_answer.md", "12_LLM_prompts_as_guide.md"):
            w(self.page / n, "【補足】x 【推測】y" if n == "02_explanation_memo.md" else "x")
        w(self.page / "00_originals/alpha.md", "x")
        w(self.page / "docs/alpha-explained-slides.md", "s")
        w(self.page / "docs/alpha-explained-slides.html", "h")
        self.row = {"id": "1-7", "title": "アルファ題", "status": "完了", "learned_on": ""}
        self._orig = page_readme.page_status
        page_readme.page_status = lambda p: dict(self.FAKE)

    def tearDown(self):
        page_readme.page_status = self._orig
        self._td.cleanup()

    def cover(self):
        return (self.page / "README.md").read_text(encoding="utf-8")

    def log(self):
        return (self.page / ".work/working-log.md").read_text(encoding="utf-8")

    def test_block_added_at_end_and_file_still_ends_with_separator(self):
        page_readme.update_cover(self.row, self.page)
        t = self.cover()
        self.assertTrue(t.endswith(SEP + "\n"))
        self.assertIn("## 状態と関連資料", t)
        self.assertIn("- 状態: 検査済み", t)
        self.assertIn("[docs/alpha-explained-slides.html](./docs/alpha-explained-slides.html)", t)
        self.assertIn("[.work/working-log.md](./.work/working-log.md)", t)
        self.assertIn("OVERVIEW", t)                                                    # 元の本文は残る

    def test_cover_links_stay_inside_page_folder(self):
        """check_docs の C-5：表紙の相対リンクは、ページのフォルダの外を指さない。"""
        import re
        page_readme.update_cover(self.row, self.page)
        for m in re.finditer(r"\]\((\.[^)]*)\)", self.cover()):
            self.assertFalse(m.group(1).startswith("../"), m.group(1))

    def test_idempotent(self):
        page_readme.update_cover(self.row, self.page)
        a, b = self.cover(), self.log()
        page_readme.update_cover(self.row, self.page)
        self.assertEqual((self.cover(), self.log()), (a, b))
        self.assertEqual(self.cover().count("page-status:start"), 1)
        self.assertEqual(self.log().count("checks:start"), 1)

    def test_state_words(self):
        for status, learned, want in (("完了", "", "検査済み"), ("完了", "2026-11-25", "確定"),
                                     ("要確認", "", "作成中"), ("作成中", "2026-11-25", "作成中")):
            self.assertEqual(page_readme.state_word({"status": status, "learned_on": learned}, {}), want)

    def test_log_created_with_checks_and_manual_text_survives_update(self):
        page_readme.update_cover(self.row, self.page)
        self.assertIn("12 PASS", self.log())
        self.assertIn("【補足】1・【推測】1", self.log())
        w(self.page / ".work/working-log.md", self.log() + "\n- 手書きの経緯: 2 回目の読み合わせで直した\n")
        page_readme.page_status = lambda p: {**self.FAKE, "memo": "11 PASS／1 FAIL"}
        page_readme.update_cover(self.row, self.page)
        self.assertIn("手書きの経緯", self.log())
        self.assertIn("11 PASS／1 FAIL", self.log())
        self.assertNotIn("12 PASS", self.log())
        self.assertIn("11 PASS／1 FAIL", self.cover())

    def test_migrated_log_gets_checks_block_before_first_section(self):
        w(self.page / ".work/working-log.md", "# 1-7 アルファ\n- 元ページ: u\n\n## 成果物\n| x |\n\n## 確認していないこと\n- 動画の中身（字幕なし）\n- 画像\n")
        page_readme.update_cover(self.row, self.page)
        t = self.log()
        self.assertLess(t.index("checks:start"), t.index("## 成果物"))
        self.assertIn("確認していないこと（要約）: 動画の中身（字幕なし）／画像", self.cover())      # 作業ログの項目が要約される

    def test_unverified_summary(self):
        long_ = "あ" * 30 + "（かっこ内は落とす）" + "い" * 20           # 40 字を超える → 最初の「（」で切る
        log = f"## 確認していないこと\n- 短い項目（かっこ内もそのまま）\n- {long_}\n- C。D\n- E\n\n## 次\n- Z\n"
        self.assertEqual(page_readme.unverified_summary(log), "短い項目（かっこ内もそのまま）／" + "あ" * 30 + "／C。Dほか")
        self.assertIn("原本のリンク先", page_readme.unverified_summary("見出しなし"))      # 無ければ既定の 3 件
        self.assertTrue(page_readme.unverified_summary("## 確認していないこと\n- " + "あ" * 80).endswith("…"))

    def test_cover_without_trailing_separator_is_refused(self):
        w(self.page / "README.md", "# 解説メモの表紙ではない\n本文\n")
        with self.assertRaises(ValueError):
            page_readme.update_cover(self.row, self.page)


class RealToolsTests(unittest.TestCase):
    """実物の木：移行後の形で、ツールの検査が通る。"""

    @unittest.skipUnless((REAL_ROOT / "ledger.csv").exists(), "実物の木が無い")
    def test_real_tree_is_new_layout(self):
        import csv
        rows = list(csv.DictReader(open(REAL_ROOT / "ledger.csv", encoding="utf-8")))
        for r in rows:
            page = REAL_ROOT / r["page_dir"]
            if not page.is_dir():
                continue
            self.assertEqual(list(page.glob("*_explained")), [], f"{r['id']}: 旧構造の *_explained が残っている")
            self.assertEqual(list(page.glob("*-explained-slides.*")), [], f"{r['id']}: スライドが直下に残っている")
            if r["status"] == "完了":
                for n in ("README.md", "01_source.md", "02_explanation_memo.md", "11_question_and_answer.md", "12_LLM_prompts_as_guide.md"):
                    self.assertTrue((page / n).is_file(), f"{r['id']}: {n} が無い")
                self.assertTrue((page / ".work/working-log.md").is_file(), f"{r['id']}: 作業ログが無い")
                self.assertTrue(list((page / "docs").glob("*-explained-slides.html")), f"{r['id']}: docs/ にスライドが無い")


if __name__ == "__main__":
    unittest.main(verbosity=2)
