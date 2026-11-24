#!/usr/bin/env python3
"""VitePress のサイトが、ビルドでき、台帳のページがすべて出て、スライドがコピーされるかの検査。

使い方:  python3 tools/test_site.py      （Node.js と `npm ci` 済みの node_modules が要る。無ければ飛ばす）
ビルドは、リンク切れ（VitePress の dead link 検査）があると失敗する。出力は一時フォルダ（VITEPRESS_OUT）。
"""
import csv, os, re, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HAVE = shutil.which("node") and (ROOT / "node_modules" / "vitepress").exists()


@unittest.skipUnless(HAVE, "node か node_modules が無い（npm ci を先に）")
class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._td = tempfile.TemporaryDirectory()
        cls.out = Path(cls._td.name) / "dist"
        env = {**os.environ, "VITEPRESS_OUT": str(cls.out), "VITEPRESS_BASE": "/learning-Claude-Academy/"}
        cls.r = subprocess.run(["npx", "vitepress", "build"], cwd=ROOT, env=env, capture_output=True, text=True)
        cls.rows = list(csv.DictReader(open(ROOT / "ledger.csv", encoding="utf-8")))

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def test_build_succeeds_with_no_dead_links(self):
        self.assertEqual(self.r.returncode, 0, self.r.stdout[-1500:] + self.r.stderr[-1500:])
        self.assertNotIn("dead link", self.r.stdout + self.r.stderr)

    def test_every_ledger_page_has_a_cover_page(self):
        for r in self.rows:
            self.assertTrue((self.out / r["page_dir"] / "README.html").is_file(), r["id"])

    def test_slides_are_copied_for_every_page_that_has_them(self):
        n = 0
        for r in self.rows:
            for f in (ROOT / r["page_dir"] / "docs").glob("*-explained-slides.html"):
                n += 1
                self.assertEqual((self.out / r["page_dir"] / "docs" / f.name).read_bytes(), f.read_bytes(), r["id"])
        self.assertGreaterEqual(n, 60)

    def test_working_dirs_and_slide_sources_are_not_published(self):
        for pat in (".work", "intermediate", "00_manifest.json"):
            self.assertEqual([p for p in self.out.rglob("*") if pat in p.name], [], pat)
        self.assertEqual(list(self.out.rglob("*-explained-slides.md")), [])
        self.assertEqual(list(self.out.rglob("*-explained-slides.md.*")), [])

    def test_base_path_is_applied(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="/learning-Claude-Academy/', html)

    def test_working_log_links_point_to_github(self):
        html = (self.out / "step1_basics/01_academy-courses-claude-101/07_working-with-skills/README.html").read_text(encoding="utf-8")
        m = re.search(r'href="(https://github\.com/[^"]*working-log\.md)"', html)
        self.assertTrue(m, "作業ログへのリンクが GitHub を指していない")
        self.assertIn("/blob/main/step1_basics/01_academy-courses-claude-101/07_working-with-skills/.work/working-log.md", m.group(1))

    def test_sidebar_lists_every_page(self):
        sample = (self.out / "step3_roles/10_engineering/02_design-doc/README.html").read_text(encoding="utf-8")
        for r in self.rows:
            if r["step"] == "3" and r["group"] == "10_engineering":
                self.assertIn(f"/{r['page_dir']}/README", sample, r["id"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
