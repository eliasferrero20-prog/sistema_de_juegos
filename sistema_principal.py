import random

PRODUCTOS_KIOSCO = {
    1: {"nombre": "Alfajor", "precio": 2000},
    2: {"nombre": "Gaseosa", "precio": 2500},
    3: {"nombre": "Bolsa de caramelo", "precio": 3000},
    4: {"nombre": "Chicle en tira", "precio": 1000},
    5: {"nombre": "Galletitas", "precio": 1350},
    6: {"nombre": "Chupetin", "precio": 300},
    7: {"nombre": "Chocolate", "precio": 2250},
    8: {"nombre": "Papitas", "precio": 3600},
    9: {"nombre": "Jugo", "precio": 650},
    10: {"nombre": "Pebete", "precio": 2500}
}

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

def piedrapapeltijera():
    aleatorio=["piedra", "papel", "tijera" ]
    opcion="2"
    while opcion == "2":
        try:
            print("\n==============================")
            print("PIEDRA, PAPEL O TIJERA")
            print("==============================")
            aleatorio2=random.choice(aleatorio)
            eleccion1=input("\n(Piedra, Papel o Tijera) ")
            eleccion1=eleccion1.lower()
            print("\n(Piedra, Papel o Tijera)", aleatorio2)
            if eleccion1 == "tijeras":
                eleccion1 = "tijera"
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

def pedir_numero_valido(numero_intento, total_intentos):
    es_numero_valido = False
    while es_numero_valido == False:
        entrada = input(f"\nIntento {numero_intento}/{total_intentos}. Ingresá un numero.\nPara regresar al menu ingrese \"m\": ")
 
        if entrada.lower() == "m":
            return None

        try:
            valor_ingresado = int(entrada)
            es_numero_valido = True
        except ValueError:
            print("¡Error! Ingresa un numero entero.")
    return valor_ingresado

def adivina_numero():
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
            print("\n¡Accediste al modo facil! Tenes", intentos_totales, "intentos para adivinar el numero del 0 al",
                  max_numero)

        elif dificultad == "2":
            intentos_totales = 5
            max_numero = 100
            print("\n¡Accediste al modo intermedio! Tenes", intentos_totales,
                  "intentos para adivinar el numero del 0 al", max_numero)

        elif dificultad == "3":
            intentos_totales = 3
            max_numero = 100
            print("\n¡Accediste al modo dificil! Tenes", intentos_totales, "intentos para adivinar el numero del 0 al",
                  max_numero)

        else:
            print("\nIngresaste una opcion incorrecta. El sistema por defecto selecciono el nivel INTERMEDIO")
            intentos_totales = 5
            max_numero = 100

        numero_secreto = random.randint(0, max_numero)
        intentos_actuales = 0
        adivino = False
        volver_al_menu = False

        while intentos_actuales < intentos_totales and adivino == False and volver_al_menu == False:
            intento_usuario = pedir_numero_valido(intentos_actuales + 1, intentos_totales)

            if intento_usuario is None:
                volver_al_menu = True
            else:
                intentos_actuales += 1
                if intento_usuario == numero_secreto:
                    print("¡FELICITACIONES", usuario + "!, ¡Adivinaste el numero secreto!")
                    adivino = True
                elif intento_usuario < numero_secreto:
                    print("El numero secreto es MAYOR.")
                else:
                    print("El numero secreto es MENOR.")

        if volver_al_menu == True:
            print("\nVolviendo al menú principal...")
            return

        if adivino == False:
            print("\n¡Te quedaste sin intentos", usuario + "! Perdiste.")
            print("El numero secreto era: ", numero_secreto)
        print()

        print("1. Jugar otra partida")
        print("2. Finalizar juego")

        opcion = input("Elegí una opción (1 o 2): ")
        if opcion == "1":
            print("\nNUEVA RONDA PARA:", usuario)
        elif opcion == "2":
            print("\n¡Gracias por jugar", usuario + "!")
            juego_activo = False
        else:
            print("\nOpción incorrecta. El programa finalizara.")
            juego_activo = False


def mostrar_lista():
    print("---Lista de precios---")
    lista_precios = list(PRODUCTOS_KIOSCO.keys())

    for i in range(len(lista_precios)):
        numero_lista = lista_precios[i]
        nombre = PRODUCTOS_KIOSCO[numero_lista]["nombre"]
        precio = PRODUCTOS_KIOSCO[numero_lista]["precio"]
        print(numero_lista, nombre, precio)


def pedir_producto():
    mostrar_lista()
    numero_lista = 0
    while numero_lista not in PRODUCTOS_KIOSCO:
        entrada = input("Ingresa el numero de lista del producto que queres llevar: ")
        if entrada.isdigit():
            numero_lista = int(entrada)
            if numero_lista not in PRODUCTOS_KIOSCO:
                print("El numero de lista no existe, ingrese un numero valido")
        else:
            print("Por favor, ingresa solo numeros.")

    cant = 0
    while cant <= 0:
        entrada = input(f"¿Cuántos/as {PRODUCTOS_KIOSCO[numero_lista]['nombre']} vas a llevar?: ")
        if entrada.isdigit():
            cant = int(entrada)
            if cant <= 0:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Por favor ingrese numeros")
    return [numero_lista, cant]


def realizar_compra():
    carrito = []

    continuar = "si"
    while continuar == "si":
        producto_comprado = pedir_producto()
        carrito.append(producto_comprado)
        continuar = input("Quieres comprar otro producto? (si/no):").lower().strip()
        while continuar != "si" and continuar != "no":
            continuar = input("Responde solo, si o no").lower().strip()

    print("Voy a llevar...: ")
    total_compra = 0
    for i in range(len(carrito)):
        num_producto = carrito[i][0]
        cant_actual = carrito[i][1]
        nombre_actual = PRODUCTOS_KIOSCO[num_producto]["nombre"]
        precio_actual = PRODUCTOS_KIOSCO[num_producto]["precio"]
        print(cant_actual, nombre_actual)
        total_compra += precio_actual * cant_actual
    return total_compra


