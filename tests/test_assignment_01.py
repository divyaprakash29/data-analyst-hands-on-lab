from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
SUB = BASE / "submissions" / "assignment_01"

def test_submission_folder_exists():
    assert SUB.exists(), "Create submissions/assignment_01/"

def test_required_files_exist():
    required = [
        "data_dictionary.csv",
        "data_quality_report.csv",
        "answers.md",
    ]
    missing = [name for name in required if not (SUB / name).exists()]
    assert not missing, f"Missing required submission files: {missing}"

def test_data_dictionary_structure():
    path = SUB / "data_dictionary.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    expected = ["table_name", "column_name", "data_type", "description", "key_type"]
    assert list(df.columns) == expected, f"Use exactly these columns: {expected}"
    assert len(df) >= 28, "Document every column from all four raw datasets."
    assert set(df["table_name"].astype(str).str.strip()) >= {
        "customers", "chat_sessions", "support_tickets", "intent_reference"
    }
    assert df["description"].fillna("").str.strip().ne("").all(), "Every field needs a description."

def test_data_dictionary_key_types():
    path = SUB / "data_dictionary.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    valid = {"primary_key", "foreign_key", "none"}
    actual = set(df["key_type"].dropna().astype(str).str.strip())
    assert actual.issubset(valid), f"key_type must use only: {sorted(valid)}"

def test_quality_report_structure():
    path = SUB / "data_quality_report.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    expected = [
        "issue_id", "table_name", "column_name", "issue_type",
        "rows_affected", "description", "recommended_action"
    ]
    assert list(df.columns) == expected, f"Use exactly these columns: {expected}"
    assert len(df) >= 10, "Identify at least 10 distinct data-quality issues."
    assert df["issue_id"].nunique() == len(df), "issue_id values should be unique."

def test_quality_report_fields_are_completed():
    path = SUB / "data_quality_report.csv"
    if not path.exists():
        return
    df = pd.read_csv(path)
    for col in ["table_name", "column_name", "issue_type", "description", "recommended_action"]:
        assert df[col].fillna("").astype(str).str.strip().ne("").all(), f"{col} cannot be blank."
    affected = pd.to_numeric(df["rows_affected"], errors="coerce")
    assert affected.notna().all(), "rows_affected must be numeric."
    assert (affected > 0).all(), "rows_affected must be greater than zero."

def test_answers_are_substantive():
    path = SUB / "answers.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    assert len(text.strip()) >= 900, "Analyst notes are too short. Explain your reasoning."
    placeholders = [
        "One row represents:",
        "**Answer:** Yes / No",
        "1.\n2.\n3.\n4.\n5."
    ]
    for placeholder in placeholders:
        assert placeholder not in text, f"Complete the template section containing: {placeholder!r}"
