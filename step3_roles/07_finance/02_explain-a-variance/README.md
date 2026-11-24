###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：財務：差異を説明（★1）
- `title`: 財務：差異を説明（★1）
- `url`: https://academy.claude.com/ja/use-cases/explain-a-variance
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:51+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude の Finance プラグインにある `/variance-analysis` を使い、月次レビュー用の差異コメンタリーを Claude Cowork で作る手順を紹介する記事。実績・前期・予算・勘定科目表のファイルを 1 つのフォルダに置いて Cowork に指定し、「10%または5万ドル」を超えて変動した行について、何が変動しなぜそうなったかを経営層向けに書かせる。要点は、しきい値・読み手・出力先・参考例・不確実な点の指摘という 5 つの指定。最後に、作業内容のスキル化、アーティファクトとしての公開、`/schedule` による定期実行、チームでの共有へと進む。注意：本文は HTML から直接変換したもので、図は再現されていない。「接続」だけのリンク行など、ページ部品の名残が本文に残っている。

-----
[toTop](#totoppage)
## 生成AIの総括
### 基準と読み手を先に伝えて、繰り返せる仕組みにする
- 横断分析：
  - 指定が出来栄えを決める：しきい値・読み手・出力先・参考例・不確実な点の指摘の 5 つは、どれも「Claude に何を省き、誰に向けて、どの形で書くか」を先に決める指定である。
  - 一度の作業を仕組みに変える：1 回の依頼で終わらせず、スキル化・公開・定期実行・共有へ進めることで、毎月のクローズが同じ基準で回る。
  - 場所が作業を支える：1 つのフォルダに材料を置き、結果もそこに書き戻させる形が、プロジェクト化・定期実行・共有のすべての土台になっている。
  - 人の判断が残る場所：要因が明確でない行を Claude に指摘させ、人が深掘りする分担が、人の確認を前提にした部分と読める【推測】。
- 一言まとめ：Claude には基準・読み手・出力先を先に伝え、うまくいったやり方はスキルにして毎月のクローズで再利用する。

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
- 原本: [00_originals/explain-a-variance.md](./00_originals/explain-a-variance.md)
- 解説スライド: [docs/explain-a-variance-explained-slides.html](./docs/explain-a-variance-explained-slides.html)（原稿: [docs/explain-a-variance-explained-slides.md](./docs/explain-a-variance-explained-slides.md)）
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
