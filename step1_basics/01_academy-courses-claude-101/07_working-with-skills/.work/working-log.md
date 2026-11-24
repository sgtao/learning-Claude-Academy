###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 1-7 スキルを活用する（Claude 101 レッスン 7）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/working-with-skills（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 15 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】4・【推測】3、スライドの（要確認: 0
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/working-with-skills.md](../00_originals/working-with-skills.md) |
| 解説メモ（入口） | [working-with-skills_explained/README.md](../README.md) |
| 解説スライド | [working-with-skills-explained-slides.html](../docs/working-with-skills-explained-slides.html)（原稿: [.md](../docs/working-with-skills-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目は C-8 で不合格（引用の末尾に原本に無い「。」）。`out/05` の引用を原本に合わせて再転記し、2 回目で 11 PASS／読み合わせ G-3（メイン）: プラン条件（スキルはすべてのプランで利用可。Team は組織レベルで既定有効、Enterprise は組織オーナーがコード実行とスキルの両方を有効にしてからメンバーが使える。Team・Enterprise ではトグルが表示されない）と有効化・作成の手順の順序を原本と照合して食い違い 0／README の概要 319 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚を確認して修正なし／出典の無い数字: 0（`05` は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 4・`【推測】` 2・`（要確認:` 0

## 確認していないこと
- 動画（ナレーションなし）・画像・リンク先（Anthropic ヘルプセンター）の中身
- 【推測】の当否（スキルが見当たらない理由、ネットワーク許可の表示条件）
- 本文に動画キャプションの行が 2 回続けて残っている（README の注意に記載）

## 学習メモとの食い違い
- 学習メモは「15 分」。本文には所要時間が無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
