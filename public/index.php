<!DOCTYPE html>
<html lang="cs-cz">
	<head>
		<meta charset="utf-8" />
		<title>Chybějící stránky (i s odkazy)</title>
	</head>
	<body>
		<form method="GET" action="process.py">
			<p>Zadejte začátek názvu</p>
			<input type="text" name="title" />
			<input type="submit" />
			<input type="hidden" value="0" name="offset" />
		</form>
		<p>Další odkazy</p>
		<ol>
			<li><a href="process.py?title=a&offset=0&special=first">Prvních 100 nejlinkovanějších článků</a></li>
			<li><a href="process.py?title=a&offset=0&special=last">Posledních 100 nejlikovanějších článků</a></li>
		</ol>
		<br/>
		<p>Program využívá dat z <?php echo(file_get_contents("/data/project/mostlinkedmissing/mostlinkedmissing/public/date.txt")); ?> </p>
	</body>
</html>
