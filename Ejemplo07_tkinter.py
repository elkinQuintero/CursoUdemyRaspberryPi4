import time
from tkinter import *
import threading as th

def cambio(valor):
    etiqueta1.set(valor)
    # time.sleep(0.2) Poner cuando trabajamos con elementos mecanicos, un pequeno delay

def aumentar():
    while True:
        cont = 0
        while True:
            time.sleep(1)
            etiqueta2.set(cont)
            cont = cont + 1

w = Tk()

#DEFINICON ETIQUETA
etiqueta1 = StringVar()
etiqueta1.set(0)
etiqueta2 = StringVar()
etiqueta2.set(0)

hilo = th.Thread(target=aumentar)
hilo.start()

#CONTENEDOR
fm = Frame(w)
fm.grid(row=0, column=0)

#SLIDER
sl = Scale(fm, from_=0, to=20, orient=HORIZONTAL, length=200, command=cambio) #Slider 0 a 20 horiontal en el contenedor fm
sl.grid(row=1, column=0) #Ubicación del slider en la fila 1 y columna 0

#LABEL
lb1 = Label(fm, textvariable=etiqueta1, height=2)
lb1.grid(row=2, column=0)

lb2 = Label(fm, textvariable=etiqueta2, height=2)
lb2.grid(row=3, column=0)

w.mainloop()