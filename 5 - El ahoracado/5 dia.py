#METODOS insert, lstrip; isdisjoint>


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, 'naranja')

print(frutas)



basura= ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

hola= basura.lstrip(',:%_#')

print(hola)




marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados= marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)





def bienvenida(nombre):
    print(f'Bienvenido {nombre}')

bienvenida('Lucas')




def invertir_palabra(palabra):
    return palabra[::-1].lower()
    

print(invertir_palabra('Curso'))


#FUNCIONES DINAMICAS


def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass 
    return False


resultado= chequear_3_cifras([543,987,94,3,1000,567])
print(resultado)



def suma_menores(lista_numeros):
    lista_suma= []
    for n in lista_numeros:
        if n in range(0,1000):
            lista_suma.append(n)
        else: 
            pass
    
    for i in lista_suma:
        suma +=i
    return suma



    