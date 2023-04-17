

'''
variable= open('prueba1.txt', 'r')

lineas= variable.read()

print(lineas)
variable.close()

variable= open('prueba1.txt', 'a')

variable.writelines(['hola\t', '1', 'linea', 'añadida'])

variable.close()


PARA QUE SE CIERRE SIEMPRE

with open('dataset.txt', 'w') as f:
    f.write('new data')



'''

#os
import os
from os import system



system('cls')




ruta= os.getcwd()
print(ruta)
#ruta1= os.chdir('ruta directoria al que cambiar')

#ruta2= os.makedirs('ruta de carpeta a crear')



# PATH

from pathlib import Path

base= Path.home()

guia= Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada_Familia.txt'))
guia2= guia.with_name('La pedrera.txt')

guia3= guia.parent.parent.parent

en_europa= guia.relative_to(Path(base, 'Europa'))


'''for txt in Path(guia3).glob('**/*.txt'):    # '*.txt' para los txt de su carpeta
    print(txt)
'''
















