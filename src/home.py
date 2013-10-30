#!/usr/bin/env python2.7

import cgi
import cgitb; cgitb.enable()

print "Content-type: text/html"

print """
<html lang="en" id="skawtch">

<head>

<title>skawtch.com - a ubiqtus project</title>

<link rel=stylesheet href=static/style.css type=text/css>

<meta charget="utf-8" />
<meta name="robots" content="index, follow" />
<meta name="referrer" content="default" id="meta_referrer" />
<meta name="description" content="Skawtch is an umbrella project spanning the Web, created by the Ubiqtus development team (a small group of engineers interested in such topics as: information security, data mining, and robotics." />

</head>

<body>

<div class=content>
<dl>
  <dt class=desc>
  <div><h2>{ <a href="/">skawtch</a> }</h2></div>
</dl>"""

form = cgi.FieldStorage()
message = form.getvalue("message", "(no message)")

print """
<div class=status>
  <strong>current:</strong> %s
</div>

<form method=post action=home.py>
  <p class=tagline>new status: <input type=text name=message class=urlinput/></p>
  <input type=submit value=share>
</form>
</div>

</body>

</html>""" % cgi.escape(message)
