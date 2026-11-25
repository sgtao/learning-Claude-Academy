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

    PAGE = "step1_basics/01_academy-courses-claude-101/07_working-with-skills"

    def test_slide_html_link_bypasses_the_router_and_manuscript_link_goes_to_github(self):
        """VitePress のルーターは .html へのリンクを自分のページとして処理し、同名の原稿 MD を出してしまう。
        target 属性があるリンクにはルーターが介入しないので、スライドの HTML は新しいタブで直接開く。"""
        html = (self.out / self.PAGE / "README.html").read_text(encoding="utf-8")
        m = re.search(r'<a [^>]*href="[^"]*working-with-skills-explained-slides\.html"[^>]*>', html)
        self.assertTrue(m, "解説スライドのリンクが無い")
        self.assertIn('target="_blank"', m.group(0))
        g = re.search(r'<a [^>]*href="(https://github\.com/[^"]*working-with-skills-explained-slides\.md)"', html)
        self.assertTrue(g, "スライド原稿のリンクが GitHub を指していない")
        self.assertIn(f"/blob/main/{self.PAGE}/docs/", g.group(1))

    def test_cover_ends_with_slides_and_has_no_status_section(self):
        html = (self.out / self.PAGE / "README.html").read_text(encoding="utf-8")
        heads = re.findall(r"<h2 id=\"([^\"]+)\"", html)
        self.assertTrue(heads[-1].startswith("解説資料"), heads)
        self.assertNotIn("状態と関連資料", html)

    def test_sidebar_lists_every_page(self):
        sample = (self.out / "step3_roles/10_engineering/02_design-doc/README.html").read_text(encoding="utf-8")
        for r in self.rows:
            if r["step"] == "3" and r["group"] == "10_engineering":
                self.assertIn(f"/{r['page_dir']}/README", sample, r["id"])


@unittest.skipUnless(HAVE, "node か node_modules が無い（npm ci を先に）")
class DevServerTests(unittest.TestCase):
    """dev サーバーでも、スライドの URL（.html）は、原稿 MD ではなくスライドの HTML を返す。"""

    PAGE = "step1_basics/01_academy-courses-claude-101/07_working-with-skills"

    def test_dev_server_serves_slide_html_not_the_manuscript(self):
        import socket, time, urllib.request
        with socket.socket() as sk:
            sk.bind(("127.0.0.1", 0)); port = sk.getsockname()[1]
        p = subprocess.Popen(["npx", "vitepress", "dev", ".", "--host", "127.0.0.1", "--port", str(port), "--strictPort"], cwd=ROOT,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        try:
            url = f"http://127.0.0.1:{port}/{self.PAGE}/docs/working-with-skills-explained-slides.html"
            body = None
            for _ in range(60):
                try:
                    with urllib.request.urlopen(url, timeout=3) as r:
                        body = r.read().decode("utf-8")
                        ctype = r.headers.get("Content-Type", "")
                    break
                except Exception:
                    time.sleep(0.5)
            self.assertIsNotNone(body, "dev サーバーが起動しない")
            self.assertTrue(body.lower().startswith("<!doctype html"), body[:80])
            self.assertIn("text/html", ctype)
            self.assertIn("data-view", body)                      # スライド（mdss の HTML）の印。VitePress の外枠ではない
            self.assertNotIn("/@vite/client", body)
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/{self.PAGE}/README", timeout=5) as r:
                self.assertEqual(r.status, 200)                   # ふつうのページは、これまでどおり VitePress が出す
        finally:
            import os, signal
            try:
                os.killpg(os.getpgid(p.pid), signal.SIGTERM)
            except Exception:
                p.terminate()


if __name__ == "__main__":
    unittest.main(verbosity=2)
