import bs4
import requests

#url sin numero de pagina
url_base=  'http://books.toscrape.com/catalogue/page-{}.html'


#lista de titulos con 4 o 5 estrellas
titulos_rating_alto= []

#iterar paginas
for pagina in range(1,51):
    
    #crear sopa de cada pagina
    url_pagina= url_base.format(pagina)
    resultado= requests.get(url_pagina)
    sopa= bs4.BeautifulSoup(resultado.text, 'lxml')


    #seleccionar datos de los libros
    libros= sopa.select('.product_pod')

    #iterar libros
    for libro in libros:

        #elegir de 4 y 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #guardar titulo en variable
            titulo= libro.select('a')[1]['title']

            #anadir titulo a la lista
            titulos_rating_alto.append(titulo)

#ver los libros en consola

for t in titulos_rating_alto:
    print(t)


'''
resultado= requests.get(url_base.format('1'))
sopa= bs4.BeautifulSoup(resultado.text, 'lxml')

libros= sopa.select('.product_pod')

estrellas= libros[0].select('.star-rating.Five')

titulo= libros[0].select('a')[1]['title']
print(titulo)'''