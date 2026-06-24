import random
palabra=["casa", "perro", "gato", "mesa", "silla", "ventana", "puerta", "escuela", "amigo", "pelota"]
aleatorio=random.choice(palabra)
palabra1=""
for i in range(len(aleatorio)):
    palabra1+="-"
print(palabra1)
palabrasecreta=""
intentos=5
print("Pista (primer letra):", aleatorio[0])
finalizado=False
while intentos!=0 and finalizado==False:
    letra=input()
    palabrasecreta=""
    intentos-=1
    for i in range(len(aleatorio)):
        if letra==aleatorio[i]:
            palabrasecreta+=letra
            intentos += 1
        else:
            palabrasecreta+=palabra1[i]
    palabra1=palabrasecreta
    print(palabrasecreta)
    if aleatorio == palabrasecreta:
        finalizado=True
if aleatorio==palabrasecreta:
    print("Ganaste")
else:
    print("Perdiste")