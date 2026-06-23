palabra=input()
palabra1=""
for i in range(len(palabra)):
    palabra1+="-"
print(palabra1)
palabrasecreta=""
intentos=5
while intentos!=0:
    letra=input()
    palabrasecreta="" 
    intentos-=1 
    for i in range(len(palabra)):
        if letra==palabra[i]:
            palabrasecreta+=letra
        else:
            palabrasecreta+=palabra1[i]
    palabra1=palabrasecreta
    print(palabrasecreta)
if palabra==palabrasecreta:
    print("Ganaste")
else:
    print("Perdiste")






