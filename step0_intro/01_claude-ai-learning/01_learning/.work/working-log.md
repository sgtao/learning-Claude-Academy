###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 0-1 学ぶ（`/learning` 入口）
- 元ページ: https://claude.ai/learning（取得: 2026-11-15／取得手段: Claude in Chrome。本文を読んで起こした `model-read`）
- 所要（ページ表示）: －（入口ページ。「はじめに」の 3 本が 4・4・7 分）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 8 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】39・【推測】2、スライドの（要確認: 3
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/learning.md](../00_originals/learning.md)（取得したままの文字: [learning.raw.txt](../00_originals/learning.raw.txt)） |
| 解説メモ（入口） | [learning_explained/README.md](../README.md) |
| 解説スライド | [learning-explained-slides.html](../docs/learning-explained-slides.html)（原稿: [.md](../docs/learning-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（サブエージェントは 2 回目で合格と報告。メインが再実行して 11 PASS を確認）／読み合わせ: R-1〜R-4 はサブエージェントが実施（英語題の訳に【補足】を足す修正 1 回）。G-3 としてメインが FAQ の数字・「本文には書かれていない」の扱いを原本と照合して食い違い 0
- スライド: 8 枚（本文 753 字のため 5〜8 枚の目安）／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／撮影した 8 枚のうち 2 枚をメインが目視（表・棒グラフとも崩れなし。棒グラフの軸ラベルは小さい）／出典の無い数字: 0（`06` は note の「06 総括」の参照で数値ではない）
- 印の件数: `【補足】` 39・`【推測】` 2・`（要確認:` 3（作成機能の有料プラン・権限の条件／チェックインの選べる頻度／リンク先の中身）

## 確認していないこと
- ページ内の「作成」3 つとチェックインの実際の動作（ボタンは押していない。説明文だけが根拠）
- リンク先（Claude 101・各チュートリアル・役割別ページ）の中身。有料プラン・権限の条件（本文に無い）
- ログイン状態による表示の違い（取得時の表示のみ）

## 学習メモとの食い違い
- なし（学習メモ 0-1 の「分」は「－」。ページの「はじめに」は 4・4・7 分で、学習メモの 0-4・0-5・0-6 と一致）

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
