#!/usr/bin/env bash
# migrate-page-structure.sh — ページのフォルダを、旧構造から新構造へ移す（一度きり。何も削除しない）
#
#   旧                                         新
#   <ページ>/README.md  (ページ README)    →   <ページ>/.work/working-log.md   （そのまま移す。相対リンクだけ直す）
#   <ページ>/<slug>_explained/README.md    →   <ページ>/README.md              （表紙）
#   <ページ>/<slug>_explained/{01,02,11,12} →  <ページ>/{01_source,02_explanation_memo,11_question_and_answer,12_LLM_prompts_as_guide}.md
#   <ページ>/<slug>_explained/out/         →   <ページ>/.work/intermediate/
#   <ページ>/<slug>-explained-slides.{html,md} → <ページ>/docs/（中のリンク ](./<slug>_explained/X) は ](../X) に直す）
#   <slug>_explained/ は、空になってから rmdir する（中身が残るときは、そのページを移さずに止める）
#
# 使い方（03_outputs/ から）:
#   bash .work/migrate-page-structure.sh                  試し（何も動かさず、やることを表示）
#   bash .work/migrate-page-structure.sh --apply          実行
#   bash .work/migrate-page-structure.sh --apply --page step1_basics/01_academy-courses-claude-101/07_working-with-skills
#   bash .work/migrate-page-structure.sh --apply --no-status   実行の最後の「状態の更新」（page_readme.py --all）をしない
#   bash .work/migrate-page-structure.sh --root <03_outputs の代わりのフォルダ>   （検査用）
# 何度実行しても同じ結果になる（移し終えたページは「移行済み」として飛ばす）。
# 実行前に、03_outputs 全体の控えを取ること（中間ファイル out/ は git に入っていない）。
#   tar -czf /tmp/03_outputs-backup.tgz -C .. 03_outputs
# 終了コード: 0＝すべて成功（飛ばしたものを含む） / 1＝止めたページがある / 2＝使い方の誤り
set -euo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SELF_DIR/.." && pwd)"
APPLY=0
ONLY=""
STATUS=1
MEMO_FILES="README.md 01_source.md 02_explanation_memo.md 11_question_and_answer.md 12_LLM_prompts_as_guide.md"
TODAY="$(date +%Y-%m-%d)"

usage() { sed -n '2,24p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit "${1:-2}"; }

while [ $# -gt 0 ]; do
  case "$1" in
    --apply) APPLY=1 ;;
    --no-status) STATUS=0 ;;
    --page) [ $# -ge 2 ] || usage 2; ONLY="$2"; shift ;;
    --root) [ $# -ge 2 ] || usage 2; ROOT="$(cd "$2" && pwd)"; shift ;;
    -h|--help) usage 0 ;;
    *) echo "不明な引数: $1" >&2; usage 2 ;;
  esac
  shift
done

migrated=0; skipped=0; stopped=0

say() { echo "$@"; }
run() { if [ "$APPLY" -eq 1 ]; then "$@"; else say "    [試し] ${*//$ROOT\//}"; fi; }

# 旧ページ README の相対リンクを、.work/ から辿れる形に直す（見出し・本文は変えない）
rebase_links() {
  sed -E \
    -e 's#\]\(\.\./\.\./\.\./#](@@ROOT@@/#g' \
    -e 's#\]\(\.\./README\.md#](@@GROUP@@/README.md#g' \
    -e 's#\]\((\./)?[^/)]*_explained/#](../#g' \
    -e 's#\]\(\./([^/)]*-explained-slides\.)#](../docs/\1#g' \
    -e 's#\]\(\./#](../#g' \
    -e 's#@@ROOT@@/#../../../../#g' \
    -e 's#@@GROUP@@/#../../#g'
}

# スライド（md・html）の中の、解説メモへのリンクを直す（docs/ から見て 1 つ上がページのフォルダ）
fix_slide_links() {
  local f="$1" tmp
  tmp="$(mktemp)"
  sed -E 's#\]\((\./)?[^/)]*_explained/#](../#g' "$f" > "$tmp"
  cat "$tmp" > "$f"                              # 権限や名前を変えないよう、中身だけ置き換える
  rm -f "$tmp"
}

# ステップ・まとまりの README（手書き）にある、ページ内の旧パスへのリンクを直す
#   ](…/<slug>-explained-slides.html) → ](…/docs/<slug>-explained-slides.html)
#   ](…/<slug>_explained/X)           → ](…/X)
# 何度かけても同じ結果になる（docs/ が既にあれば、いったん外してから付け直す）
fix_index_links() {
  local f="$1" tmp
  tmp="$(mktemp)"
  sed -E \
    -e 's#/docs/([^/)]*-explained-slides\.(html|md))#/\1#g' \
    -e 's#\]\(([^)]*/)([^/)]*-explained-slides\.(html|md))#](\1docs/\2#g' \
    -e 's#/[^/)]*_explained/#/#g' "$f" > "$tmp"
  if ! cmp -s "$f" "$tmp"; then
    if [ "$APPLY" -eq 1 ]; then cat "$tmp" > "$f"; say "  リンクを直した: ${f#"$ROOT"/}"; else say "  [試し] リンクを直す: ${f#"$ROOT"/}"; fi
  fi
  rm -f "$tmp"
}

stop_page() { say "  止める: $1"; stopped=$((stopped + 1)); }

