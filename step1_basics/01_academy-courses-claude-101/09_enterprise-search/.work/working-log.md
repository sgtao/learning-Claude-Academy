###### [toTopPage](../../README.md)
###### [toREADME](../README.md)
# 1-9 Enterprise Search（Claude 101 レッスン 9）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/enterprise-search（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 15 分（学習メモの値。**取得した本文には分数が無い**）　内容の種類: 学習・ビジネス　状態: 完了

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】14・【推測】3、スライドの（要確認: 0
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/enterprise-search.md](../00_originals/enterprise-search.md) |
| 解説メモ（入口） | [enterprise-search_explained/README.md](../README.md) |
| 解説スライド | [enterprise-search-explained-slides.html](../docs/enterprise-search-explained-slides.html)（原稿: [.md](../docs/enterprise-search-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目から 11 PASS。読み合わせで総括の「使いながら足していく設計」という本文に無い言い切りを「あとからいつでも追加できる」に直して再転記。利用上限で一度停止し、再開して完了／読み合わせ G-3（メイン）: プラン条件（Team・Enterprise 向け。すべての Team・Enterprise 組織で既定有効だが、チームメンバーが使う前にオーナーが初期セットアップを完了する必要がある。2 段階のセットアップ）と管理者 6 手順・利用者 4 手順の順序を原本と照合して食い違い 0／README の概要 332 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち 3 枚を修正（図解のラベル重なり、point の帯とカードの重なり、steps の番号の二重表示）／出典の無い数字: 0（なし は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 14・`【推測】` 3・`（要確認:` 0

## 確認していないこと
- ページの動画・画像・リンク先（ヘルプセンター）の中身
- 本文の「管理者」と「オーナー」が同じ人かどうか（【推測】のまま）
- 解説メモ一式へのスライドの出典リンクは URL ではなくユーザー提供の記載

## 学習メモとの食い違い
- 学習メモは「Team・Enterprise 向け・15 分」。Team・Enterprise 向けは本文と一致。本文には所要時間が無く、解説・スライドには分数を書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
