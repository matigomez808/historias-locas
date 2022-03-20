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


conn = sqlite3.connect('historias_locas.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS historias_locas''')
cur.execute('''CREATE TABLE IF NOT EXISTS historias_locas(
                id INTEGER PRIMARY KEY,
                autor TEXT,
                titulo TEXT UNIQUE,
                texto TEXT UNIQUE
                ); '''
            )
url = input('URL:')
if len(url) < 1:
    url = 'https://www.actualidadliteratura.com/los-mejores-microrrelatos-la-historia/'

urllib.request.urlretrieve(url, 'sitio.html')

with open('sitio.html', 'r', encoding = 'UTF_8') as fileh:
    documento = fileh.read()
    soup = BeautifulSoup(documento, 'html.parser')
    texto = soup.find_all('p', style = 'text-align: left;')
    print(type(texto))
    palabras = None
    count = 0
    for each in texto:
        linea = each.text
        lista = re.findall('^[A-Z].+,\sde\s[A-Z].+\s.+', linea)
        if len(lista) == 0:
            palabras = linea
        else:
            for item in lista:
                posb = item.find(',')
                titulo = item[0:posb]
                autor = item[posb + 5:]
        cur.execute('''INSERT OR IGNORE INTO historias_locas(autor, titulo, texto)
        VALUES(?, ?, ?);''', (autor, titulo, palabras))
        print('adding entry...')

conn.commit()
cur.close()
