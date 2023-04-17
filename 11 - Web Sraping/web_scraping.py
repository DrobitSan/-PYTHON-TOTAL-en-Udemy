import bs4
import requests


'''
resultado= requests.get('https://escueladirecta-blog.blogspot.com/')

sopa= bs4.BeautifulSoup(resultado.text, 'lxml' )

columna_lateral= sopa.select('.slide')
'''


resultado= requests.get('https://www.escueladirecta.com/courses')
sopa= bs4.BeautifulSoup(resultado.text, 'lxml' )
imagenes= sopa.select('.course-box-image')[0]['src']
print(imagenes)

im_curso1= requests.get(imagenes)

f= open('mi_imagen.jpg', 'wb')
f.write(im_curso1.content)
f.close()