import Adafruit_DHT as dht

sensor = dht.DHT11

continuar = True
while continuar:
    dato = input("Digite algo para leer el sensor: ")
    if dato == "z":
        continuar = False
    else:
        h,t = dht.read_retry(sensor,4)
        print("T=",t," ,H=",h)
print("Fin de programa")