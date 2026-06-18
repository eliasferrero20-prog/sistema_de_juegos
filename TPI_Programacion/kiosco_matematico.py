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
print(mostrar_lista())