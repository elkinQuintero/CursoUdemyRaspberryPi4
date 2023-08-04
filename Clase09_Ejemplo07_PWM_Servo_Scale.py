import RPi.GPIO as GPIO
import tkinter
import time

def cambio(valor):
    print(type(valor),valor)
    etiqueta.set(valor)
    dc = (float(valor) + 45)/18
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.2)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
pwm = GPIO.PWM(2,50)
pwm.start(2.5)
w = tkinter.Tk()
etiqueta = tkinter.StringVar()
etiqueta.set(0)
fm = tkinter.Frame(w)
fm.grid(row=0,column=0)
sl = tkinter.Scale(fm,from_=0,to=180,orient=tkinter.HORIZONTAL,length=200,command=cambio)
sl.grid(row=1,column=0)
lb = tkinter.Label(fm,textvariable=etiqueta,width=20,height=2)
lb.grid(row=2,column=0)
w.mainloop()
pwm.stop()
GPIO.cleanup()
print("Fin de programa")