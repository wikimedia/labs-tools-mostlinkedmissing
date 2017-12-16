##Run on cswiki.labsdb
SELECT pl_namespace AS namespace, pl_title AS title, COUNT(*) AS value FROM pagelinks LEFT JOIN page AS pg1 ON pl_namespace = pg1.page_namespace AND pl_title = pg1.page_title LEFT JOIN page AS pg2 ON pl_from = pg2.page_id WHERE pg1.page_namespace IS NULL AND pl_namespace NOT IN ( 2, 3 ) AND pg2.page_namespace NOT IN ( 8, 10 ) GROUP BY pl_namespace, pl_title ORDER BY value;
