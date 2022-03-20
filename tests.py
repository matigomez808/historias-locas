# import re
#
# fileh = open('texto.txt', encoding = 'utf_8')
#
# for line in fileh:
#     if len(line) < 1: continue
#     line = line.strip()
#
from bs4 import BeautifulSoup


#conn =

with open('sitio.html', 'r', encoding = 'utf_8') as fileh:
    doc = fileh.read()

    soup = BeautifulSoup(doc, 'html.parser')
    tags = soup.find_all('p', style = 'text-align: left;')
    count = 0
    for each in tags:
        count = count + 1
        line = each.strong
        if line is None: continue
        line = line.text.replace('\n','')
        line = line.strip()
        line = line.rstrip()
        #line = line.strip().rstrip()
        print(count, line)
