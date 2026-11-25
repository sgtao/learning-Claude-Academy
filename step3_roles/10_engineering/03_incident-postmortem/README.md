###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：エンジニアリング：ポストモーテム（★2）
- `title`: エンジニアリング：ポストモーテム（★2）
- `url`: https://academy.claude.com/ja/use-cases/incident-postmortem
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:59+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude Cowork を使い、インシデント後のポストモーテムのドラフトを作る手順を紹介する記事です。Engineeringプラグインの/incident-responseなどが出発点になります。まず Customize → Connectors で Slack・PagerDuty・Datadog を接続し、テンプレートやランブックなどを1つのフォルダにまとめて Cowork に指定します。次にインシデントのチャンネルを示し、時系列の再構築、顧客への影響の要約、根本原因と寄与要因、担当者つきのアクションアイテムを、ブレームレスで依頼します。プロンプトの工夫点6つ、スキル化、/schedule による平日午後6時の自動ドラフトも述べます。本文に見出しと図はありません。

-----
[toTop](#totoppage)
## 生成AIの総括
### 記憶ではなく証拠から、責めずに書く
- 横断分析：
  - 材料の渡し方：コネクタ（Slack・PagerDuty・Datadog）とフォルダで、テンプレートや記録をそろえてから依頼する。
  - 依頼の仕方：要約ではなく再構築、単一原因ではなく根本原因と寄与要因、というように、出力の形を指定する。
  - 書き方の姿勢：ブレームレスを明示し、システムの挙動だけを書かせることで、文書がレビューに耐える。
  - 運用への広げ方：1 回の依頼をスキルにし、/schedule で定時に動かして、チームで同じ方法を共有する。
- 一言まとめ：材料と書き方の基準を先に渡せば、Cowork は証拠に基づく責めない下書きを、レビュー前に用意してくれる。

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
<!-- slides:start -->
## 解説資料（別タブで開きます）
- [解説スライド](./docs/incident-postmortem-explained-slides.html)
- [スライド原稿](./docs/incident-postmortem-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
