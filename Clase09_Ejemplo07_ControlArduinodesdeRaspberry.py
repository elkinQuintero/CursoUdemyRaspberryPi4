import serial
s = serial.Serial("/dev/ttyACM0",9600)

continuar = True
while continuar:
    dato = input("Digite una letra: ")
    if dato == "z":
        continuar = False
    else:
        s.write(dato.encode())

s.close()
print("Fin de Programa")