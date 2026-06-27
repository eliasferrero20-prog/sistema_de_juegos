import random


def pedir_numero_valido(numero_intento, total_intentos):
    es_numero_valido = False
    while es_numero_valido == False:
        try:
            valor_ingresado = int(input(f"\nIntento {numero_intento}/{total_intentos}. Ingresá un numero: "))
            es_numero_valido = True
        except ValueError:
            print("¡Error! Ingresa un numero entero.")
    return valor_ingresado


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

    numero_secreto = random.randint(0, max_numero)
    intentos_actuales = 0
    adivino = False

    while intentos_actuales < intentos_totales and adivino == False:
        intento_usuario = pedir_numero_valido(intentos_actuales + 1, intentos_totales)

        intentos_actuales += 1
        if intento_usuario == numero_secreto:
            print("¡FELICITACIONES", usuario+"!, ¡Adivinaste el numero secreto!")
            adivino = True
        elif intento_usuario < numero_secreto:
            print("El numero secreto es MAYOR.")
        else:
            print("El numero secreto es MENOR.")

    if adivino == False:
        print("\n¡Te quedaste sin intentos", usuario+"! Perdiste.")
        print("El numero secreto era: ", numero_secreto)
    print()

    print("1. Jugar otra partida")
    print("2. Finalizar juego")

    opcion = input("Elegí una opción (1 o 2): ")
    if opcion == "1":
        print("\nNUEVA RONDA PARA:",usuario)
    elif opcion == "2":
        print("\n¡Gracias por jugar",usuario+"!")
        juego_activo = False
    else:
        print("\nOpción incorrecta. El programa finalizara.")
        juego_activo = False