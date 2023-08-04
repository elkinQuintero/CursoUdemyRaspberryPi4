import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

continuar = True
while continuar:
    dato = input("Digite la letra de control: ")
    if dato == "a":
        GPIO.output(2,GPIO.HIGH)
    elif dato == "b":
        GPIO.output(2,GPIO.LOW)
    elif dato == "z":
        continuar = False
print("Fin de programa")
GPIO.cleanup()