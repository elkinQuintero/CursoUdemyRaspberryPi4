import tkinter
import RPi.GPIO as GPIO

def apagar():
    print("Apagar")
    GPIO.output(2,GPIO.LOW)
    etiqueta.set("Apagado")
    
def encender():
    print("Encender")
    GPIO.output(2,GPIO.HIGH)
    etiqueta.set("Encendido")

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)
w = tkinter.Tk()
etiqueta=tkinter.StringVar()
etiqueta.set("Apagado")
fm = tkinter.Frame(w)
fm.grid(row=0,column=0)
b1 = tkinter.Button(fm,text = "Apagar",command=apagar)
b1.grid(row=1,column=0)
b2 = tkinter.Button(fm,text = "Encender",command=encender)
b2.grid(row=1,column=1)
lb = tkinter.Label(fm,textvariable=etiqueta)
lb.grid(row=2,column=0,columnspan=2)
w.mainloop()