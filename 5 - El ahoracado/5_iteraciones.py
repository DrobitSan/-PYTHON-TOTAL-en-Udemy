import random  
'''
def lanzar_dados():
    a= randint(1,6)
    b= randint(1,6)
    return a, b
    
a,b= lanzar_dados()

def evaluar_jugada(a,b):
    suma_dados= a+b
    if suma_dados <=6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados >6 and suma_dados<10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

evaluar_jugada(a,b)





def reducir_lista(lista):
    lista.sort()
    new_lista= set(lista)
    new2_lista= list(new_lista)
    new2_lista.pop()
    return new2_lista


lista_numeros= [1,2,5,9,5,1,7,3]
lista_reducida= reducir_lista(lista_numeros)
print(lista_reducida)

def promedio(lista1):
    lista=list(lista1)
    suma=0
    divisor=0
    for e in lista:
        suma+=e
        divisor+=1
    promedio= suma/divisor
    return promedio 


promedio1= promedio(lista_reducida)
print(promedio1)


'''


def lanzar_moneda():
    moneda=['Cara', 'Cruz']
    resultado= random.choice(moneda)
    return resultado


def probar_suerte(res= lanzar_moneda(),lista_numeros=[5,2,6,3] ):
    if res== 'Cara':
        print('La lista se autodestruirá')   
        lista_numeros.clear()
        return lista_numeros
    elif res== 'Cruz':
        print('La lista fue salvada')
        return lista_numeros


print(probar_suerte())



# *ARGs

def suma_cuadrados(*args):
    total=0
    for arg in args:
        total += arg**2 
    return total




def numeros_persona(nombre, *args):
    suma_numeros=0
    for arg in args:
        suma_numeros+=arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"





#  **KARGs




def describir_persona(nombre, **caracteristicas):
    print(f'Características de {nombre}:')
    for key, value in caracteristicas.items():
        print(f'{key}:{value}')


describir_persona("Cintia", color_ojos="azules", color_pelo="rubio")
