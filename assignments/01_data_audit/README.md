# Assignment 01 — Customer Support Data Audit

## Business scenario

You have joined the **Customer Experience Analytics** team at a telecom company.

The company uses a chatbot for customer-service questions. The analytics team wants to build reporting around:

- chatbot volume
- customer intents
- resolution rate
- escalations to human support
- customer satisfaction
- repeat support contacts

Before anyone builds SQL queries or dashboards, the team needs to understand whether the raw data can be trusted.

You have received four CSV extracts:

- `data/raw/customers.csv`
- `data/raw/chat_sessions.csv`
- `data/raw/support_tickets.csv`
- `data/raw/intent_reference.csv`

Your first responsibility is to **audit the data**.

Do not clean the raw files in this assignment.

---

## Learning objectives

By the end of this assignment, you should be able to explain:

- what a row and column represent
- what table **grain** means
- primary key vs foreign key
- how tables relate
- missing values and why some may be acceptable
- duplicate records
- inconsistent categorical values
- invalid values and dates
- referential-integrity problems
- why a Data Analyst performs data validation before reporting
- how to communicate data-quality findings clearly

You will also practice:

- Excel filters
- sorting
- conditional formatting
- `COUNTIF`
- `COUNTBLANK`
- `COUNTA`
- `XLOOKUP`
- PivotTables
- Git / GitHub

---

# Part 1 — Explore the raw files in Excel

Open all four CSV files in Excel or Google Sheets.

For **each table**, determine:

1. What does one row represent?
2. How many rows are there?
3. How many columns are there?
4. What is the likely primary key?
5. Which columns could be foreign keys?
6. Which columns contain missing values?
7. Are any IDs duplicated?
8. Are category values consistent?
9. Are numeric values reasonable?
10. Are dates/timestamps valid?
11. Do foreign-key values always exist in the parent table?

Do not simply look at the first few rows. Use filters, sorts, formulas, and PivotTables.

---

# Part 2 — Build a Data Dictionary

Create:

`submissions/assignment_01/data_dictionary.csv`

Use **exactly** these columns:

```text
table_name,column_name,data_type,description,key_type
```

Example:

```csv
customers,customer_id,text,Unique identifier for a customer,primary_key
```

Allowed `key_type` values:

```text
primary_key
foreign_key
none
```

Document **every column from all four raw datasets**.

### Think before choosing a data type

For example, an ID such as `C001` is not really a number even though it contains digits.

---

# Part 3 — Create a Data Quality Report

Create:

`submissions/assignment_01/data_quality_report.csv`

Use exactly these columns:

```text
issue_id,table_name,column_name,issue_type,rows_affected,description,recommended_action
```

Examples of possible `issue_type` labels include:

```text
missing_value
duplicate
invalid_value
inconsistent_category
invalid_date
referential_integrity
```

These are examples, not necessarily a complete answer.

Identify **at least 10 distinct data-quality issues**.

### Important distinction

If 5 rows have the same problem, that is usually **one issue affecting 5 rows**, not 5 separate issues.

Bad:

```text
Issue 1: row 10 has missing spend
Issue 2: row 15 has missing spend
```

Better:

```text
Issue 1: monthly_spend contains 2 missing values
```

---

# Part 4 — Analyst Notes

Copy:

`assignments/01_data_audit/starter/answers_template.md`

to:

`submissions/assignment_01/answers.md`

Complete every question in your own words.

Do not write only one-line answers. Explain the reasoning.

---

# Part 5 — Excel mini-analysis

Using a PivotTable, answer these two questions:

1. Which chatbot intents have the highest number of sessions?
2. Which chatbot intents have the highest number of escalated sessions?

Add your observations to `answers.md`.

At this stage, you are **not** expected to calculate a statistically rigorous KPI. The goal is to practice exploring data before deeper analysis.

---

# Required deliverables

Your submission should contain:

```text
submissions/
└── assignment_01/
    ├── data_dictionary.csv
    ├── data_quality_report.csv
    └── answers.md
```

Optional but recommended:

```text
assignment_01_audit.xlsx
```

Keep the workbook as evidence of your Excel practice.

---

# Submission checklist

Before pushing to GitHub, confirm:

- [ ] I did not modify `data/raw/`
- [ ] Every source column appears in my data dictionary
- [ ] I identified at least 10 distinct data-quality issues
- [ ] I explained the grain of every table
- [ ] I identified keys and relationships
- [ ] I completed every question in `answers.md`
- [ ] I created the requested PivotTable analysis
- [ ] My files are saved under `submissions/assignment_01/`

---

# Grading rubric

| Area | Points |
|---|---:|
| Data dictionary completeness and accuracy | 20 |
| Identification of data-quality issues | 30 |
| Understanding of grain, keys, and relationships | 20 |
| Analytical reasoning and business impact | 20 |
| Organization and professional submission | 10 |
| **Total** | **100** |

### Score guide

- **90–100:** Excellent — ready for Assignment 02
- **80–89:** Good — minor corrections
- **70–79:** Needs revision before continuing
- **Below 70:** Revisit the concepts and resubmit

---

# Hint policy

If you are stuck, open:

### [HINTS.md](HINTS.md)

Start with Hint 1 and move gradually.

Do not search for a full solution. The struggle is part of the exercise.

---

# After you finish

Push your work to GitHub.

Suggested commands:

```bash
git add .
git commit -m "Complete assignment 01 data audit"
git push
```

GitHub Actions will run the automated submission checks.

Your mentor can then review the actual analytical reasoning before Assignment 02 is unlocked.
