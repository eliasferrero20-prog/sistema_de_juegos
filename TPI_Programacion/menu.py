
def menu_principal():
    opcion = ""
    while opcion != "0":
        print("Menu de opciones de juegos")
        print("Selecciona el juego a jugar")
        print("Opcion 1 - Kiosco matematico")
        print("Opcion 2 - Piedra, Papel o Tijera ")
        print("Opcion 3 - ")
        print("Opcion 4 - ")
        print("Opcion 0 - Salir del sistema")

        opcion = input("Ingresa una opcion del menu: ")

        if opcion == "1":
            print("Opcion 1 elegida")
        elif opcion == "2":
            print("Opcion 2 elegida")
        elif opcion == "3":
            print("Opcion 3 elegida")
        elif opcion == "4":
            print("Opcion 4 elegida")
        elif opcion == "0":
            print("Saliendo del menu")
        else:
            print("Opcion no valida. Elija una opcion del menu")