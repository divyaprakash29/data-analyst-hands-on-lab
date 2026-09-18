# Assignment 02 — Hint Ladder

Use hints only when needed.

## Q1

Start by asking:

> What makes `Billing`, `billing`, and `BILLING` equivalent?

Look at `LOWER()` and `TRIM()`.

Remember that the source contains duplicate session IDs.

---

## Q2

You can calculate several KPIs in one query using conditional aggregation.

Pattern:

```sql
SUM(CASE WHEN condition THEN 1 ELSE 0 END)
```

For a rate, divide a conditional count by the total count.

Be careful with integer division and duplicate sessions.

---

## Q3

This is Q2 plus `GROUP BY`.

A useful strategy is:

1. make a clean/deduplicated CTE
2. calculate metrics from that CTE

---

## Q4

Ask yourself:

```text
COUNT(*)
```

versus

```text
COUNT(DISTINCT session_id)
```

Which one reflects unique chatbot sessions?

Use `HAVING` after grouping.

---

## Q5

The customer table owns customer attributes such as segment.

The chat table owns interaction metrics.

Join using the shared identifier.

If a session refers to a customer that does not exist, decide whether that row should contribute to a customer-segment analysis.

---

## Q6

Both tables contain `session_id`.

Start from escalated chatbot sessions, then join to tickets.

For unresolved tickets, `resolution_hours` may be NULL. Do not remove them unless the question requires it.

---

## Q7

Break the problem into multiple small queries.

For example:

- one query finds duplicate IDs
- one finds invalid dates
- one finds invalid CSAT
- one finds orphan customer IDs

Then combine the outputs.

Useful functions / patterns:

```sql
TRY_CAST(...)
GROUP BY ... HAVING ...
LEFT JOIN ...
UNION ALL
```

---

## Q8

Normalize status first.

Ask:

> Which status values represent completed work?

Then filter invalid resolution times.

Do not average negative numbers.

---

## Q9

Use a CTE to isolate failed chatbot sessions first.

Then use a join that preserves those sessions even if there is no ticket.

Ask:

> Which join keeps every row from the left side?

---

## Business-insight hint

A useful analyst statement often follows:

```text
Observation → Evidence → Business impact → Next question
```

Example using an unrelated scenario:

> Weekend orders had a 22% cancellation rate versus 9% overall. This suggests weekend fulfillment may need investigation. I would next compare staffing levels and delivery delays.

Notice that this does not claim causation without evidence.