migrate_page() {
  local page="$1" rel expl="" n=0 d f s base
  rel="${page#"$ROOT"/}"
  for d in "$page"/*_explained; do
    if [ -d "$d" ]; then expl="$d"; n=$((n + 1)); fi
  done
  if [ "$n" -eq 0 ]; then
    skipped=$((skipped + 1))
    return 0                                   # 解説メモが無いページ、または移行済み
  fi
  say "$rel"
  if [ "$n" -gt 1 ]; then stop_page "*_explained が $n 個ある（1 個だけ移せる）: $rel"; return 0; fi

  # --- 事前の点検（1 つでも当たったら、このページは何も動かさない）
  for f in $MEMO_FILES; do
    [ -f "$expl/$f" ] || { stop_page "$expl に $f が無い"; return 0; }
  done
  [ -d "$expl/out" ] || { stop_page "$expl に out/ が無い"; return 0; }
  for d in "$expl"/* "$expl"/.[!.]*; do
    [ -e "$d" ] || continue
    base="$(basename "$d")"
    case " $MEMO_FILES out .DS_Store " in *" $base "*) ;; *) stop_page "$expl に想定外のファイル: $base"; return 0 ;; esac
  done
  for f in $MEMO_FILES; do
    [ "$f" = "README.md" ] && continue
    [ -e "$page/$f" ] && { stop_page "移し先に $f が既にある: $rel"; return 0; }
  done
  [ -e "$page/.work/intermediate" ] && { stop_page "移し先 .work/intermediate が既にある: $rel"; return 0; }
  [ -e "$page/.work/working-log.md" ] && { stop_page "移し先 .work/working-log.md が既にある: $rel"; return 0; }
  for s in "$page"/*-explained-slides.html "$page"/*-explained-slides.md; do
    [ -e "$s" ] || continue
    [ -e "$page/docs/$(basename "$s")" ] && { stop_page "移し先 docs/$(basename "$s") が既にある: $rel"; return 0; }
  done

  # --- 移す
  run mkdir -p "$page/.work" "$page/docs"
  if [ -f "$page/README.md" ]; then
    # 旧ページ README → 作業ログ（本文はそのまま。リンクだけ直す。末尾に移行の 1 行を足す）
    if [ "$APPLY" -eq 1 ]; then
      { rebase_links < "$page/README.md"
        printf '\n## 作業の経緯（移行）\n- %s: 構造を移した（`.work/migrate-page-structure.sh`）。この README は旧構造のページ README の内容。リンクは .work/ から辿れる形に直した。検査の記述は移行前のもの（最新は「検査の結果」）\n' "$TODAY"
      } > "$page/.work/working-log.md"
    else
      say "    [試し] 旧 README.md → .work/working-log.md（リンクを直して移す）"
    fi
  fi
  run mv "$expl/README.md" "$page/README.md"
  for f in $MEMO_FILES; do
    [ "$f" = "README.md" ] && continue
    run mv "$expl/$f" "$page/$f"
  done
  run mv "$expl/out" "$page/.work/intermediate"
  for s in "$page"/*-explained-slides.html "$page"/*-explained-slides.md; do
    [ -e "$s" ] || continue
    run mv "$s" "$page/docs/$(basename "$s")"
    if [ "$APPLY" -eq 1 ]; then fix_slide_links "$page/docs/$(basename "$s")"; fi
  done
  if [ "$APPLY" -eq 1 ]; then
    rm -f "$expl/.DS_Store"                    # macOS のごみだけは消す（git にも入っていない）
    rmdir "$expl" 2>/dev/null || { stop_page "移した後も $expl が空にならない（残りを確かめる）"; return 0; }
  else
    say "    [試し] rmdir $expl"
  fi
  migrated=$((migrated + 1))
}

if [ -n "$ONLY" ]; then
  [ -d "$ROOT/$ONLY" ] || { echo "ページが無い: $ROOT/$ONLY" >&2; exit 2; }
  pages=("$ROOT/${ONLY%/}")
else
  pages=()
  for p in "$ROOT"/step*/*/*/; do
    [ -d "$p" ] && pages+=("${p%/}")
  done
fi

if ! grep -q 'working-log.md' "$ROOT/.gitignore" 2>/dev/null; then
  say "注意: $ROOT/.gitignore に working-log.md を残す指定が無い（.work/ ごと無視されて、作業ログが追跡されない）"
fi
[ "$APPLY" -eq 1 ] || say "（試し。実行するには --apply）"

for p in ${pages[@]+"${pages[@]}"}; do migrate_page "$p"; done

if [ -z "$ONLY" ]; then
  for f in "$ROOT"/step*/README.md "$ROOT"/step*/*/README.md; do
    [ -f "$f" ] && fix_index_links "$f"
  done
fi

say ""
say "移した: ${migrated}／飛ばした（解説メモなし・移行済み）: ${skipped}／止めた: ${stopped}"

if [ "$APPLY" -eq 1 ] && [ "$STATUS" -eq 1 ] && [ "$migrated" -gt 0 ] && [ -f "$ROOT/tools/page_readme.py" ]; then
  say "表紙の状態と作業ログの検査の結果を更新する（tools/page_readme.py --all）"
  (cd "$ROOT" && python3 tools/page_readme.py --all)
fi
[ "$stopped" -eq 0 ]
