with new_table1 as
(select
year,
revised_data,
old_data,
Round(pct_change,2) AS pct_change
from sa_liquidations_yearly),

new_table2 as
(SELECT
AVG (revised_data) AS avg_revised_data,
old_data,
pct_change,
year
FROM new_table1
GROUP BY old_data,pct_change, year)

SELECT * FROM new_table2;