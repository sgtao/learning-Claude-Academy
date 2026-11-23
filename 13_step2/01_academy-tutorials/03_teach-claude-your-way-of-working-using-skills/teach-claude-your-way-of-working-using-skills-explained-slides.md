---
title: Skills で Claude に仕事の進め方を教える
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# Skills で Claude に<br>仕事の進め方を教える
subtitle: 2 回説明したことを、一度でまとめる
badges: [初心者向け, Claude Academy チュートリアル]
note: 原本は Claude Academy の日本語版チュートリアル（2026-11-24 取得）。所要時間は本文に書かれていないので載せていない。
---
<!-- slide: points -->
badge: なぜ
## 毎回の説明を、==一度で済ませる==
lead: うまくいった作業では、自分が基準・構成・例を示している
- **毎回の手間**：基準の説明、構成の記述、例の提示、ずれの修正を、新しい会話のたびにやり直している
- **Skill**：そのやり方をパッケージ化する。関連する依頼のとき、Claude が自動で読み込む
- **作ること**：Skill を作るのは「記述する行為」。書くうちに形式・トーン・例が言葉になる
point: 説明を毎回やり直す代わりに、一度書いてまとめる
note: 原本の冒頭の節による。Skill を作成することは記述する行為、という言い方が原本にある。
---
<!-- slide: table -->
badge: 使い分け
## ==4 つの道具==の使い分け
| 道具 | 向く仕事 | 効く範囲 |
|---|---|---|
| プロンプト | 一度だけの作業・探索 | その会話 |
| カスタム指示 | Claude 全般への好み | すべての会話 |
| Projects | 文脈がたまる作業 | そのプロジェクトの中 |
| Skill | 繰り返す手順 | どの会話でも、関連するときだけ |
note: 原本の比較の節による。Projects は製品ローンチ・リサーチ・キャンペーンが例。Projects にアップロードした文脈はそこにしか無い。両方が要る作業には併用する。
---
<!-- slide: steps, tone: dark -->
badge: 作る場面
## ==3 つの場面==で Skill が効く
lead: 原本が挙げる例
```steps
style: cards
items:
  - icon: "🔁"
    title: 繰り返す手順
    desc: 週次更新、顧客の声の分析、営業の通話準備、リサーチの整理
  - icon: "📦"
    title: 素材を束ねる作業
    desc: ブランド基準、技術文書、法務の契約
  - icon: "🧩"
    title: たまの複雑な作業
    desc: 製品ローンチ、市場分析、取締役会の資料
```
point: 同じ説明を何度もしている作業が、いちばんの候補
---
<!-- slide: points -->
badge: 準備
## 使う前に、==プランと設定==を確かめる
- **プラン**：Free・Pro・Max・Team・Enterprise で利用できる
- **設定**：コード実行とファイル作成を有効にする。Free・Pro・Max は Settings > Capabilities
- **Team・Enterprise**：組織の Owner が、Organization settings > Plugins & skills の Policy タブで管理する
- **始め方**：Customize > Skills の Discover から、事前構築済みの Skill を追加できる
> 画面の表記は変わりうる。使う前に自分の画面で確かめる
note: 原本の「プランと設定」の節による。確認日 2026-11-24。
---
<!-- slide: steps -->
badge: 作り方
## 渡すのは==この 3 つ==
lead: 2 回以上説明した作業を選び、1 つのメッセージで Claude に説明する
```steps
style: circled
items:
  - { icon: "📐", title: 形式を名指し, desc: 「3 つのセクション、各 3 つまでの箇条書き」のように }
  - { icon: "🎙️", title: トーンを設定, desc: 誰のためで、どう読まれるか }
  - { icon: "📄", title: 良い例を 1 つ, desc: 満足できた実際の出力を貼る }
```
point: 良い例は、どんな説明よりも品質の基準を伝える
note: 原本の作り方の節による。技術的な知識は要らず、Claude と話しながら Skill を作る方法も原本で案内されている。
---
<!-- slide: steps -->
badge: 確かめ方
## 作ったら、==新しい会話==で確かめる
lead: 普段どおりに頼んで、2 つを見る
```steps
style: cards
items:
  - icon: "💬"
    title: 新しい会話で頼む
    desc: 例：このメモから今週のチーム更新を下書きして
  - icon: "👀"
    title: 読み込みを見る
    desc: 思考モードに Skill の読み込みが出るか。出なければ名前・説明を直す
  - icon: "⚖️"
    title: 例と並べる
    desc: 構造と文体が同じか。手で直したくなる所は Skill に書き足す
```
point: ずれは、Skill を磨く材料になる
---
<!-- slide: summary -->
badge: まとめ
## 今日から使える==3 つの習慣==
1. **2 回目で気づく**：同じ 3 つ（形式・トーン・例）を 2 回名指ししたら、Skill にまとめる時
2. **役割で分ける**：繰り返す手順は Skill、文脈がたまる作業は Projects
3. **確かめて直す**：新しい会話で頼み、例と並べて、差を Skill に書き足す
---
<!-- slide: sources -->
## 出典
- [Skillsを使ってClaudeにあなたの仕事の進め方を教える（Claude Academy・日本語版）](https://academy.claude.com/ja/tutorials/teach-claude-your-way-of-working-using-skills) — 原本
- [ヘルプセンター：Skillsの使用](https://support.claude.com/en/articles/12512180-use-skills-in-claude) — 原本が案内するセットアップとトラブルシューティング
- [Claudeを使ったSkillの作成方法](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation) — 原本が案内する最初の Skill の作り方
