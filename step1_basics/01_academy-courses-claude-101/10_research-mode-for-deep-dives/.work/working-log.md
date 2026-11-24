###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 1-10 深掘り調査のためのリサーチ機能（Claude 101 レッスン 10）
- 元ページ: https://academy.claude.com/ja/courses/claude-101/research-mode-for-deep-dives（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 10 分（学習メモの値。**取得した本文には分数が無い**。本文の「数分かそれ以上」は 1 回のリサーチにかかる時間で、レッスンの所要ではない）　内容の種類: 学習・ビジネス　状態: 完了

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
| 原本 | [00_originals/research-mode-for-deep-dives.md](../00_originals/research-mode-for-deep-dives.md) |
| 解説メモ（入口） | [research-mode-for-deep-dives_explained/README.md](../README.md) |
| 解説スライド | [research-mode-for-deep-dives-explained-slides.html](../docs/research-mode-for-deep-dives-explained-slides.html)（原稿: [.md](../docs/research-mode-for-deep-dives-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（メインが再実行）／サブエージェントの修正: 1 回目は 9 PASS / 2 FAIL（C-6 概要 403 字、C-8 本文に無い「」の引用 3 件）。概要を短くし `out/03` の「」を外して再転記。読み合わせで「だれが」の断定を【推測】付きに直して再転記し、2 回目で 11 PASS。利用上限で一度停止し、再開して完了／読み合わせ G-3（メイン）: 本文にプラン条件は無いことを原本と照合（本文の時間の記述は「数分かそれ以上」のみ）。依頼文にあった「（有料）」は本文に無いため事実として書かれていないことを確認／README の概要 364 字（上限 400）
- スライド: 10 枚／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚で修正なし／出典の無い数字: 0（`03`・`05` は note 内の解説メモの参照番号で数値ではない）
- 印の件数: `【補足】` 13・`【推測】` 1・`（要確認:` 1（利用できるプラン・権限の条件。原本には書かれていない）

## 確認していないこと
- 動画チュートリアルとヘルプセンターのリンク先の中身
- 利用できるプラン・権限の条件（本文に無い。スライド 9 に要確認）
- 【推測】の当否

## 学習メモとの食い違い
- 学習メモは「有料・10 分」。このレッスンの本文には有料プランの記述も所要時間も無い。なお 0-2（Claude 101 のコースのトップ）の本文には「Cowork と Research 機能は有料プラン（Pro・Max・Team・Enterprise）が必要」とあり、そちらが学習メモの「有料」の根拠。解説・スライドには、このレッスンの本文に無い条件は書いていない

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
