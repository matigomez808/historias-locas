import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL cetificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False


conn = sqlite3.connect ('spider.sqlite')
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
        starturl = 'https://www.eldiario.es/madrid/somos/malasana/diez-microrrelatos-de-terror_1_6421787.html'


document = urlopen(starturl, context = ctx)
html = document.read()
# No me estaria saliendo crear un archivo html como dios manda. Volver a chequear a dr Chuck

soup = BeautifulSoup(html, 'html.parser')
stuff = html.decode()



fh = open('10_microrrelatos.html', 'w')
fh.write(stuff)
fh.close()



#print (soup)
print (starturl, 'All done! C-ya!')
cur.close()