def ver_si_alcanza(mi_dinero, total_compra):
    if mi_dinero >= total_compra:
        alcanza_dinero = "si"
    else:
        alcanza_dinero = "no"

    print("Tengo $", mi_dinero, "en total y la compra fue de $", total_compra)
    respuesta_alcanza = input("¿Te alcanza el dinero para pagar la compra? (si/no):").lower().strip()

    if respuesta_alcanza != alcanza_dinero:
        print("¡Hiciste mal los cálculos! Te confundiste al razonar si te alcanzaba la plata o no.")
        return False

    return True


def evaluar_vuelto(mi_dinero, total_compra):
    vuelto_real = mi_dinero - total_compra

    print("¡Muy bien! Si te alcanza, pagas con $", mi_dinero)

    respuesta_vuelto = -1
    while respuesta_vuelto == -1:
        entrada = input("¿Cuanto deberia recibir de vuelto?")
        if entrada.isdigit():
            respuesta_vuelto = int(entrada)
        else:
            print("Ingresa un valor numerico valido.")
    if respuesta_vuelto != vuelto_real:
        print("Hiciste mal los calculos, el vuelto es de ", vuelto_real)
        return False
    return True


def jugar_kiosco():
    jugar_otra_vez = "si"

    while jugar_otra_vez == "si":
        print("\n================================")
        print("BIENVENIDOS AL KIOSKO MATEMÁTICO")
        print("================================")
        mi_dinero = random.randint(500, 25000)
        print("Llegas al kiosco, miras tu bolsillo y tienes: ", mi_dinero)

        total_compra = realizar_compra()

        if not ver_si_alcanza(mi_dinero, total_compra):
            print("¿Querés intentar una nueva partida en el kiosco?")
            jugar_otra_vez = input("Escribí 'si' para volver a intentar o 'no' para ir al menú: ").lower().strip()
            while jugar_otra_vez != "si" and jugar_otra_vez != "no":
                jugar_otra_vez = input("Por favor, respondé 'si' o 'no': ").lower().strip()
            continue

        if mi_dinero >= total_compra:
            if not evaluar_vuelto(mi_dinero, total_compra):
                print("\n¿Querés intentar una nueva partida en el kiosco?")
                jugar_otra_vez = input("Escribí 'si' para volver a intentar o 'no' para ir al menú: ").lower().strip()
                while jugar_otra_vez != "si" and jugar_otra_vez != "no":
                    jugar_otra_vez = input("Por favor, respondé 'si' o 'no': ").lower().strip()
                continue
            print("¡COMPRA TERMINADA CON ÉXITO! Recibís tu vuelto y te vas contento.")

        else:
            print("Compra terminada con exito. Pensaste exelente, no te alcanzaba el dinero")

        print("¡Felicitaciones! Completaste la actividad sin errores matemáticos.")
        nombre = input("Ingresá tu nombre para registrarte en el historial de expertos: ")

        with open("ranking.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Jugador: {nombre} | Bolsillo: ${mi_dinero} | Compra: ${total_compra} | ¡Cálculo Perfecto!")
        print("¡Partida registrada con éxito!")

        print("¿Querés jugar otra partida en el kiosco?")
        jugar_otra_vez = input("Escribí 'si' para jugar otra vez o 'no' para volver al menú: ").lower().strip()
        while jugar_otra_vez != "si" and jugar_otra_vez != "no":
            jugar_otra_vez = input("Por favor, respondé 'si' o 'no': ").lower().strip()

        print("Preciona enter para volver al menu principal...")
        input()

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
    fila = -1
    columna = -1
    while posicion_valida == False:
        print("\nIngrese 0 en la fila para abandonar la partida.")
        try:
            fila = int(input("Ingrese la fila: "))
            if fila == 0:
                posicion_valida = True
            else:
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
            print("\nDebe ingresar una opción válida.")
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
        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion < 1 or opcion > 2:
                print("\nOpción inválida.")
        except ValueError:
            print("\nError: debe ingresar una opción válida.")
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
    if categoria == "Geografía":
        print ("\nDebe unir paises con su respectiva capital.")
    if categoria == "Inglés":
        print ("\nDebe unir palabras en inglés con su traducción al español.")
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
    input("\nPresione ENTER para continuar...")

def menu_principal_memoria():

    opcion = 0
    while opcion != 3:
        print("\n==============================")
        print("     DESAFÍO DE MEMORIA")
        print("==============================")
        print("1 - Nueva partida")
        print("2 - Ver historial")
        print("3 - Salir")
        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                nueva_partida()
            elif opcion == 2:
                mostrar_historial()
            elif opcion == 3:
                print("\n¡Gracias por jugar!")
            else:
                print("\nOpción inválida.")
        except ValueError:
            print("\nError: debe ingresar una opción valida.")

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
        elif opcion_principal == 2:
            piedrapapeltijera()
        elif opcion_principal == 3:
            adivina_numero()
        elif opcion_principal == 4:
            jugar_kiosco()
        elif opcion_principal == 5:
            menu_principal_memoria()
        else:
            if opcion_principal != 0:
                print("\nPor favor ingrese una opción valida.")

    if opcion_principal == 0:
        print("\nMuchas gracias por utilizar el sistema.")
        print("PLATAFORMA EDUCATIVA")

menu_principal()