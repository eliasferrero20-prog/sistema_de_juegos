import random

print("\n========================================")
print("     ¡BIENVENIDO AL JUEGO DE ADIVINAR!  ")
print("========================================")

usuario = input("INGRESE NOMBRE DE USUARIO: ")

juego_activo = True

while juego_activo == True:
    print("\nSELECCIONA LA DIFICULTAD:\n1. FACIL (7 intentos)\n2. INTERMEDIO (5 intentos)\n3. DIFICIL (3 intentos)")
    dificultad = input("Elegí una opción (1, 2 o 3): ")

    if dificultad == "1":
        intentos_totales = 7
        max_numero = 100
        print("\n¡Accediste al modo facil! Tenes", intentos_totales, "intentos para adivinar el numero del 0 al", max_numero)

    elif dificultad == "2":
        intentos_totales = 5
        max_numero = 100
        print("\n¡Accediste al modo intermedio! Tenes", intentos_totales, "intentos para adivinar el numero del 0 al", max_numero)

    elif dificultad == "3":
        intentos_totales = 3
        max_numero = 100
        print("\n¡Accediste al modo dificil! Tenes", intentos_totales, "intentos para adivinar el numero del 0 al", max_numero)

    else:
        print("\nIngresaste una opcion incorrecta. El sistema por defecto selecciono el nivel INTERMEDIO")
        intentos_totales = 5
        max_numero = 100