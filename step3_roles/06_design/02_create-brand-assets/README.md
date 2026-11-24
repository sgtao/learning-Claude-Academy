###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：一貫した品質のために[Skill（新しいタブで開きます）](https://www.anthropic.com/news/skills)を作成する
- `title`: 一貫した品質のためにSkill（新しいタブで開きます）を作成する
- `url`: https://academy.claude.com/ja/use-cases/create-brand-assets
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:48+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
入力の見出しによる区切りです。

- 1 : [一貫した品質のためにSkill（新しいタブで開きます）を作成する](./01_source.md#一貫した品質のためにskill新しいタブで開きますを作成する)

-----
[toTop](#totoppage)
## 概要
この記事は、Claudeで名刺やチラシなどの印刷用ブランド素材を作る方法を、コーヒーショップ「Morning Ritual」の例で説明します。ブランドガイドライン（書体・配色・余白・雰囲気）をアップロードし、必要な素材・寸法・印刷仕様と、重なりやはみ出しを自己点検させる指示を最初のプロンプトに入れるのが要点です。成果物は名刺PDF、角丸のQRコード、チラシPDFです。その後、会話から参照用のブランドガイドラインを作り、同じ雰囲気のHTMLページへ広げ、最後にSkill化して再利用します。記事にある成果物の画像の中身は読めていないため、図に基づく記述はしていません。

-----
[toTop](#totoppage)
## 生成AIの総括
### 基準を渡し、点検まで頼み、成果を使い回す

- 横断分析：
  - 入力の質：言葉で説明するより、ガイドラインや見本を渡すほうが、書体・色・余白・雰囲気がそろう。
  - 出力の質：寸法・印刷仕様に加えて、自己採点と点検項目を最初に頼むと、修正の回数が減る。
  - 成果の使い回し：会話はリファレンスドキュメントになり、手順は Skill になって、次の依頼で説明し直さずに済む。
  - 広がり：印刷物で決めた雰囲気を、同じ基準で HTML ページなどのオンライン素材へ広げられる。
- 一言まとめ：基準を先に渡し、点検まで頼み、うまくいった形は Skill にして使い回す。

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
- 原本: [00_originals/create-brand-assets.md](./00_originals/create-brand-assets.md)
- 解説スライド: [docs/create-brand-assets-explained-slides.html](./docs/create-brand-assets-explained-slides.html)（原稿: [docs/create-brand-assets-explained-slides.md](./docs/create-brand-assets-explained-slides.md)）
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
