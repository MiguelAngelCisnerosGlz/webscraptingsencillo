import bs4
import requests

#Crear una url sin numero de pagina{}
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#lista vacia para agregar los titulos encontrados 4 o 5 estrellas
titulos_rating_alto = []


#iterar las paginas
for pagina in range (1,51):

    #cada iteracion creara una sopa
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    #Seleccionamos datos de cada libro
    libros = sopa.select('.product_pod')

    #iteramos en los libros
    for libro in libros:

        #vemos que tengas minimo 4 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #Guardar el titulo en una variable
            titulo_libro = libro.select('a')[1]['title']

            #agregamos el libro ala lista

            titulos_rating_alto.append(titulo_libro)

#Codigo que nos permite ver los libros ya filtrados
for t in titulos_rating_alto:
    print(t)