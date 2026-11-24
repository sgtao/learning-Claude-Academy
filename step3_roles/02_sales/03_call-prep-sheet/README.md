###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：営業：商談準備（★2）
- `title`: 営業：商談準備（★2）
- `url`: https://academy.claude.com/ja/use-cases/call-prep-sheet
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:40+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
商談前に確認できる準備シートを、Claude に作らせる手順を紹介する記事。Sales プラグインの `/call-prep` などの Skills が出発点だが、記事のプロンプトはプラグインなしでも動く。相互アクションプラン・自分のメモ・提案書を 1 つのフォルダに集め、Salesforce のレコードや直近 3 件の Gong の文字起こしと合わせて読ませる。シートには、商談の現状、相手が重視していること、依頼事項、想定される反論と回答が載る。うまくいった内容は `/call-prep-sheet` という Skill に保存し、平日の朝のスケジュール済みタスクで自動実行して、チームで共有できる。図は無い。

-----
[toTop](#totoppage)
## 生成AIの総括
### 1 回の依頼を、毎朝届く共通の型にする
- 横断分析：
  - 材料：CRM の項目だけでなく、フォルダの自分の文書と直近の文字起こしを読ませるので、シートは実際の商談に寄る。
  - 設計：依頼事項と反論の回答を指定するので、シートは読む資料ではなく動くための計画になる【補足】。
  - 確認：フラグで不確かな点を先に見せるので、人が確かめる場所が絞られる。
  - 仕組み化：Skill とスケジュール実行で、1 回の成功が毎朝の習慣と全員の共通の形式になる。
- 一言まとめ：材料を絞って 1 回作り、型にして朝に届け、全員で共有する。

-----
[toTop](#totoppage)
## 本文
- [01_source.md](./01_source.md)：入力 Markdown の複製（本文は変更していません）

-----
[toTop](#totoppage)
## 解説メモ
- [02_explanation_memo.md](./02_explanation_memo.md)

-----
[toTop](#totoppage)
## FAQ
- [11_question_and_answer.md](./11_question_and_answer.md)

-----
[toTop](#totoppage)
## LLM 用プロンプト
- [12_LLM_prompts_as_guide.md](./12_LLM_prompts_as_guide.md)

-----
[toTop](#totoppage)
<!-- page-status:start -->
## 状態と関連資料
- 状態: 検査済み（2026-11-25 時点。解説メモ 12 PASS／スライド 10 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/call-prep-sheet.md](./00_originals/call-prep-sheet.md)
- 解説スライド: [docs/call-prep-sheet-explained-slides.html](./docs/call-prep-sheet-explained-slides.html)（原稿: [docs/call-prep-sheet-explained-slides.md](./docs/call-prep-sheet-explained-slides.md)）
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
