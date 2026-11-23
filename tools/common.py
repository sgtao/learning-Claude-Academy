"""台帳・索引・ページ検査で共通に使うもの（標準ライブラリのみ。Python 3.9 以上）。"""
import csv, re, subprocess, shutil, glob, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # 03_outputs/
LEDGER = ROOT / "ledger.csv"
INDEX = ROOT / "00_index.md"
COLS = ["id", "step", "group", "page_dir", "slug", "title", "minutes", "kind", "fetch", "url",
        "status", "memo", "slides", "learned_on", "note"]
STATUSES = ["未着手", "取得済", "作成中", "完了", "薄いページ", "重複", "失敗", "要確認"]
STEPS = {
    "0": ("step0_intro", "入口"),
    "1": ("step1_basics", "基礎（Claude 101）"),
    "2": ("step2_tools", "道具を整える"),
    "3": ("step3_roles", "職種で習熟"),
    "4": ("step4_advanced", "発展"),
}


def read_ledger():
    with open(LEDGER, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        return list(rd.fieldnames or []), list(rd)


def write_ledger(rows):
    with open(LEDGER, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})


def body_of(md_path):
    """frontmatter を除いた本文。"""
    t = Path(md_path).read_text(encoding="utf-8")
    if t.startswith("---"):
        parts = t.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return t


def find_checker():
    """ced-craft-explanation-docs の check_docs.py の、いちばん新しい版を探す。"""
    c = sorted(glob.glob(str(Path.home() / ".claude/plugins/cache/ced-skills/ced-skills/*/ced-craft-explanation-docs/scripts/check_docs.py")))
    return c[-1] if c else None


def run_py(script, *args):
    """uv があれば Python 3.12、なければ python3 で script を動かす。"""
    base = ["uv", "run", "--python", "3.12"] if shutil.which("uv") else ["python3"]
    return subprocess.run(base + [str(script)] + [str(a) for a in args],
                          capture_output=True, text=True)
