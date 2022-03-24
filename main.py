import random
import time

def dino(x):
    cuento_og = 'Cuando despertó, el dinosaurio todavía estaba allí.'
    p1 = input('Ingrese un verbo en pasado: ')
    lst.append(p1)
    p2 = input('Ingrese un sustantivo: ')
    lst.append(p2)
    print('\n\n')
    print ('Estamos reconfigurando su historia. Aguarde un momento...')
    print('\n\n')
    time.sleep(3)
    return f'Cuando {lst[0]}, el {lst[1]} todavía estaba allí.'

    #El dinosaurio, de Augusto Monterroso

def iran(x):
    cuento_og = '''En un desierto lugar del Irán hay una no muy alta torre de piedra,
    sin puerta ni ventana. En la única habitación (cuyo piso es de tierra y que tiene
    la forma de círculo) hay una mesa de maderas y un banco. En esa celda circular,
    un hombre que se parece a mi escribe en caracteres que no comprendo un largo
    poema sobre un hombre que en otra celda circular escribe un poema sobre un hombre
    que en otra celda circular…

     El proceso no tiene fin y nadie podrá leer lo que los prisioneros escriben.'''

    p1 = input('Ingrese un adjetivo: ')
    lst.append(p1)
    p2 = input('Ingrese un sustantivo: ')
    lst.append(p2)
    p3 = input('Ingrese un sustantivo: ')
    lst.append(p3)
    p4 = input('Ingrese un sustantivo: ')
    lst.append(p4)
    p5 = input('Ingrese un sustantivo propio: ')
    lst.append(p5)
    p6 = input('Ingrese un verbo en plural: ')
    lst.append(p6)
    print('\n\n')
    print ('Estamos reconfigurando su historia. Aguarde un momento...')
    print('\n\n')
    time.sleep(3)


    return f'''
En un desierto {lst[0]} del Irán hay una no muy alta torre de {lst[1]},
sin {lst[2]} ni ventana. En la única habitación (cuyo piso es de tierra y que tiene
la forma de círculo) hay una mesa de maderas y un {lst[3]}. En esa celda circular,
un hombre que se parece a {lst[4]} escribe en caracteres que no comprende un largo
poema sobre un {lst[4]} que en otra celda circular escribe un poema sobre un {lst[4]}
que en otra celda circular…

El proceso no tiene fin y nadie podrá leer lo que los prisioneros {lst[5]}.'''


print('Bienvenide a la Madlibs Experience\n\n     "luces de colores"\n\n')

ticket = input('Presione ENTER o elija: ')
lst = []

if len(ticket) == 0:
    ticket = random.randrange(2)

if int(ticket) == 0:
    print(dino(lst))
if int(ticket) == 1:
    print(iran(lst))
