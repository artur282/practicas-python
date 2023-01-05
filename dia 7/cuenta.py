class persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class cliente(persona):

    def __init__(self, nombre, apellido, numero_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = 0

    def imprimir_cliente(self):
        print(
            f"bienvenido {self.nombre} {self.apellido} #{self.numero_cuenta} tu balance es:{self.balance}")

    def depositar(self):
        a = int(input("ingrese la cantidad a depositar: "))
        self.balance += a

    def retirar(self):
        a = int(input("ingrese cantidad a retirar:"))
        if a <= self.balance:
            self.balance -= a
            print("el monto se a retirado correctamente ")
        else:
            print("fondos insuficientes")


def crear_cliente():
    nombre = input("dime tu nombre: ")
    apellido = input("dime tu apellido: ")
    numero_cuenta = int(input("ingresa un numero de cuenta: "))
    return cliente(nombre, apellido, numero_cuenta)


def inicio():
    cliente = crear_cliente()
    menu = True
    while menu:
        print("\n")
        cliente.imprimir_cliente()
        print("\n")
        r = int(
            input(f"¿que deseas hacer? [1]depositar [2]retirar [3]salir: \n"))
        if r == 1:
            cliente.depositar()
        elif r == 2:
            cliente.retirar()
        elif r == 3:
            menu = False


inicio()
