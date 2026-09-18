# Data Analyst Hands-On Lab

A progressive, assignment-based course for learning Data Analytics by **doing the work**, not just watching tutorials.

The assignments build toward one portfolio project:

> **Customer Support & Chatbot Analytics Platform**

You will gradually move from raw operational data to SQL analysis, Python cleaning, data models, Snowflake, dbt, BI dashboards, statistics, and automated pipelines.

## Learning path

| Stage | Assignment | Main tools | Outcome |
|---|---|---|---|
| 1 | Data Audit — optional | Excel / Sheets | Basic data-quality practice |
| 2 | **SQL Business Analysis — current** | SQL, DuckDB, GitHub | Answer real business questions |
| 3 | Advanced SQL | SQL | CTEs, windows, reusable analytical logic |
| 4 | Data Cleaning & EDA | Python, Pandas, Jupyter | Clean and explore data |
| 5 | Data Modeling | SQL, ERD | Fact/dimension model and star schema |
| 6 | Cloud Warehouse | Snowflake | Raw, staging, analytics layers |
| 7 | Analytics Engineering | dbt | Models, tests, documentation, lineage |
| 8 | Statistics | Python | A/B testing and analytical validation |
| 9 | BI Dashboard | Tableau / Power BI | Executive KPI dashboard |
| 10 | Business Storytelling | Markdown / Slides | Findings and recommendations |
| 11 | Pipeline Automation | Airflow | Orchestrated analytics pipeline |
| 12 | Capstone | All tools | End-to-end portfolio project |

## Start here

### [Assignment 02 — SQL Business Analysis](assignments/02_sql_business_analysis/README.md)

Assignment 01 is kept only as an optional basic exercise. It is **not required**.

## How the course works

For each assignment:

1. Read the business scenario.
2. Do the hands-on work yourself.
3. Use the hint ladder only when blocked.
4. Save the required deliverables under `submissions/`.
5. Push to GitHub.
6. GitHub Actions runs objective checks.
7. The analytical reasoning is reviewed manually.
8. The next assignment is then unlocked.

## Automated checks

Install once:

```bash
python -m pip install -r requirements.txt
```

For the current assignment:

```bash
pytest -q tests/test_assignment_02.py
```

## Important rules

- Do not modify `data/raw/`.
- Do not copy solutions from the grader.
- Prefer understanding over memorizing syntax.
- Explain the business meaning of results, not just the numbers.

Track progress in [PROGRESS.md](PROGRESS.md).
