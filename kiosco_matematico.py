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
        entrada = input("Cuantos/as ", PRODUCTOS_KIOSCO[numero_lista]["nombre"], "vas a llevar?")
        if entrada.isdigit():
            cantidad = int(entrada)
        else:
            print("Por favor ingrese numeros")
    return [numero_lista, cantidad]

def jugar_kiosco():
    print("Bienvenidos al kiosoco matematico")

    mi_dinero = random.randint(500, 25000)
    print("Llegas al kiosco, miras tu bolsillo y tienes: ", mi_dinero)

    carrito = []

    continuar = "si"
    while continuar == "si":
        producto_comprado = pedir_producto()
        carrito.append(producto_comprado)
        continuar = input("Quieres comprar otro producto? (si/no):").lower().strip()
        while continuar != "si" and continuar != "no":
            continuar = input("Responde solo, si o no").lower().strip()