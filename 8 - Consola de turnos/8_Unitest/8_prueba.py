
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hoola')
        funcion(palabra)
        print('Adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

@decorar_saludo #se va a usar siempre que se llame a titulo 
def titulo(texto):
    print(texto.title())


mayuscula_decorada= decorar_saludo(mayusculas)




n=0
def generador1():
    global n
    while True:
        n+=1
        yield n

generador= generador1()
next(generador)




vida= 4
def juego():
    global vida
    while True: 
        vida -=1 
        if vida> 1:
            yield f'Te quedan {vida} vidas.' 
        elif vida==1:
            yield f'Te queda {vida} vida.'
        elif vida==0:
            yield f'Game Over'
    
perder_vida= juego()


for i in range(4):
    print(next(perder_vida))

"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"