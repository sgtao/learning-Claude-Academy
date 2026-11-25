#!/usr/bin/env python3
"""索引（00_index.md）の更新の検査（標準ライブラリのみ）。

決めていること:
  - build_index.py が書き換えるのは、「## ステップ N：」の節の表だけ。表の外の文章（見出し・注記・フォルダの見方）は、
    手で直してよく、何度 build_index.py を動かしても変わらない（毎回戻されると、手で直した形を保てないため）。
  - 台帳が変わったときだけ、その行の表が変わる。
  - 索引が無いときだけ、ひな形（index_text）から作る。ひな形は、今の索引の形と同じ。

使い方:  python3 tools/test_index.py
"""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index as b
from common import read_ledger, INDEX


class IndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, cls.rows = read_ledger()
        cls.text = INDEX.read_text(encoding="utf-8")

    def test_real_index_is_not_rewritten(self):
        """今の索引は、台帳と同じなら 1 字も変わらない（毎回更新されない）。"""
        self.assertEqual(b.update_index(self.text, self.rows), self.text)

    def test_template_equals_the_current_form_and_is_stable(self):
        tpl = b.index_text(self.rows)
        self.assertEqual(tpl, self.text)                              # ひな形は、今の索引の形
        self.assertEqual(b.update_index(tpl, self.rows), tpl)

    def test_hand_edits_outside_the_tables_survive(self):
        edited = (self.text.replace("# 学習メモ 索引（Claude Academy）", "# 学習メモ 索引（手で直した題）\n\n手書きの補足。")
                  .replace("## note", "## 手書きの節").replace("手で直さない", "表以外は手で直してよい"))
        self.assertNotEqual(edited, self.text)
        self.assertEqual(b.update_index(edited, self.rows), edited)

    def test_only_the_changed_row_changes_when_the_ledger_changes(self):
        rows = [dict(r) for r in self.rows]
        rows[0]["status"] = "作成中"
        new = b.update_index(self.text, rows)
        old_l, new_l = self.text.split("\n"), new.split("\n")
        self.assertEqual(len(old_l), len(new_l))
        diff = [(a, c) for a, c in zip(old_l, new_l) if a != c]
        self.assertEqual(len(diff), 1, diff)
        self.assertIn(f"| {rows[0]['id']} |", diff[0][1])
        self.assertIn("作成中", diff[0][1])

    def test_new_page_adds_a_row_and_a_missing_step_section_is_added(self):
        rows = [dict(r) for r in self.rows]
        extra = dict(rows[-1]); extra["id"] = "9-add-999"; extra["title"] = "追加ページ"; extra["page_dir"] = "step9_added/01_added/x"
        new = b.update_index(self.text, rows + [extra])
        self.assertIn("| 9-add-999 |", new)
        self.assertEqual(new.count("| 9-add-999 |"), 1)
        self.assertEqual(b.update_index(new, rows + [extra]), new)    # 何度でも同じ
        # ステップ 4 の節を消した索引から、台帳どおりに戻る（位置は最後のステップの後ろ）
        a = self.text.index("## ステップ 4：")
        z = self.text.index("## ステップ 9：")
        cut = self.text[:a] + self.text[z:]
        back = b.update_index(cut, self.rows)
        self.assertIn("## ステップ 4：", back)
        self.assertEqual(back.count("| 4-"), self.text.count("| 4-"))

    def test_check_flags_a_stale_table(self):
        """表の行が台帳と違う索引は、更新後の本文と一致しない（check_index が古いと判定する）。"""
        stale = self.text.replace("| 完了 |", "| 作成中 |", 1)
        self.assertNotEqual(b.update_index(stale, self.rows), stale)


if __name__ == "__main__":
    unittest.main(verbosity=2)
