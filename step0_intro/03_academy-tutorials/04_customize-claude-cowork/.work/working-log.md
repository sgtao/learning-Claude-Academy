###### [toTopPage](../../README.md)
###### [toREADME](../README.md)
# 0-6 Claudeをカスタマイズする（Customize Claude）
- 元ページ: https://academy.claude.com/ja/tutorials/customize-claude-cowork（取得: 2026-11-15／取得手段: Academy 日本語版を url-to-md で変換、`direct`）
- 所要（ページ表示）: 7 分（`/learning` の表示＝0-1 と学習メモ。**取得した本文には分数が無い**）　内容の種類: 技術・ハウツー　状態: 完了
- **ステップ 2 の 2-1 と同一ページ**。実体はここ（ステップ 2 には参照用の README だけ置く）

<!-- checks:start -->
## 検査の結果（`tools/page_readme.py` が更新する。最新）
- 確認日: 2026-11-25
- 解説メモ: `check_docs.py`（`--out-dir .work/intermediate`）で 12 PASS
- スライド: 10 枚／lint 0
- 数字の照合: 出典の無い数字 0 件
- リンク切れ: 0 件
- 印の件数: 解説メモの【補足】17・【推測】8、スライドの（要確認: 5
<!-- checks:end -->

## 成果物
| 種類 | ファイル |
|---|---|
| 原本 | [00_originals/customize-claude-cowork.md](../00_originals/customize-claude-cowork.md) |
| 解説メモ（入口） | [customize-claude-cowork_explained/README.md](../README.md) |
| 解説スライド | [customize-claude-cowork-explained-slides.html](../docs/customize-claude-cowork-explained-slides.html)（原稿: [.md](../docs/customize-claude-cowork-explained-slides.md)） |

## 検査（実際に出力した結果）
- 解説メモ: `check_docs.py` 11 PASS / 0 FAIL（サブエージェントは 1 回目から 11 PASS、読み合わせで 3 点を直して再転記と報告。メインが再実行して 11 PASS を確認）／読み合わせ: メインが G-3 として、所要・有料プラン・手順の順序（コネクタ → 指示 → Skill → プラグイン → 追加機能）を原本と照合して食い違い 0。「依頼元の情報」という曖昧な出典の書き方は残っていない
- スライド: 10 枚（本文が約 4,400 字のため 8〜10 枚の目安）／`mdss-convert --strict` の lint は warnings 0・lint 0（メインが再実行）／サブエージェントが撮影した 10 枚のうち 2 枚を修正（リード文の折り返し、steps の番号の二重表示）／出典の無い数字: 0
- 印の件数: `【補足】` 17・`【推測】` 8・`（要確認:` 5（所要時間・必要な有料プラン・管理者以外がコネクタ／プラグインを使えるか・グローバル指示とプロジェクト指示が食い違うときの優先順位・Skill を作るときの依頼文）

## 確認していないこと
- リンク先・動画・画像の中身
- 【推測】の当否。本文は「次の 2 つのレベル」と書いたあとに 3 項目を並べており（理由は本文から分からない）、「こう頼みます：」の直後に頼む文面が無い
- 有料プラン・権限の条件（本文には「エンタープライズでは管理者が組織の設定を行う」という言及だけ）

## 学習メモとの食い違い
- なし（所要 7 分は本文には無いが、`/learning` の表示と学習メモが一致）
- 作成時の気づき（スキル側）: 見出しが 1 つだけの記事（本文の後半にある「プラグインの例」）が「セクション 1 つ」になり、解説メモは同じ節の中を前半・後半に分けて扱った。分割なし扱いの方が自然な場合がある

-----
[toTop](#totoppage)

## 作業の経緯（移行）
- 2026-11-25: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）
- 2026-11-25: README の重複した節「Proposed Prompts」（旧版のスキルが「利用者の追加」として記録していた。「LLM 用プロンプト」と同じリンクだけ）を削除した。check_docs の C-9 が参照する `.work/intermediate/00_manifest.json` の `foreign_sections` からも、この 1 項目だけを外した（検査の側は変えていない）
