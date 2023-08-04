import paho.mqtt.client as mqtt
import random
import time
cliente = mqtt.Client()
cliente.connect("192.168.0.53",1883)

for x in range(1,4):

    a1 = random.randint(1,20)
    a2 = random.randint(1,20)
    a3 = random.randint(1,20)
    data = [a1,a2,a3]
    cliente.publish("demo3",bytearray(data))#Cuando se manda una lista se debe de pasar a bytearray
    # time.sleep(1)
    print("enviado: ", a1, " ", a2, " ", a3)
print("Fin de programa")


 