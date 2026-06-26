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

def mostrar_tablero(tablero, estado):

    cantidad_filas = len(tablero)
    cantidad_columnas = len(tablero[0])
    print()
    print("   ", end="")
    for j in range(cantidad_columnas):
        texto = completar_espacios(str(j + 1), ANCHO)
        print(texto, end="")
    print()
    for i in range(cantidad_filas):
        print(str(i + 1) + " | ", end="")
        for j in range(cantidad_columnas):
            if estado[i][j] == 0:
                texto = "[ ? ]"
            else:
                texto = tablero[i][j][0]
            texto = completar_espacios(texto, ANCHO)
            print(texto, end="")
        print()

def seleccionar_categoria():

    opcion = 0
    while opcion < 1 or opcion > 3:
        print("\nSeleccione una categoría:")
        print("1 - Geografía")
        print("2 - Matemática")
        print("3 - Inglés")
        opcion = int(input("\nIngrese una opción: "))
        if opcion < 1 or opcion > 3:
            print("\nOpción inválida.")
    if opcion == 1:
        nombre_archivo = "geografia.txt"
    elif opcion == 2:
        nombre_archivo = "matematica.txt"
    else:
        nombre_archivo = "ingles.txt"
    return nombre_archivo

def seleccionar_dificultad():

    opcion = 0
    while opcion < 1 or opcion > 3:
        print("\nSeleccione la dificultad:")
        print("1 - Fácil (2 x 2)")
        print("2 - Medio (4 x 4)")
        print("3 - Difícil (4 x 5)")
        opcion = int(input("\nIngrese una opción: "))
        if opcion < 1 or opcion > 3:
            print("\nOpción inválida.")
    if opcion == 1:
        filas = 2
        columnas = 2
        cantidad_parejas = 2
    elif opcion == 2:
        filas = 4
        columnas = 4
        cantidad_parejas = 8
    else:
        filas = 4
        columnas = 5
        cantidad_parejas = 10

    return filas, columnas, cantidad_parejas

