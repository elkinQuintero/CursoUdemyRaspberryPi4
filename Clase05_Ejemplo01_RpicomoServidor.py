import socket

s = socket.socket()
s.bind(("192.168.1.2",2020))
s.listen(10)
print("Esperando conexiones...")
(sc,addrc) = s.accept()
print("Cliente conectado",addrc)
continuar = True
while continuar:
    dato = sc.recv(64)
    if not dato:
        continuar = False
        print("Cliente desconectado")
    else:
        print(dato)
sc.close()
s.close()
print("Fin de programa")