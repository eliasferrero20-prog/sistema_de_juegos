import random

print("\n========================================")
print("     ¡BIENVENIDO AL JUEGO DE ADIVINAR!  ")
print("========================================")

usuario = input("INGRESE NOMBRE DE USUARIO: ")

juego_activo = True

while juego_activo == True:
    print("\nSELECCIONA LA DIFICULTAD:\n1. FACIL (7 intentos)\n2. INTERMEDIO (5 intentos)\n3. DIFICIL (3 intentos)")
    dificultad = input("Elegí una opción (1, 2 o 3): ")