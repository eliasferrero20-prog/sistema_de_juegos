import random

def seleccionar_palabra_ahorcado():

    palabras = ["casa", "perro", "gato", "mesa", "silla", "ventana", "puerta", "escuela", "amigo", "pelota"]
    return random.choice(palabras)

def mostrar_inicio_ahorcado(palabra):

    palabra_oculta = "-" * len(palabra)
    print(palabra_oculta)
    print("Pista (primera letra):", palabra[0])
    return palabra_oculta

def jugar_ahorcado():

    print("\n==============================")
    print("     AHORCADO")
    print("==============================")
    palabra_aleatoria = seleccionar_palabra_ahorcado()
    palabra_progreso = mostrar_inicio_ahorcado(palabra_aleatoria)
    intentos = 5
    finalizado = False
    while intentos > 0 and finalizado == False:
        letra = input("\nIngresa una letra: ").lower()
        palabra_secreta = ""
        intentos -= 1
        acierto = False
        for i in range(len(palabra_aleatoria)):
            if letra == palabra_aleatoria[i]:
                palabra_secreta += letra
                acierto = True
            else:
                palabra_secreta += palabra_progreso[i]
        if acierto == True:
            intentos += 1
        palabra_progreso = palabra_secreta
        print(palabra_progreso)
        print("Intentos restantes:", intentos)
        if palabra_aleatoria == palabra_progreso:
            finalizado = True
    if palabra_aleatoria == palabra_progreso:
        print("\n¡Ganaste!")
    else:

        print("\nPerdiste. La palabra era: " + palabra_aleatoria)

def menu_principal():
    opcion_principal = -1
    while opcion_principal != 0:
        print("\n==============================")
        print("     PLATAFORMA EDUCATIVA")
        print("==============================")
        print("1 - Ahorcado")
        print("2 - Piedra, Papel o Tijera")
        print("3 - Adivina el Número")
        print("4 - Kiosco Matemático")
        print("5 - Desafío de Memoria")
        print("0 - Salir del Sistema")
        valida = False
        while valida == False:
            try:
                opcion_principal = int(input("Ingresa una opcion del menu: "))
                valida = True
            except ValueError:
                print("Debe ingresar una opción válida.")

        if opcion_principal == 1:
            jugar_ahorcado()
        else:
            if opcion_principal != 0:
                print("\nPor favor ingrese una opción valida.")

    if opcion_principal == 0:
        print("\nMuchas gracias por utilizar el sistema.")
        print("PLATAFORMA EDUCATIVA")

menu_principal()