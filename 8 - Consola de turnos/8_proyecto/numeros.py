"""
Generadores y decorador
"""


def perfumeria():
     for n in range (1,100):
        yield  f'P - {n}'


def farmacia():
     for n in range (1,100):
        yield  f'F - {n}'


def cosmetica():
     for n in range (1,100):
        yield  f'C - {n}'



turno_perfumeria= perfumeria()
turno_farmacia= farmacia()
turno_cosmetica= cosmetica()



def decorador(funcion):
    def f_decorada():
        print('\n   Su turno es el: ')
        print('       '+ (next(funcion)))
        print('En breve sera atendido.\n\n')
    return f_decorada

farmacia_decorada= decorador(turno_farmacia)
perfumeria_decorada= decorador(turno_perfumeria)
cosmetica_decorada= decorador(turno_cosmetica)
