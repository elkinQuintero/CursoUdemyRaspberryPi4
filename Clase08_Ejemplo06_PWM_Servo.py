import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

pwm = GPIO.PWM(2,50)
pwm.start(2.5)

continuar = True
while continuar:
    dato = input("Digite el dc para el servo: ")
    if dato == "z":
        continuar=False
    else:
        pwm.ChangeDutyCycle(float(dato))
pwm.stop()
GPIO.cleanup()
print("Fin de programa")