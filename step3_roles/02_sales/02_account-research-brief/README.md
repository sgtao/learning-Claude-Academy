###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：営業：アカウントリサーチ（★1）
- `title`: 営業：アカウントリサーチ（★1）
- `url`: https://academy.claude.com/ja/use-cases/account-research-brief
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:39+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Claudeに、Salesforce・最近のニュース・10-K・役員のLinkedIn投稿・前回の通話メモを集めさせ、Northwindを例に1ページのアカウントブリーフを作る方法を示した記事です。プロンプトには、欲しいセクション、期間（直近の四半期）、社内情報と公開情報の組み合わせを書き、ファイルは1つのフォルダに置きます。気に入ったブリーフの作り方は/account-briefというSkillにして保存し、毎週月曜日の午前7時のスケジュールタスクで5件のアカウントに実行させ、チームで共有します。本文に見出しは無く、変換方法が direct のため、図に基づく記述は避けています。

-----
[toTop](#totoppage)
## 生成AIの総括
### 一度の工夫を、毎週の仕組みとチームの標準に育てる
- 横断分析：
  - 指定の力：項目（セクション）、期間、情報の取得元、保存先を先に言葉にすると、ブリーフが一般的な会社概要ではなく自分用の資料になる。
  - 順序の力：前回の続きから始め、その上に公開情報を積む順序が、今のきっかけに結びついた切り出し方を生む。
  - 繰り返しの力：うまくいったやり方をSkillにして定期実行させると、下調べを待つ時間が無くなり、事前に用意された状態で商談に臨める。
  - 共有の力：Skillを共有すると、担当者によらず同じ方法・一貫した形のブリーフが得られ、マネージャーが確認しやすくなる。
- 一言まとめ：良いプロンプトを1回作り、Skillにして回し、チームで共有することが、アカウントリサーチを個人の技から標準の仕組みにする道筋である。

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
- [解説スライド](./docs/account-research-brief-explained-slides.html)
- [スライド原稿](./docs/account-research-brief-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
<!-- page-status:start -->
## 状態と関連資料
- 状態: 検査済み（2026-11-25 時点。解説メモ 12 PASS／スライド 10 枚／lint 0／出典の無い数字 0 件／リンク切れ 0 件。今の状態は台帳 00_index.md が正）
- 原本: [00_originals/account-research-brief.md](./00_originals/account-research-brief.md)
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
