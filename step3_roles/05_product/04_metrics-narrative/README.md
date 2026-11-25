###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 資料：プロダクト：メトリクスのナラティブ化（★3）
- `title`: プロダクト：メトリクスのナラティブ化（★3）
- `url`: https://academy.claude.com/ja/use-cases/metrics-narrative
- `source_format`: html
- `retrieved_at`: 2026-11-24T09:49:48+09:00
- `profile`: article
- `content_type`: 技術・ハウツー

-----
[toTop](#totoppage)
## セクション
分割なし

-----
[toTop](#totoppage)
## 概要
Product Managementプラグインに同梱された`/metrics-review`などの分析スキルを使い、Claude Coworkに「今週の数値はなぜ動いたのか」をナラティブ（説明文）にまとめさせる手順の記事です。コネクタを設定し、AmplitudeやMixpanelのCSV、先週のナラティブ、チェンジログを1つのフォルダに置いて指定します。続いて、アクティベーションファネルの異常探し、プラン・プラットフォーム・サインアップ元での要因特定、リリース内容との照合、2つのチャート付きのナラティブ作成を頼むプロンプトが示され、依頼の6つの工夫が解説されます。最後に、スキルのカスタマイズと`/schedule`による毎週の自動実行、共有による週次レポートの一貫性が語られます。本文に図はなく、ボタンやリンクの記法が残っています。

-----
[toTop](#totoppage)
## 生成AIの総括
### 数値の「なぜ」を、毎週同じ型で書き続ける仕組みを作る
- 横断分析：
  - 依頼の設計：異常探し、セグメントの順序、リリースとの照合、チャート数の上限、不確実な点の指摘は、どれも出力を「根拠のある、絞られた形」にそろえる工夫である。
  - 材料の整え方：コネクタと1つのフォルダ、Coworkプロジェクトにより、数値・過去の文章・変更の記録が毎回同じ場所から読める状態になる。
  - 育てる流れ：1回の依頼で終わらせず、フィードバックでスキルを編集し、`/schedule`で自動化し、共有する、という段階的な運用になっている。
  - 【補足】人の役割：Coworkが下書きと根拠の整理を担い、人は不確実な点を中心に確認し、因果仮説をチームの行動に結びつける。
- 一言まとめ：型を決めた依頼を1回通し、それをスキルにして、毎週のナラティブを自動で届ける。

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
- [解説スライド](./docs/metrics-narrative-explained-slides.html)
- [スライド原稿](./docs/metrics-narrative-explained-slides.md)
<!-- slides:end -->

-----
[toTop](#totoppage)
