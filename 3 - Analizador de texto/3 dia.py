#1. METODO INDEX()

from re import M
from sre_parse import ESCAPES


texto= "Esto es una prueba"

resultado= texto.index('prueba')
res2= texto.index('s', 3, 8) # donde empezar y terminar de buscar


palabra= 'ordenador'

variable= palabra.index('n')



frase= 'En teoria, la teoria y la practica son los mismos. En la practica, no lo son.'

res3= frase.index('practica')

#print(res3)

#print(frase.index('practica', res3 +1))




# 2. SLICING   -    Extraer fragmentos de arrays.

oracion= 'Dicen que Tupac es el mejor'

x= int(6)   # Donde empieza 
y= int(12)  # Donde acaba (sin incluir)
z= int(2)   # Saltos entre posiciones

esto= oracion[x: y: z]
solo_saltos= oracion [::3]
orden_inverso= oracion[::-1]

#print(esto)
#print(solo_saltos)
#print(orden_inverso)
#print(oracion[8::3])





# METODO UPPER() -> Poner en mayuscula

print(texto[::-1].upper())


# METODO LOWER() -> Poner en minusculas

texto.lower()


#METODO SPLIT() ->  Separar un array, por defecto en cada espacio

print(texto.split('t'))


#METODO JOIN()  -> Unir elementos de una lista en una sola

a= 'Hola'
b= 'me'
c= 'llamo'
d= 'yogur'

union= ' '.join([a,b,c,d])

print(union)

#METODO FIND() -> Como index pero en vex de error da -1

print(oracion.find('T') )




#METODO REPLACE()

texto2= 'Me cago en tu puta madre'

esta_mierda= texto2.replace('puta madre', 'puto padre')

print(esta_mierda)





#LISTAS

mi_lista= ['a', 'b', 'c']

mi2_lista= [ 'd', 'e', 'f']

print(mi_lista[1:])

mi3_lista= mi_lista + mi2_lista

mi3_lista[0]= 'alfa'

mi3_lista.append('g')

eliminado= mi3_lista.pop(0)    #LE INDICAMOS EL INDICE DE LA LISTA QUE QUEREMOS ELIMiNAR

print(mi3_lista)
print(eliminado)


lista= ['s', 'e', 'r', 'h', 'i', 'y']

lista.sort()    #Ordena y lo deja en la misma lista, numeros o caracteres alfabeticamente

print(lista)

lista.reverse()     #Lo transforma en el lugar

print(lista)





#DICCIONARIOS   No tienen indice, solo clave

diccionario= {'c1':'valor1', 'c2': 'valor2'}

resultado= diccionario['c1']
print(resultado)

cliente= {'nombre':'Juan', 'apellido': 'Fuentes', 'peso': 88,'altura': 1.88 }

consulta= cliente['apellido']

print('Apellido: ', consulta)


dic= {'c1': 55, 'c2': [10,20, 'lechuga'], 'c3': {'s1': 100, 's2': 200} }

print(dic['c2'][0])
print(dic['c3']['s2'])

dic2= {'c1': ['a', 'b', 'c'], 'c2': [ 'd', 'e', 'f']}

print(dic2['c2'][1].upper())

dic2[3]= 'ojo'  #añadir una clave y un valor que no existen al diccionario

print(dic2)

print(dic.keys())
print(dic.values())
print(dic.items())





#TUPLAS -> inmutables(a prueba de daño) y ocupan menos espacio 

mi_tuple= (1,2,(8,4),4)
mi2_tupla= 1,3,2,1

mi2_tupla=list(mi2_tupla)

t= (1,2,3)

x,y,z= t

print(x,y,z)

print(mi2_tupla.count(1))
print(mi_tuple.index(2))




#SETS   No tienen indice y son inmutables, NO ADMITEN LISTAS NI DICCIONARIOS

mi_set= set([1,2,3,4])     #Hay que meterlos en un tipo de dato para que lo cuente como un elemento/argumento


otro_set= {1,3,5,7}     #Lo coge como un set directamente

eset= set((1,2,3,4,1,1,))

s1= {1,2,3}
s2= {3,4,5}
s3= s1.union(s2)    #union de sets

s1.add(4)   #añadir elementos

s1.remove(3)    #eliminar, si no tiene da error

s1.discard(8)      #eliminar sin error 

s1.pop()        #eliminar un elemento aleatorio (creo que el primero en realidad)

s1.clear()    #borrar todos

print(s1)



#BOOLEANOS in, not in, ==, !=, 

numero= bool(9<3)
print(numero )

ya=  ['YouTube', 'Facebook', 'Twitter', 'Whatsapp']
si= [3,6,2,6]
ya.sort()
print(ya)


 





