###### [toTopPage](../README.md)
###### [toREADME](./README.md)
# 本文：Claudeを使い始める（Intro to Claude）
- `title`: Claudeを使い始める（Intro to Claude）
- `url`: https://academy.claude.com/ja/tutorials/getting-started-with-claude
- `source_format`: html
- `retrieved_at`: 2026-11-15T16:51:28+09:00
- 解説の入口：[README.md](./README.md)

> 要約：Claudeを使い始める最初の日に知っておくこと、最初のプロンプトの書き方、回答の形式（チャット内の答え・図・アーティファクト・ファイル）、＋メニューと記憶の機能、使える場所、困ったときの頼み方を紹介するチュートリアル。

-----
[toTop](#totoppage)

<!-- source-body:start -->
ClaudeはAnthropicが開発したAIアシスタントです。ドキュメントを読んだり、文章の作成や編集を行ったり、さまざまなツールを横断して作業したり、難しい問題についてあなたと一緒に考えたりすることができます。ここでは、最初の日に知っておくべきことと、使い方がわかってきたら次に進むべき場所を紹介します。

Claudeには普通の言葉で書きかけるだけで構いません。以下のヒントが役立ちますし、リクエストの内容に不明な点があれば、作業を始める前にClaudeに質問してもらうこともできます。ドキュメントを添付すれば、さらに多くの情報を与えることができます。

最初のプロンプトは完璧である必要はありません。答えがあまり正しくない場合は、そう伝えればClaudeが調整します。このあと少し進むと、自分のファイルやツールを接続した、自分自身のタスクを設定します。

Claudeはタスクに応じて必要な形式で回答し、その形式の種類は増え続けています。実際に必要なものをリクエストしてください。それが普通の回答であっても、インラインで描かれたチャートであっても、プレゼンテーション、会話の中で作成されたデザインやドキュメント、Excel用のスプレッドシート、あるいは実際に作れるレシピであっても構いません。Claudeがそれを作成し、あなたがそれを導きます。

デフォルトでは、チャット内で役立つ回答が返されます。

図、チャート、インタラクティブな説明が回答の中に描かれます。*「これがどう動くか見せて」* や *「このデータをチャートにして」* と頼めば、言葉と一緒にビジュアルが表示されます。[カスタムビジュアルの詳細（新しいタブで開きます）](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork)。

会話の中で作成され、チャットの横に開かれる成果物そのものです。いくつかの種類には専用のエディタがあり、それ以外はインタラクティブなアーティファクトになります。

- **Claude Design:** 画面、フロー、ビジュアルを、あなたのデザインシステムに沿って手動で編集できるアートボードとしてレイアウトします。
- **Claude Slides:** Claude内で発表できるプレゼンテーションで、PowerPointやPDFとしてダウンロードしたり、Google Slidesにエクスポートしたりできます。
- **Claude Docs:** チームが読み、コメントし、Claudeと一緒にその場で編集できるドキュメントです。
- **Claude Dashboards:** データのダッシュボードで、各チャートにはデータが最後に更新された時刻が表示されます。有料プランでベータ版として提供されています。
- **Claude Motion:** アニメーションによる説明、チャート、またはプロダクトウォークスルーで、MP4ファイルとしてダウンロードできます。TeamおよびEnterpriseプランでベータ版として提供されています。
- **インタラクティブなアーティファクト:** プランナー、計算機、または小さなツールをリクエストすれば、Claudeがその場で使えるように作成します。

これらのいずれかをClaudeに変更してもらうことも、デザイン、プレゼンテーション、ドキュメントを直接編集することもできます。チームと共有することができ、サイドバーのアーティファクトタブで再度見つけることができます。Enterpriseプランでは、組織のOwnerがこれらのうちどれを有効にするかを選択します。[アーティファクトの詳細（新しいタブで開きます）](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)。

実際に動く数式を含むスプレッドシート、送付用のPDF、PowerPointで開くプレゼンテーションなど、ファイル形式そのものが必要な場合、Claudeはダウンロードしたり、Google Driveで開いたり、そのファイルを扱うアプリで開いたりできるファイルを作成します。[ファイル作成の詳細（新しいタブで開きます）](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)。

天気、ステップごとの調理モード付きレシピ、地図上の場所、メールから送信できる下書きなど、日常的な依頼に対する既成の回答に加え、接続したアプリからのカードも表示されます。[ビジュアルおよびインタラクティブなコンテンツの詳細（新しいタブで開きます）](https://support.claude.com/en/articles/13641943-visual-and-interactive-content)。

Claudeが返せるものについてはご覧いただきました。次は最初のタスクを設定しましょう。以下のウォークスルーでは、Claudeに何を与えるか、どのコントロールを設定するか、そして必要なものをどのように依頼するかを説明します。

+メニューには、タスクに必要な場合に使えるいくつかの追加オプションがあります。

- **[コネクタ（新しいタブで開きます）](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities):** メール、カレンダー、ドライブ、チャット、CRMなど、すでに使用しているアプリの中でClaudeに読み取りや操作をさせることができます。一度オンにすれば、すべての会話でそれを検索したり、引用したり、許可した範囲で書き込んだりできるようになります。[ディレクトリを見る（新しいタブで開きます）](https://claude.com/connectors)。
- **[ウェブ検索（新しいタブで開きます）](https://support.claude.com/en/articles/10684626-enable-and-use-web-search):** Free、Pro、Maxプランではデフォルトでオンになっています。TeamおよびEnterpriseプランではデフォルトでオフになっており、管理者がオンにできます。回答がドキュメントのみから得られるべき場合はオフにしてください。
- **[リサーチ（新しいタブで開きます）](https://support.claude.com/en/articles/11088861-use-research-on-claude):** 多数の検索を実行し、出典付きの1つのブリーフを返します。数分かかるため、大きな質問のために使っておきましょう。
- **[スキル（新しいタブで開きます）](https://support.claude.com/en/articles/12512176-what-are-skills):** 毎回同じ方法で行う作業のための保存済みの指示で、必要に応じたトーンやフォーマットも含まれます。Claudeデスクトップアプリでは、タスクを一度実行する様子を記録し、それをスキルとして保存することもできます。
- **フォルダを追加** ([デスクトップアプリ（新しいタブで開きます）](https://academy.claude.com/ja/tutorials/navigating-the-claude-desktop-app)): ファイルを1つずつアップロードする代わりに、コンピュータ上のフォルダ全体をClaudeに渡して、読み取りや保存を行わせます。

プロジェクト、チーム、あるいは自分の仕事の進め方について一度説明したら、もう一度説明する必要はないはずです。いくつかの機能が重要な情報を引き継ぐことで、各会話が前回の会話の続きから始まるようになっています。

- **[プロジェクト（新しいタブで開きます）](https://support.claude.com/en/articles/9517075-what-are-projects):** 1つの継続的な作業のための場所です。Claudeが常に手元に持っておくべきファイルを追加し、数行の指示(ブランドの声、フォーマット、決して忘れてはいけないこと)を書いておけば、その中のすべての会話はすでにそれらを知った状態で始まります。同じファイルを何度もアップロードしたり、同じルールを何度も説明したりしている場合は、プロジェクトを作成しましょう。
- **[Claudeへの指示（新しいタブで開きます）](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features):** 設定プロフィール内の短いメモで、あなたが誰か、何を前提とすべきか、どのように話しかけるべきかなど、Claudeがすべての会話で念頭に置く内容です。一度設定すれば、どこでも適用されます。
- **[メモリ（新しいタブで開きます）](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context):** チーム、プロジェクト、仕事の進め方など、会話をまたいでClaudeがあなたについて記憶している内容です。設定でオンにすると、使っていくうちに内容が埋まっていきます。いつでも読んだり編集したりできます。

ほとんどの人はチャットから始めます。同じClaudeは、異なる種類の作業に合わせて形を変え、他のいくつかの場所にも登場します。

- [デスクトップアプリ（新しいタブで開きます）](https://academy.claude.com/ja/tutorials/navigating-the-claude-desktop-app)は同じチャットをコンピュータ上にもたらし、Macでは、どこからでもすぐに入力できる機能、スクリーンショット、音声入力が追加されます。
- [Claude Code（新しいタブで開きます）](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code)は、エンジニアや開発者向けに、ターミナルとエディタの中で動くClaudeです。
- [Claude Design（新しいタブで開きます）](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)は、今ではどの会話からでも、またサイドバーのDesignタブからでも開始できます。画面、フロー、プロトタイプを、あなたのデザインシステムに沿って手動で編集できるアートボードとしてレイアウトします。
- [Claude Tag（新しいタブで開きます）](https://support.claude.com/en/articles/15594475-what-is-claude-tag)は、チームのSlackワークスペースにClaudeをもたらします。チャンネルやスレッドでClaudeをタグ付けすると、その会話と管理者が接続したツールを使って、その場でタスクを実行します。
- Claudeは、すでに使用しているアプリの中でも動作します。[Excel（新しいタブで開きます）](https://claude.com/docs/office-agents/excel)、[Word（新しいタブで開きます）](https://claude.com/docs/office-agents/word)、[PowerPoint（新しいタブで開きます）](https://claude.com/docs/office-agents/powerpoint)、[Outlook（新しいタブで開きます）](https://claude.com/docs/office-agents/outlook)、[Chrome（新しいタブで開きます）](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)、そして[モバイル（新しいタブで開きます）](https://support.claude.com/en/collections/9387080-claude-mobile-apps)でも利用できます。

ボタンが何をするのか、あるいは回答がなぜうまくいかなかったのかわからないときは、Claudeがトラブルシューティングを手伝ってくれます。

- **機能の仕組みを尋ねる:** *「リサーチは何をするもので、ウェブ検索の代わりにいつ使えばいいですか?」*
- **出力を改善するためにより鋭いプロンプトを得る:** *「私が何をしようとしているのか質問してから、より良いプロンプトを書いてください。」*
- **見覚えのないものをスクリーンショットする:** Claudeは画像を読み取れます。Claudeのどの画面でもスクリーンショットを貼り付けて、何をするものか尋ねてみてください。
