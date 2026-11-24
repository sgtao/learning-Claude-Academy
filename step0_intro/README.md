###### [toTopPage](../README.md)
###### [toREADME](../README.md)
# 11_step0 — ステップ 0：入口（講義メモ・解説スライド）

学習メモ（[02_learning-memo.md](../../01_sources/11_ref-effective-Claude-Learning/02_learning-memo.md)）のステップ 0。`/learning` を開き、Intro to Claude と Cowork の最初の 3 本を読み、Claude 101 の入口を確かめる。
ページごとに、**解説メモ 5 本（README・01_source・02_explanation_memo・11_question_and_answer・12_LLM_prompts_as_guide）と解説スライド**を作った（作成日 2026-11-15。作り方は [../instruction.md](../../01_sources/11_ref-effective-Claude-Learning/instruction.md)）。

- ねらい: 全体をつかむ
- 自己チェック（学習メモ）: **Claude に自分の言葉で最初の依頼を出せた**
- 目安時間（学習メモ）: 約 20〜30 分

## 台帳

<!-- ledger:start -->
| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |
|---|---|---|---|---|---|---|
| 0-1 | [学ぶ（/learning 入口）](01_claude-ai-learning/01_learning/README.md) | － | 学習・ビジネス | 完了 |  | Chrome で読む。ボタンは押さない |
| 0-2 | [Claude 101（コースのトップ）](02_academy-courses-claude-101/01_claude-101/README.md) | 150 | 学習・ビジネス | 完了 |  |  |
| 0-3 | [Claudeを使い始める](03_academy-tutorials/01_getting-started-with-claude/README.md) | 5 | 技術・ハウツー | 完了 |  |  |
| 0-4 | [Coworkを3つのステップで始める](03_academy-tutorials/02_get-started-in-claude-cowork-in-three-steps/README.md) | 4 | 技術・ハウツー | 完了 |  | 旧名称の題名 |
| 0-5 | [Coworkで最初のタスクを委任する](03_academy-tutorials/03_delegating-your-first-task-in-claude-cowork/README.md) | 4 | 技術・ハウツー | 完了 |  | 旧名称の題名 |
| 0-6 | [Claudeをカスタマイズする](03_academy-tutorials/04_customize-claude-cowork/README.md) | 7 | 技術・ハウツー | 完了 |  | 2-1 と同じページ（実体はここ） |
<!-- ledger:end -->

「修正回数」はサブエージェントが報告した、合格した往復の番号（2＝読み合わせで直して再転記した）。「解説メモ」の PASS はメインが `check_docs.py` を再実行して確認した結果。

## まとまり

| まとまり | ページ |
|---|---|
| [01_claude-ai-learning/](./01_claude-ai-learning/README.md) | 0-1 |
| [02_academy-courses-claude-101/](./02_academy-courses-claude-101/README.md) | 0-2 |
| [03_academy-tutorials/](./03_academy-tutorials/README.md) | 0-3・0-4・0-5・0-6 |

## ステップの関門（S-1〜S-6）

| # | 結果 | 内容 |
|---|---|---|
| S-1 | 合格 | 台帳 6 行すべてに状態と検査結果がある（未着手 0）。薄いページ 0・失敗 0 |
| S-2 | 合格（差の記録あり） | ページ表示の分数の合計は、チュートリアル 4 本で 5＋4＋4＋7＝**20 分**。学習メモの目安「約 20〜30 分」の下限と一致（0-1 の閲覧と「作成」ボタンを試す時間が加わる）。0-2 の「約 150 分」はステップ 1 の時間でここには含めない |
| S-3 | 合格（後述） | 自己チェックの項目を、どのページで確かめられるか対応づけた |
| S-4 | 合格 | 有料プランの条件が README・ページで一致（Cowork は Pro・Max・Team・Enterprise。0-2 と 0-5 が一致。0-3 の Dashboards は「有料プラン」のみで、どのプランかは本文に無い）。Enterprise Search（Team・Enterprise）は 0-2 に記載 |
| S-5 | 合格 | 相対リンクの確認で切れ 0（下記の確認コマンド） |
| S-6 | 合格 | 下の「確認していないこと」「食い違い」に記載 |

