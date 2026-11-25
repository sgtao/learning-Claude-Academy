###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：研究：生データから統計を検証（★2）
- `title`: 研究：生データから統計を検証（★2）
- `url`: https://academy.claude.com/ja/use-cases/verify-statistics-from-raw-data
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:57+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claudeに論文の原稿と補足データファイルを渡し、報告されたp値・平均値・標準誤差・サンプルサイズ・検定結果をすべて抽出させ、実データで各分析を再実行させる方法を紹介するページ。主張ごとに、論文の記述、データから計算した値、一致の有無の3点を示させ、誤った検定やサンプルサイズの不一致などにフラグを立てさせる。結果は、計算過程のシートと問題のサマリーシートを持つExcelワークブックにまとめさせる。例として、31件中22件が一致、3件が軽微な不一致、6件が要注意という検証結果が載る。続けて、図の確認、警告サインの学習、査読コメントへの変換も依頼できる。本文に見出しはなく、画像（ワークブックのプレビュー）の中身は確認していない。

-----
[toTop](#totoppage)
## 生成AIの総括
### 論文の数字は、生データと突き合わせて初めて信頼できる
- 横断分析：
  - 手順の構造：原稿と生データを渡し、抽出、再実行、3点の比較、ワークブックの順に進める。AIに任せる範囲が、すべての主張を網羅する作業にあることが分かる。
  - 問題の種類：例で見つかったのは、サンプルサイズ、単位、検定の選び方、p値の精度、方法記述の5つ。数字の誤りだけでなく、方法の選び方や説明の食い違いも含まれる。
  - 人間の役割：AIの指摘が本当の誤りか分野の慣行かを見分け、AIが問題なしと言ったときも前提を評価するのは、利用者の専門知識である。
  - 学びの広がり：検証の経験は、生データがない論文での警告サイン探しや、建設的な査読コメントの書き方にもつながる。
- 一言まとめ：Claudeに全件の再計算を任せ、結果の意味づけと最終判断は自分の専門知識で行う。

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
## 解説資料（`Ctrl+Shift+クリック`で開くことをお勧めします）
- [解説スライド](./docs/verify-statistics-from-raw-data-explained-slides.html)
- [スライド原稿](./docs/verify-statistics-from-raw-data-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
