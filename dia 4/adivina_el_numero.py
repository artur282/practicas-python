from random import *

usuario = input("como te llamas:\n ")
intentos = 8
i = 0
numero = randint(0, 101)


while intentos > 0:
    n_ingresado = int(input(f"{usuario} adivina un numero entre 1 y 100:\n"))
    i = i + 1
    if n_ingresado < 1:
        print("el numero es menor al permitido\n")
    elif n_ingresado > 100:
        print("el numero es superior a lo permitido\n")
    elif n_ingresado < numero:
        print("el numero es menor al mio\n")
    elif n_ingresado > numero:
        print("el numero es mayor al mio\n")
    elif n_ingresado == numero:
        print(
            f"{usuario} felicidades acertaste el numero te tomo {i} intentos adivinar el numero")
        break

    intentos = intentos-1
else:
    print(f"te quedaste sin intentos el numero era:{numero}")
