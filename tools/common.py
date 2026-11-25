"""台帳・索引・ページ検査で共通に使うもの（標準ライブラリのみ。Python 3.9 以上）。"""
import csv, re, subprocess, shutil, glob, json, tempfile
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
    "9": ("step9_added", "追加（台帳の対象外で、URL を渡して作ったもの）"),
}


# ---- ページのフォルダの形（新構造）----
#   <ページ>/README.md（表紙）・00_originals/・解説メモ 5 本（直下）・docs/（スライド）・.work/（working-log.md と intermediate/）
MEMO_FILES = ["README.md", "01_source.md", "02_explanation_memo.md", "11_question_and_answer.md", "12_LLM_prompts_as_guide.md"]
WORK = ".work"
LOG_NAME = "working-log.md"
INTERMEDIATE = ".work/intermediate"
DOCS = "docs"


# ---- 解説メモ 5 本の冒頭リンクと「解説資料」の節 ----
# 冒頭：toTopPage は 1 つ上（まとまり）の README、toREADME は同じフォルダの README（README 自身も自分を指す）。
NAV_RE = re.compile(r"\A###### \[toTopPage\]\([^)]*\)\n###### \[toREADME\]\([^)]*\)")
NAV_NEW = "###### [toTopPage](../README.md)\n###### [toREADME](./README.md)"
NAV_CHECKER = "###### [toTopPage](./README.md)\n###### [toREADME](./README.md)"   # check_docs が決め打ちしている形
SLIDES_START, SLIDES_END = "<!-- slides:start -->", "<!-- slides:end -->"
SEP_LINES = "-----\n[toTop](#totoppage)\n"
# 解説資料の節。後ろの区切りは、あってもなくてもよい（版によって違うため）
SLIDES_BLOCK_RE = re.compile(re.escape(SLIDES_START) + r".*?" + re.escape(SLIDES_END) + r"\n(?:\n?" + re.escape(SEP_LINES) + r")?", re.S)


def checker_view_text(text):
    """check_docs に渡すための写し。冒頭リンクを check_docs が期待する形に戻し、「解説資料」の節（印の間）を外す。
    check_docs（ced-skills）は、冒頭を ./README.md と決め打ちし、フォルダの外を指すリンクを不合格にするため。
    それ以外は 1 字も変えない（ほかの検査項目は、本物のファイルのまま確かめる）。"""
    t = NAV_RE.sub(NAV_CHECKER, text, count=1)
    return SLIDES_BLOCK_RE.sub("", t, count=1)


def run_check_docs(page, checker):
    """ページのフォルダの解説メモ 5 本を check_docs で検査する。(subprocess の結果)
    ページのフォルダを複製し（リンク先の存在も検査されるため。中間ファイルは除く。中間ファイルは本物の場所を --out-dir で渡す）、
    5 本だけ、冒頭リンクと「解説資料」の節を check_docs が期待する形に戻して検査する。"""
    page = Path(page)
    with tempfile.TemporaryDirectory() as td:
        view = Path(td) / "page"
        shutil.copytree(page, view, ignore=shutil.ignore_patterns("intermediate", "aborted", ".DS_Store"))
        for n in MEMO_FILES:
            f = view / n
            if f.is_file():
                f.write_text(checker_view_text(f.read_text(encoding="utf-8")), encoding="utf-8")
        return run_py(checker, view, "--out-dir", intermediate_dir(page))


def has_memo(page):
    """解説メモ 5 本が、ページのフォルダの直下にそろっているか。"""
    return all((Path(page) / n).is_file() for n in MEMO_FILES)


def intermediate_dir(page):
    return Path(page) / INTERMEDIATE


def working_log(page):
    return Path(page) / WORK / LOG_NAME


def slide_mds(page):
    return sorted((Path(page) / DOCS).glob("*-explained-slides.md"))


def slide_htmls(page):
    return sorted((Path(page) / DOCS).glob("*-explained-slides.html"))


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


def find_ced(name):
    """ced-url-to-md の scripts/<name>（いちばん新しい版）。"""
    c = sorted(glob.glob(str(Path.home() / f".claude/plugins/cache/ced-skills/ced-skills/*/ced-url-to-md/scripts/{name}")))
    return c[-1] if c else None


def today():
    import datetime
    return datetime.date.today().isoformat()


_NAV = re.compile(r"^\s*(\*|-|\d+\.)?\s*\[[^\]]*\]\([^)]*\)\s*$")          # リンクだけの行（ナビ・一覧）
_NOISE = re.compile(r"^\s*(読み込み中|視聴|言語\s*日本語|!\[.*\]\(.*\)|\s*)$")


def body_text_chars(md_path):
    """本文の字数（空白除く）。ナビ・リンクだけの行・画像・フッターを除く。

    薄いページの判定（P-2）に使う。『© 』の行より後ろは、フッターとして数えない。
    """
    lines = body_of(md_path).split("\n")
    # Academy の共通ナビ（「AIについて学ぶ」などの見出しから、フッターまで）は本文ではない
    nav_heads = ("## AIについて学ぶ", "## 対象者別", "## 種類別", "## 製品別", "## ヘルプとドキュメント")
    kept = []
    skip = False
    for ln in lines:
        if ln.strip() in nav_heads:
            skip = True
        if ln.lstrip().startswith("©"):
            skip = False
            break
        if skip:
            continue
        if _NAV.match(ln) or _NOISE.match(ln):
            continue
        kept.append(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", ln))   # 本文中のリンクは文字だけ残す
    return len(re.sub(r"\s", "", "\n".join(kept)))
