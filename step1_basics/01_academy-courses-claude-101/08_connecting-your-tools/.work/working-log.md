###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 1-8 ツールを接続する（Claude 101 レッスン 8）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/connecting-your-tools（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 15 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 11 PASS／1 FAIL
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】13・【推測】6、スライドの（要確認: 0
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/connecting-your-tools.md](../00_originals/connecting-your-tools.md) |
| 解説メモ（入口） | [connecting-your-tools_explained/README.md](../README.md) |
| 解説スライド | [connecting-your-tools-explained-slides.html](../docs/connecting-your-tools-explained-slides.html)（原稿: [.md](../docs/connecting-your-tools-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目は 11 PASS。読み合わせで 3 点（デスクトップ拡張機能の手順に当てはまらない書き方、活用案冒頭の補足の印、本文に無い見出し名のような呼び方）を直して再転記。利用上限で一度停止し、再開して完了／読み合わせ G-3（メイン）: 接続手順の順序と、Team・Enterprise では組織のオーナーが先にコネクタを組織向けに追加する条件を原本と照合して食い違い 0。Team・Enterprise 以外のプランの可否は本文に無く、スライド 8 に「書かれていない」と明記／README の概要 302 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚で修正なし／出典の無い数字: 0（なし は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 13・`【推測】` 5・`（要確認:` 0

## 確認していないこと
- リンク先（コネクタのディレクトリ・ダウンロード・ヘルプセンター）の中身、画像
- Team・Enterprise 以外（無料プランなど）でコネクタが使えるか、許可されるアクションの範囲（本文に無い）
- 【推測】の当否

## 学習メモとの食い違い
- 学習メモは「15 分」。本文には所要時間が無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
