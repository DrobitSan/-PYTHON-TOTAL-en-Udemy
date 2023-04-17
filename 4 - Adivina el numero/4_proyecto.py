'''PROGRAMA PARA ADIVINAR NUMERO 
8 INTENTOS -> 4 RESPUESTAS DEL PROGRAMA: FUERA DE LOS LIMITES, MAYOR, MENOR Y NUMERO CORRECTO
'''

from random import randint


n_correcto= randint(1,100)

guess= int(input('¿Que numero crees que estoy pensando, del 1 al 100? Tienes 8 intentos, suerte ;P\n'))

while 0>guess or guess>100:
    guess= int(input('El numero no se encuentra dentro de los limites, prueba con otro: '))

intentos=8

while intentos>0:
    if guess== n_correcto:
        print('Enhorabuena, has acertado el número.')
        break
    elif guess>n_correcto:
        print('Busca un numero mas pequeño, como tu pene: ')
    elif guess<n_correcto:
        print('Busca un numero mas grande, como las mentiras de tu ex: ')

    intentos -=1

    guess= int(input(f'Te quedan {intentos} intentos. Prueba con otro: '))
