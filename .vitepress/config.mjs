// VitePress の設定。Markdown はこのフォルダ（03_outputs/）をそのまま読む（コピーしない）。
// ローカル:  npm run docs:dev      ビルド:  npm run docs:build      GitHub Pages: .github/workflows/pages.yml
import { defineConfig } from 'vitepress'
import { cpSync, existsSync, mkdirSync, readdirSync } from 'node:fs'
import { dirname, join, posix, relative } from 'node:path'
import { ROOT, buildNav, buildSidebar } from './ledger.mjs'

// GitHub Pages の公開先は https://<user>.github.io/<リポジトリ名>/ なので、ビルド時に base を渡す（ローカルは '/'）
const base = process.env.VITEPRESS_BASE || '/'

// 作業ログ（.work/working-log.md）はドット始まりのフォルダにあり、VitePress のページにならない。
// 表紙からのリンクは、GitHub 上のファイルを指すように、描画のときに書き換える
const repo = process.env.GITHUB_REPOSITORY || 'sgtao/learning-Claude-Academy'
const blob = `https://github.com/${repo}/blob/main`
function workLogLinks(md) {
  md.core.ruler.push('worklog-link-to-github', state => {
    const rel = state.env.relativePath // 例: step1_basics/.../README.md
    if (!rel) return
    for (const t of state.tokens) {
      for (const c of t.children || []) {
        if (c.type !== 'link_open') continue
        const href = c.attrGet('href') || ''
        if (/(^|\/)\.work\/working-log\.md$/.test(href)) {
          c.attrSet('href', `${blob}/${posix.normalize(posix.join(posix.dirname(rel), href))}`)
          c.attrSet('target', '_blank'); c.attrSet('rel', 'noopener')
        }
      }
    }
  })
}

/** ステップ・まとまり・ページの 3 段にある、スライドの HTML（docs/*-explained-slides.html）を探す。 */
function slideHtmls() {
  const out = []
  for (const s of readdirSync(ROOT, { withFileTypes: true })) {
    if (!s.isDirectory() || !/^step\d+_/.test(s.name)) continue
    for (const g of readdirSync(join(ROOT, s.name), { withFileTypes: true })) {
      if (!g.isDirectory()) continue
      for (const p of readdirSync(join(ROOT, s.name, g.name), { withFileTypes: true })) {
        const d = join(ROOT, s.name, g.name, p.name, 'docs')
        if (!p.isDirectory() || !existsSync(d)) continue
        for (const f of readdirSync(d)) if (f.endsWith('-explained-slides.html')) out.push(join(d, f))
      }
    }
  }
  return out
}

export default defineConfig({
  lang: 'ja',
  title: 'Claude Academy 学習メモ',
  description: 'Claude Academy のページごとに、解説メモ・FAQ・LLM 用プロンプト・解説スライドをまとめた学習メモ',
  base,
  // 出力先。検査（tools/test_site.py）が、一時フォルダに出すために VITEPRESS_OUT で変える
  outDir: process.env.VITEPRESS_OUT || '.vitepress/dist',
  cleanUrls: true,
  lastUpdated: false,

  // 読む人向けのものだけを出す。作業ログ（.work/working-log.md）は表紙からリンクがあるので出す。
  // 中間ファイル・中断した作業・取得の記録・依存・スライドの原稿（MD。スライドは HTML で出す）は出さない
  srcExclude: ['catalog/**', '**/.work/intermediate/**', '**/.work/aborted/**', 'node_modules/**', '**/docs/*-explained-slides.md'],

  // - スライドの HTML は、ビルドの最後（buildEnd）に写すので、ビルド中はリンク先が無い
  // - 01_sources/ は、このリポジトリの外（親のリポジトリ）を指すリンク
  ignoreDeadLinks: [/-explained-slides$/, /(^|\/)01_sources\//],

  markdown: { config: workLogLinks },

  themeConfig: {
    nav: buildNav(),
    sidebar: buildSidebar(),
    outline: { level: [2, 3], label: 'このページの目次' },
    docFooter: { prev: '前のページ', next: '次のページ' },
    returnToTopLabel: 'ページの先頭へ',
    sidebarMenuLabel: 'メニュー',
    darkModeSwitchLabel: '表示の切り替え',
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '検索', buttonAriaLabel: '検索' },
          modal: { noResultsText: '見つかりません', resetButtonTitle: '消す', footer: { selectText: '選ぶ', navigateText: '移動', closeText: '閉じる' } },
        },
      },
    },
  },

  // スライドの HTML は VitePress のページではないので、ビルドの最後に同じ相対パスで出力へ写す
  buildEnd(siteConfig) {
    for (const f of slideHtmls()) {
      const dest = join(siteConfig.outDir, relative(ROOT, f))
      mkdirSync(dirname(dest), { recursive: true })
      cpSync(f, dest)
    }
  },
})
