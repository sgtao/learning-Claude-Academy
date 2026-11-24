---
title: マーケティングの役割ページ（Claude Academy）の解説
palette: ocean
---
<!-- slide: title -->
# マーケティングの役割ページ：<br>==まず試す 6 つ==と、学べる 16 の事例
subtitle: Claude Academy の役割ページを、初めて読む人向けに整理した解説スライド
badges: [Claude Academy, マーケティング, 初学者向け]
note: 元ページは 2026-11-24 に Chrome で読み、本文のテキストだけを写した原本です。件数（6・12・4）は原本の行を数えた値です。
---
<!-- slide: points -->
badge: 全体像
## このページには、==2 つの一覧==が載っている
lead: 本文に見出しは無く、行の並びで前半と後半に分かれる
- **プロンプトを試す（6 件）**：各プロンプトは下書きとして開かれ、送信前に編集できる
- **使用事例（16 件）**：実際のワークフローをステップごとに説明する。ユースケース 12 件とチュートリアル 4 件
- **所要時間と種類つき**：使用事例の各行に分数と種類が付く（7〜18 分）。題名は英語のまま
point: 事例の中身は本文に書かれていない。ここでわかるのは題名・時間・種類まで
note: 例え話：メニュー表（プロンプト）と、所要時間つきの料理教室の案内（使用事例）が 1 枚に載ったページです。これは解説メモの補足で、原本の記述ではありません。
---
<!-- slide: table -->
badge: プロンプト
## 6 つのプロンプトは、==何を貼って何が返るか==
lead: 貼り付けるものが本文にあるのは 3 件。ほかは本文に書かれていない
| プロンプト | 作るもの | 貼るもの |
|---|---|---|
| ブランドガイドラインに沿ったコピーを作成 | ランディングページ、メール、広告のコピー | 本文に記載なし |
| キャンペーンブリーフの下書きを作成 | 1 ページのキャンペーン概要 | アイデア |
| Web ページの検索順位を上げる | 改善点を効果の高い順に並べたプラン | 本文に記載なし |
| コンテンツカレンダーを作成 | 4 週間分のカレンダー（スプレッドシート） | 本文に記載なし |
| 今週のキャンペーンの動きをまとめる | 短いスライド資料 | 今週と先週の数値 |
| オーディエンスの声を把握する | 対応が必要な順のテーマ整理 | レビュー、アンケートのコメント、SNS での言及 |
note: キャンペーン概要の中身は、目的、対象者、メッセージ、チャネル、成功指標と本文に書かれています。
---
<!-- slide: steps -->
badge: 使い方（解説メモの補足）
## 試すときの流れは、==4 ステップ==
lead: 本文の「下書きとして開かれ、送信前に編集できる」を、手順に直したもの
```steps
style: cards
items:
  - icon: "1"
    title: 1 件を選ぶ
    desc: 手元に材料がある日は、貼り付け型のプロンプトが試しやすい
  - icon: "2"
    title: 自分の情報に直す
    desc: 下書きとして開かれる。数値やコメントを自分のものに置き換える
  - icon: "3"
    title: 送る
    desc: 送信前に、期間の食い違いや、外に出せない情報がないかを見る
  - icon: "4"
    title: 結果を見て直す
    desc: 足りない点を言葉にして、もう一度依頼する
    tone: outline
```
point: 出てきた下書きは、そのまま使わず、自分で判断してから使う
note: この 4 ステップは解説メモの補足（筆者の整理）で、元ページの手順ではありません。
---
<!-- slide: chart-bar, layout: side-list -->
badge: 所要時間
## チュートリアル 4 件は、==7〜14 分==
lead: 使用事例のうち、チュートリアルの所要時間（元ページの分数）
```chart
type: bar
title: チュートリアルの所要時間（分）
data:
  - { label: Customize Claude, value: 7 }
  - { label: Intro to Projects, value: 7 }
  - { label: Teach Claude（skills）, value: 11 }
  - { label: Marketing ops 週次, value: 14 }
source: { name: Claude Academy 役割ページ（2026-11-24 取得）, url: https://claude.ai/learning/roles/marketing }
```
### 題名（原本のまま）
- **7 分**：Customize Claude
- **7 分**：Intro to Projects
- **11 分**：Teach Claude your way of working using skills
- **14 分**：Using Claude for marketing ops: run a weekly review that preps itself
note: 横軸の Teach Claude（skills）と Marketing ops 週次は、長い題名を縮めた表示用の略称です。ユースケース 12 件は 10〜18 分で、最長は Create on-brand content の 18 分です。
---
<!-- slide: table, layout: compact -->
badge: ユースケース 12 件
## 題名から見ると、==4 つの分類==に分けられる
lead: 分類は解説メモの補足（筆者の整理）。事例の中身は本文に無く、題名からの推測を含む
| 分類（筆者の整理） | 題名（原本のまま） |
|---|---|
| 数値を見る | Recap your ad performance／Analyze campaign performance／Analyze fundraising performance |
| つくる | Build a campaign brief／Build customer personas／Build the competitive comparison doc／Create brand assets／Create on-brand content |
| 展開する | Adapt content across platforms／Repurpose content across channels |
| ブランドを守る | Audit a folder of visual assets against your guidelines／Package your brand guidelines in a skill |
note: 数は 3 + 5 + 2 + 2 で 12 件です。プロンプトと事例の対応（例：キャンペーンブリーフのプロンプトと Build a campaign brief）は題名の類似からの推測です。
---
<!-- slide: points -->
badge: 注意点
## ==本文に書かれていないこと==を知っておく
lead: 題名だけから、中身を想像して使わない
- **各事例のステップ**：本文には題名・所要時間・種類しかない
- **リンク先の中身・画像・動画**：原本は Chrome で読んだテキストだけで、ボタンは押していない
- **ユースケースとチュートリアルの違い**：説明は無い。題名からは、チュートリアルが機能の基本に近いと読める（推測）
- **冒頭の「概要」「学ぶ」**：役割は本文から決められない（推測にとどめる）
point: 分からないことは、実際のページを開いて自分で確かめる
note: 確かめた内容は、解説メモに書き足すと自分の学習記録になります。
---
<!-- slide: summary -->
badge: まとめ
## ==今日の 1 件==を決めて終わる
1. **プロンプトは下書き**：6 件から 1 件を選び、自分の情報に直して送る
2. **事例は所要時間つき**：短い事例から 1 件ずつ学ぶと負担が小さい（7 分のチュートリアルなど）
3. **中身は自分で確かめる**：本文にない点は、元ページで読んで書き足す
> 次の 1 手：今週の仕事で材料が手元にあるプロンプトを 1 件選び、結果と気づきを 3 行で記録する。
note: 次の 1 手は解説メモの活用案に基づく提案です。
---
<!-- slide: sources -->
## 出典・参考リンク
- [Claude Academy マーケティングの役割ページ](https://claude.ai/learning/roles/marketing) — 元ページ（2026-11-24 取得）
- [解説メモ（README）](../README.md) — 概要と総括
- [解説メモ（本体）](../02_explanation_memo.md) — 解説・グループ別・活用案
- [FAQ](../11_question_and_answer.md) — 7 問の Q&A
note: このスライドは上の解説メモだけを情報源にしています。Web 検索はしていません。
