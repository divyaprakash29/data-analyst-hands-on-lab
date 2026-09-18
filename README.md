# Data Analyst Hands-On Lab

A progressive, assignment-based course for learning Data Analytics by **doing the work**, not just watching tutorials.

The assignments build toward one portfolio project:

> **Customer Support & Chatbot Analytics Platform**

You will gradually learn how analysts move from messy raw data to clean datasets, SQL analysis, warehouse models, dashboards, statistical analysis, automated pipelines, and business recommendations.

## Learning path

| Stage | Assignment | Main tools | Outcome |
|---|---|---|---|
| 1 | Data Audit | Excel / Google Sheets, GitHub | Understand raw data and data quality |
| 2 | SQL Foundations | SQL, DuckDB/PostgreSQL | Answer business questions |
| 3 | Advanced SQL | SQL | Joins, CTEs, subqueries, window functions |
| 4 | Data Cleaning & EDA | Python, Pandas, Jupyter | Clean and explore raw data |
| 5 | Data Modeling | SQL, ERD | Fact/dimension model and star schema |
| 6 | Cloud Warehouse | Snowflake | Raw, staging, analytics layers |
| 7 | Analytics Engineering | dbt | Models, tests, documentation, lineage |
| 8 | Statistics | Python | A/B testing and analytical validation |
| 9 | BI Dashboard | Tableau / Power BI | Executive KPI dashboard |
| 10 | Business Storytelling | Markdown / Slides | Findings and recommendations |
| 11 | Pipeline Automation | Airflow | Orchestrated analytics pipeline |
| 12 | Capstone | All tools | End-to-end portfolio project |

Assignments are added progressively so each one reuses the work from earlier assignments.

## How to use this course

For every assignment:

1. Read the scenario and learning objectives.
2. Attempt the work yourself before looking for an answer.
3. If stuck, use the hint ladder one level at a time.
4. Save your work in the required submission folder.
5. Push your work to GitHub.
6. GitHub Actions will run automatic checks.
7. Your mentor can review reasoning and business interpretation that cannot be graded automatically.

## Start here

### [Assignment 01 — Customer Support Data Audit](assignments/01_data_audit/README.md)

This first assignment focuses on **Excel, data quality, keys, table relationships, and analytical thinking**.

## Automated checks

After you push a submission, GitHub Actions checks whether required files, columns, and basic deliverables are present.

You can also run checks locally:

```bash
python -m pip install -r requirements.txt
pytest -q
```

> Automated tests verify objective requirements. They do not replace human review of analytical reasoning.

## Repository structure

```text
data/
  raw/
assignments/
  01_data_audit/
submissions/
  assignment_01/
tests/
.github/workflows/
```

## Important rules

- Do not modify files under `data/raw/`.
- Do not skip directly to later assignments.
- Use hints before searching for full solutions.
- Explain your reasoning, not just your result.

The goal is not to finish quickly. The goal is to understand **why** each step exists in a real analytics workflow.
