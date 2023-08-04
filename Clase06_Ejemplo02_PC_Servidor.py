import socket
import threading as th

def manejar(sc,addrc):
    print("Cliente conectado:",addrc)
    continuar = True
    while continuar:
        dato = sc.recv(64)
        if not dato:
            continuar=False
            print("Cliente desconectado")
        else:
            print(dato)
    sc.close()

s = socket.socket()
s.bind(("192.168.1.6",2020))
s.listen(10)
print("Iniciando servidor")
while True:
    (sc,addrc) = s.accept()
    hilo = th.Thread(target = manejar,args=(sc,addrc))
    hilo.start()
    
print("Fin de programa")
s.close()
    