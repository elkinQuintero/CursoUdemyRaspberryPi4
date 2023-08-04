import socket
s = socket.socket()

s.connect(("192.168.1.6",2020))
print("Conectado al servidor")
continuar = True
while continuar:
    dato = input("Digite la data a enviar: ")
    if dato == "z":
        continuar=False
    else:
        s.send(dato.encode())
s.close()
print("Fin de programa")