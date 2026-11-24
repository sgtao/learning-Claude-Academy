---
title: 論文の統計を生データで検証する（Claude Academy 解説）
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# 論文の数字を、==生データ==で確かめる
subtitle: Claudeに原稿とデータを渡し、統計の主張を1件ずつ再計算してもらう方法
badges: [Claude Academy, 研究, 初めて読む人向け]
note: 解説メモ（README・解説メモ・FAQ）だけをもとにしたスライドです。Web 検索はしていません。
---
<!-- slide: points -->
badge: WHY
## 引用する前に、数字を==突き合わせる==
lead: 文献レビューの中心になる論文ほど、広く引用する前に深く理解したい
- **渡すもの**：公開された原稿と、論文の補足データファイル
- **頼むこと**：p値・平均値・標準誤差・サンプルサイズ・検定結果をすべて抽出し、実データで各分析を再実行する
- **得られるもの**：研究の結論がデータで裏付けられているかが分かり、批判的に読む力が身につく
- **たとえ**：【補足】決算書の数字を、領収書の束と1枚ずつ照合する監査に似ている
point: 数字の突き合わせはClaudeに任せ、==意味づけと最終判断==は自分で行う
note: 本文は、生データを検証できると何に注意すべきかを学べる、と述べています。
---
<!-- slide: steps -->
badge: HOW
## 検証の流れは==5ステップ==
lead: 原稿とデータを渡すところから、ワークブックの作成までを1つの依頼にまとめる
```steps
style: cards
items:
  - icon: "📎"
    title: 渡す
    desc: 原稿とデータを(+)ボタンかドラッグ＆ドロップで。調べる理由も添える
  - icon: "🔎"
    title: 抽出と再実行
    desc: すべての統計的主張を取り出し、実データで各分析を計算し直す
  - icon: "⚖️"
    title: 3点を比べる
    desc: 論文の記述・データからの計算・一致するか。問題にはフラグ
  - icon: "📊"
    title: ワークブック
    desc: 各分析のシートと、問題をまとめたサマリーシートのExcel
  - icon: "💬"
    title: 会話を続ける
    desc: 図の照合や警告サイン、査読コメントを追加で頼む
    tone: outline
```
point: 主張ごとに==3点（記述・計算・一致）==を並べさせるのが核心
note: ワークブックには、固定ヘッダー、フィルター付きの列、見つけたことの注記を求めています。
---
<!-- slide: chart-donut -->
badge: RESULT
## 例の検証：31件の内訳
lead: 31件の統計的主張のうち、22件は検証済み。残る9件に確認が必要
```chart
type: donut
title: 統計的主張31件の検証結果
unit: 件
data:
  - { label: 正しく検証済み, value: 22 }
  - { label: 軽微な不一致, value: 3 }
  - { label: 要注意, value: 6 }
source: { name: Claude Academy「研究：生データから統計を検証」, url: https://academy.claude.com/ja/use-cases/verify-statistics-from-raw-data }
```
note: 22+3+6=31 で、全件が3区分のどれかに入ります。軽微と要注意の線引きの基準は、本文には書かれていません。
---
<!-- slide: table, compact -->
badge: FINDINGS
## 例で見つかった==5つの問題==
lead: 数字の誤りだけでなく、検定の選び方や説明の食い違いも見つかる
| 問題 | 論文の記載 | データが示す値 |
|---|---|---|
| サンプルサイズ | 各群n=12 | 対照群でn=11 |
| 単位（総移動距離） | 2456 cm（対照群） | 24.43 m（対照群） |
| 検定（コルチコステロン） | 対応のないt検定、p=0.003 | 対応のある検定でp<0.001 |
| p値の精度 | p=0.004、p=0.02 | p=0.0001、p=0.026 |
| 方法の記述 | 群間比較は対応のない検定 | 同一マウスの前後の値 |
point: 【補足】報告値を100で割ると24.56mで、データの24.43mとは完全には一致しない（本文は触れていない）
note: 本文は、サンプルサイズの不一致が対照群比較すべての統計的検出力と妥当性に影響すると述べています。コルチコステロンの効果は、報告より実際は強いとされています。
---
<!-- slide: steps -->
badge: NEXT
## 続けて頼める==3つの依頼==
lead: 同じ会話の中で、検証を深め、学びを広げ、相手に伝える
```steps
style: cards
items:
  - icon: "📈"
    title: 図を照合する
    desc: 棒グラフの高さ、誤差棒、データポイントが実際の値と合うか確認させる
  - icon: "🚩"
    title: 警告サインを学ぶ
    desc: 方法の不整合、不自然に丸い数字、研究デザインと合わない統計の選び方
  - icon: "✉️"
    title: 査読コメントにする
    desc: 何を直すかは明確に、直し方は励みになる言い方に変換させる
```
point: 生データがない論文でも、==警告サイン==を知っていれば懐疑的に読める
note: 3つとも、本文に依頼文の例が載っています。
---
<!-- slide: points -->
badge: CAUTION
## 最後に判断するのは==自分==
lead: Claudeの指摘も「問題なし」も、そのまま信じない
- **問題を指摘されたとき**：本当のエラーか、分野特有の慣行の誤解かを、自分の専門知識で判断する
- **「問題なし」と言われたとき**：正しい前提を検証したかを評価する
- **プレビューの限界**：チャット内は構造だけ。数式や条件付き書式は、ダウンロードした実物で確かめる
- **重要な数値**：【補足】Claudeの再計算も間違えうるので、元のデータで自分でも確かめる
point: 自分の分野の論文で試すと、==専門知識が判断を支える==ことを実感できる
---
<!-- slide: summary -->
## まとめ
1. 原稿と生データを渡し、すべての統計的主張を再計算させる
2. 主張ごとに「論文の記述・データからの計算・一致するか」の3点を並べる
3. 例では31件中9件に確認が必要で、サンプルサイズ・単位・検定・p値・方法の記述が挙がった
4. 図の照合、警告サイン、査読コメントへと会話を広げられる
5. 指摘も「問題なし」も、最後は自分の専門知識で評価する
point: 次の一歩：自分の分野の論文を1本選び、==依頼文をそのまま==試す
---
<!-- slide: points -->
badge: SOURCE
## 出典と、確認していないこと
lead: このスライドは解説メモだけをもとにしている（Web 検索なし）
- **原本**：[Claude Academy「研究：生データから統計を検証」](https://academy.claude.com/ja/use-cases/verify-statistics-from-raw-data)（取得: 2026-11-24）
- **解説メモ**：[README](./verify-statistics-from-raw-data_explained/README.md)・[解説メモ](./verify-statistics-from-raw-data_explained/02_explanation_memo.md)・[FAQ](./verify-statistics-from-raw-data_explained/11_question_and_answer.md)
- **未確認**：ワークブックの画像の中身、手順を自分のアカウントで操作した結果、例の論文が実在するか
- **本文に無い**：対応するプランやモデル、所要時間
---
<!-- slide: sources -->
## 出典・参考リンク
- [Claude Academy「研究：生データから統計を検証」](https://academy.claude.com/ja/use-cases/verify-statistics-from-raw-data) — 原本（取得: 2026-11-24）
- [解説メモ（README）](./verify-statistics-from-raw-data_explained/README.md) — 概要と総括
- [FAQ](./verify-statistics-from-raw-data_explained/11_question_and_answer.md) — 初心者向けの質問と回答
