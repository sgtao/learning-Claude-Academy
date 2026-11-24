// ledger.csv（台帳）を読んで、サイドバーとナビを作る。標準の node だけで動く（依存なし）。
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

export const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..')

/** RFC 4180 の CSV（引用符の中のカンマ・改行・"" に対応）。 */
export function parseCsv(text) {
  const rows = []
  let row = [], cell = '', q = false
  for (let i = 0; i < text.length; i++) {
    const c = text[i]
    if (q) {
      if (c === '"' && text[i + 1] === '"') { cell += '"'; i++ }
      else if (c === '"') q = false
      else cell += c
    } else if (c === '"') q = true
    else if (c === ',') { row.push(cell); cell = '' }
    else if (c === '\n') { row.push(cell); rows.push(row); row = []; cell = '' }
    else if (c !== '\r') cell += c
  }
  if (cell !== '' || row.length) { row.push(cell); rows.push(row) }
  const [head, ...body] = rows
  return body.filter(r => r.length === head.length).map(r => Object.fromEntries(head.map((h, i) => [h, r[i]])))
}

export function readLedger() {
  return parseCsv(readFileSync(resolve(ROOT, 'ledger.csv'), 'utf-8'))
}

const STEP_LABEL = {
  '0': 'ステップ 0：入口', '1': 'ステップ 1：基礎（Claude 101）', '2': 'ステップ 2：道具を整える',
  '3': 'ステップ 3：職種で習熟', '4': 'ステップ 4：発展', '9': 'ステップ 9：追加',
}

/** ステップごとのサイドバー。/<step フォルダ>/ 以下のページで、そのステップのまとまりとページを出す。 */
export function buildSidebar(rows = readLedger()) {
  const steps = {}
  for (const r of rows) {
    const stepDir = r.page_dir.split('/')[0]
    ;(steps[r.step] ??= { dir: stepDir, groups: {} }).groups[r.group] ??= []
    steps[r.step].groups[r.group].push(r)
  }
  const sidebar = {}
  for (const [step, { dir, groups }] of Object.entries(steps)) {
    sidebar[`/${dir}/`] = [
      { text: STEP_LABEL[step] ?? dir, link: `/${dir}/README` },
      ...Object.entries(groups).map(([g, pages]) => ({
        text: g,
        collapsed: false,
        link: `/${dir}/${g}/README`,
        items: pages.map(p => ({
          text: `${p.id} ${p.title}${p.status !== '完了' ? `（${p.status}）` : ''}`,
          link: `/${p.page_dir}/README`,
        })),
      })),
    ]
  }
  return sidebar
}

export function buildNav(rows = readLedger()) {
  const dirs = {}
  for (const r of rows) dirs[r.step] ??= r.page_dir.split('/')[0]
  return [
    { text: '地図', link: '/README' },
    { text: '索引', link: '/00_index' },
    { text: 'ステップ', items: Object.entries(dirs).map(([s, d]) => ({ text: STEP_LABEL[s] ?? d, link: `/${d}/README` })) },
  ]
}
