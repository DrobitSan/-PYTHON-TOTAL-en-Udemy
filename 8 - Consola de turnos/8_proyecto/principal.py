"""
PROYECTO 8 DEL CURSO DE UDEMY
Turnero de una FARMACIA
"""

import numeros

def saludo():
    print('Bienvenido a la Farmacia Mari Carmen')
    print("""
    F - Farmacia \n
    P - Perfumeria \n
    C - Cosmetica \n
    """)


def opcion():
    while True:
        try:
            eleccion= input('Inserte la letra de la categoria deseada: ').upper()
            ['P','C','F'].index(eleccion)
        except ValueError:
            print('Esa no es una opcion valida.')
        else:
            return eleccion


def imprimir_resultado(eleccion):
    if eleccion== 'F':
        numeros.farmacia_decorada()
    elif eleccion== 'P':
        numeros.perfumeria_decorada()
    elif eleccion== 'C':
        numeros.cosmetica_decorada()


while True:
    saludo()
    eleccion= opcion()
    imprimir_resultado(eleccion)






