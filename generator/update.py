#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wmflabs import db

# Get the data from database
conn = db.connect('cswiki')
with conn.cursor() as cur:
	sql = "SELECT pl_namespace AS namespace, pl_title AS title, COUNT(*) AS value FROM pagelinks LEFT JOIN page AS pg1 ON pl_namespace = pg1.page_namespace AND pl_title = pg1.page_title LEFT JOIN page AS pg2 ON pl_from = pg2.page_id WHERE pg1.page_namespace IS NULL AND pl_namespace NOT IN ( 2, 3 ) AND pg2.page_namespace NOT IN ( 8, 10 ) GROUP BY pl_namespace, pl_title ORDER BY value;"
	cur.execute(sql)
	data = cur.fetchall()


# Store the data into tools-db
conn = db.connect('s53348__mostLinkedMissing')
with conn.cursor() as cur:
	sql = 'drop table if exists mostLinkedMissingNew;'
	cur.execute(sql)

with conn.cursor() as cur:
	sql = 'create table mostLinkedMissingNew ( namespace int , title varchar(256) , value int );'
	cur.execute(sql)

for row in data:
	with conn.cursor() as cur:
		sql = 'insert into mostLinkedMissingNew(namespace, title, value) values(' + str(row[0]) + ', "' + row[1].replace('"', '\\"') + '", ' + str(row[2]) + ');'
		print sql
		cur.execute(sql)
