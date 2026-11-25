###### [toTopPage](../../README.md)
###### [toREADME](../README.md)
# 0-4 Claude Coworkを3つのステップで始める（Get started with Claude in three steps）
- 元ページ: https://academy.claude.com/ja/tutorials/get-started-in-claude-cowork-in-three-steps（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 4 分（`/learning` の一覧の表示＝0-1。**取得した本文には分数が無い**）　内容の種類: 技術・ハウツー　状態: 完了
- 題名に旧名称「Cowork」が残っている（学習メモの付録 D）

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】14・【推測】6、スライドの（要確認: 1
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/get-started-in-claude-cowork-in-three-steps.md](../00_originals/get-started-in-claude-cowork-in-three-steps.md) |
| 解説メモ（入口） | [get-started-in-claude-cowork-in-three-steps_explained/README.md](../README.md) |
| 解説スライド | [get-started-in-claude-cowork-in-three-steps-explained-slides.html](../docs/get-started-in-claude-cowork-in-three-steps-explained-slides.html)（原稿: [.md](../docs/get-started-in-claude-cowork-in-three-steps-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（サブエージェントは 2 回目で合格と報告。1 回目は C-6 で概要が 410 字（上限 400 字）。メインが再実行して 11 PASS を確認）／読み合わせ: サブエージェントが本文に無い「入力欄」の語を直し、FAQ 9 の引用を差し替え。メインが G-3 として、プラン条件（本文に無い）・手順の順序（アプリを開いてサインイン → `/setup-claude` → Work in a folder → 最初のタスク）を原本と照合して食い違い 0
- スライド: 10 枚（本文が約 2,450 字のため 8〜10 枚の目安）／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚を目視して修正なし／出典の無い数字: 0（`03`・`06` は note 内の解説メモの参照で数値ではない）
- 印の件数: `【補足】` 14・`【推測】` 5・`（要確認:` 1（所要時間）

## 確認していないこと
- リンク先（support.claude.com など）・動画・画像の中身
- 【推測】の当否。原本に見出し・番号が無く、「3 つのステップ」の内訳（`/setup-claude`・作業場所の指定・最初のタスク）は推測。フォルダとプロジェクトの使い分けも推測
- 有料プラン・権限の条件（本文に書かれていない）

## 学習メモとの食い違い
- なし（学習メモの「4 分」はページの本文には無いが、0-1 の `/learning` の表示と一致）

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
