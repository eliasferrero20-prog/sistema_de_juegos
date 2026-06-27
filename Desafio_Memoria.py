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

def pedir_posicion(filas, columnas, estado):

    posicion_valida = False
    while posicion_valida == False:
        print("\nIngrese 0 en la fila para abandonar la partida.")
        try:
            fila = int(input("Ingrese la fila: "))
            if fila == 0:
                return -1, -1
            columna = int(input("Ingrese la columna: "))
            if fila < 1 or fila > filas:
                print("Fila fuera de rango.")
            elif columna < 1 or columna > columnas:
                print("Columna fuera de rango.")
            elif estado[fila - 1][columna - 1] != 0:
                print("La carta seleccionada no está disponible.")
            else:
                posicion_valida = True
        except ValueError:
            print("\nDebe ingresar un número entero.")
    return fila - 1, columna - 1

def mostrar_tablero(tablero, estado):

    cantidad_filas = 4
    cantidad_columnas = 4
    ancho_columna = 16
    print()
    print("     ", end="")
    for j in range(cantidad_columnas):
        num_str = str(j + 1)
        espacios_faltantes = ancho_columna - len(num_str)
        print(num_str + (" " * espacios_faltantes), end="")
    print()
    for i in range(cantidad_filas):
        print(" " + str(i + 1) + " | ", end="")
        for j in range(cantidad_columnas):
            if estado[i][j] == 0:
                texto_celda = "[ ? ]"
            else:
                texto_celda = str(tablero[i][j][0])
            espacios_faltantes = ancho_columna - len(texto_celda)
            print(texto_celda + (" " * espacios_faltantes), end="")
        print()

def seleccionar_categoria():

    opcion = 0
    while opcion < 1 or opcion > 2:
        print("\nSeleccione una categoría:")
        print("1 - Geografía")
        print("2 - Inglés")
        opcion = int(input("\nIngrese una opción: "))
        if opcion < 1 or opcion > 2:
            print("\nOpción inválida.")
    if opcion == 1:
        nombre_archivo = "geografia.txt"
        categoria = "Geografía"
    else:
        nombre_archivo = "ingles.txt"
        categoria = "Inglés"
    return nombre_archivo, categoria

def nueva_partida():

    print("\n=== NUEVA PARTIDA ===")
    nombre_archivo, categoria = seleccionar_categoria()
    filas = 4
    columnas = 4
    cantidad_parejas = 8
    parejas = leer_parejas(nombre_archivo)
    parejas = seleccionar_parejas(parejas, cantidad_parejas)
    cartas = generar_cartas(parejas)
    tablero = crear_tablero(cartas, filas, columnas)
    estado = crear_estado(filas, columnas)
    intentos = 0
    aciertos = 0
    partida_cancelada = False
    while aciertos < cantidad_parejas and partida_cancelada == False:
        print("\nIntentos:", intentos)
        print("Parejas encontradas:", aciertos, "de", cantidad_parejas)
        mostrar_tablero(tablero, estado)
        fila1, columna1 = pedir_posicion(filas, columnas, estado)
        if fila1 == -1:
            partida_cancelada = True
        else:
            estado[fila1][columna1] = 1
            mostrar_tablero(tablero, estado)
            fila2, columna2 = pedir_posicion(filas, columnas, estado)
            if fila2 == -1:
                estado[fila1][columna1] = 0
                partida_cancelada = True
            else:
                estado[fila2][columna2] = 1
                mostrar_tablero(tablero, estado)
                carta1 = tablero[fila1][columna1]
                carta2 = tablero[fila2][columna2]
                if carta1[1] == carta2[1]:
                    estado[fila1][columna1] = 2
                    estado[fila2][columna2] = 2
                    aciertos += 1
                    print("\n¡Encontraste una pareja!")
                    input("\nPresione ENTER para continuar...")
                else:
                    print("\nNo forman una pareja.")
                    input("\nPresione ENTER para continuar...")
                    estado[fila1][columna1] = 0
                    estado[fila2][columna2] = 0
                intentos += 1
    if partida_cancelada == True:
        print("\nPartida cancelada.")
        input("\nPresione ENTER para volver al menú principal...")
    else:
        print("\n===================================")
        print("      PARTIDA FINALIZADA")
        print("===================================")
        print("\n¡Felicitaciones!")
        print("Completaste el Desafío de Memoria.")
        print("\nCategoría:", categoria)
        print("Intentos realizados:", intentos)
        print("Parejas encontradas:", aciertos, "de", cantidad_parejas)
        guardar_historial(categoria, intentos, aciertos)
        input("\nPresione ENTER para volver al menú principal...")

def guardar_historial(categoria, intentos, aciertos):

    with open("historial_memoria.txt", "a") as archivo:
        archivo.write(categoria + ";")
        archivo.write(str(intentos) + ";")
        archivo.write(str(aciertos) + "\n")

def mostrar_historial():

    print("\n========== HISTORIAL ==========\n")
    with open("historial_memoria.txt", "r") as archivo:
        registros = archivo.readlines()
        if len(registros) == 0:
            print("Todavía no hay partidas registradas.")
        else:
            for linea in registros:
                datos = linea.strip().split(";")
                print("Categoría:", datos[0])
                print("Intentos:", datos[1])
                print("Parejas:", datos[2])
                print()
    input("Presione ENTER para continuar...")

def menu_principal():

    opcion = 0
    while opcion != 3:
        print("\n==============================")
        print("     DESAFÍO DE MEMORIA")
        print("==============================")
        print("1 - Nueva partida")
        print("2 - Ver historial")
        print("3 - Salir")
        opcion = int(input("\nIngrese una opción: "))
        if opcion == 1:
            nueva_partida()
        elif opcion == 2:
            mostrar_historial()
        elif opcion == 3:
            print("\n¡Gracias por jugar!")
        else:
            print("\nOpción inválida.")

menu_principal()