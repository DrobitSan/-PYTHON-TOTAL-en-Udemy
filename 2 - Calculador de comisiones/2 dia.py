minumero= 1+3.5
print(minumero + minumero)
print(type(minumero))

'''edad= int(input('Mete tu edad= '))
nueva_edad = edad +1
print('Tu edad el año que viene es ' + str(nueva_edad))
'''

#Formatear Cadenas

#1: Funcion fomrmat
nombre= 'Manolo'
edad= 34
print('Me llamo {} y tengo {} años.'.format(nombre, edad))


#2: Cadenas literales
print(f'Me llamo {nombre} y tengo {edad} años.')



print("El numero {} más {} es igual a: {}".format(minumero, edad, minumero+edad))  #suma en el parentesis

puntos_nuevos= 560
puntos_anteriores= 130
print(f'Has ganado {puntos_nuevos} puntos! En toal, acumulas {puntos_anteriores + puntos_nuevos} puntos.')