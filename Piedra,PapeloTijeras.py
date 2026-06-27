def piedrapapeltijeras():
    import random
    aleatorio=["piedra", "papel", "tijera" ]
    opcion="2"
    while opcion == "2":
        try:
            aleatorio2=random.choice(aleatorio)
            eleccion1=input("\n(Piedra, Papel o Tijera) ")
            eleccion1=eleccion1.lower()
            print("\n(Piedra, Papel o Tijera)", aleatorio2)
            if eleccion1 == "piedra" and aleatorio2 == "papel":
                print("\nGanador: Papel")
            elif eleccion1 == "tijera" and aleatorio2 == "papel":
                print("\nGanador: Tijera")
            elif eleccion1 == "piedra" and aleatorio2 == "tijera":
                print("\nGanador: Piedra")
            elif eleccion1 == "papel" and aleatorio2 == "piedra":
                print("\nGanador: Papel")
            elif eleccion1 == "papel" and aleatorio2 == "tijera":
                print("\nGanador: Tijera")
            elif eleccion1 == "tijera" and aleatorio2 == "piedra":
                    print("\nGanador: Piedra")
            elif eleccion1 == aleatorio2:
                print("\nEmpate")
            else :
                print("\nDato ingresado no valido")
            print("\n2 = Seguir", "\n0 = Salir del juego")
            opcion = input("\nIngresa una opcion del menu: ")
        except ValueError:
            print("\nDato ingresado no valido")