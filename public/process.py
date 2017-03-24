#!/usr/bin/env python
#-*- coding: utf-8 -*-

##############################################

from xml.sax.saxutils import escape as html_escape
import cgi
import sys
import HTML
import os
from wmflabs import db
conn = db.connect("s52741__mostLinkedMissing")

#Print header
print 'Content-type: text/html\n'

#Print header of html document
print """
<!DOCTYPE html>
<html lang="cs-cz">
        <head>
                <meta charset="utf-8" />
                <title>Chybějící stránky</title>
        </head>
        <body>
		<p><a href="index.html">Zpět</a>
"""
###############FUNCTIONS######################
#Print end header
def tail():
	print """
        </body>
	</html>
	"""
	quit()
def escape(html):
	"""Returns the given HTML with ampersands, quotes and carets encoded."""
	html_escape_table = {
		'"': "&quot;",
		"'": "&apos;"
	}
	return html_escape(html, html_escape_table)

sql = ''
#Parse webargs if present
if 'QUERY_STRING' in os.environ:
	nosql = False
	QS = os.environ['QUERY_STRING']
	qs = cgi.parse_qs(QS)
	try:
		title = qs['title'][0]
	except:
		title = ""
	try:
		offset = int(qs['offset'][0])
	except:
		offset = 0
	if 'special' in qs:
		if qs['special'][0] == 'first':
			nosql = True
			sql = 'select * from mostLinkedMissing where namespace=0 order by value desc limit ' + str(offset) + ', 100;'
		if qs['special'][0] == 'last':
			nosql = True
			sql = 'select * from mostLinkedMissing where namespace=0 order by value limit ' + str(offset) + ', 100;'


#Init db conn
cur = conn.cursor()
#Set names to utf so we could use non-ascii chars
with cur:
	cur.execute("SET NAMES utf8;")

cur = conn.cursor()
with cur:
	if nosql:
		cur.execute(sql)
		data = cur.fetchall()
	else:
		pass

table = HTML.table(data, header_row=['Jmenný prostor', 'Stránka', 'Počet odkazů'])
print table

tail()
