'''
Ingresar texto
3 letras a ingresar
1.Cuantas veces aparecen las letras
2.cuantas palabras en total
3.primera y ultima letra
4 invertir el orden del texto
5. aparece 'python' en el texto? 
'''


texto= 'Este es el texto de prueba, que tengo. Punto final. python'                  #input('Ingresa el texto a analizar')

print(texto+'\n')

texto_low= texto.lower()

a= input('Ingresa una letra:').lower()
b= input('Ingresa otra letra:').lower()
c= input('Ingresa otra letra:').lower()


#1. apariciones en el texto
a1= texto_low.count(a)
a2= texto_low.count(b)
a3= texto_low.count(c)

print(f'\nLa letra {a} aparece {a1} veces en el texto.')
print(f'La letra {b} aparece {a2} veces en el texto.')
print(f'La letra {c} aparece {a3} veces en el texto.\n')



texto2= texto.replace('.', '')
texto3= texto2.replace(',', '')


#2. palabras en total

lista= texto3.split()
print(f'La longitud del texto es de: {len(lista)} palabras\n')

#3. primer y ultima letra

primera_letra= texto3[0]
ultima_letra= texto3[len(texto3)-1]

print(f'La primera letra es: {primera_letra}')
print(f'La ultima letra es: {ultima_letra}\n')


#4 invertir el orden del texto

lista.reverse()
invertido= ' '.join(lista)
print(f'El texto invertido es: \n{invertido}\n')

#5. Aparece 'Python' en el texto?

python= texto_low.find('python')

boleano= python == -1
diccionario= {True: 'No aparece \'Python\' en el texto', False: 'Sí aparece \'Python\' en el texto'}

print(diccionario[boleano])











