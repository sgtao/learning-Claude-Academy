###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：データ：アドホックなデータ質問に答える（★1）
- `title`: データ：アドホックなデータ質問に答える（★1）
- `url`: https://academy.claude.com/ja/use-cases/answer-the-adhoc
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:50:01+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
<!-- slides:start -->
## 解説資料
- [解説スライド](./docs/answer-the-adhoc-explained-slides.html)
- [スライド原稿](./docs/answer-the-adhoc-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
アドホックなデータ質問に Claude で答える手順の解説です。Dataプラグイン（/write-query など）があれば出発点になり、無くてもプロンプトは動くとされています。コネクタでツールとつなぎ、スキーマのエクスポートやdbtモデルなどを1つのフォルダにまとめて渡すと、実際のテーブル名に沿った SQL と回答メモがそのフォルダに書き戻されます。サンプルは EMEA の粗利益率が下がった理由を尋ねる質問で、要因の内訳とチャート仕様まで求めます。最後に、やったことを /adhoc-answer という Skill にし、平日は毎時のスケジュール済みタスクで下書きを作らせ、アナリスト全員で共有して数値をそろえます。なお本文は直接変換で、画像・リンク先の中身は読めていません。本文には「接続」と書かれたリンクだけの行が残っています。

-----
[toTop](#totoppage)
## 生成AIの総括
### 質問を型にして、下書きまで自動で回す
- 横断分析：
  - 入力を整える：質問はそのまま貼り、資料は1つのフォルダにまとめることで、Claude が相手の言葉と実際のテーブル名に沿って答えられるようにしている。
  - 出力を再利用する：SQL と回答メモに加えてチャート仕様まで求め、次回は質問者が自分で更新できる成果物にしている。
  - 手順を資産にする：うまくいった作業を /adhoc-answer という Skill にし、スケジュール済みタスクで新しい質問に自動で当てている。
  - 人の役割を残す：下書きを用意させる設計で、送り返す前のレビューは人が行う。フラグの依頼で、確認の優先順位も付く。
- 一言まとめ：質問と資料を整えて Skill にし、下書きの自動化と共有までつなげれば、誰に聞いても同じ数値で答えられる。

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
- 状態: 検査済み（2026-11-25 時点。解説メモ 11 PASS／1 FAIL／スライド 10 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/answer-the-adhoc.md](./00_originals/answer-the-adhoc.md)
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
