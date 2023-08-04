import paho.mqtt.client as mqtt

cliente = mqtt.Client()
cliente.connect("192.168.0.68",1883)

data = "Hello"

cliente.publish("demo",data)#Cuando se manda una lista se debe de pasar a bytearray
print("Fin de programa")


