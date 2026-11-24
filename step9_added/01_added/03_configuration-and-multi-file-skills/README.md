###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：設定とマルチファイルSkills
- `title`: 設定とマルチファイルSkills
- `url`: https://academy.claude.com/ja/tutorials/configuration-and-multi-file-skills
- `source_format`: html
- `retrieved_at`: 2026-11-24T07:47:25+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
<!-- slides:start -->
## 解説資料
- [解説スライド](./docs/configuration-and-multi-file-skills-explained-slides.html)
- [スライド原稿](./docs/configuration-and-multi-file-skills-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude Code で skill を設定する方法と、マルチファイルの skill の構造の扱い方を扱う動画のページ（4 分）。本文は 1 文の説明と、動画の訂正の注記だけで、本文が短い。訂正は、動画で allowed-tools が Claude の使えるツールを制限すると述べている箇所（0:40、1:20、3:35）が誤りで、実際には、リストしたツールを事前に承認するものだと書いている。ツールを取り除くには disallowed-tools を使う。手順やファイルの書き方は本文に無いので、解説は動画の内容を書いていない（注意点として扱う）。ナビとフッターは除いた。

-----
[toTop](#totoppage)
## 生成AIの総括
### 訂正を正しく読み、承認と取り除きを使い分ける
- 横断分析：
  - 訂正：動画の「制限」は誤りで、allowed-tools は事前承認である
  - 使い分け：確認なしにするなら allowed-tools、取り除くなら disallowed-tools
  - 限界：手順と、マルチファイルの構造は本文に無い。動画を見て確かめる必要がある
- 一言まとめ：この本文は訂正の注記が中心なので、動画を見る前にこの意味の違いを押さえる

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
- 状態: 検査済み（2026-11-25 時点。解説メモ 11 PASS／1 FAIL／スライド 7 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/configuration-and-multi-file-skills.md](./00_originals/configuration-and-multi-file-skills.md)
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
