---
title: 営業：商談準備シートを Claude に作らせる
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# 商談の前に、==1 枚のシート==を Claude に作らせる
subtitle: プロンプトで 1 回作る → Skill にする → 毎朝自動で届ける
badges: [営業, 商談準備, 技術・ハウツー]
note: 元は Claude Academy の営業向けユースケース「商談準備」。解説メモ（README・02_explanation_memo・11_question_and_answer）だけを情報源にしたデッキで、Web 検索はしていません。
---
<!-- slide: points -->
## このデッキで分かること
lead: 初めて読む人向け。自分の仕事に置き換えて読む
- **ねらい**：商談と文字起こしを読み取らせ、通話の 1 分前にさっと確認できるシートを作る
- **前提**：Sales プラグインがなくても、記事のプロンプトは動く
- **広げ方**：うまくいったやり方を Skill に保存し、平日の朝に自動実行して、チームで共有する
> 管理者がプラグインを管理していて使えない場合は、プラグインのステップを飛ばす
point: 1 回の依頼を、毎朝届く共通の型にする
note: 本文の冒頭に、Sales プラグインには /call-prep などの商談サイクル用 Skills が同梱されているとある。使えなくても、以降のプロンプトは単独で動く。
---
<!-- slide: steps -->
badge: 準備
## 読ませる材料を、==1 つのフォルダ==に集める
lead: 先にコネクタとフォルダを用意する
```steps
style: cards
items:
  - icon: "🔌"
    title: コネクタを追加
    desc: Claude に使わせたいツールごとに追加。接続リンクは 3 つ（Salesforce・Apollo・Google Drive）
  - icon: "📁"
    title: 文書を 1 フォルダへ
    desc: 相互アクションプラン、自分のメモ、提案書をパソコン上のフォルダにドラッグ
  - icon: "🔑"
    title: フォルダを許可
    desc: Claude Desktop アプリで、Claude にそのフォルダへのアクセスを許可する
  - icon: "🗂️"
    title: 定期なら、プロジェクト化
    desc: そのフォルダからプロジェクトを作ると、コンテキスト・指示・メモリが保たれる
```
point: 権限とアクセスは自分で管理する。Claude は読み取り、シートも同じフォルダに書き戻す
note: 接続リンクの URL 上の名前は salesforce-headless-360・apollo・google-drive-drivemcp。依頼文に出てくる Gong の接続方法は、本文には書かれていない。
---
<!-- slide: points -->
## 1 回目の依頼：何を読ませて、何を出させるか
lead: 本文の例は、Northwind とのミーティングが明日にある場面
- **読ませる**：Salesforce のレコード、直近 3 件の Gong の文字起こし、相互アクションプラン
- **出させる（1）**：商談の現状
- **出させる（2）**：相手が重視していること
- **出させる（3）**：この通話でするべき 2〜3 件の依頼事項
- **出させる（4）**：想定される反論と、それに対する回答
> 「Northwind」は例の名前と読める（推測）。自分の商談では自分のアカウント名に置き換える
point: 依頼事項を指定すると、シートは振り返りから行動計画に変わる
note: 依頼文の原文は「明日Northwindとのミーティングがあります。Salesforceのレコード、直近3件のGongの文字起こし、そして相互アクションプランをもとに、準備シートを作成してください。」で始まる。
---
<!-- slide: table -->
## シートを良くする、==6 つの工夫==
lead: 依頼文に足すと効く点が、本文に挙がっている
| 工夫 | 何が変わるか |
|---|---|
| 通話で何をすべきかを尋ねる | 通話が終わるまでに達成すべきことを把握して臨める |
| 反論と回答をセットにする | 実際に効果があった切り返しが添えられる |
| 十分な履歴を与える | 購買担当者が繰り返し言う内容を見つけられる |
| 自分で管理する文書を含める | CRM のステージ項目だけでなく、自分の文書から商談状況を読む |
| お手本の例を追加する | その構成と文体に合わせて作られる |
| 不確かな点にフラグを立てさせる | 下書きで最初に確認すべき箇所が分かる |
> 「自信のない部分にはフラグを立ててください」は、例のプロンプト本体ではなくヒントとして書かれている
note: 「十分な履歴」は、直近 3 件の Gong の通話を指定する例で説明されている。履歴が相手の関心の情報源になる。
---
<!-- slide: steps -->
badge: 仕組み化
## うまくいったら、==Skill にして回す==
lead: 1 回きりの依頼を、再利用できる型にする
```steps
style: circled
items:
  - icon: "✍️"
    title: プロンプトで作る
    desc: 1 件の商談でシートを作り、出来を見る
  - icon: "💾"
    title: Skill に保存
    desc: これまでの内容を /call-prep-sheet にまとめるよう頼み、保存を確認させる
  - icon: "⏰"
    title: 毎朝、自動で実行
    desc: スケジュール済みタスクで、その日の外部ミーティング分のシートを作る
  - icon: "🤝"
    title: チームで共有
    desc: 全員が同じ準備、マネージャーも同じ形式で読める
```
point: ディスカバリーフレームワークや反論対応プレイブックを、Skill に組み込める
note: Skill には、ディスカバリーフレームワーク、反論対応プレイブック、シートの形式が組み込まれる。プラグイン付属の /call-prep と、自分で作る /call-prep-sheet は別の名前。
---
<!-- slide: points -->
## 自動実行の中身と、守る条件
lead: 平日の朝にシートが届く設定
- **いつ**：平日の午前 7 時 30 分
- **何を**：今日のカレンダーにあるすべての外部ミーティングについて /call-prep-sheet を実行
- **どこへ**：各シートを Accounts 配下の該当アカウントの calls フォルダに書き込む
- **条件**：パソコンの電源を入れたままスリープさせず、Claude Desktop アプリを開いておく
> 条件を満たさないと実行されず、シートが届かないおそれがある（推測）
point: 自動実行は、パソコンの状態に頼る
note: スケジュール済みタスクは、Claude に設定を頼むか、サイドバーのスケジュールを開いて作る。
---
<!-- slide: summary -->
## まとめ
1. **材料**：Salesforce・文字起こし・自分の文書を読ませると、シートが実際の商談に寄る
2. **設計**：依頼事項と、反論への回答を指定して、行動計画にする
3. **確認**：フラグが付いた不確かな点から、先に見直す
4. **仕組み化**：Skill と朝の自動実行で、全員が同じ形のシートを使う
> 本文に書かれていないこと：Gong の接続方法、Skill やスケジュールの細かい操作画面
---
<!-- slide: points -->
## 次に試す 1 つと、読み返す先
lead: まず 1 件の商談で、依頼文を試す
- **次に試す 1 つ**：明日の商談 1 件で、フォルダを許可して準備シートを作らせる
- **確認の質問**：自分のシートに入れたい項目と、読ませたいフォルダの中身は何か
- **元のページ**：[Claude Academy「call-prep-sheet」](https://academy.claude.com/ja/use-cases/call-prep-sheet)
- **ツールアクセス**：[Claude のツールアクセスを管理する](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)
- **フォルダ許可**：[Claude Desktop アプリのフォルダ](https://academy.claude.com/ja/tutorials/navigating-the-claude-desktop-app#folders)
point: 試すのは 1 件の商談から
note: リンクはすべて、元の記事の本文に出てくるもの。リンクの先は、このデッキでは開いて確かめていない。
---
<!-- slide: sources -->
## 出典・参考リンク
- [Claude Academy「call-prep-sheet」](https://academy.claude.com/ja/use-cases/call-prep-sheet) — 元の記事（取得日 2026-11-24）
- [Claude のツールアクセスを管理する](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access) — 記事内のリンク
- [Claude Desktop アプリのフォルダ](https://academy.claude.com/ja/tutorials/navigating-the-claude-desktop-app#folders) — 記事内のリンク
- [プロジェクトで作業を整理する](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) — 記事内のリンク
