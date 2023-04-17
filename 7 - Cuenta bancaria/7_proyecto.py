from random import randint
from os import system

#BANCO

n_clientes= int(0)
dic_clientes={}

class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre= nombre
        self.apellido= apellido

class Cliente(Persona):
    balance= 0
    def __init__(self, nombre, apellido, __contra, numero_cuenta) -> None:
        super().__init__(nombre, apellido)
        self.__contra= __contra
        self.numero_cuenta= numero_cuenta
        
    def comprobar_contrasena(self, intento):
        if intento== self.__contra:
            return True
        else:
            return False
    
    
    def __str__(self) -> str:
        str= '{:<10} {:<10} {:<10}'.format(self.nombre, self.apellido, self.numero_cuenta)
        return str 

    def depositar(self):
        deposito= input('Introduzca el importe a depositar: ')
        self.balance+= int(deposito)
        print(f'El balance de su cuenta es: {self.balance} glipidops.')

    def retirar(self):
        retiro= int(input('Introduzca el importe a retirar: '))
        if self.balance >= retiro:
            self.balance-= retiro
            print(f'Aqui tiene sus {retiro} glipidops.')
        else: 
            print('No tiene suficiente liquidez.')

def inicio(): #devuelbe el numero de la cuenta
    registrado= int(input('Tiene ya una cuenta? \n0 - No \n1 - Si \nRespuesta: '))
    if registrado:
        n_cuenta= int(input('Introduzca el numero de su cuenta: '))
    else:
        n_cuenta= crear_cliente()
        global n_clientes
        n_clientes+= 1
    return n_cuenta
        
def crear_numero():
        numero= randint(111,999)
        return numero

def crear_cliente():
    global n_clientes
    nombre= input('Introduzca su nombre: ')
    apellido= input('Introduzca su apellido: ')
    contra= input('Introduzca una contrasena: ')
    numero= crear_numero()
    #cliente= 'cliente_%s= Cliente("%s", "%s") \ncliente_1= Cliente("Tu","Madre") \nlista_objetos[n_clientes]= cliente_%s' % (n_clientes, nombre, apellido, n_clientes)
    cliente= 'cliente_{n}= Cliente("{}","{}","{}","{}") \ndic_clientes[{n}]= cliente_{n}'.format(nombre, apellido, contra, numero, n= n_clientes)
    exec(cliente)
    print(dic_clientes[n_clientes].numero_cuenta)
    return dic_clientes[n_clientes].numero_cuenta
    
def buscar_cuenta(n_cuenta): #recive el numero de cuenta, tiene que retornar el objeto
    for objeto in dic_clientes.values():
        if int(objeto.numero_cuenta)== int(n_cuenta):
            password= input('Inserte la contrasena: ')
            intentos= 5
            while intentos > 0 and not objeto.comprobar_contrasena(password):
                intentos-= 1
                password= input(f'Le quedan {intentos} intentos. \nInserte la contrasena: ')
            if objeto.comprobar_contrasena(password):
                return objeto
            else:
                print('Contrasena incorrecta.')
                return None
    print('La cuenta no existe')
    return None


def print_menu(objeto):
    print('\n{:<10} {:<10} {:<10}'.format('Nombre', 'Apellido', 'N. de cuenta'))
    print(objeto)
    print(f'\nSaldo: {objeto.balance} glipidops.')
    
def eleccion_menu(): #devuelbe el numero de la eleccion
    eleccion= input('''\nOpciones:\n
     1 - Depositar G's.
     2 - Retirar G's.
     3 - Salir de la cuenta.
     4 - Salir del programa.\n''')
    return eleccion
    

#PROGRAMA
eleccion=int

numero_cuenta= inicio()
objeto= buscar_cuenta(numero_cuenta)
if objeto != None:
    while eleccion!= 4:
        print_menu(objeto)
        eleccion= int(eleccion_menu())
        if eleccion==1:
            objeto.depositar()
        elif eleccion==2:
            objeto.retirar()
        elif eleccion==3:
            numero_cuenta= inicio()
            objeto= buscar_cuenta(numero_cuenta)

print('Fin programa')






#cliente_0= Cliente("Serhiy", "Drobit")

