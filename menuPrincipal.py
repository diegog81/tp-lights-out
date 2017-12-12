#import juegoPredeterminado

def menuBienvenida():
    print()
    print("Bienvenido al juego TP-Lights-Out")
    print()
    print("Ingrese una opcion")
    print("1 - jugar en modo PREDETERMINADO")
    print("2 - salir")


def menuPrincipal():

    opcion = 0
    while opcion != 3:

        menuBienvenida()
        opcion = input("Ingrese opción: ")
        if opcion == 1:
            juegoPredeterminado()

        elif opcion == "2":
            break
        else:
            print("no ingreso ninguna opción")
menuPrincipal()

