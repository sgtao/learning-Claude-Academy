###### [toTopPage](../../../README.md)
###### [toREADME](../README.md)
# 0-2 Claude 101（コースのトップ）
- 元ページ: https://academy.claude.com/ja/courses/claude-101（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 約 150 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/claude-101.md](./00_originals/claude-101.md) |
| 解説メモ（入口） | [claude-101_explained/README.md](./claude-101_explained/README.md) |
| 解説スライド | [claude-101-explained-slides.html](./claude-101-explained-slides.html)（原稿: [.md](./claude-101-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（サブエージェントは 2 回目で合格と報告。1 回目は C-6 で README の概要が 431 字（上限 400 字）。メインが再実行して 11 PASS を確認）／読み合わせ: サブエージェントが、本文に無い「13 レッスン」「Claude Academy」の語を除いた。メインが数字・プラン条件を原本と照合して食い違い 0
- スライド: 8 枚（本文が約 800 字のため 5〜8 枚の目安）／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 8 枚のうち 1 枚の折り返しを修正／出典の無い数字: 0
- 印の件数: `【補足】` 26・`【推測】` 4・`（要確認:` 4（レッスンの一覧・所要時間・Chat/Cowork/Code の向き不向き・有料プランの注記の中身）

## 確認していないこと
- 13 レッスンの一覧と各レッスンの内容（本文に無い。ステップ 1 で扱う）
- 【推測】の当否（例: Free プランでは Cowork・Research・Enterprise Search を試せないと読める）。各レッスンの注記で確かめる

## 学習メモとの食い違い
- 学習メモは「約 150 分・13 レッスン」。ページの本文にはどちらも書かれていない（本文を根拠にした解説・スライドには書いていない）

-----
[toTop](#totoppage)
