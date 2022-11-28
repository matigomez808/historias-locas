import time

lst = []

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
    return f'Cuando {lst[0]}, el {lst[1]} todavía estaba allí.' + '\n\n' + 'El cuento original es "El dinosaurio", de Augusto Monterroso'

    #El dinosaurio, de Augusto Monterroso

def iran(x):
    cuento_og = '''En un desierto lugar del Irán hay una no muy alta torre de piedra,
    sin puerta ni ventana. En la única habitación (cuyo piso es de tierra y que tiene
    la forma de círculo) hay una mesa de maderas y un banco. En esa celda circular,
    un hombre que se parece a mi escribe en caracteres que no comprendo un largo
    poema sobre un hombre que en otra celda circular escribe un poema sobre un hombre
    que en otra celda circular…

    El proceso no tiene fin y nadie podrá leer lo que los prisioneros escriben.'''

    p1 = input('Ingrese un adjetivo masculino: ')
    lst.append(p1)
    p2 = input('Ingrese un sustantivo común: ')
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
El proceso no tiene fin y nadie podrá leer lo que los prisioneros {lst[5]}.


El cuento original es "Un sueño", de Jorge Luis Borges'''

def caballo(x):
    cuento_og: '''
    'Numeración incorrecta', de Isabel González
    "Un día me compraré un caballo de éstos. Rosa y con alas", dice la niña y señala,
    en el libro abierto sobre sus muslos, la foto de un flamenco. El hombre, alentado
    por tanta inocencia, se quita la chaqueta, estrecha su acercanza y escarba los
    bordes de la hoja sesgada mientras le explica que alguien arrancó una página entre
    definición e imagen, que después del doce no viene el quince y que imagínate si
    Genghis Khan hubiera dominado Mongolia sobre un ave de tan frágiles patas. Como
    si la niña no supiera. Como si no apretara en su puño la hoja extirpada. Como si
    las cosas no pudieran ser de otra forma.
    '''


def fantasma(x):
    cuento_og: '''
    'Fantasma', inédito de Patricia Esteban Erlés
    El hombre que amé se ha convertido en fantasma. Me gusta ponerle mucho suavizante,
    plancharlo al vapor y usarlo como sábana bajera las noches que tengo una cita prometedora.
    '''

def jodo(x):
    cuento_og: '''
    “Calidad y cantidad” – Alejandro Jodorowsky
    No se enamoró de ella, sino de su sombra. La iba a visitar al alba, cuando su
    amada era más larga.
    '''
