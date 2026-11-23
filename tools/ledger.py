#!/usr/bin/env python3
"""台帳（ledger.csv。学習ページの一覧と状態の正本）を作る・更新する。

使い方:
  python3 tools/ledger.py seed      初回だけ。ステップ 0〜4 の約 70 ページの行を作る（ledger.csv があれば止まる。--force で作り直す）
  python3 tools/ledger.py refresh   フォルダのあるページを検査し直し、memo・slides・状態を書き換える
                                    （手で決めた状態「薄いページ・重複・失敗」と、学習済みの日・備考は変えない）
  python3 tools/ledger.py learned <ID> [YYYY-MM-DD]   学習済みの日を入れる（日付を省くと今日）
"""
import datetime, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, LEDGER, STEPS, read_ledger, write_ledger
from page_status import page_status

A = "https://academy.claude.com/ja"
KB, TH = "学習・ビジネス", "技術・ハウツー"


def row(id_, step, group, d, slug, title, minutes, kind, fetch, url, status="未着手", note="", memo="", slides=""):
    return dict(id=id_, step=step, group=group, page_dir=f"{STEPS[step][0]}/{group}/{d}", slug=slug,
                title=title, minutes=minutes, kind=kind, fetch=fetch, url=url, status=status,
                memo=memo, slides=slides, learned_on="", note=note)


