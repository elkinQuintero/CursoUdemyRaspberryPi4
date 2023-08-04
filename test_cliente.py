import socket

s = socket.socket()
s.connect(("192.168.0.68",2020))
continuar = True
while continuar:
    dato = input("Digite lo que desea enviar: ")
    if dato == "z":
        continuar = False
    else:
        s.send(dato.encode())#.encode convierte el dato que esta en String a Bytes

s.close()
print("Fin del programa")