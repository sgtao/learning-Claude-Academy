###### [toTopPage](./README.md)
###### [toREADME](./README.md)
# 資料：エンジニアリング：オンコール引き継ぎ（★3）
- `title`: エンジニアリング：オンコール引き継ぎ（★3）
- `url`: https://academy.claude.com/ja/use-cases/oncall-handoff-brief
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:50:00+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
この記事は、Claude Cowork でオンコール引き継ぎブリーフを作る手順を紹介する。Engineering プラグインの `/standup` を出発点に、コネクタ（接続リンク）を設定し、引き継ぎテンプレート・先週のブリーフ・ランブックインデックスを 1 つのフォルダに置いて Cowork に指定する。依頼文では、過去 7 日間のページとインシデントチャンネル、#support-escalations の CS エスカレーション、本番デプロイを対象にし、各項目にステータス・一行の原因・注意点を書かせ、フォルダと #oncall に出力させる。コツは次のとおり（ソース・フィールド・出力先の指定、前回版の添付、ノイズの多いアラートの一覧、ランブックへのリンク）。最後に `/schedule` で毎週の自動実行とスキルの共有を行う。

-----
[toTop](#totoppage)
## 生成AIの総括
### 引き継ぎを「毎回同じ形で、忘れずに」届ける仕組みにする
- 横断分析：
  - 指定の力：見る場所（ページ・CS エスカレーション・デプロイ）、書く項目（ステータス・原因・注意点）、出す先（フォルダと #oncall）を依頼文で名指しすることが、結果の質を決める。
  - 文脈の力：テンプレート、先週のブリーフ、ランブックインデックスを 1 つのフォルダに入れておくと、前回の「監視中」が引き継がれ、受け取る人が使う形に揃う。
  - 一文足す力：ノイズの多いアラートの一覧やランブックのリンクを足すだけで、引き継ぎが整理のバックログや修正への入口にも変わる。
  - 仕組み化の力：スキル化・`/schedule`・共有で、書き忘れや人ごとの差を防ぎ、誰も手探りでシフトを始めずに済む。
- 一言まとめ：Cowork に「どこを見て、何を書き、どこへ出し、前回の何を持ち越すか」を決めて渡し、毎週の自動実行にすれば、疲れていても同じ品質の引き継ぎが届く。

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
- 状態: 検査済み（2026-11-25 時点。解説メモ 12 PASS／スライド 9 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/oncall-handoff-brief.md](./00_originals/oncall-handoff-brief.md)
- 解説スライド: [docs/oncall-handoff-brief-explained-slides.html](./docs/oncall-handoff-brief-explained-slides.html)（原稿: [docs/oncall-handoff-brief-explained-slides.md](./docs/oncall-handoff-brief-explained-slides.md)）
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
