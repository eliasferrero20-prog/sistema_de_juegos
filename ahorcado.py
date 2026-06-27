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


jugar_ahorcado()