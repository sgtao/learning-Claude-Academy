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
├── ledger.csv             台帳。全 71 ページの ID・場所・状態・検査結果・学習済みの日（正本）
├── tools/                 台帳・索引・検査のスクリプト（tools/README.md）
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
        ├── README.md                  入口。状態、検査の結果、確認していないこと
        ├── 00_originals/              原本（取得したままの本文。frontmatter 付き）
        ├── working-with-skills_explained/   解説メモ一式（README・01_source・02_explanation_memo・11_question_and_answer・12_LLM_prompts_as_guide）
        ├── working-with-skills-explained-slides.html   解説スライド
        └── working-with-skills-explained-slides.md     スライドの原稿（これを直して HTML を作り直す）
```

番号（`01_`、`02_`…）は並び順で、学ぶ順と台帳の順にそろえてある。ステップの番号とフォルダ名は台帳の `step` 列と同じ。

## URL を 1 つ追加するとき
プロジェクトのスキル `learning-page`（リポジトリ直下の `.claude/skills/learning-page/`）に従う。取得と台帳は `tools/add_page.py`、解説とスライドは ced-skills、確かめは `tools/ledger.py refresh`。

## 状態の意味
`未着手`／`取得済`／`作成中`／`完了`（解説メモ 12 PASS・スライド lint 0・数字とリンクの検査が通った）／`薄いページ`（本文が 300 字未満で作らない）／`重複`（同じページが別の場所にある）／`失敗`（取得できない）／`要確認`（検査が通らない）

## 読むときの注意
- 各ページの README にある検査の記述は、作成当時の記録。**今の結果は台帳（`ledger.csv`・`00_index.md`）が正**。
- 内容は 2026-11-15〜11-24 に取得した時点のもの。所要時間・プラン条件は、使う前に公式ページで確かめる。
- 旧リポジトリ（`01_sources/11_ref-effective-Claude-Learning/`）から写したページは、2026-11-24 に今の形（ced-skills 0.0.3）にそろえた。
