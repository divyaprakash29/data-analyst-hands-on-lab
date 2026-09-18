-- Example only. This is not one of the assignment answers.
-- Run with:
-- python tools/run_sql.py assignments/02_sql_business_analysis/examples/example.sql

SELECT
    customer_segment,
    COUNT(*) AS customer_rows
FROM customers
GROUP BY customer_segment
ORDER BY customer_rows DESC;
