###### [toTopPage](../../../../README.md)
###### [toREADME](../../README.md)
# 0-5 Claude Coworkで最初のタスクを委任する（Delegating your first task to Claude）
- 元ページ: https://academy.claude.com/ja/tutorials/delegating-your-first-task-in-claude-cowork（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 4 分（本文の先頭に「· 4 min」の表示あり。`/learning` の表示も 4 分）　内容の種類: 技術・ハウツー　状態: 完了
- 題名に旧名称「Cowork」が残っている（学習メモの付録 D）。**旧名称かどうかは原本では確認できない**ので、解説・スライドでは【補足】として学習メモの付録 D に基づくと明記した

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】8・【推測】1、スライドの（要確認: 0
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/delegating-your-first-task-in-claude-cowork.md](../00_originals/delegating-your-first-task-in-claude-cowork.md) |
| 解説メモ（入口） | [delegating-your-first-task-in-claude-cowork_explained/README.md](../README.md) |
| 解説スライド | [delegating-your-first-task-in-claude-cowork-explained-slides.html](../docs/delegating-your-first-task-in-claude-cowork-explained-slides.html)（原稿: [.md](../docs/delegating-your-first-task-in-claude-cowork-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（サブエージェントは 2 回目で合格と報告。1 回目は C-8 で、本文に無い引用「どこまで Claude が動くか」。メインが再実行して 11 PASS を確認）／読み合わせ: メインが G-3 として、プラン条件（Pro・Max・Team・Enterprise 向け、macOS・Windows の Claude Desktop で一般提供）・所要（4 min）を原本と照合して食い違い 0。出典の書き方「依頼元の情報」を実際の出典（学習メモの付録 D）に直し、`out/` を直して `assemble.py` をやり直し、11 PASS を再確認
- スライド: 10 枚（本文が約 800 字を超えるため 8〜10 枚の目安）／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行。出典の直しのあとの HTML 再生成でも 10 枚）／サブエージェントが撮影した 10 枚を目視し、1 枚（基本ループの図と帯の重なり）を修正／出典の無い数字: 0（`03` は note 内の解説メモの参照）
- 印の件数: `【補足】` 8・`【推測】` 1・`（要確認:` 0

## 確認していないこと
- リンク先・動画・画像の中身
- スライド 7 の基本ループ（提案 → 調整 → 承認 → 実行）の「実行のあとに提案へ戻るか」は原本に無い（note に記載）

## 学習メモとの食い違い
- なし（所要 4 分は本文の「· 4 min」・`/learning` の表示・学習メモが一致）

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
