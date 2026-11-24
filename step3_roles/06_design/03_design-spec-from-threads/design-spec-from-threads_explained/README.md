###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：(無題)
- `title`: (無題)
- `url`: https://academy.claude.com/ja/use-cases/design-spec-from-threads
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:50+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude Coworkを使い、散らばったデザインの議論（エクスポートしたSlackスレッド、会議メモ、スクリーンショット）を1つのデザイン仕様書にまとめる手順の記事です。ファイルを1つのフォルダに集めてCoworkに指定し、問題・目標・制約・提案する解決策・未解決の質問・対象外という構成で依頼します。コツとして、セクション順序の指定、出典の引用、矛盾の指摘、お手本の追加、不確実な点の指摘の依頼が挙げられています。さらに、作業をスキルにして保存し、アーティファクトとして公開し、/scheduleで平日朝に自動更新する流れも紹介されます。本文に見出しは無く、セクションは分けていません。

-----
[toTop](#totoppage)
## 生成AIの総括
### 散らばった議論を、更新される1枚の仕様書にする
- 横断分析：
  - 集約：スレッド、メモ、スクリーンショットを1つのフォルダに置くだけで、形式の違う材料が1つの読み取りの対象になる。
  - 指定：構成・出典・矛盾の指摘を最初の依頼で指定すると、出力が並べ替え不要になり、蒸し返しも減る。
  - 再利用：1回きりの依頼で終わらせず、スキルにして保存すると、自分の基準が以降の実行に組み込まれる。
  - 鮮度：公開リンクと/scheduleの組み合わせで、仕様書が古くなる問題に対処できる。
- 一言まとめ：材料を集め、頼み方を決め、スキルにして、毎朝更新させる。

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
