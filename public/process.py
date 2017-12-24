#!/usr/bin/env python
#-*- coding: utf-8 -*-

##############################################

from xml.sax.saxutils import escape as html_escape
import cgi
import sys
import HTML
import os
from wmflabs import db
conn = db.connect("s53348__mostLinkedMissing")

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
		<p><a href="index.php">Zpět</a>
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
	try:
		if qs['smer'][0] == 'asc':
			smer = 'asc'
		else:
			smer = 'desc'
	except:
		smer = 'desc'
	if 'special' in qs:
		if qs['special'][0] == 'first':
			nosql = True
			special = 'first'
			sql = 'select title, value from mostLinkedMissing where namespace=0 order by value desc limit ' + str(offset) + ', 100;'
		if qs['special'][0] == 'last':
			nosql = True
			sql = 'select title, value from mostLinkedMissing where namespace=0 order by value limit ' + str(offset) + ', 100;'
			special = 'last'


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
		sql = 'select title, value from mostLinkedMissing where namespace=0 and title like "' + title + '%" order by value ' + smer + ' limit ' + str(offset) + ', 100;'
		cur.execute(sql)
		data = cur.fetchall()

table = HTML.table(data, header_row=['Stránka', 'Počet odkazů'])
print table

urlNext = 'process.py?title=' + title + '&offset=' + str(offset+100)
if nosql:
	urlNext += "&special=" + special
urlPrev = "process.py?title=" + title + '&offset=' + str(offset-100)
if nosql:
	urlPrev += "&special=" + special

toPrint = '<a href="' + urlNext + '">Další</a>'
if offset != 0:
	toPrint += ' <a href="' + urlPrev + '">Předchozí</a>'

print toPrint

tail()
