# Claude Academy 学習メモ（learning-Claude-Academy）

Claude の公式学習ページ（claude.ai/learning、実体は Claude Academy）を、ページごとに学び、まとめた成果物のリポジトリ。
ページごとに「原本 → 解説メモ 5 本 → 解説スライド」があり、全体は台帳と索引で管理する。

## まず見る場所
| 知りたいこと | 開くもの |
|---|---|
| 全ページの一覧と、作成の状態 | [00_index.md](./00_index.md)（台帳から作る索引） |
| 学ぶ順番（5 つのステップ） | 下の「フォルダの見方」と、各 `step*/README.md` |
| あるページの解説 | `step*/<まとまり>/<ページ>/README.md`（そこから解説メモ・スライドへ） |
| ページの状態を直す・学習済みにする | [ledger.csv](./ledger.csv)（正本）と [tools/README.md](./tools/README.md) |

## フォルダの見方
```
03_outputs/
├── README.md              この地図
├── 00_index.md            索引（ledger.csv から自動で作る。手で直さない）
├── ledger.csv             台帳。全 73 ページの ID・場所・状態・検査結果・学習済みの日（正本）
├── tools/                 台帳・索引・検査・参照のスクリプト（tools/README.md）
├── .work/                 構造を移したときのスクリプト（migrate-page-structure.sh。一度きり）
├── .vitepress/            ブラウザで読むための VitePress の設定（config.mjs）。index.md・package.json・.github/workflows/pages.yml とあわせて使う
├── step0_intro/           ステップ 0：入口
├── step1_basics/          ステップ 1：基礎（Claude 101 の 15 ページ）
├── step2_tools/           ステップ 2：道具を整える
├── step3_roles/           ステップ 3：職種で習熟（11 役割。未着手のためフォルダは作成時に増える）
└── step4_advanced/        ステップ 4：発展（未着手のため、作成時に増える）
```

ステップの中は、いつも同じ 3 段になっている。

```
step1_basics/                          ← ステップ
└── 01_academy-courses-claude-101/     ← まとまり（関連するページ。README に一覧）
    └── 07_working-with-skills/        ← ページ（1 ページ分）
        ├── README.md                  表紙（タイトル、概要、AI の総括、各資料へのリンク、解説資料＝スライド HTML・原稿 MD へのリンク、最下段に状態 1 行と確認していないことの要約）
        ├── 00_originals/              原本（取得したままの本文。frontmatter 付き）
        ├── 01_source.md               解説メモ一式（本文の複製）
        ├── 02_explanation_memo.md     解説メモ
        ├── 11_question_and_answer.md  FAQ
        ├── 12_LLM_prompts_as_guide.md LLM 用プロンプト
        ├── docs/
        │   ├── working-with-skills-explained-slides.html   解説スライド
        │   └── working-with-skills-explained-slides.md     スライドの原稿（これを直して HTML を作り直す）
        └── .work/                     作業用（読む人は開かなくてよい）
            ├── working-log.md         状態、検査の結果、確認していないこと、作業の経緯（git で追跡する）
            └── intermediate/          スキルで作成した中間ファイル（git では追跡しない）
```

解説メモ 5 本の冒頭リンクは統一：`toTopPage` は 1 つ上（まとまり）の `../README.md`、`toREADME` は同じフォルダの `./README.md`（README 自身も自分を指す）。
解説メモがないページ（薄いページ・取得失敗・重複）は、`README.md`（ページの説明）と `00_originals/` だけを置く。

番号（`01_`、`02_`…）は並び順で、学ぶ順と台帳の順にそろえてある。ステップの番号とフォルダ名は台帳の `step` 列と同じ。

## ブラウザで読む（VitePress と GitHub Pages）
この Markdown を、そのまま VitePress のサイトにして読める（Markdown は写さない。サイドバーは台帳 `ledger.csv` から作る）。

```bash
# 初回だけ（Node.js 20 以上）
npm ci
# 手元で開く（http://localhost:5173/）。保存すると自動で更新される
npm run docs:dev
# 公開用に作る（.vitepress/dist/）。リンク切れがあると失敗する
npm run docs:build
# ビルドと中身の検査（一時フォルダに出す）
python3 tools/test_site.py
```

- コマンドは 1 行ずつ貼り付ける（行末の `# …` を付けて実行しない。zsh は `#` 以降を引数にして、`npm run docs:dev # …` だと表示されないことがある）。
- 出るもの：ステップ・まとまり・ページの README と解説メモ・FAQ・LLM 用プロンプト・原本、スライド（HTML）、`tools/README.md`。出ないもの：`.work/` の中間ファイル、スライドの原稿 MD、`catalog/`。
- 表紙の「詳細・経緯・検査の記録」（`.work/working-log.md`）のリンクは、GitHub 上のファイルを開く（`.work/` は VitePress のページにならないため）。
- 表紙の「解説スライド」は新しいタブでスライド（HTML）を開く。「スライド原稿」（`docs/*-slides.md`）は、サイトには出さないので、GitHub 上のファイルを開く（VitePress は `.html` へのリンクを自分のページとして処理し、同名の原稿 MD を出してしまうため、リンクの描画で振り分けている）。
- ページを足したら、台帳を更新（`tools/ledger.py refresh`）すれば、サイドバーに出る。設定は `.vitepress/config.mjs`。

**GitHub Pages**：`main` に push すると `.github/workflows/pages.yml` がビルドして公開する。公開先は `https://<ユーザー名>.github.io/<リポジトリ名>/`。
最初の 1 回だけ、リポジトリの Settings → Pages → Build and deployment → Source を「GitHub Actions」にする（コマンドなら下）。

```bash
gh api -X POST repos/<ユーザー名>/<リポジトリ名>/pages -f build_type=workflow
```

## URL を 1 つ追加するとき
プロジェクトのスキル `learning-page`（リポジトリ直下の `.claude/skills/learning-page/`）に従う。取得と台帳は `tools/add_page.py`、解説とスライドは ced-skills、確かめは `tools/ledger.py refresh`。

## 状態の意味
`未着手`／`取得済`／`作成中`／`完了`（解説メモ 12 PASS・スライド lint 0・数字とリンクの検査が通った）／`薄いページ`（本文が 300 字未満で作らない）／`重複`（同じページが別の場所にある）／`失敗`（取得できない）／`要確認`（検査が通らない）

## 読むときの注意
- 各ページの README（表紙）の末尾にある「状態」は 1 行の要約。検査の細かい結果・経緯・確認していないことの全文は `.work/working-log.md`。**今の結果は台帳（`ledger.csv`・`00_index.md`）が正**（作業ログの旧 README の記述は、移行前の記録）。
- 表紙の状態の言葉は 作成中／検査済み／確定（検査済み＝台帳が「完了」、確定＝学習済みの日がある）。台帳の「状態の意味」とは別。
- 内容は 2026-11-15〜11-24 に取得した時点のもの。所要時間・プラン条件は、使う前に公式ページで確かめる。
- 旧リポジトリ（`01_sources/11_ref-effective-Claude-Learning/`）から写したページは、2026-11-24 に今の形（ced-skills 0.0.3）にそろえた。
