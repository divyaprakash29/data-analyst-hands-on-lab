# Assignment 01 — Hint Ladder

Use the smallest hint necessary.

---

## Hint 1 — Start by understanding the tables

Before hunting for errors, answer:

> What does one row represent?

This is called the **grain** of the table.

Examples from other datasets:

- one row per customer
- one row per transaction
- one row per order item

Do this for all four tables.

---

## Hint 2 — Finding missing values in Excel

Use filters and look for blanks.

You can also use:

```excel
=COUNTBLANK(A2:A100)
```

Remember:

> A missing value is not automatically an error.

Ask whether the business process allows the value to be absent.

---

## Hint 3 — Finding duplicate IDs

If column A contains an ID:

```excel
=COUNTIF($A:$A,A2)
```

A result greater than 1 means the value appears more than once.

Then ask:

> Should this ID be unique for this table?

---

## Hint 4 — Finding inconsistent categories

Create a PivotTable or sort categorical fields.

Look for values that appear to mean the same thing but differ by:

- capitalization
- spacing
- abbreviations
- spelling

Example from a completely different dataset:

```text
Premium
premium
PREMIUM
```

---

## Hint 5 — Understanding foreign keys

Look for the same identifier in multiple tables.

If:

```text
customers.customer_id
```

uniquely identifies a customer, then another table might contain:

```text
chat_sessions.customer_id
```

as a foreign key.

---

## Hint 6 — Checking referential integrity

A foreign key should normally point to an existing parent record.

In Excel, `XLOOKUP` can help:

```excel
=XLOOKUP(A2,Customers!$A:$A,Customers!$A:$A,"NOT FOUND")
```

If you receive `NOT FOUND`, investigate.

---

## Hint 7 — Check numeric ranges

Ask:

> What values are logically possible?

For example:

- a rating system may have a minimum and maximum
- duration should usually not be negative
- monetary values need business context

Sort numeric columns ascending and descending.

---

## Hint 8 — Check dates

Sort timestamps chronologically.

Look for:

- malformed dates
- impossible dates
- unexpected time periods
- text values in a date column

Do not fix them yet. Record the issue.

---

## Hint 9 — Data quality is about business impact

For every problem, ask:

> What metric or decision could this problem distort?

Examples:

- duplicate sessions could inflate volume
- broken customer IDs could make joins incomplete
- inconsistent categories could split one business category into several dashboard rows

This reasoning belongs in your analyst notes.

---

## Hint 10 — Still stuck?

Focus on one table at a time.

For each column ask:

1. What does this column mean?
2. What type should it be?
3. Can it be blank?
4. Should it be unique?
5. Does it have an allowed range?
6. Does it reference another table?
7. Are the values consistently formatted?

That checklist will reveal most data-quality issues.
