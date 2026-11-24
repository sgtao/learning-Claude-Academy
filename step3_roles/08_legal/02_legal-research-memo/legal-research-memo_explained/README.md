###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：法務：法律リサーチ（★1）
- `title`: 法務：法律リサーチ（★1）
- `url`: https://academy.claude.com/ja/use-cases/legal-research-memo
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:54+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude Cowork で法律リサーチメモを作る手順を紹介するページです。Litigation Legal プラグインを出発点に、リサーチ依頼・関連する事実・過去のメモを 1 つのフォルダにまとめて Cowork に渡し、提示された質問・簡潔な回答・議論・未解決の論点という構成で、すべての命題に出典を付けたメモを作らせます。うまくいくプロンプトの工夫を 6 つ挙げ、最後に同じやり方を /research-memo スキルとして保存し、/schedule で平日午前 9 時に新しい依頼へ自動実行させる方法まで説明します。本文は HTML から直接変換されたもので、見出しが無く、ボタンのリンク文字が前後の文脈なしに残っています。図は含まれません。

-----
[toTop](#totoppage)
## 生成AIの総括
### 出典と確認箇所をはっきりさせて、手順ごと仕組みにする
- 横断分析：
  - 確認できる形にする：出典の指定・すべての命題への引用・不確実な点のフラグは、どれも「あとで人が何を確かめればよいか」を見えるようにするための工夫である。
  - 材料を先に渡す：依頼・事実・過去のメモを 1 つのフォルダに入れることで、メモは一般論ではなく自分の状況に当てはまる形になる。
  - 一度うまくいった手順を残す：同じやり方を /research-memo スキルとして保存し、/schedule で予約すると、毎回の頼み方に頼らず同じ品質の初稿が出る。
  - 使う前に自分の条件を確かめる：ローカルかクラウドか、Team・Enterprise か Pro・Max かで、ファイルの扱いが変わる。
- 一言まとめ：材料を渡し、出典と不確実さを見える形にして頼み、うまくいった型をスキルと予約で回す。

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
