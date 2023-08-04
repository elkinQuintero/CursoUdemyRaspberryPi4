import paho.mqtt.client as mqtt
import mysql.connector as mysql


cliente = mqtt.Client()
cliente.connect("192.168.0.53",1883)
db = mysql.connect(host="192.168.0.68", user="excelec",passwd="1234", database="test")
cursor = db.cursor()

def escuchar(cliente,userdata,mensaje):
    print(str(mensaje.payload[0])," ",str(mensaje.payload[1])," ",str(mensaje.payload[2]))
    valores = (mensaje.payload[0], mensaje.payload[1], mensaje.payload[2])
    cursor.execute(query,valores)
    db.commit()

cliente.on_message = escuchar
cliente.subscribe("demo3")
query = "INSERT INTO prueba1(v1,v2,v3) VALUES(%s,%s,%s)"

print("Iniciando escuchador")
cliente.loop_forever()

print("Fin OK")