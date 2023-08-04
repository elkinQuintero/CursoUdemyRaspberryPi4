import paho.mqtt.client as mqtt

cliente = mqtt.Client()
cliente.connect("192.168.0.53",1883)


def escuchar(cliente,userdata,mensaje):
    print(str(mensaje.payload[0])," ",str(mensaje.payload[1])," ",str(mensaje.payload[2]))

cliente.on_message = escuchar
cliente.subscribe("demo3")

print("Iniciando escuchador")
cliente.loop_forever()

print("Fin OK")