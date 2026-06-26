import random

ANCHO = 16

def leer_parejas(nombre_archivo):

    parejas = []
    with open(nombre_archivo, "r") as archivo:
        registros = archivo.readlines()
        for linea in registros:
            linea = linea.strip()
            dato1, dato2 = linea.split(";")
            parejas.append((dato1, dato2))
    return parejas

def generar_cartas(parejas):

    cartas = []
    id_pareja = 1
    for i in parejas:
        cartas.append((i[0], id_pareja))
        cartas.append((i[1], id_pareja))
        id_pareja += 1
    return cartas

def seleccionar_parejas(parejas, cantidad):

    parejas_seleccionadas = []

    while len(parejas_seleccionadas) < cantidad:

        posicion = random.randint(0, len(parejas) - 1)

        pareja = parejas[posicion]

        if pareja not in parejas_seleccionadas:

            parejas_seleccionadas.append(pareja)

    return parejas_seleccionadas

def crear_tablero(cartas, filas, columnas):

    cartas_mezcladas = []

    while len(cartas) > 0:

        posicion = random.randint(0, len(cartas) - 1)

        cartas_mezcladas.append(cartas[posicion])

        cartas.pop(posicion)

    tablero = []

    posicion = 0

    for i in range(filas):

        fila = []

        for j in range(columnas):

            fila.append(cartas_mezcladas[posicion])

            posicion += 1

        tablero.append(fila)

    return tablero

def crear_estado(filas, columnas):

    estado=[[0]*columnas for i in range(filas)]

    return estado

def verificar_pareja(carta1, carta2):

    resultado = 0

    if carta1[1] == carta2[1]:
        resultado = 1

    return resultado

def pedir_posicion(filas, columnas, estado):

    posicion_valida = False

    while posicion_valida == False:

        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))

        if fila < 1 or fila > filas:
            print("Fila fuera de rango.")

        elif columna < 1 or columna > columnas:
            print("Columna fuera de rango.")

        elif estado[fila - 1][columna - 1] != 0:
            print("La carta seleccionada no está disponible.")

        else:
            posicion_valida = True

    return fila - 1, columna - 1

def completar_espacios(texto, ANCHO):

    while len(texto) < ANCHO:
        texto += " "

    return texto

