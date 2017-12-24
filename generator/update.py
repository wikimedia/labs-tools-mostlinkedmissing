#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import generators
from wmflabs import db

def ResultIter(cursor, arraysize=1000):
	 'An iterator that uses fetchmany to keep memory usage down'
	 while True:
	 	results = cursor.fetchmany(arraysize)
		if not results:
			break
		for result in results:
			yield result

# Prepare database for storing

conn = db.connect('s53348__mostLinkedMissing')
with conn.cursor() as cur:
	sql = 'drop table if exists mostLinkedMissingNew;'
	cur.execute(sql)

with conn.cursor() as cur:
	sql = 'create table mostLinkedMissingNew ( namespace int , title varchar(256) , value int );'
	cur.execute(sql)


# Get the data from database
conn = db.connect('cswiki')
with conn.cursor() as cur:
	sql = "SELECT pl_namespace AS namespace, pl_title AS title, COUNT(*) AS value FROM pagelinks LEFT JOIN page AS pg1 ON pl_namespace = pg1.page_namespace AND pl_title = pg1.page_title LEFT JOIN page AS pg2 ON pl_from = pg2.page_id WHERE pg1.page_namespace IS NULL AND pl_namespace NOT IN ( 2, 3 ) AND pg2.page_namespace NOT IN ( 8, 10 ) GROUP BY pl_namespace, pl_title ORDER BY value;"
	cur.execute(sql)
	tconn = db.connect('s53348__mostLinkedMissing')
	with tconn.cursor() as cur2:
		sql = 'set charset utf8;'
		cur2.execute(sql)
	for row in ResultIter(cur):
		with tconn.cursor() as cur2:
			sql = 'insert into mostLinkedMissingNew(namespace, title, value) values(' + str(row[0]) + ', "' + row[1].replace('"', '\\"') + '", ' + str(row[2]) + ');'
			cur2.execute(sql)
