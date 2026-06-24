import random
aleatorio=["piedra", "papel", "tijera" ]
aleatorio2=random.choice(aleatorio)
eleccion1=input("(Piedra, Papel o Tijera)")
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
elif eleccion1 == "tijera" and aleatorio2 == "tijera":
    print("Empate")
elif eleccion1 == "piedra" and aleatorio2 == "piedra":
    print("Empate")
elif eleccion1 == "papel" and aleatorio2 == "papel":
    print("Empate")
else :
    print("Dato ingresado no valido")