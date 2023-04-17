
#2 tipos de atributos ->atributos de clase (valor predefinido)
#                      ->de instancia(valor pasado)

class Animal:

    def __init__(self, edad, color) -> None:
        self.edad=edad
        self.color= color
        
    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal ha hablado')


class Pajaro(Animal):#clase de la que hereda como atributo

    alas= True

    def __init__(self, edad, color, especie) -> None:
        super().__init__(edad, color) #heredar atributos con SUPER
        self.especie= especie

    #método de instancia
    #decoradores:   -de clase @classmethod
    #               -estaticos @staticmethod

    def piar(self):  #METODO DE INSTANCIA -> acceden a atributos de clase e instancia
        print('pio pio')
    
    def volar(self, metros):
        print(f'El {self.especie} ha volado {metros} metros.')
        self.piar()

    def pintar_negro(self):
        self.color= 'negro'
        print(f'Ahora el pájaro es {self.color}')

    @classmethod        #acceden a atributos de clase
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos.')
        cls.alas= False

    @staticmethod   #no acceden ni clase ni instancia
    def mirar():
        print('El pajaro mira')


class Lobo(Animal):
    def hablar(self):
        print('Aúlla')

    def morder(self, mordiscos):
        print(f'El lobo hizo {mordiscos} mordiscos.')

mi_animal= Pajaro(13, 'amarillo', 'tucan')


class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('jajaja')
    def hablar(self):
        print('Que tal?')

class Hijo(Padre, Madre): #si tienen un metodo con el mismo nombre, se ejecuta el primero en ser heredado
    pass

class Nieto(Hijo):
    pass

nieto= Nieto()




class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass




class Vaca:
    def __init__(self, nombre) -> None:
        self.nombre= nombre
    def hablar(self):
        print(self.nombre, 'dice muuu')

class Oveja:
    def __init__(self, nombre) -> None:
        self.nombre= nombre
    def hablar(self):
        print(self.nombre, 'dice beee')

vaca= Vaca('Aurora')
oveja= Oveja('Nube')

animales= [vaca, oveja]


def animal_hablar(animal):  #se pueden llamar metodos con el mismo nombre que hagas cosas distintas dependiendo del oobjeto al que se refiera
    animal.hablar()

animal_hablar(oveja)