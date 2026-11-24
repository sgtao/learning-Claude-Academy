---
title: 人事の役割ページ（Claude Academy）を学ぶ
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# 人事の役割ページ<br>プロンプト5件と使用事例6件
subtitle: Claude Academy の人事向けページを、初めて読む人のために整理
badges: [自己学習, 非エンジニア向け, 一覧の解説]
note: 2026-11-24 に取得したページの本文（一覧だけ）と、その解説メモに基づく。プロンプトの全文や使用事例の手順は本文に無い。
---
<!-- slide: points -->
badge: プロンプトを試す
## 試せるプロンプトは5件
lead: 各プロンプトは下書きとして開かれ、送信前に編集できます
- **同僚へのフィードバックを下書き**：具体的な事例をもとに、バランスの取れた評価を作成
- **求人票を作成**：採用担当マネージャーのメモをもとに、わかりやすくインクルーシブな求人票を作成
- **政策に関する問題を分析**：社内ポリシーに関する質問について、慎重に検討した==初期見解==を得る
- **掲載前に求人票を確認する**：職位レベルの妥当性、公平性、わかりやすさのチェックと面接キット
- **アンケートのコメントをテーマ別に整理**：テーマ、各テーマの出現頻度、経営陣向けの報告用スライド
- **出典**：[人事の役割ページ（Claude Academy）](https://claude.ai/learning/roles/hr)
point: 政策の分析は「初期見解」。最終判断は人が行います（補足）
note: 5件の分け方（評価・採用・社内ルール・従業員の声）は筆者の整理で、ページの分類ではない。
---
<!-- slide: chart-bar, layout: side-list -->
badge: 使用事例
## 使用事例は6件、どれも10〜15分
lead: 実際のワークフローをステップごとに説明する一覧（題名は本文のまま英語）
```chart
type: bar
title: 所要時間ごとの使用事例の件数（件）
unit: 件
data:
  - { label: 10分, value: 3 }
  - { label: 11分, value: 2 }
  - { label: 15分, value: 1 }
source: { name: 人事の役割ページ（Claude Academy・2026-11-24 取得）, url: https://claude.ai/learning/roles/hr }
```
### 6件の題名
- **10分**：Interview debrief synthesis／Open a new role／Performance review administrator
- **11分**：Engagement survey to action plan／Offer process
- **15分**：Create new hire onboarding guides
point: 6件を通して学ぶと合計67分（本文の所要時間を足した値）
note: 題名が英語のままの理由は本文からは分からない。内容は題名と所要時間以外、本文に書かれていない。
---
<!-- slide: steps -->
badge: 学び方の一例
## 自分の仕事で試す、==4ステップ==
lead: 【補足】筆者（AI）の整理です。ページに書かれた手順ではありません
```steps
style: cards
items:
  - icon: "1"
    title: 場面を選ぶ
    desc: 5件のうち、今週の自分の作業に近いものを1つ
  - icon: "2"
    title: 下書きを開く
    desc: プロンプトは下書きとして開かれる
  - icon: "3"
    title: 自分の事例を足す
    desc: 送信前に編集して、状況に合わせる
  - icon: "4"
    title: 人が確かめる
    desc: 内容と、個人情報の扱いを職場のルールで確認
    tone: outline
```
point: 次に試す1つ：今週の作業に近いプロンプトを1件開き、自分の事例を足す
note: 本文に無いこと（プロンプトの全文・使用事例の手順）は、実際のページを開いて確かめる。
---
<!-- slide: sources -->
## 出典
- [人事の役割ページ（Claude Academy）](https://claude.ai/learning/roles/hr) — 原本（2026-11-24 に Chrome で本文を取得）
- [解説メモ README](../README.md) — 概要と総括
- [解説メモ本体](../02_explanation_memo.md) — 解説・活用案
- [FAQ](../11_question_and_answer.md) — 質問と回答
