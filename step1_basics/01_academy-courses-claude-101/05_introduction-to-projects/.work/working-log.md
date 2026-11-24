###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 1-5 プロジェクト入門（Claude 101 レッスン 5）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/introduction-to-projects（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 15 分（学習メモの値。本文の「数分」はプロジェクト作成の説明。**取得した本文にレッスンの分数は無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 11 PASS／1 FAIL
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】11・【推測】6、スライドの（要確認: 2
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/introduction-to-projects.md](../00_originals/introduction-to-projects.md) |
| 解説メモ（入口） | [introduction-to-projects_explained/README.md](../README.md) |
| 解説スライド | [introduction-to-projects-explained-slides.html](../docs/introduction-to-projects-explained-slides.html)（原稿: [.md](../docs/introduction-to-projects-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS。読み合わせ R-2 で `out/07` の補足の印が足りない箇所を直して再転記／読み合わせ G-3（メイン）: 共有は Claude for Work（Team・Enterprise）向け、作成の手順の順序、「最大10倍」の扱い（基準が本文に無い→要確認）、原本内のゆれ（画面名・公開範囲の呼び名・容量・説明文の扱い）を原本と照合して食い違い 0／README の概要 326 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち 1 枚（スライド 4 の見出し文言）を修正して再撮影／出典の無い数字: 0（`03`・`05` は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 11・`【推測】` 5・`（要確認:` 2（「最大10倍」の倍率の基準・Claude for Work 以外のプランでのプロジェクトの利用可否）

## 確認していないこと
- 動画の字幕・画像・リンク先（プロジェクトのページ・ヘルプセンター）の中身
- 【推測】の当否（画面名・公開範囲の呼び名の揺れ、「最大10倍」の意味）。実際の画面の表示
- Claude for Work 以外のプランでのプロジェクトの利用可否（本文に無い。スライド 8 に要確認）
- 本文は約 8,500 字で見出しが無く、解説メモは「分割なし・グループ 1 つ」。ステップ 2 の「Intro to Projects」（チュートリアル）とは別のページ
## 学習メモとの食い違い
- 学習メモは「15 分」。本文にレッスンの所要時間は無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
