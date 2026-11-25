###### [toTopPage](../../README.md)
###### [toREADME](../README.md)
# 1-1 Claudeとは何ですか？（Claude 101 レッスン 1）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/what-is-claude（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 約 5 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 9 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】31・【推測】3、スライドの（要確認: 1
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/what-is-claude.md](../00_originals/what-is-claude.md) |
| 解説メモ（入口） | [what-is-claude_explained/README.md](../README.md) |
| 解説スライド | [what-is-claude-explained-slides.html](../docs/what-is-claude-explained-slides.html)（原稿: [.md](../docs/what-is-claude-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS。読み合わせで「だれが」を【補足】にし、解釈に【推測】を付けて再転記／読み合わせ G-3（メイン）: プラン条件（Free・Pro・Max・Team・Enterprise の全プランで利用可、100 万トークンは対応モデルと Pro・Max・Team・Enterprise）と数字（20 万トークン・約 500 ページ）を原本と照合して食い違い 0／README の概要 352 字（上限 400）
- スライド: 9 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 9 枚を確認して修正なし／出典の無い数字: 0（`03`・`05` は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 31・`【推測】` 3・`（要確認:` 1（このレッスンの所要時間（分）

## 確認していないこと
- 動画・画像・各リンク先の中身
- 【推測】の当否（偏りチェックなど）
- このレッスンの所要時間（本文に無い。スライド 6 に要確認）

## 学習メモとの食い違い
- 学習メモは「約 5 分」。本文には所要時間が無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
