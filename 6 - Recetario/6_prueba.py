import os 
import pathlib

#ruta= os.getcwd()      nos da la ruta actual
#ruta= os.chdir()       cambia a la ruta especificada

#ruta= os.makedirs('C:\\Users\\wwwse\\Documents\\Python visual\\Udemy Python\\Recetas\\Recetas\\Nueva categoria')
#   crea una nueva carpeta

ruta= 'C:\\Users\\wwwse\\Documents\\Python visual\\Udemy Python\\Recetas\\Recetas'

#archivo= os.path.basename(ruta)
#directorio= os.path.dirname(ruta)
#tupla= os.path.split(ruta)     nos da una tupla con las dos anteriores 
#eliminar_carpeta= os.rmdir('ruta directorio a borrar')


contenido= os.listdir(r'C:\\Users\wwwse\Documents\Python visual\Udemy Python\Recetas\Recetas')

'''with os.scandir(ruta) as ficheros:
    for f in ficheros:
        print(f.name)'''

ruta2= pathlib.Path(ruta)
'''for f in ruta2.iterdir():
    print(f.name)'''


diccionario= []


#categorias= [f.name for f in ruta2.iterdir() if f.is_dir()]

'''
categorias= []

for n, f in enumerate(ruta2.iterdir()):
    if f.is_dir():
        categorias.append([f.name])
        with os.scandir(ruta / f) as ficheros:
                categorias[n].append([ fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.txt')])
        print(categorias[n])
'''
import re
patron= r'N[A-Za-z]{3}-\d{5}'

texto= 'aonw uwvnbiev Nrft-32123 dvdf dfb'
x= re.search(patron, texto)


with open('C:\\Users\\wwwse\\Documents\\Python visual\\mi_texto_A.txt', 'r') as f:
    print(f)