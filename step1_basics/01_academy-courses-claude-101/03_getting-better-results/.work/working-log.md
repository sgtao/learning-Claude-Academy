###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 1-3 より良い結果を得る（Claude 101 レッスン 3）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/getting-better-results（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 10 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】11・【推測】2、スライドの（要確認: 0
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/getting-better-results.md](../00_originals/getting-better-results.md) |
| 解説メモ（入口） | [getting-better-results_explained/README.md](../README.md) |
| 解説スライド | [getting-better-results-explained-slides.html](../docs/getting-better-results-explained-slides.html)（原稿: [.md](../docs/getting-better-results-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS。読み合わせで「動画に当たる部分と推測」という根拠の弱い書き方を、「動画は本文に含まれない」に直して再転記／読み合わせ G-3（メイン）: 「Rio の例」（原本 7 か所）・評価（eval）の 4 手順・4D フレームワークの順序を原本と照合して食い違い 0／README の概要 239 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち 1 枚（見出しの折り返し）を修正／出典の無い数字: 0（`03` は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 10・`【推測】` 1・`（要確認:` 0

## 確認していないこと
- 動画（本文に「上の動画は…」の行があるが、動画自体は取得していない）・画像・各リンク先の中身
- 【補足】【推測】の当否

## 学習メモとの食い違い
- 学習メモは「10 分」。本文には所要時間が無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
