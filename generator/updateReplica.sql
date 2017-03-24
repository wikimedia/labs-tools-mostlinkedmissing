##Run on cswiki.labsdb

#Make sure the database&table exists
drop database if exists u13367__mostLinkedMissing;
create database u13367__mostLinkedMissing;
use u13367__mostLinkedMissing;
create table mostLinkedMissingNew ( namespace tinyint(10) , title varchar(256) , value tinyint(10) );

#Copy data
use cswiki_p;
insert into u13367__mostLinkedMissing.mostLinkedMissingNew
SELECT pl_namespace AS namespace, pl_title AS title, COUNT(*) AS value FROM pagelinks LEFT JOIN page AS pg1 ON pl_namespace = pg1.page_namespace AND pl_title = pg1.page_title LEFT JOIN page AS pg2 ON pl_from = pg2.page_id WHERE pg1.page_namespace IS NULL AND pl_namespace NOT IN ( 2, 3 ) AND pg2.page_namespace NOT IN ( 8, 10 ) GROUP BY pl_namespace, pl_title ORDER BY value
