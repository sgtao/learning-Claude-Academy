---
title: フィードバック統合：顧客の声を1ページのブリーフにする
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# フィードバック統合<br>顧客の声を 1 ページのブリーフにする
subtitle: Claude Cowork で VoC ブリーフを作り、スキルにして毎週回す
badges: [プロダクト, ハウツー, 自己学習用]
note: 解説メモ（README・02_explanation_memo・11_question_and_answer）だけに基づく。Web 検索はしていない。
---
<!-- slide: points -->
## この資料でわかること
lead: 非エンジニアの初学者が、自分の仕事で再現できる形にまとめた
- **何をするか**：散らばった顧客の声を、ロードマップレビュー用の 1 ページ Voice of Customer（VoC）ブリーフにまとめる
- **どう頼むか**：5〜7 のテーマ、頻度と深刻度、最良の引用、Linear との対応を指定する
- **どう育てるか**：やり取りをスキルにして、/schedule で毎週金曜に自動実行し、チームで共有する
- **本文に無いこと**：Zendesk の接続方法や、深刻度の段階の決め方は書かれていない
note: 要約は解説メモ 02 の「1. 要約」に基づく。
---
<!-- slide: steps -->
## 全体の流れ：6 つの段階
badge: 手順
```steps
style: circled
items:
  - icon: "🔌"
    title: 接続設定
    desc: Slack・Linear・Google Drive をつなぐ
  - icon: "📁"
    title: 材料集め
    desc: 4 種類を 1 つのフォルダへ
  - icon: "💬"
    title: 依頼
    desc: 5〜7 のテーマで 1 ページに
  - icon: "🔧"
    title: 改善
    desc: 6 つのコツで依頼文を磨く
  - icon: "🧩"
    title: スキル化
    desc: 自分の基準を入れる
  - icon: "⏰"
    title: 定期実行
    desc: 毎週自動で回し、共有する
```
---
<!-- slide: points -->
## 準備と材料：1 つのフォルダに集める
badge: 段階 1・2
- **コネクタ**：Cowork の Customize → Connectors で Slack・Linear・Google Drive を設定する。権限とアクセスは自分で管理する
- **材料の 4 種類**：NPS の逐語エクスポート、サポートチケットの CSV、セールスコールの抜粋、6 件のインタビュー記録
- **フォルダ**：材料を 1 つのフォルダに入れて Cowork に指定すると、Cowork はそこから読み、ブリーフもそこに書き戻す
- **四半期ごとに回すなら**：そのフォルダから Cowork プロジェクトを作ると、ソース・指示・メモリが紐付いたままになる
- **プラグイン**：Product Management プラグインが使えなければスキップしてよい。以降の内容は必要としない
note: 【補足】NPS は顧客の推奨度を測る指標で、逐語は自由記述の文章そのままを指すと考えられる（解説メモ FAQ 2）。
---
<!-- slide: points -->
## 依頼文の例：何を頼むか
badge: 段階 3
lead: フォルダ・Slack の #product-feedback・feedback タグ付きの未解決 Zendesk チケットを読ませる
- **整理**：すべてを 5〜7 のテーマにクラスタリングする
- **数える**：それぞれの出現頻度と深刻度を数える
- **引用**：各テーマの最良の引用を抜き出す
- **計画との対応**：Linear のロードマップ項目に対応するものと新規のものをフラグ付けする
- **成果物**：ロードマップレビュー用の 1 ページの VoC ブリーフを作る
point: 一度の依頼で「整理・重み付け・証拠・計画との突き合わせ」まで頼むのが型
---
<!-- slide: steps, layout: grid -->
## 6 つのコツ：依頼文を磨く
badge: 段階 4
```steps
style: cards
items:
  - icon: "🔢"
    title: 数の範囲を指定
    desc: 5〜7 のテーマで、40 行のタグリストにならず 1 ページに収まる
  - icon: "⚖️"
    title: 頻度と深刻度
    desc: 重要な順にテーマが返ってくる
  - icon: "💬"
    title: 最良の一例
    desc: 証拠の山より、最良の引用 1 つが効く
  - icon: "🗺️"
    title: 既存の計画と比較
    desc: 計画済みの検証と、見落としていたものに分かれて届く
  - icon: "📎"
    title: 参考例を追加
    desc: 気に入った例をフォルダに入れると構成とトーンが合う
  - icon: "🚩"
    title: 不確実な点をフラグ
    desc: ドラフトで最初に確認すべき箇所がわかる
```
---
<!-- slide: points -->
## スキル化と定期実行：自分の基準で毎週回す
badge: 段階 5・6
- **スキル化**：「このタスクでこれまで行ったことをスキルにしてください」と頼む。または /synthesize-research スキルを編集してもらう
- **効果**：数分の対話で、それ以降は自分の基準で実行される。深刻度スケール、常設のソース、ブリーフの形式が組み込まれる
- **定期実行**：/schedule と入力するか、Cowork のサイドバーで Scheduled を開く
- **本文の例**：毎週金曜日の午後 4 時に実行し、voc-brief-の日付付きの md ファイルとして書き出す
- **共有**：チームの全 PM が同じ方法でクラスタリングでき、ロードマップレビューは一貫した VoC ページを読める
point: 一度の成功を、スキル化と定期実行で毎週・チーム全員の習慣にする
note: 実行時刻の例は本文の例示。自分の運用に合わせて変える（解説メモ 05 の注意点）。
---
<!-- slide: points -->
## つまずきやすい点と出典
badge: 注意
- **Zendesk**：コネクタの一覧に Zendesk は無い。接続方法は本文には書かれていない【推測】別の設定が必要かもしれない
- **深刻度の段階**：具体的な決め方は本文には書かれていない。自分の仕事に合わせて決める【補足】
- **出力の確認**：不確実な点のフラグから先に元の記録で確かめる
- **出典（解説メモ）**：[README](./feedback-synthesis_explained/README.md)・[解説メモ](./feedback-synthesis_explained/02_explanation_memo.md)・[FAQ](./feedback-synthesis_explained/11_question_and_answer.md)
- **出典（原本）**：[Claude Academy のフィードバック統合の記事](https://academy.claude.com/ja/use-cases/feedback-synthesis)
---
<!-- slide: summary -->
## まとめ
1. 材料は 1 つのフォルダとコネクタに集め、読む場所と書く場所をそろえる
2. 5〜7 のテーマ、頻度と深刻度、最良の引用、既存計画との対応を指定する
3. 不確実な点のフラグを付けさせ、確認の順番を決めておく
4. うまくいったやり取りをスキルにして、自分の基準を入れる
5. /schedule で毎週実行し、チームで共有する
---
<!-- slide: sources -->
## 出典
- [Claude Academy：フィードバック統合（原本）](https://academy.claude.com/ja/use-cases/feedback-synthesis) — 本資料の元の記事
- [解説メモ README](./feedback-synthesis_explained/README.md) — 概要と総括
- [解説メモ本体](./feedback-synthesis_explained/02_explanation_memo.md) — 手順と注意点
- [FAQ](./feedback-synthesis_explained/11_question_and_answer.md) — 10 問の質問と回答
