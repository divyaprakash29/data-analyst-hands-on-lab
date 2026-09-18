# Assignment 02 — SQL Business Analysis

## Scenario

You are now working as a **Data Analyst on the Customer Experience team**.

Leadership wants answers about chatbot performance, escalation behavior, repeat contacts, customer segments, and support-ticket outcomes.

The data is still imperfect. Your job is to write SQL that produces **trustworthy business metrics despite messy source data**.

This is not a syntax-only exercise. You are expected to think like an analyst:

> What should be counted? What should be excluded? What business definition am I using?

---

## What you will practice

This assignment gives hands-on practice with:

- `SELECT`, `WHERE`, `ORDER BY`
- `COUNT`, `COUNT(DISTINCT ...)`, `AVG`
- `CASE WHEN`
- `GROUP BY`, `HAVING`
- string cleanup with `LOWER`, `TRIM`
- `INNER JOIN` and `LEFT JOIN`
- handling duplicates
- handling invalid dates with `TRY_CAST`
- conditional aggregation
- CTEs
- business KPI definitions
- translating query output into business insights

You will use **DuckDB** so you can query the CSV files directly without setting up a database server.

---

# 0. Setup

Clone/pull the repository and install dependencies:

```bash
python -m pip install -r requirements.txt
```

Test the SQL runner:

```bash
python tools/run_sql.py assignments/02_sql_business_analysis/examples/example.sql
```

If that works, you are ready.

The SQL runner automatically creates these views:

```text
customers
chat_sessions
support_tickets
intent_reference
```

They point to the CSV files under `data/raw/`.

---

# Submission structure

Create:

```text
submissions/assignment_02/
├── q01.sql
├── q02.sql
├── q03.sql
├── q04.sql
├── q05.sql
├── q06.sql
├── q07.sql
├── q08.sql
├── q09.sql
└── insights.md
```

Each SQL file should contain **one final query** that answers the question.

Run any query with:

```bash
python tools/run_sql.py submissions/assignment_02/q01.sql
```

---

# Analyst rules for this assignment

Unless a question explicitly says otherwise:

1. Treat `session_id` as the business identifier for a chatbot session.
2. Avoid double-counting duplicate session IDs.
3. Treat satisfaction scores outside **1–5** as invalid for CSAT calculations.
4. Use `TRY_CAST` rather than allowing bad date values to crash a query.
5. Do not silently drop records without understanding why.
6. Do not use `SELECT *` in final submissions.
7. Use readable aliases.

---

# Q1 — Normalize intent names and measure volume

The same intent may appear with inconsistent capitalization.

Write a query that returns:

```text
intent_normalized
session_count
```

Requirements:

- normalize intent using SQL string functions
- count **distinct sessions**
- sort highest volume first

### Business question

> Which intents generate the most chatbot traffic?

---

# Q2 — Build an overall chatbot KPI summary

Return exactly one row with:

```text
total_sessions
resolution_rate
escalation_rate
avg_csat
```

Requirements:

- use distinct session IDs
- resolution rate = resolved sessions / total sessions
- escalation rate = escalated sessions / total sessions
- average CSAT should include only scores from 1 through 5
- return rates as decimals between 0 and 1

### Example interpretation

A value of `0.40` means **40%**.

Do not hard-code results.

---

# Q3 — Compare performance by intent

Return:

```text
intent_normalized
total_sessions
resolution_rate
escalation_rate
avg_csat
```

Requirements:

- normalize intent text
- one row per normalized intent
- remove duplicate sessions
- exclude invalid CSAT values from the average
- sort by `escalation_rate` descending

### Business question

> Which intents appear to struggle most with self-service?

---

# Q4 — Find repeat-contact customers

Return customers with **more than one distinct chatbot session**.

Required columns:

```text
customer_id
session_count
```

Sort from highest to lowest session count.

### Business question

> Which customers are returning to support repeatedly?

