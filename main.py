import random
import time
import sys
from cuentitos import dino, iran



print('Bienvenide a la Torre de Mabel')
print('''
 ^ ^ ^\n |"|"|\n\-----/\n |  o|\n |   |\n
 |o  |\n |  o|                     /\ \n=======                   /  \ \n |   | /\                /    \                         /\ \n |o o|/  \              /      \                /\        /  \  /\ \n/|   |    \  /\        /        \      /\      /  \      /    \/  \    /\ \n |  o|     \/  \  /\  /          \  /\/  \    /    \  /\/          \  /  \/\ \n/=====\         \/  \/            \/      \/\/      \/              \/      \/\ \n
    ''')
ticket = None
while ticket is None:
    
    ticket = input('Presione ENTER o elija 1 o 0: ')
    # try:
    #     len(ticket) >= 1
    # except:
    #     print('Error. Entrada inválida.')
lst = []

if len(ticket) == 0:
    ticket = random.randrange(2)

if int(ticket) == 0:
    res = dino(lst)
    print(res)
if int(ticket) == 1:
    res = iran(lst)
    print(res)
