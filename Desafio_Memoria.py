import random

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
