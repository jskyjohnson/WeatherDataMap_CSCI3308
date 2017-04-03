#!/usr/bin/python
import cgitb
cgitb.enable()
print ("Content-type: text/html")
print ('''
<html>
     <head>
          <title>My website</title>
     </head>
     <body>
          <p>Here I am</p>
     </body>
</html>
''')
