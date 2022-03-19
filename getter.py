import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs
import re

# Ignore SSL cetificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False


conn = sqlite3.connect ('Cuentos.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Cuentos
    (id INTEGER PRIMARY KEY, Titulo TEXT UNIQUE, Autor TEXT,
     Cuerpo TEXT, error INTEGER)''')


#check to se if we are already going
cur.execute('SELECT id, Titulo FROM Cuentos WHERE Cuerpo is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')

row = cur.fetchone()
if row is not None:
    print('Restarting existing crawl. Remove spider.sqlite to start a fresh crawl.')
else:
    # Esto es para sacar unos cuentitos que estan en un mismo link
    starturl = input('Enter web url or enter:')
    # Link por default
    if len(starturl) < 1:
        starturl = 'https://www.actualidadliteratura.com/los-mejores-microrrelatos-la-historia/'

            # Esto crea un pretty html del target
        urllib.request.urlretrieve(starturl, 'site.html')

        # No se si puedo usar BS con el '.html'
link = urllib.request.urlopen(starturl, context = ctx)
html = link.read()

soup = BeautifulSoup(html, 'html.parser')
pretty = soup.prettify()
text = soup.get_text()

fh = open('sitio.html', 'w', encoding = 'utf_8')
fh.write (pretty)
fh.close()


fh = open('texto.txt', 'w', encoding = 'utf_8')
file = fh.write(text)
fh.close()
# text = text.rstrip()
#             # Este loop aun no funciona creo. RegEx
# for x in text:
#     if len(x) == 0: continue
#     res = re.search('/[0-9.] ', x)
#     if res == None: continue
#     print (res)

            # Ya tengo todo el texto de la pagina en un archivo local.

    # Ahora capturo los cuentos

# fh = open('texto.txt', encoding = 'utf_8')
#
#
# for line in fh:
#     if len(line) < 1: continue
#     line = line.strip()
#     line = re.findall('/[0-9.] ',line)
#


print (starturl + '\n' + 'Learning most definitly not all done... yet! C-ya!')
cur.close()
