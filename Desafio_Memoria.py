def leer_parejas(nombre_archivo):

    parejas = []
    with open(nombre_archivo, "r") as archivo:
        registros = archivo.readlines()
        for linea in registros:
            linea = linea.strip()
            dato1, dato2 = linea.split(";")
            parejas.append((dato1, dato2))
    return parejas