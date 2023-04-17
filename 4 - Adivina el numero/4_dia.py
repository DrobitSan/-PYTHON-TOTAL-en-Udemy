#ZIP    -> combinar listas en tuples por indices, hasta la lista mas corta

nombres= ['Carla','David', 'Jon']

edades= [67, 4, 45]

ciudad= ['Lima', 'Madrid', 'Lviv']


combinado= list(zip(nombres, edades, ciudad))

print(combinado)



for nombre, edad, ciudad in combinado:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}.')

#min y max


#random fuck

from random import *


aleatorio= randint(1,50)

otro= round(uniform(1,5))

aja= random()

colores=['azul','rojo','tu padre']
este= choice(colores)

numeros= list(range(0,80,4))
shuffle(numeros)

print(aleatorio)
print(otro)
print(este)
print(numeros)


#COMPRENSION DE LISTAS

palabra= 'Python'

lista= [letra for letra in palabra]
lista2= [letra for letra in 'python']
yoquese= [n/2 for n in range(0,40,2) if n > 10]     #ACCION para ITERACION en OBJETO ITERABLE SI CONDICION
yaves= [n if n > 10 else 'no' for n in range(40)]   #DEVOLUCION SI CONDICION, SI NO OTRA DEVOLUCION PARA ITERACION EN OBJETO ITERABLE

print(lista)
print(yoquese)
print(yaves)


pies= [10,20,34,56,27]
metros= [round(n*3.281, 2) for n in pies]

print(metros)



#MATCH -> CASE   puede sustituir varios if,elifs, else tipo SWITCH 
#PYTHON 3.10

serie= 'NH-2'

match serie: 
    case 'NH-1':
        print('Samsung')
    case 'NH-2':
        print('Nokia')
    case 'NH3': 
        print('Motorola')
    case _:
        print('No existe este producto')


cliente={'nombre': 'Federico',
        'edad': 45,
        'ocupacion': 'instructor'}

pelicula={'titulo':'matrix',
        'ficha tecnica': {'protagonista': 'Keanu Reeves',
                        'director':'Lana y Lilly Wachowski'}}

elementos= [cliente, pelicula, 'libro']

