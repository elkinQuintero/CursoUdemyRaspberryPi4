inicio = True
while inicio == True:
    a = input("digite un numero: ")
    if a == "fin":
        inicio = False
    else:
        b = int(a)
        c = b%2
        if c == 0:
            print("Numero par")
        else:
            print("Numero impar")
print("Fin de programa")