### S-3：自己チェック「Claude に自分の言葉で最初の依頼を出せた」

| 確かめたいこと | 読むページ |
|---|---|
| 最初のプロンプトの書き方（完璧でなくてよい。通常の言葉で頼む。不明点は Claude に質問させる） | 0-3 の [解説メモ](./03_academy-tutorials/01_getting-started-with-claude/02_explanation_memo.md)・[スライド](./03_academy-tutorials/01_getting-started-with-claude/docs/getting-started-with-claude-explained-slides.html) |
| 最初のタスクをまるごと任せる流れ | 0-5 の [解説メモ](./03_academy-tutorials/03_delegating-your-first-task-in-claude-cowork/02_explanation_memo.md) |
| 自分の設定（コネクタ・指示・Skill）を整える | 0-6（ステップ 2 でも使う） |
| 全体の道筋（どこから学ぶか） | 0-1・0-2 |

**ページからは確かめられないこと**: 「自分の言葉で最初の依頼を実際に出せたか」は、ユーザーが自分のアカウントで 1 件試して確かめる。各ページの解説メモの「活用案」と、スライドの「次に試す 1 件」が出発点になる。

## 食い違い（記録。どちらも直していない）

- 分数: 0-2〜0-6 の**本文には分数が無い**（0-5 だけ「· 4 min」の表示）。分数は `/learning`（0-1）の表示と学習メモによる。0-2 の「約 150 分」「13 レッスン」も本文に無い
- 題名の「Cowork」が旧名称かどうかは、原本（ページ本文）では確認できない。学習メモの付録 D の記述に基づく

## 用語の揺れ（H-2。原本の表記に合わせ、言い換えていない）

| 概念 | 表記 | 見られるページ |
|---|---|---|
| Skills | 「Skill」「スキル」 | 0-2・0-6 は Skill、0-3・0-4 は スキル |
| Connectors | 「Connectors」「コネクタ」 | 0-2 は Connectors、0-3〜0-6 は コネクタ |
| Artifacts | 「Artifacts」「アーティファクト」 | 0-1・0-2・0-6 は Artifacts、0-3 は アーティファクト |
| デスクトップアプリ | 「デスクトップアプリ」「Claude Desktop」 | 0-2〜0-4 は デスクトップアプリ、0-5 は Claude Desktop |
| Projects | 「プロジェクト」 | 全ページ共通（Projects の英語表記は無い） |

## 確認していないこと

- 各ページのリンク先（support.claude.com など）・動画・画像の中身。ページに動画があっても字幕は取っていない
- `/learning` のボタン（「作成」の 3 つ・学習チェックイン）の実際の動作（押していない）。ログイン状態による表示の違い
- 各ページの手順を実際に操作した結果
- 【推測】・【補足】の当否。読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）。数字・プランの条件は、最後は公式ページで確かめる
- 解説スライドの見た目: サブエージェントが全枚を撮影して確認。メインは 0-1 の 2 枚だけを目視

## 作り方の記録

- 取得: Academy 5 ページは `url-to-md`（日本語版）、`/learning` は Claude in Chrome。薄いページ（本文 300 字未満）は 0 件
- 作成: ページごとに `craft-explanation-docs`（v0.0.6）→ `websearch-slide-ja`（`mdss-convert` v0.6.1）をサブエージェントで実行（最大 3 並列）。1 ページあたり約 4〜6 分
- 検査: サブエージェントの報告を信じず、メインが `check_docs.py`・`mdss-convert --strict`・数字照合・原本との照合を再実行

## 次のステップ

[../instruction.md](../../01_sources/11_ref-effective-Claude-Learning/instruction.md) の「3-1」のプロンプトで、ステップ 1（`12_step1/`）を実行する。

-----
[toTop](#totoppage)
