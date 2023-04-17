
def suma():
    a= input('Sumando 1: ')
    b= input('Sumando 2: ')
    print(a+b)

#forma habitual de hacerlo
try:
    suma()
except ValueError:
    print('Eso no es un numero.')
else:
    print('Hiciste todo bien')
finally:
    print('Eso fue todo')







def pedir_numero():

    while True:
        try: 
            numero= int(input('Ingresa un numero: '))
        except ValueError:
            print('Eso no es un numero.')
        else:
            print(f'Numero: {numero}\t Esto se ejecuta si va bien el try.')
            break
        finally:
            print('Esto se ejecuta siempre')

