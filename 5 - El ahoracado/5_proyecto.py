palabras='''
ambiente
espacio
entorno
area
superficie
volumen
region
zona
lado
mundo
planeta
sol
luna
estrella
galaxia
universo
clima
despejado
nublado
lluvia
nieve
viento
trueno
rayo
tormenta
cielo
este
oeste
sur
norte
derecha
izquierda
diagonal
exterior
interior
materiales'''

import random

lista_palabras= palabras.split()
letras_usadas=[]

palabra= random.choice(lista_palabras)
print('-'*len(palabra))


def pedir_letra():
    letra= input('Introduzca una letra:').lower()
    return letra


def validar_letra(letra):
    if len(letra)==1 and letra.isalpha()==1 and letra not in letras_usadas:   #PROBAR CONDICIONES CON UNA SOLA    
        letras_usadas.append(letra)
        return True
    else:
        return False


    


def correcto():
    for i in palabra:
        if i == letra:
            return True
    return False



def guiones():
    resultado=[]
    palista= list(palabra)
    for i in palista:
        if i in letras_usadas:
            resultado.append(i)
        elif i not in letras_usadas:
            resultado.append('-')
    return resultado


        
def completa(resultado):
    palista= list(palabra)
    if palista== resultado:
        return True
    return False


lista_incorrectas=[]
vidas=6


def incorrecta():
    global vidas
    vidas -=1
    print(f'Te quedan {vidas} vidas.')
    #lista_incorrectas.append(letra)
    print(f'Letras usadas: {letras_usadas}')


def fin_win():
    print('Enhorabuena, has ganado.')

def fin_lose():
    print('Has perdido.')
    


lista_incorrectas=[]
vidas=6

while vidas>0 and completa!=True:
    letra= pedir_letra()
    while validar_letra(letra)!=True:
        letra= pedir_letra()
    resultado= guiones()
    print(resultado)
    if correcto():
        if completa(resultado):
            fin_win()
            break
    else:
        incorrecta()
        if vidas==0:
            fin_lose()
            break





