from pathlib import Path
import sys
import duckdb

ROOT = Path(__file__).resolve().parents[1]

def build_connection():
    con = duckdb.connect(database=":memory:")

    files = {
        "customers": ROOT / "data" / "raw" / "customers.csv",
        "chat_sessions": ROOT / "data" / "raw" / "chat_sessions.csv",
        "support_tickets": ROOT / "data" / "raw" / "support_tickets.csv",
        "intent_reference": ROOT / "data" / "raw" / "intent_reference.csv",
    }

    for view_name, path in files.items():
        escaped = str(path).replace("'", "''")
        con.execute(
            f"""
            CREATE OR REPLACE VIEW {view_name} AS
            SELECT *
            FROM read_csv_auto('{escaped}', header=true, all_varchar=true);
            """
        )

    return con

def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/run_sql.py <path-to-sql-file>")
        raise SystemExit(2)

    sql_path = Path(sys.argv[1])
    if not sql_path.exists():
        print(f"File not found: {sql_path}")
        raise SystemExit(2)

    sql = sql_path.read_text(encoding="utf-8").strip()
    if not sql:
        print(f"No SQL found in: {sql_path}")
        raise SystemExit(2)

    con = build_connection()

    try:
        result = con.execute(sql)
        if result.description:
            df = result.fetchdf()
            print(df.to_string(index=False))
            print(f"\nRows returned: {len(df)}")
        else:
            print("Query executed successfully.")
    except Exception as exc:
        print("\nSQL ERROR")
        print(exc)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
