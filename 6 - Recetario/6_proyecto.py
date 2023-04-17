#RECETAS
from pathlib import Path
import os
from os import system
from shutil import rmtree

#VARIABLES

#os.chdir(r'C:\\Users\wwwse\Documents\Python visual\Udemy Python\Recetas\Recetas')
ruta= input('Copia y pega la ruta de la carpeta "Recetas": ')
base=Path(ruta)
carpeta= base / 'Carnes' / 'Entrecot al Malbec.txt' 

categorias= [
    {
        'categoria':'Carnes',
        'recetas': {'Entrecot al Malbec': 'Entrecot al Malbec.txt',
            'Matambre a la Pizza': 'Matambre a la Pizza.txt'}
    },
    {
        'categoria':'Ensaladas',
        'recetas': {'Ensalada Griega': 'Ensalada Griega.txt',
            'Ensalada Mediterranea': 'Ensalada Mediterranea.txt'}
    },
    {
        'categoria':'Pastas',
        'recetas': {'Canelones de Espinaca': 'Canelones de Espinaca.txt',
            'Ravioles de Ricotta': 'Ravioles de Ricotta.txt'}
    },
    {
        'categoria':'Postres',
        'recetas': {'Compota de Manzana': 'Compota de Manzana.txt',
            'Tarta de Frambuesa': 'Tarta de Frambuesa.txt'}
    },    
]

opciones= {
    '1': 'Leer receta',
    '2': 'Crear receta',
    '3': 'Crear categoria',
    '4': 'Eliminar receta',
    '5': 'Eliminar categoria',
    '6': 'Finalizar programa'
}

#FUNCIONES

def eliminar_receta(receta_key, categoria1):
    decision= input(f'''¿Esta seguro que quiere eliminar la receta {receta_key}?
    Si es asi introduzca 1, si no 0: ''')
    if decision == '1':
        categoria= int(categoria1)
        ruta_categoria= categorias[categoria]['categoria']
        archivo= categorias[categoria]['recetas'][receta_key]
        ruta= base / ruta_categoria / archivo
        os.remove(ruta)
        categorias[categoria]['recetas'].pop(receta_key)
        print(f'La receta {receta_key} se ha eliminado.')
        
def eliminar_categoria(categoria1):
    categoria= int(categoria1)
    nombre_categoria= categorias[categoria]['categoria']
    decision= input(f'''¿Esta seguro que quiere eliminar la categoria {nombre_categoria}?
    Si es asi introduzca 1, si no 0: ''')
    if decision == '1':
        carpeta= categorias[categoria]['categoria']
        ruta= base / carpeta 
        rmtree(ruta)
        print(f'La receta {nombre_categoria} ha sido borrada.')
        categorias.pop(categoria)
        
def crear_receta(categoria1):        #introducir el indice como argumento
    receta= input('Introduce el nombre de la receta a crear: ')
    receta_txt= receta+'.txt'
    categoria= int(categoria1)
    nombre= categorias[categoria]['categoria']
    with open(base/nombre/receta_txt, 'w') as f:
        f.write(input('Introduce el contenido de la receta:'))
    try:
        categorias[categoria]['recetas'].update({receta : receta_txt})
    except KeyError:
        categorias[categoria]['recetas']= {receta : receta_txt}
    for n in categorias:
        print(n)

def crear_categoria(): #validacion?
    categoria= input('Introduzca el nombre de la categoria a crear: ')
    os.makedirs(base / categoria)
    diccionario={
        'categoria':f'{categoria}'
    }
    categorias.append(diccionario)
    for n in categorias:
        print(n)

def saludo():
    system('cls')
    recetas=0
    for txt in Path(base).glob('**/*.txt'):
        recetas+=1
    print(f'Hay {recetas} recetas.')

def input_opciones():
    for k,v in opciones.items():
        print(f'{k} - {v}')

    opcion= input('Introduce el nº de la opción deseada:')
    while not '0'< opcion< '7' or not opcion.isdigit():
        opcion= input('Introduce el nº de la opción deseada, entre 1 y 6:')
    return opcion

def elegir_categoria(): #devuelbe el indice de la lista principal elegido   intentar hacerlos con la libreria os
    n_categorias= len(categorias)
    for n in range(n_categorias):
        print( n,' - ', categorias[n]['categoria'])
    eleccion= input('Introduzca el número de la categoria:') #validacion
    while not 0 <= int(eleccion)< len(categorias) or not eleccion.isdigit():
        eleccion= input(f'Introduce el nº de la opción deseada, entre 0 y {n_categorias-1}:')
    return eleccion

def mostrar_recetas(eleccion): #intentar hacerlos con la libreria os
    num=0
    for n in categorias[int(eleccion)]['recetas'].keys():
        print(f'{num} - {n}')
        num +=1

def elegir_receta(eleccion): #devuelbe la key, nombre de la receta
    num=0
    receta= input('Introduzca el numero de la receta a leer: ')
    for key in categorias[int(eleccion)]['recetas'].keys():
        if num == int(receta):
            return key
        num+=1
    
def leer_receta(eleccion, key):
    categoria= categorias[int(eleccion)]['categoria']
    txt= categorias[int(eleccion)]['recetas'][key]
    ruta= base /categoria / txt
    with open(ruta, 'r') as f:
        print('\n',f.read(), '\n')

print('Hola, esto es un recetario, ¿que vamos a hacer hoy?')
print('Directorio:', base)
opcion= input_opciones()
while opcion != '6':
    saludo()
    if opcion== '1':
            categoria= elegir_categoria()
            mostrar_recetas(categoria)
            key= elegir_receta(categoria)
            leer_receta(categoria, key)
    elif opcion== '2':
            categoria= elegir_categoria()
            crear_receta(categoria)
    elif opcion==  '3':
            crear_categoria()
    elif opcion==  '4':
            categoria= elegir_categoria()
            mostrar_recetas(categoria)
            key= elegir_receta(categoria)
            eliminar_receta(key, categoria)
    elif opcion==  '5':
            categoria= elegir_categoria()
            eliminar_categoria(categoria) 
    opcion= input_opciones()
            



