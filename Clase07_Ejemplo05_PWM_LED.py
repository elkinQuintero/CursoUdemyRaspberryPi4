import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

pwm = GPIO.PWM(2,500)
pwm.start(0)

continuar = True
while continuar:
    dato = input("Digite el nuevo DC: ")
    if dato == "z":
        continuar=False
    else:
        pwm.ChangeDutyCycle(int(dato))
pwm.stop()
GPIO.cleanup()
print("Fin de Programa")