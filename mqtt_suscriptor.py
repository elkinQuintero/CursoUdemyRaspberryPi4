# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

import mysql.connector as mysql

 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("demotest")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    mensaje = str(msg.payload.decode("utf-8"))
    valor = [mensaje]
    print(type(valor))
    print(msg.topic+" "+mensaje)
    db = mysql.connect(host="192.168.0.68", user="excelec", passwd="1234", database="test")
    cursor = db.cursor()
    query = "INSERT INTO prueba2mqtt (mensaje) VALUES(%s)"
    cursor.execute(query,valor)
    db.commit()
    cursor.close()
    db.close()
    if mensaje == "Encender":
        GPIO.output(2, GPIO.HIGH)
        print("Led ON")
        # Do something


    elif mensaje == "Apagar":
        GPIO.output(2, GPIO.LOW)
        print("Led OFF")
        # Do something else


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.53", 1883)
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions

client.loop_forever()
