# import re
#
# fileh = open('texto.txt', encoding = 'utf_8')
#
# for line in fileh:
#     if len(line) < 1: continue
#     line = line.strip()
#
from bs4 import BeautifulSoup

with open('sitio.html', 'r', encoding = 'utf_8') as fileh:
    doc = fileh.read()

    soup = BeautifulSoup(doc, 'html.parser')
    print (soup.prettify())
