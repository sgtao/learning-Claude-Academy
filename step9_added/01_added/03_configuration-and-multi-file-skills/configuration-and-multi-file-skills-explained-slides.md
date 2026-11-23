---
title: 設定とマルチファイル Skills ― 訂正で読む allowed-tools
palette: ocean
purpose: self-study
---
<!-- slide: title -->
# 設定とマルチファイル Skills<br>訂正を正しく読む
subtitle: allowed-tools は制限ではなく承認
badges: [初心者向け, 動画 4 分, Claude Code]
note: 原本は Claude Academy の動画ページ（2026-11-24 取得）。本文は 1 文と訂正の注記だけ。手順の説明は本文に無い。
---
<!-- slide: points -->
badge: 本文
## このページに書かれているのは==2 つ==だけ
- **1 文**：Claude Code で skill を設定する方法と、マルチファイルの skill の構造を学ぶ
- **訂正**：動画の 0:40・1:20・3:35 の説明が誤りだという注記
point: 手順や構造は、動画か公式のドキュメントで確かめる
note: 原本の冒頭の 1 文と、訂正の注記による。
---
<!-- slide: points -->
badge: 訂正
## allowed-tools は==制限ではなく承認==
- **動画の説明（誤り）**：Claude の使えるツールを制限する
- **正しい意味**：リストしたツールを、次のメッセージを送るまで確認なしで使えるよう事前承認する
- **ほかのツール**：通常の権限設定のもとで、今までどおり使える
note: 訂正の注記の言い換え。原文は「実際には、リストしたツールを事前承認するものであり」。
---
<!-- slide: table -->
badge: 使い分け
## ==承認==と==取り除き==を分ける
| 目的 | 書く場所（語） | 効き方 |
|---|---|---|
| 確認なしにしたい | allowed-tools | 次のメッセージまで、確認なしで使える |
| 使わせたくない | disallowed-tools | skill が有効な間、取り除く |
note: disallowed-tools の説明は本文の「skill が有効な間にツールを取り除くには」による。書き方の細部は本文に無い。
---
<!-- slide: points -->
badge: 確かめ方
## 動画を見て、==3 か所==を照らし合わせる
- **0:40・1:20・3:35**：動画で「制限する」と述べている箇所
- **訂正と比べる**：承認の意味になっているかを確かめる
- **字幕**：この資料では字幕を取っていないので、確かめていない
> 確かめるまで、allowed-tools を「制限」として使わない
---
<!-- slide: summary -->
badge: まとめ
## 今日の==一歩==
1. **意味を押さえる**：allowed-tools は承認、disallowed-tools は取り除き
2. **自分の skill を見る**：確認なしにするツールだけを残す
3. **動画で確かめる**：0:40・1:20・3:35 を見て、訂正の意味を自分で確かめる
---
<!-- slide: sources -->
## 出典
- [設定とマルチファイルSkills（Claude Academy・日本語版）](https://academy.claude.com/ja/tutorials/configuration-and-multi-file-skills) — 原本
- [Claude Code の skill のドキュメント（事前承認の項）](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill) — 原本の訂正が参照するページ
