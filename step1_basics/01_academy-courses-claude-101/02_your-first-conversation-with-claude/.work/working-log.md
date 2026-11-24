###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 1-2 Claudeとの最初の会話（Claude 101 レッスン 2）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/your-first-conversation-with-claude（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 15 分（学習メモの値。**取得した本文には分数が無い**。本文にある「5分から45分」はリサーチ的なレポートの所要で、レッスンの所要ではない）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】18・【推測】8、スライドの（要確認: 3
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/your-first-conversation-with-claude.md](../00_originals/your-first-conversation-with-claude.md) |
| 解説メモ（入口） | [your-first-conversation-with-claude_explained/README.md](../README.md) |
| 解説スライド | [your-first-conversation-with-claude-explained-slides.html](../docs/your-first-conversation-with-claude-explained-slides.html)（原稿: [.md](../docs/your-first-conversation-with-claude-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS（修正なし）／読み合わせ G-3（メイン）: メモリの既定（Free・Pro・Max はオン、Team・Enterprise はオフ）、手順の順序（サイドバー → プロンプト → ファイル → 検索とツール → モデル → 対話）、「5分から45分」の主語（本文は Claude Sonnet）を原本と照合して食い違い 0／README の概要 321 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち 1 枚（スライド 2 の steps カードの折り返し）を 2 周で修正／出典の無い数字: 0（なし は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 18・`【推測】` 7・`（要確認:` 3（この機能の名前と使える条件・変更時の文脈の扱い・自分のプランとメモリの設定）

## 確認していないこと
- 動画の中身（字幕は取っていない）・画像・リンク先（4D フレームワークのコース、ヘルプセンター、ユースケースギャラリー）の中身
- 【推測】の当否。原本の前半と後半が同じ内容の 2 通りの述べ方に見える点、「5分から45分」が別機能を指すかどうか（本文は機能名・対応プランを書いていない）
- スライド 8 の要確認 3 件（5 分から 45 分のレポートの機能名と使える条件／モデル変更時の文脈の扱い／自分のプランとメモリの設定）

## 学習メモとの食い違い
- 学習メモは「15 分」。本文には所要時間が無く、解説・スライドにはレッスンの分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
