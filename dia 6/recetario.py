"""
-saludar al usuario
-dar ruta donde esta
-informar cuantas recetas hay en el directorio
-crear opciones

1)leer receta:
-elegir categoria
-mostrar recetas
-elegir receta
-leer recta
2)crear receta
-elegir categoria
-crear nombre
-crear contenio
3)leer categoria
-nombre de la categoria a crear
-crear categoria
4)eliminar receta
-elegir categoria
-mostrar recetas
-elegir receta
-eliminar receta
5)eliminar categoria
-nombre de categoria
-eliminar categoria
6)finalizar programa
break
"""
from os import system
from pathlib import Path
import os


ruta = Path(Path.home(), "proyectos", "python",
            "curso python", "dia 6", "Recetas")
finalizar_programa = False


def contador_recetas(d):
    c = 0
    for txt in Path(d).glob("**/*.txt"):
        c += 1
    return c


def inicio():
    system("cls")
    print("*"*50)
    print("           bienvenido al recetario")
    print("*"*50)
    print("\n")
    print(f"las recetas se en cuentran en: {ruta}")
    print(f"el total de recetas es: {contador_recetas(ruta)}\n")

    elecion = "x"

    while not elecion.isnumeric() or int(elecion) not in range(1, 7):
        print("Elige un opcion: \n")
        print("""
        [1] - leer receta
        [2] - crear receta nueva
        [3] - crear categoria nueva
        [4] - eliminar receta
        [5] - eliminar categoria
        [6] - salir del programa
            """)
        elecion = input()
        return int(elecion)


def categoria(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria: ")

    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - [{receta_str}]")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegir_receta(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input("\nelige una receta:")

    return lista[int(eleccion_receta)-1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False
    while not existe:
        print("escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"tu receta {nombre_receta} a sido creada")
            existe = True
        else:
            print("lo siento esa receta ya existe")


def crear_categoria(ruta):
    existe = False
    while not existe:
        print("escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"tu receta {nombre_categoria} a sido creada")
            existe = True
        else:
            print("lo siento esa categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"la receta{receta.name} a sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"la categoria{categoria.name} a sido eliminada")


def volver_inicio():
    eleccion_regresar = "x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\npresione v para voler al menu:")

    pass


while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(ruta)
        mi_receta = elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    if menu == 2:
        mis_categorias = categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    if menu == 3:
        crear_categoria(ruta)
        volver_inicio()

    if menu == 4:
        mis_categorias = categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(ruta)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    if menu == 5:
        mis_categorias = categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    if menu == 6:
        finalizar_programa = True