Think carefully about why `COUNT(*)` and `COUNT(DISTINCT session_id)` may produce different answers.

---

# Q5 — Compare chatbot performance by customer segment

Join `customers` to `chat_sessions`.

Return:

```text
customer_segment
total_sessions
resolution_rate
escalation_rate
avg_csat
```

Requirements:

- normalize customer segment capitalization
- do not count duplicate sessions
- do not include sessions whose customer does not exist in the customer table
- exclude invalid CSAT from the average

### Business question

> Are some customer segments having a worse chatbot experience than others?

---

# Q6 — Analyze escalations that created support tickets

Identify chatbot sessions that:

- were escalated
- have a matching support ticket

Return:

```text
session_id
customer_id
intent
ticket_id
ticket_status
resolution_hours
```

Requirements:

- use an appropriate join
- one row per matched ticket
- sort longest valid `resolution_hours` first
- keep unresolved tickets visible

### Business question

> What happened after chatbot escalation?

---

# Q7 — Detect session-level data-quality problems with SQL

Create one result set with:

```text
session_id
issue_type
issue_detail
```

Your query must detect at least these four issue families:

- duplicate session ID
- invalid `started_at`
- invalid CSAT outside 1–5
- customer ID not present in `customers`

You may use CTEs and `UNION ALL`.

### Goal

This is your first hands-on example of using SQL for **data-quality monitoring**, not just reporting.

---

# Q8 — Analyze ticket resolution performance

Return:

```text
ticket_category
resolved_ticket_count
avg_resolution_hours
```

Requirements:

- normalize status capitalization
- only include tickets that are actually resolved/closed
- exclude missing or negative resolution times
- group by ticket category
- sort slowest average resolution first

### Business question

> Which types of support tickets take longest to resolve?

---

# Q9 — Build an unresolved-escalation customer journey

Use at least one CTE.

Find chatbot sessions that were:

- unresolved
- escalated

and then determine whether they generated a support ticket.

Return:

```text
customer_id
session_id
intent
ticket_id
ticket_status
resolution_hours
```

Use a join that still keeps an escalated chatbot session even if no ticket is found.

### Business question

> Where does the customer journey break after chatbot failure?

---

# Final deliverable — insights.md

After running all queries, write:

`submissions/assignment_02/insights.md`

Use this structure:

```markdown
# Assignment 02 — Business Insights

## Finding 1
What did you find?

Evidence:
Which query / metric supports it?

Business meaning:
Why should the company care?

## Finding 2
...

## Finding 3
...

## Data caveats
List at least 3 issues that could affect the conclusions.

## What I would investigate next
Write 2 follow-up questions.
```

Do not simply say:

> "Billing had the most sessions."

Translate the result into business meaning.

---

# Grading rubric

| Area | Points |
|---|---:|
| SQL correctness and successful execution | 35 |
| Correct joins / aggregation / deduplication | 25 |
| KPI definitions and data handling | 15 |
| Readability and SQL organization | 10 |
| Business insights | 15 |
| **Total** | **100** |

A score of **80+** is required before moving to Assignment 03.

---

# Automated checking

Run locally:

```bash
pytest -q tests/test_assignment_02.py
```

The grader checks:

- required files exist
- queries execute
- expected output columns exist
- obvious quality rules are respected
- insights are completed

It does **not** fully judge whether your business interpretation is good. That part is reviewed manually.

---

# Hints

If stuck, use:

[HINTS.md](HINTS.md)

Use the smallest hint needed. Do not inspect the test file for answers before completing the assignment.

---

# Stretch challenge — optional

Write one additional query named:

```text
bonus.sql
```

Create a metric called `support_pressure_score` using your own defensible formula based on:

- escalation rate
- unresolved rate
- CSAT

Rank intents from highest to lowest support pressure.

Document your formula and explain why you chose those weights in `insights.md`.

There is intentionally no single correct formula.
