"""
Abrir zip con codigo y ver de que trata el proyecto de hoy

import shutil

shutil.unpack_archive('Proyecto+Dia+9.zip', 'Proyecto 9 descomp', 'zip')
"""

import os
from pathlib import Path
import re
import datetime
import time
import math

ruta= 'C:\\Users\\wwwse\\Documents\\Python visual\\Proyecto 9 descomp\\Mi_Gran_Directorio'

#BUSCAR ARCHIVOS
def buscar_coincidencias():
    patron= r'N[A-Za-z]{3}-\d{5}'
    dict_referencias= {}
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            with open(Path(carpeta) / arch, 'r') as file:
                texto= file.read()
                finded= re.search(patron, texto)
            if finded: 
                dict_referencias[arch]= finded.group(0)
    return dict_referencias
    

def fecha():
    dia= datetime.date.today().day
    mes= datetime.date.today().month
    ano= datetime.date.today().year
    print(f'\nFecha de busqueda: {dia}/{mes}/{ano} \n')


def imprimir_coincidencias(dic):
    print('{:<15} {:<15}'.format('ARCHIVO', 'REFERENCIA'))
    print('{:<15} {:<15}'.format('-------', '----------'))
    for k, v in dic.items():
        print('{:<15} {:<15}'.format(k, v))
    print('\n')
    


#EJECUCION DEL PROGRAMA
inicio= time.time()
print('-'*40)

fecha()
apariciones= buscar_coincidencias()
imprimir_coincidencias(apariciones)
n= apariciones.__len__()
print(f'Numeros encontrados: {n}')

final= time.time()
tiempo= math.ceil(final-inicio)
print(f'Duracion de la busqueda: {tiempo} segundo')
print('-'*40)