def seed_rows():
    R = []
    g = "01_claude-ai-learning"
    R.append(row("0-1", "0", g, "01_learning", "learning", "学ぶ（/learning 入口）", "", KB, "C", "https://claude.ai/learning", note="Chrome で読む。ボタンは押さない"))
    g = "02_academy-courses-claude-101"
    R.append(row("0-2", "0", g, "01_claude-101", "claude-101", "Claude 101（コースのトップ）", "150", KB, "A", f"{A}/courses/claude-101"))
    g = "03_academy-tutorials"
    R.append(row("0-3", "0", g, "01_getting-started-with-claude", "getting-started-with-claude", "Claudeを使い始める", "5", TH, "A", f"{A}/tutorials/getting-started-with-claude"))
    R.append(row("0-4", "0", g, "02_get-started-in-claude-cowork-in-three-steps", "get-started-in-claude-cowork-in-three-steps", "Coworkを3つのステップで始める", "4", TH, "A", f"{A}/tutorials/get-started-in-claude-cowork-in-three-steps", note="旧名称の題名"))
    R.append(row("0-5", "0", g, "03_delegating-your-first-task-in-claude-cowork", "delegating-your-first-task-in-claude-cowork", "Coworkで最初のタスクを委任する", "4", TH, "A", f"{A}/tutorials/delegating-your-first-task-in-claude-cowork", note="旧名称の題名"))
    R.append(row("0-6", "0", g, "04_customize-claude-cowork", "customize-claude-cowork", "Claudeをカスタマイズする", "7", TH, "A", f"{A}/tutorials/customize-claude-cowork", note="2-1 と同じページ（実体はここ）"))
    g = "01_academy-courses-claude-101"
    L = [("what-is-claude", "Claudeとは何ですか？", "5"), ("your-first-conversation-with-claude", "Claudeとの最初の会話", "15"),
         ("getting-better-results", "より良い結果を得る", "10"), ("claude-desktop-app-chat-cowork-code", "デスクトップでClaudeとどのように仕事をするか", "10"),
         ("introduction-to-projects", "プロジェクト入門", "15"), ("creating-with-artifacts", "アーティファクトで作成する", "10"),
         ("working-with-skills", "スキルを活用する", "15"), ("connecting-your-tools", "ツールを接続する", "15"),
         ("enterprise-search", "Enterprise Search（Team・Enterprise 向け）", "15"), ("research-mode-for-deep-dives", "深掘り調査のためのリサーチ機能（有料）", "10"),
         ("claude-in-action-use-cases-by-role", "Claudeの活用例：職種別ユースケース", "2"), ("other-ways-to-work-with-claude", "Claudeを活用するその他の方法", "15"),
         ("what-s-next", "次のステップ", "2"), ("certificate-of-completion", "コースクイズ", "8"), ("badge", "修了バッジ", "")]
    for i, (slug, t, m) in enumerate(L, 1):
        note = {"enterprise-search": "プラン条件（Team・Enterprise）を照合する", "research-mode-for-deep-dives": "プラン条件（有料）を照合する"}.get(slug, "")
        st = "未着手"
        if slug == "certificate-of-completion": st, note = "薄いページ", "本文なし（題名とクイズ 8 分だけ）"
        if slug == "badge": st, note = "失敗", "JS で描画されるため取得できない（--force は使わない）"
        R.append(row(f"1-{i}", "1", g, f"{i:02d}_{slug}", slug, t, m, KB, "A", f"{A}/courses/claude-101/{slug}", st, note))
    g = "01_academy-tutorials"
    R.append(row("2-1", "2", g, "01_customize-claude-cowork", "customize-claude-cowork", "Claudeをカスタマイズする", "7", TH, "A", f"{A}/tutorials/customize-claude-cowork", note="重複予定（実体は 0-6）。README だけ置く"))
    R.append(row("2-2", "2", g, "02_intro-to-projects", "intro-to-projects", "Projectsの概要", "7", TH, "A", f"{A}/tutorials/intro-to-projects", note="動画のみで本文が薄い可能性"))
    R.append(row("2-3", "2", g, "03_teach-claude-your-way-of-working-using-skills", "teach-claude-your-way-of-working-using-skills", "Skillsを使ってClaudeにあなたの仕事の進め方を教える", "", TH, "A", f"{A}/tutorials/teach-claude-your-way-of-working-using-skills", note="M1 の実例。本文に分数なし（学習メモの目安は 11）"))
    roles = [
        ("marketing", "マーケティング", [("campaign-brief", "キャンペーンブリーフ", 10), ("on-brand-content", "ブランドに沿ったコンテンツ", 10), ("repurpose-content", "チャネル横断で再利用", 10)]),
        ("sales", "営業", [("account-research-brief", "アカウントリサーチ", 10), ("call-prep-sheet", "商談準備", 10), ("transcript-themes", "通話記録テーマ抽出", 10)]),
        ("operations", "オペレーション", [("workflow-improvement-planner", "ワークフロー改善プランナー", 16), ("vendor-negotiation", "ベンダー交渉の準備", 10), ("prep-scattered-documents-for-a-compliance-audit", "監査向けの文書準備", 14)]),
        ("hr", "人事", [("create-new-hire-onboarding-guides", "オンボーディングガイド", 15), ("open-new-role", "新ポジション開設", 10), ("engagement-survey-themes", "サーベイからアクションプラン", 11)]),
        ("product", "プロダクト", [("prd-from-a-one-pager", "PRD 作成", 6), ("feedback-synthesis", "フィードバック統合", 10), ("metrics-narrative", "メトリクスのナラティブ化", 10)]),
        ("design", "デザイン", [("create-brand-assets", "ブランドアセット", 13), ("design-spec-from-threads", "デザイン仕様書", 12), ("uxr-synthesis", "インタビュー統合", 12)]),
        ("finance", "財務", [("explain-a-variance", "差異を説明", 12), ("organize-your-business-finances", "ビジネスの財務を整理", 13), ("variance-exec-slides", "差異から経営層向けスライド", 10)]),
        ("legal", "法務", [("legal-research-memo", "法律リサーチ", 10), ("regulatory-analysis", "規制とコンプライアンス", 11), ("organize-your-legal-workflows-using-projects", "Projects で法務ワークフロー整理", 16)]),
        ("research", "研究", [("plan-your-literature-review", "文献レビュー計画", 15), ("verify-statistics-from-raw-data", "生データから統計を検証", 16), ("work-through-grant-options-in-chat-with-claude", "助成金の選択肢", 14)]),
        ("engineering", "エンジニアリング", [("design-doc", "設計書（RFC）", 10), ("incident-postmortem", "ポストモーテム", 10), ("oncall-handoff-brief", "オンコール引き継ぎ", 10)]),
        ("data", "データ", [("answer-the-adhoc", "アドホックなデータ質問に答える", 10)]),
    ]
    for n, (role, jp, items) in enumerate(roles, 1):
        g = f"{n:02d}_{role}"
        R.append(row(f"3-{n:02d}-01", "3", g, f"01_roles-{role}", f"roles-{role}", f"{jp}の役割ページ", "", KB, "C", f"https://claude.ai/learning/roles/{role}", note="Chrome で読む。ボタンは押さない"))
        for k, (slug, t, m) in enumerate(items, 2):
            R.append(row(f"3-{n:02d}-{k:02d}", "3", g, f"{k:02d}_{slug}", slug, f"{jp}：{t}（★{k - 1}）", str(m), TH, "A", f"{A}/use-cases/{slug}"))
    R.append(row("4-1", "4", "01_academy-courses", "01_ai-fluency-framework-foundations", "ai-fluency-framework-foundations", "AI Fluency: Framework and foundations", "240", KB, "A", f"{A}/courses/ai-fluency-framework-foundations", note="コースのトップだけ（4 時間・14 レッスン）"))
    R.append(row("4-2", "4", "01_academy-courses", "02_ai-capabilities-and-limitations", "ai-capabilities-and-limitations", "AI capabilities and limitations", "210", KB, "A", f"{A}/courses/ai-capabilities-and-limitations", note="コースのトップだけ（3.5 時間・13 レッスン）"))
    R.append(row("4-3", "4", "01_academy-courses", "03_introduction-to-claude-cowork", "introduction-to-claude-cowork", "Introduction to Claude Cowork", "150", KB, "A", f"{A}/courses/introduction-to-claude-cowork", note="有料機能を含む。プラン条件を照合する"))
    R.append(row("4-4", "4", "02_academy-collections", "01_claude-for-you", "claude-for-you", "Claude for personal use（コレクション）", "", KB, "A", "https://academy.claude.com/collections/claude-for-you", note="日本語版なし。英語版を取り、解説は日本語で書く"))
    R.append(row("4-5", "4", "02_academy-collections", "02_claude-for-work", "claude-for-work", "Claude for work（コレクション）", "", KB, "A", "https://academy.claude.com/collections/claude-for-work", note="日本語版なし"))
    return R


