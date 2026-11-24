###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：文書インベントリ
- `title`: 文書インベントリ
- `url`: https://academy.claude.com/ja/use-cases/prep-scattered-documents-for-a-compliance-audit
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:43+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
入力の見出しによる区切りです。

- 1 : [文書インベントリ](./01_source.md#文書インベントリ)
- 2 : [管理領域別のカバレッジ](./01_source.md#管理領域別のカバレッジ)
- 3 : [特定された不足箇所](./01_source.md#特定された不足箇所)

-----
[toTop](#totoppage)
## 概要
この記事は、SOC 2 監査を控えた100件以上の文書が散らばるフォルダを、Cowork で Claude に整理させる使い方を紹介します。フォルダを指定し、監査範囲と管理フレームワークを伝えるだけで、Claude が全ファイルを読み、管理領域別の分類とファイル名の変更案を作り、文書の不足箇所を指摘します。例として156件の確認結果（文書の種類別の件数、領域別のカバレッジ、不足の3点）を示し、スプレッドシート作成・Jira 連携・参照資料づくりという発展と、データの扱いや始め方のコツも紹介します。図は無く、リンク表記に「新しいタブで開きます」という画面表示の残りがあります。

-----
[toTop](#totoppage)
## 生成AIの総括
### 散らかった文書を、中身から整える進め方
- 横断分析：
  - 入力の軽さ：名前や構成を事前に整えなくてよく、必要なのは監査フレームワークと範囲という最小限の情報だけ。
  - 結果の読み方：件数（156件の内訳、領域別の件数）から、少ない領域を見つけ、不足の証拠へと具体化していく流れ。
  - 人の確認：再編成の前に承認を求める設計があり、Claude に任せる部分と、人が決める部分が分かれている。
  - 広がり：同じフォルダ作業から、マトリクス、Web ツールの読み取り、参照資料づくりへ進められる。
- 一言まとめ：範囲を伝えて任せ、不足と再編成案を確かめてから承認するのが、この記事の使い方の核心。

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
- 原本: [00_originals/prep-scattered-documents-for-a-compliance-audit.md](./00_originals/prep-scattered-documents-for-a-compliance-audit.md)
- 解説スライド: [docs/prep-scattered-documents-for-a-compliance-audit-explained-slides.html](./docs/prep-scattered-documents-for-a-compliance-audit-explained-slides.html)（原稿: [docs/prep-scattered-documents-for-a-compliance-audit-explained-slides.md](./docs/prep-scattered-documents-for-a-compliance-audit-explained-slides.md)）
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
