#!/usr/bin/env python3
"""台帳（ledger.csv）から、索引（00_index.md）と、各ステップ・各まとまりの README の台帳の表を作る。

使い方:  python3 tools/build_index.py          書き込む
         python3 tools/build_index.py --check  書かずに、今のファイルが台帳と同じかを確かめる（違えば終了コード 1）
README の表は <!-- ledger:start --> と <!-- ledger:end --> の間だけを書き換える（外の文章は触らない）。
README が無いステップ・まとまりは、作る。人が書いた README（印が無いもの）は変えない。
"""
import sys
from collections import Counter, OrderedDict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, INDEX, STEPS, STATUSES, read_ledger

START, END = "<!-- ledger:start -->", "<!-- ledger:end -->"


def rel(path_from, target):
    import os
    return os.path.relpath(target, path_from).replace(os.sep, "/")


def table(rows, base):
    out = ["| ID | ページ | 分 | 種類 | 状態 | 学習済みの日 | 備考 |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        readme = ROOT / r["page_dir"] / "README.md"
        title = r["title"].replace("|", "／")
        cell = f"[{title}]({rel(base, readme)})" if readme.exists() else title
        out.append(f"| {r['id']} | {cell} | {r['minutes'] or '－'} | {r['kind']} | {r['status']} | {r['learned_on'] or ''} | {r['note'].replace('|', '／')} |")
    return "\n".join(out)


def index_text(rows):
    c = Counter(r["status"] for r in rows)
    L = ["# 学習メモ 索引（Claude Academy）", "",
         "> このファイルは `tools/build_index.py` が `ledger.csv` から作る。手で直さない（直すなら `ledger.csv`）。", "",
         "## 状態の数（全 %d ページ）" % len(rows), "", "| 状態 | 件数 |", "|---|---|"]
    L += [f"| {s} | {c.get(s, 0)} |" for s in STATUSES]
    L += ["", "## フォルダの見方", "", "```", "03_outputs/",
          "├── README.md            この場所の地図",
          "├── 00_index.md          この索引（台帳から作る）",
          "├── ledger.csv           台帳（ページの一覧と状態の正本）",
          "├── tools/               検査と台帳のスクリプト（tools/README.md）",
          "└── step<N>_<名前>/       ステップごと（0 入口 ／ 1 基礎 ／ 2 道具 ／ 3 職種 ／ 4 発展）",
          "    └── <NN>_<まとまり>/  関連するページのまとまり",
          "        └── <NN>_<ページ>/ 1 ページ分（README=表紙、00_originals、解説メモ 5 本、docs/=スライド、.work/=作業用）",
          "```", ""]
    by = OrderedDict()
    for r in rows:
        by.setdefault(r["step"], []).append(r)
    for s, rs in by.items():
        name, jp = STEPS[s]
        L += [f"## ステップ {s}：{jp}（`{name}/`）", "", table(rs, ROOT), ""]
    return "\n".join(L)


def block(rows, base):
    return f"{START}\n{table(rows, base)}\n{END}"


def readme_new(kind, d, title, rows):
    top = rel(d, ROOT / "README.md")
    if kind == "step":
        head = f"###### [toTopPage]({top})\n###### [toREADME]({top})\n# {d.name} — {title}\n\nこのステップのページの台帳。`ledger.csv` から作る（表は自動で更新される。外の文章は手で書いてよい）。\n\n## 台帳\n"
    else:
        up = rel(d, d.parent / "README.md")
        head = f"###### [toTopPage]({rel(d, ROOT / 'README.md')})\n###### [toREADME]({up})\n# {d.name}\n\nこのまとまりのページ。`ledger.csv` から作る。\n\n"
    return head + block(rows, d) + "\n"


def apply(path, kind, title, rows, check, bad):
    base = path.parent
    if path.exists():
        t = path.read_text(encoding="utf-8")
        if START not in t:
            return                     # 人が書いた README は触らない
        a, b = t.index(START), t.index(END) + len(END)
        new = t[:a] + block(rows, base) + t[b:]
    else:
        new = readme_new(kind, base, title, rows)
    if not path.exists() or path.read_text(encoding="utf-8") != new:
        if check:
            bad.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(new, encoding="utf-8")


def main():
    check = "--check" in sys.argv
    _, rows = read_ledger()
    bad = []
    txt = index_text(rows)
    if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != txt:
        if check:
            bad.append("00_index.md")
        else:
            INDEX.write_text(txt, encoding="utf-8")
    steps, groups = OrderedDict(), OrderedDict()
    for r in rows:
        steps.setdefault(r["step"], []).append(r)
        groups.setdefault((r["step"], r["group"]), []).append(r)
    for s, rs in steps.items():
        d = ROOT / STEPS[s][0]
        if any((ROOT / r["page_dir"]).exists() for r in rs):
            apply(d / "README.md", "step", f"ステップ {s}：{STEPS[s][1]}", rs, check, bad)
    for (s, g), rs in groups.items():
        d = ROOT / STEPS[s][0] / g
        if any((ROOT / r["page_dir"]).exists() for r in rs):
            apply(d / "README.md", "group", g, rs, check, bad)
    if check:
        for b in bad:
            print("古い:", b)
        print(f"古いファイル: {len(bad)}")
        sys.exit(1 if bad else 0)
    print("索引と README の表を作りました")


if __name__ == "__main__":
    main()