MANUAL = {"薄いページ", "重複", "失敗"}


def refresh(rows):
    for r in rows:
        st = page_status(ROOT / r["page_dir"])
        if not st["has_dir"]:
            continue
        r["memo"], r["slides"] = st.get("memo", ""), st.get("slides", "")
        if r["status"] in MANUAL:
            continue
        has_memo = bool(st.get("memo")); has_slides = bool(st.get("slides"))
        ok = (has_memo and st["memo"] == "12 PASS" and has_slides and st.get("lint", 1) == 0
              and st["html"] and not st.get("numbers_missing") and st["links_broken"] == 0
              and (ROOT / r["page_dir"] / "README.md").exists())
        if ok:
            r["status"] = "完了"
        elif has_memo and has_slides:
            r["status"] = "要確認"
        else:
            r["status"] = "作成中" if (st.get("has_original") or has_memo) else "取得済"
    return rows


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    if a[0] == "seed":
        if LEDGER.exists() and "--force" not in a:
            print("ledger.csv が既にあります。作り直すなら --force"); sys.exit(1)
        write_ledger(seed_rows()); print(f"{len(seed_rows())} 行を書きました")
    elif a[0] == "refresh":
        _, rows = read_ledger(); write_ledger(refresh(rows)); print("更新しました")
    elif a[0] == "learned":
        d = a[2] if len(a) > 2 else datetime.date.today().isoformat()
        _, rows = read_ledger(); hit = [r for r in rows if r["id"] == a[1]]
        if not hit:
            print("その ID はありません"); sys.exit(1)
        hit[0]["learned_on"] = d; write_ledger(rows); print(f"{a[1]} を {d} に学習済みにしました")
    else:
        print(__doc__); sys.exit(2)


if __name__ == "__main__":
    main()
