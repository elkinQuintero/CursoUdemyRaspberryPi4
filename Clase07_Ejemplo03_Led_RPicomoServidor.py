import socket
import RPi.GPIO as GPIO

s = socket.socket()
s.bind(("192.168.0.68",2020))
s.listen(10)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

while True:
    (sc,addrc) = s.accept()
    print("Cliente conectado:",addrc)
    continuar = True
    while continuar:
        dato = sc.recv(64)
        if not dato:
            continuar = False
            print("Cliente desconectado")
        else:
            dato2 = dato.decode()
            if dato2 == "a":
                print("Led encendido")
                GPIO.output(2,GPIO.HIGH)
            elif dato2 == "b":
                print("Led apagado")
                GPIO.output(2,GPIO.LOW)
s.close()
print("Fin de programa")