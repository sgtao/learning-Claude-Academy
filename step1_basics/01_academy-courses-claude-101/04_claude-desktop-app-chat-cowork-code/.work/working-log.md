###### [toTopPage](../../README.md)
###### [toREADME](../README.md)
# 1-4 デスクトップでClaudeとどのように仕事をするか（Claude 101 レッスン 4）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/claude-desktop-app-chat-cowork-code（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 10 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】13・【推測】2、スライドの（要確認: 1
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/claude-desktop-app-chat-cowork-code.md](../00_originals/claude-desktop-app-chat-cowork-code.md) |
| 解説メモ（入口） | [claude-desktop-app-chat-cowork-code_explained/README.md](../README.md) |
| 解説スライド | [claude-desktop-app-chat-cowork-code-explained-slides.html](../docs/claude-desktop-app-chat-cowork-code-explained-slides.html)（原稿: [.md](../docs/claude-desktop-app-chat-cowork-code-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS。読み合わせで一部の【補足】の位置を直して再転記／読み合わせ G-3（メイン）: プラン条件（Cowork は Pro・Max・Team・Enterprise、コンピュータ使用は Pro・Max でリサーチプレビュー、クラウド版 Cowork は Pro・Max で利用可・Team と管理者が有効にした Enterprise はベータ版）と、(Mac) の注記が付く 3 機能を原本と照合して食い違い 0／README の概要 260 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち、スライド 3 の表を 2 周修正。表の「Codeタブ」が 2 行に折り返す点は未解消（はみ出し・切れは無い軽微な見た目）／出典の無い数字: 0（`07` は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 13・`【推測】` 2・`（要確認:` 1（Windowsなど、Mac以外での対応可否。本文に記載なし）

## 確認していないこと
- リンク先（Claude Code in Action・Cowork in the cloud）の中身、動画の字幕
- Mac 以外の OS での対応可否（本文に記載なし。スライド 8 に要確認）
- 製品の最新の画面・プラン条件（本文の記述のみ。原本も新しい機能が定期的に追加されると述べている）
- 本文冒頭の「6 つの情報源」の内訳（本文に無い）
- 【推測】の当否（Code の「知っておく価値」の解釈の 1 か所）
- 題名・本文の「Cowork」の呼び方は原本のまま（旧名称かどうかの手がかりは、修了バッジのページ（1-15）の告知バナー）
## 学習メモとの食い違い
- 学習メモは「10 分」。本文には所要時間が無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
