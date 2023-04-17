#1
def devolber_distintos(a,b,c):
    lista=[a,b,c]
    lista.sort()
    if sum(lista)<10:
        return lista[0]
    elif 10<sum(lista)<15:
        return lista[1]
    elif sum(lista)>15:
        return lista[2]


#2
def set_palabra(string):
    palabra=list(string)
    palabra.sort()
    lista=[]
    for e in palabra:
        if e not in lista:
            lista.append(e)
    return lista

    



#3
def consecutive_ceros(*numbers):
    z = int
    for n in numbers:
        if n==z==0:
            return True
        z= n
    return False





#4
def contar_primos(max):
    num=0
    lista=[]
    for n in range(1,max+1):
        for i in range(1,n+1):
            if n%i==0:
                lista.append(i)
        if len(lista)==2:
            num+=1
        lista.clear()
    return num







