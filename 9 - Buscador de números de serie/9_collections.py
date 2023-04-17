from collections import Counter, defaultdict, namedtuple

lista=[2,4,3,6,8,3,7,6]
frase='hola esto es una frase que tiene una palabra repetida'

Counter(frase.split())

serie= Counter([1,1,1,1,3,3,3,4,5,6,6])

#print(serie.most_common(2))
#print(list(serie)) #como set?



mi_dict= defaultdict(lambda: 'nada')

mi_dict['uno']= 'verde'
#print(mi_dict['dos'])
#print(mi_dict)




mi_tupla=('pimientos', 18, 65)

Persona= namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel= Persona('Ariel', 1.76, 79)

#print(ariel.altura)




import os


ruta=r'C:\Users\wwwse\Documents\Python visual\Recetas'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta {carpeta}')
    print('Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        if arch.endswith('txt'):
            print(f'\t{arch}')
    print('\n')




import datetime

minutos= datetime.datetime.now().minute

#print(minutos)


#Expresiones regulares

"""
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado 
como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que 
cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase 
no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
"""

import re

def verificar_mail(email):
    patron= re.compile(r'\w+@\w+\.com(.br)?$')
    verificar=re.match(patron, email)
    print(verificar)
    if not verificar:
        print("La dirección de email es incorrecta")
    elif verificar:
        print("Ok")
    else:
        print('No se que pasa')



#hola@gmail.com

def verificar_saludo(frase): #inicia con 'Hola'
    patron= r'^Hola'
    saludo= re.search(patron, frase)
    print(saludo)
    if not saludo:
        print('No has saludado')
    else:
        print('Ok')

 






'''
import zipfile

#mi_zip= zipfile.ZipFile('archivo_comprimido.zip', 'w')
#mi_zip.write('mi_texto_A.txt')
#mi_zip.write('mi_texto_B.txt')
#mi_zip.close()

zip_abierto= zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()
'''


import shutil


carpeta_origen= r'C:\Users\wwwse\Documents\Python visual\Udemy Python\Recetas'

archivo_destino= 'Recetas_comprimidas'
'''
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Recetas_comprimidas.zip', 'Recetas descomprimidas', 'zip')
'''
