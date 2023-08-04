import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.IN)
GPIO.output(2,GPIO.LOW)

try:
    while True:
        GPIO.output(2,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(2,GPIO.LOW)
        t1 = time.time()
        while GPIO.input(20) == GPIO.LOW:
            t1 = time.time()
        while GPIO.input(20) == GPIO.HIGH:
            t2 = time.time()
        t = t2-t1
        d = 17000*t
        print("Distancia: ",round(d,1),"cms")
        time.sleep(0.2)
except:
    GPIO.cleanup()
    print("Fin de programa")