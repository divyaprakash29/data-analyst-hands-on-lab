from pathlib import Path
import re
import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / "submissions" / "assignment_02"

REQUIRED_SQL = [f"q{i:02d}.sql" for i in range(1, 10)]

EXPECTED_COLUMNS = {
    "q01.sql": {"intent_normalized", "session_count"},
    "q02.sql": {"total_sessions", "resolution_rate", "escalation_rate", "avg_csat"},
    "q03.sql": {"intent_normalized", "total_sessions", "resolution_rate", "escalation_rate", "avg_csat"},
    "q04.sql": {"customer_id", "session_count"},
    "q05.sql": {"customer_segment", "total_sessions", "resolution_rate", "escalation_rate", "avg_csat"},
    "q06.sql": {"session_id", "customer_id", "intent", "ticket_id", "ticket_status", "resolution_hours"},
    "q07.sql": {"session_id", "issue_type", "issue_detail"},
    "q08.sql": {"ticket_category", "resolved_ticket_count", "avg_resolution_hours"},
    "q09.sql": {"customer_id", "session_id", "intent", "ticket_id", "ticket_status", "resolution_hours"},
}

def connection():
    con = duckdb.connect(database=":memory:")
    for name in ["customers", "chat_sessions", "support_tickets", "intent_reference"]:
        path = (ROOT / "data" / "raw" / f"{name}.csv").as_posix()
        con.execute(
            f"""
            CREATE OR REPLACE VIEW {name} AS
            SELECT *
            FROM read_csv_auto('{path}', header=true, all_varchar=true)
            """
        )
    return con

def run_query(filename):
    sql = (SUB / filename).read_text(encoding="utf-8").strip()
    con = connection()
    return con.execute(sql).fetchdf()

def test_submission_folder_and_files_exist():
    assert SUB.exists(), "Create submissions/assignment_02/"
    missing = [f for f in REQUIRED_SQL if not (SUB / f).exists()]
    assert not missing, f"Missing SQL files: {missing}"
    assert (SUB / "insights.md").exists(), "Missing insights.md"

def test_queries_are_not_empty_or_select_star():
    for filename in REQUIRED_SQL:
        path = SUB / filename
        if not path.exists():
            continue
        sql = path.read_text(encoding="utf-8").strip()
        assert len(sql) > 20, f"{filename} looks incomplete."
        assert not re.search(r"select\s+\*", sql, flags=re.I), f"{filename}: avoid SELECT * in final work."

def test_queries_execute_and_have_required_columns():
    for filename in REQUIRED_SQL:
        if not (SUB / filename).exists():
            continue
        try:
            df = run_query(filename)
        except Exception as exc:
            raise AssertionError(f"{filename} failed to execute: {exc}") from exc
        missing = EXPECTED_COLUMNS[filename] - set(df.columns)
        assert not missing, f"{filename} is missing columns: {sorted(missing)}"

def test_q02_kpi_shape_and_ranges():
    path = SUB / "q02.sql"
    if not path.exists():
        return
    df = run_query("q02.sql")
    assert len(df) == 1, "q02 should return exactly one KPI summary row."
    for col in ["resolution_rate", "escalation_rate"]:
        values = pd.to_numeric(df[col], errors="coerce")
        assert values.notna().all(), f"{col} must be numeric."
        assert values.between(0, 1).all(), f"{col} must be between 0 and 1."
    csat = pd.to_numeric(df["avg_csat"], errors="coerce")
    assert csat.notna().all(), "avg_csat must be numeric."
    assert csat.between(1, 5).all(), "avg_csat should exclude invalid scores outside 1–5."

def test_q04_only_repeat_contacts():
    path = SUB / "q04.sql"
    if not path.exists():
        return
    df = run_query("q04.sql")
    counts = pd.to_numeric(df["session_count"], errors="coerce")
    assert counts.notna().all(), "session_count must be numeric."
    assert (counts > 1).all(), "q04 should only return repeat-contact customers."

def test_q05_no_unknown_segment():
    path = SUB / "q05.sql"
    if not path.exists():
        return
    df = run_query("q05.sql")
    assert df["customer_segment"].fillna("").astype(str).str.strip().ne("").all(), (
        "q05 should not include sessions that cannot be mapped to a customer segment."
    )

def test_q07_detects_multiple_issue_families():
    path = SUB / "q07.sql"
    if not path.exists():
        return
    df = run_query("q07.sql")
    assert df["issue_type"].nunique() >= 4, "q07 should detect at least four issue families."

def test_q08_resolution_times_are_non_negative():
    path = SUB / "q08.sql"
    if not path.exists():
        return
    df = run_query("q08.sql")
    values = pd.to_numeric(df["avg_resolution_hours"], errors="coerce")
    assert values.notna().all(), "avg_resolution_hours must be numeric."
    assert (values >= 0).all(), "Resolved-ticket averages should exclude negative resolution times."

def test_insights_are_substantive():
    path = SUB / "insights.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8").strip()
    assert len(text) >= 900, "insights.md is too short. Explain findings, evidence, meaning, and caveats."
    lower = text.lower()
    assert lower.count("finding") >= 3, "Document at least three findings."
    assert "data caveats" in lower, "Include a Data caveats section."
    assert "investigate next" in lower, "Include follow-up questions."
