###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：エンジニアリング：設計書（RFC）（★1）
- `title`: エンジニアリング：設計書（RFC）（★1）
- `url`: https://academy.claude.com/ja/use-cases/design-doc
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:58+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
<!-- slides:start -->
## 解説資料
- [解説スライド](./docs/design-doc-explained-slides.html)
- [スライド原稿](./docs/design-doc-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claude に設計ドキュメント（RFC）の下書きを作らせる手順を示した記事です。Engineering プラグインの `/system-design` が出発点で、使えないときもプロンプトだけで進められます。RFC テンプレートや過去の RFC、1 ページ概要、アーキテクチャ図を 1 つのフォルダに置いて Claude に読ませ、プロジェクトにします。依頼例は、イベントパイプラインをバッチ処理からストリーミングへ移行する設計ドキュメントで、問題・目標と非目標・2〜3 件のアプローチ・推奨案・未解決の課題を求めます。最後に、ここまでの内容を `/rfc-draft` という Skill に保存し、平日の午前 9 時に inbox の 1 ページ概要を下書きへ変えるスケジュール済みタスクを設定します。本文に見出しと図はありません。

-----
[toTop](#totoppage)
## 生成AIの総括
### 構成と調査は任せ、判断は人が持つ
- 横断分析：
  - 分担：Claude は構成と調査、人は「私にしかわからない部分」の記入と判断を担う。依頼文でも、この分担を先に宣言する。
  - 材料の集め方：テンプレート・過去の RFC・概要メモ・図を 1 つのフォルダとプロジェクトにまとめ、出力の形と文体を自分たちのものに合わせる。
  - 繰り返しの仕組み化：うまくいった依頼を Skill に保存し、スケジュール済みタスクで自動実行する。再現性が高まる。
  - 疑う仕掛け：2〜3 件のアプローチと、不確かな点のフラグで、鵜呑みにせずにレビューできる。
- 一言まとめ：Claude に材料と型を渡して初稿を任せ、人は判断とレビューに時間を使う。

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
- 状態: 検査済み（2026-11-25 時点。解説メモ 11 PASS／1 FAIL／スライド 10 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/design-doc.md](./00_originals/design-doc.md)
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
