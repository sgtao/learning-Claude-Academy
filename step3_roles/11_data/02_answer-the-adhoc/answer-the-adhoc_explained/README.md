###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：(無題)
- `title`: (無題)
- `url`: https://academy.claude.com/ja/use-cases/answer-the-adhoc
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:50:01+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

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
