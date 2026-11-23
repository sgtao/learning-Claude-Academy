#!/usr/bin/env python3
"""台帳と索引の検査（合格条件 6）。

確かめること:
  1. ledger.csv の列が決まりどおりで、ID が重ならず、状態が決まった 8 つのどれかで、必須の欄が空でない
  2. 状態が「未着手」でない行は、ページのフォルダがある。「完了」は README・解説メモ「12 PASS」・スライドがある
  3. フォルダに実在するページ（00_originals があるフォルダ）が、すべて台帳にある（抜け 0）
  4. 学習済みの日が、空か YYYY-MM-DD
  5. 索引（00_index.md）の表の行数が台帳の行数と同じで、台帳から作り直したものと一致する
使い方:  python3 tools/check_index.py        終了コード: 0＝合格 / 1＝不合格
"""
import re, sys, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, COLS, STATUSES, INDEX, STEPS, read_ledger

REQ = ["id", "step", "group", "page_dir", "slug", "title", "kind", "fetch", "url", "status"]


def main():
    fails = []
    try:
        cols, rows = read_ledger()
    except FileNotFoundError:
        print("不合格: ledger.csv が無い"); sys.exit(1)
    if cols != COLS:
        fails.append(f"列が決まりと違う: {cols}")
    seen = set()
    for r in rows:
        i = r.get("id", "?")
        if i in seen:
            fails.append(f"{i}: ID が重なっている")
        seen.add(i)
        for c in REQ:
            if not (r.get(c) or "").strip():
                fails.append(f"{i}: {c} が空")
        st = r.get("status", "")
        if st not in STATUSES:
            fails.append(f"{i}: 状態「{st}」は決まった 8 つのどれでもない")
        d = ROOT / r.get("page_dir", "")
        if st and st != "未着手" and not d.is_dir():
            fails.append(f"{i}: 状態が{st}なのにフォルダが無い: {r['page_dir']}")
        if st == "完了":
            if not (d / "README.md").exists():
                fails.append(f"{i}: 完了なのに README.md が無い")
            if (r.get("memo") or "") != "12 PASS":
                fails.append(f"{i}: 完了なのに解説メモの検査が「12 PASS」でない: {r.get('memo')!r}")
            if not (r.get("slides") or "").strip():
                fails.append(f"{i}: 完了なのにスライドの記録が空")
        lo = r.get("learned_on") or ""
        if lo and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lo):
            fails.append(f"{i}: 学習済みの日が日付でない: {lo}")
    paths = {r["page_dir"] for r in rows}
    for step_dir in [v[0] for v in STEPS.values()]:
        for o in sorted((ROOT / step_dir).glob("*/*/00_originals")) if (ROOT / step_dir).exists() else []:
            p = o.parent.relative_to(ROOT).as_posix()
            if p not in paths:
                fails.append(f"台帳に無いページがある: {p}")
    if not INDEX.exists():
        fails.append("00_index.md が無い")
    else:
        t = INDEX.read_text(encoding="utf-8")
        n = len(re.findall(r"^\| \d-[\d-]+ \|", t, re.M))
        if n != len(rows):
            fails.append(f"索引の行数 {n} が台帳の行数 {len(rows)} と違う")
        r = subprocess.run([sys.executable, str(Path(__file__).with_name("build_index.py")), "--check"], capture_output=True, text=True)
        if r.returncode != 0:
            fails.append("索引か README の表が台帳より古い（python3 tools/build_index.py で作り直す）: " + r.stdout.replace("\n", " "))
    for f in fails:
        print("不合格:", f)
    print(f"台帳 {len(rows)} 行、不合格 {len(fails)} 件")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
