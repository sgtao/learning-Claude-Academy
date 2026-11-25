###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：営業：通話記録テーマ抽出（★3）
- `title`: 営業：通話記録テーマ抽出（★3）
- `url`: https://academy.claude.com/ja/use-cases/transcript-themes
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
Salesプラグインの /call-summary を出発点に、通話のトランスクリプトを Claude Cowork に読ませ、顧客の発言をテーマごとにまとめる手順を紹介する記事です。トランスクリプトや過去のブリーフを 1 つのフォルダに集め、各テーマの件数・最良の一行引用・発言したアカウントを入れた 1 ページのブリーフを、プロダクトチームとマーケティングチーム向けに書き出させます。プロンプトの工夫として、根拠・対象読者・長さの上限・フォルダ・手本・不確実な点の指摘が挙げられ、最後にスキル化と /schedule による定期実行、チームでの共有が示されます。本文に見出しは無く、画像もありません。冒頭の説明とコネクタの「接続」リンクは、ページ上のボタンの残りです。

-----
[toTop](#totoppage)
## 生成AIの総括
### 一度のフォルダ作業を、基準つきの定期ブリーフに育てる

- 横断分析：
  - 手順の構造：フォルダ → 依頼 → 6 つの工夫 → スキル化 → 定期実行 → 共有、と、一回きりの作業が少しずつ仕組みに変わる。
  - 根拠の考え方：件数・最良の一行引用・アカウントを必ず付けさせ、各テーマを顧客の言葉まで追えるものにする。
  - 絞り込みの考え方：読み手と 1 ページの上限を決めることで、順位付けと行動に移せる内容が先頭に来る。
  - 共有の考え方：【補足】テーマ名と書式をスキルに入れて配ると、地域や担当者が違っても同じ言葉で話せます。
- 一言まとめ：集めて、根拠つきで絞り、スキルと定期実行で回し、同じテーマ名で共有する。

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
- [解説スライド](./docs/transcript-themes-explained-slides.html)
- [スライド原稿](./docs/transcript-themes-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
<!-- page-status:start -->
## 状態と関連資料
- 状態: 検査済み（2026-11-25 時点。解説メモ 12 PASS／スライド 9 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/transcript-themes.md](./00_originals/transcript-themes.md)
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
