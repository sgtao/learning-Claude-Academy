###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：法務：規制とコンプライアンス（★2）
- `title`: 法務：規制とコンプライアンス（★2）
- `url`: https://academy.claude.com/ja/use-cases/regulatory-analysis
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:54+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
<!-- slides:start -->
## 解説資料
- [解説スライド](./docs/regulatory-analysis-explained-slides.html)
- [スライド原稿](./docs/regulatory-analysis-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
新しい規則を自社の製品説明と現行ポリシーに照らして読み、コンプライアンスブリーフを作る手順を紹介する記事。法務向けの Regulatory Legal プラグイン（/policy-diff を同梱）と Claude Cowork を使い、規制の PDF・製品説明・現行ポリシーを 1 つのフォルダに置いて依頼する。プロンプトに入れる表現の狙い 6 点、スキルへの保存、/schedule による定期実行も述べる。見出しが無く、分割なしで扱った。図は無い。

-----
[toTop](#totoppage)
## 生成AIの総括
### 規制を「自社向けの期限付きタスク」に翻訳し、その型を使い回す
- 横断分析：
  - 材料：規制だけでなく、自社の製品説明と現行ポリシーを同じフォルダに置くことで、ブリーフが自社を名指しで語るものになる。
  - 依頼の書き方：変更点・適用条項とその理由・期限という 3 つの問いを依頼文に入れると、新しい義務が先頭に来て、担当者が着手できる形になる。
  - 安全と確認：ローカルかクラウドかでファイルの行き先が変わり、プランによって訓練への扱いも違う。不確実な条項へのフラグは、人の確認の順番を決める。
  - 再利用：うまくいった作業はスキルにし、/schedule で定期実行すると、次の規則でも同じ構成のブリーフが出る。
- 一言まとめ：規制と自社の文書を同じフォルダに置いて「変更点・適用・期限」を頼み、型になったらスキルと定期実行で使い回す。

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
- 原本: [00_originals/regulatory-analysis.md](./00_originals/regulatory-analysis.md)
- 確認していないこと（要約）: 原本のリンク先の中身、画像・動画／手順を実際に自分のアカウントで操作した結果／読み合わせは作成者（AI）が行ったもの（第三者の確認ではない）
- 詳細・経緯・検査の記録: [.work/working-log.md](./.work/working-log.md)
<!-- page-status:end -->

-----
[toTop](#totoppage)
