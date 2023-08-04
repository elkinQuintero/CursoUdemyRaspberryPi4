import socket

s = socket.socket()
s.connect(("192.168.1.2",2020))

continuar = True
while continuar:
    dato = input("Digite lo que desea enviar: ")
    if dato == "z":
        continuar=False
    else:
        s.send(dato.encode())
s.close()
print("Fin de Programa")