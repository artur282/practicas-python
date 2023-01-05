import bs4
import requests

# url sin numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 o 5 estrellas

titulos_rating_alto = []

# iterar paginas

for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionar datos de libros

    libros = sopa.select(".product_pod")

    # iterar en los libros

    for libro in libros:
        # chequear rating
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # guardar titulo
            titulo_libro = libro.select("a")[1]["title"]
            titulos_rating_alto.append(titulo_libro)

# ver libro de rating alto
for t in titulos_rating_alto:
    print(t)
