###### [toTopPage](../../../README.md)
###### [toREADME](../README.md)
# 1-11 Claudeの活用例：職種別ユースケース（Claude 101 レッスン 11）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/claude-in-action-use-cases-by-role（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 2 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/claude-in-action-use-cases-by-role.md](./00_originals/claude-in-action-use-cases-by-role.md) |
| 解説メモ（入口） | [claude-in-action-use-cases-by-role_explained/README.md](./claude-in-action-use-cases-by-role_explained/README.md) |
| 解説スライド | [claude-in-action-use-cases-by-role-explained-slides.html](./claude-in-action-use-cases-by-role-explained-slides.html)（原稿: [.md](./claude-in-action-use-cases-by-role-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS。読み合わせで 4 点（引用でない文の「…」、`out/02` の依頼文由来の件数の記述、システムプロンプトの本文に無い語、補足の位置）を直して再転記／読み合わせ G-3（メイン）: 本文のユースケースへのリンク 15 件・7 区分（一般 3・営業 3・マーケティング 2・財務 3・人事 1・法務 1・研究 2）を原本のリンクと照合して一致。題名と説明の範囲だけで書かれ、リンク先の中身を推測で書いていないことを確認／README の概要 297 字（上限 400）
- スライド: 8 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 8 枚のうち 1 枚（表の最終行と下部の帯の近接）を修正。リンク一覧の水増しはしていない／出典の無い数字: 0（なし は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 13・`【推測】` 4・`（要確認:` 0

## 確認していないこと
- リンク先のユースケース 15 件（ユースケースギャラリーの詳細ガイド）の中身、動画・画像
- 【推測】の当否
- 本文に件数の記載は無い（「15 件」は原本のリンクを数えた補足）

## 学習メモとの食い違い
- 学習メモは「2 分」。本文には所要時間が無く、解説・スライドには分数を書いていない。本文は大半がユースケースへのリンクの一覧で、ステップ 3 の役割ページ・ユースケースと一部重なる題名がある（例: ブランドガイドラインをスキルにパッケージ化、文献レビューの計画、新入社員オンボーディングガイドの作成）

-----
[toTop](#totoppage)
