#pedir ingresar texto, pedir ingresar 3 letras
#1)analizar cuantas veces aparece cada letra
#2)contar la cantidad de palabras en el texto
#3)cual es la primera y ultima letra del texto
#4)como que daria el texto si se invierte el orden de las palabras
#5)visualizar si la palabra"python" aparece en el texto

texto = input("ingrese texto: ")

letra1 = input("ingrese letra 1:")
letra2 = input("ingrese letra 2:")
letra3 =input("ingrese letra 3:")

lista = [letra1,letra2,letra3]

print(f"la primera letra aparece:{texto.count(lista[0])} la segunda letra aparece:{texto.count(lista[1])} la tercera letra parece:{texto.count(lista[2])}")

palabras = texto.split()

print(f"la cantidad de palabras en el texto es:{len(palabras)}")

print(f"la primera letra es:{texto[0]} y la ultima letra es:{texto[-1]}")

palabras.reverse()
invertido= " ".join(palabras)

print(f"el texto invertido es: {invertido}")














