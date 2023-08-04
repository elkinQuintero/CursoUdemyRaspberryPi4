from bluedot.btcomm import BluetoothServer
import RPi.GPIO as GPIO

def leer(data):
    print(data)
    if data == "F":
        GPIO.output(2,GPIO.HIGH)
    elif data == "B":
        GPIO.output(2,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
print("Iniciando servidor Bluetooth")
s = BluetoothServer(leer)