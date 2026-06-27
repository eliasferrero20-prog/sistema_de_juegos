def piedrapapeltijeras():
    import random
    aleatorio=["piedra", "papel", "tijera" ]
    opcion=2
    aleatorio2=random.choice(aleatorio)
    while opcion == 2:
        try:
            eleccion1=input("(Piedra, Papel o Tijera)")
            eleccion1=eleccion1.lower()
            print(aleatorio2)
            if eleccion1 == "piedra" and aleatorio2 == "papel":
                print("Ganador: Papel")
            elif eleccion1 == "tijera" and aleatorio2 == "papel":
                print("Ganador: Tijera")
            elif eleccion1 == "piedra" and aleatorio2 == "tijera":
                print("Ganador: Piedra")
            elif eleccion1 == "papel" and aleatorio2 == "piedra":
                print("Ganador: Papel")
            elif eleccion1 == "papel" and aleatorio2 == "tijera":
                print("Ganador: Tijera")
            elif eleccion1 == "tijera" and aleatorio2 == "piedra":
                    print("Ganador: Piedra")
            elif eleccion1 == aleatorio2:
                print("Empate")
            else :
                print("Dato ingresado no valido")
            print("2 = Seguir", "\n0 = Salir del juego")
            opcion = input("Ingresa una opcion del menu: ")
        except ValueError:
            print("Dato ingresado no valido")