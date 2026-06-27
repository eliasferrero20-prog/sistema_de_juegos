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
        print("Bienvenidos al kiosoco matematico")

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