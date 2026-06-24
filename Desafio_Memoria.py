def leer_parejas(nombre_archivo):

    parejas = []

    archivo = open(nombre_archivo, "r")

    for registro in archivo:

        registro = registro.strip()

        dato1, dato2 = registro.split(";")

        parejas.append((dato1, dato2))

    archivo.close()

    return parejas