###### [toTopPage](../../../README.md)
###### [toREADME](../README.md)
# 0-4 Claude Coworkを3つのステップで始める（Get started with Claude in three steps）
- 元ページ: https://academy.claude.com/ja/tutorials/get-started-in-claude-cowork-in-three-steps（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 4 分（`/learning` の一覧の表示＝0-1。**取得した本文には分数が無い**）　内容の種類: 技術・ハウツー　状態: 完了
- 題名に旧名称「Cowork」が残っている（学習メモの付録 D）

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/get-started-in-claude-cowork-in-three-steps.md](./00_originals/get-started-in-claude-cowork-in-three-steps.md) |
| 解説メモ（入口） | [get-started-in-claude-cowork-in-three-steps_explained/README.md](./get-started-in-claude-cowork-in-three-steps_explained/README.md) |
| 解説スライド | [get-started-in-claude-cowork-in-three-steps-explained-slides.html](./get-started-in-claude-cowork-in-three-steps-explained-slides.html)（原稿: [.md](./get-started-in-claude-cowork-in-three-steps-explained-slides.md)） |

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
