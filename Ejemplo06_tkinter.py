import time
from tkinter import *

def cambio(valor):
    etiqueta.set(valor)
    time.sleep(0.2)

w = Tk()

#DEFINICON ETIQUETA
etiqueta = StringVar()
etiqueta.set(0)

#CONTENEDOR
fm = Frame(w)
fm.grid(row=0, column=0)

#SLIDER
sl = Scale(fm, from_=0, to=20, orient=HORIZONTAL, length=200, command=cambio) #Slider 0 a 20 horiontal en el contenedor fm
sl.grid(row=1, column=0) #Ubicación del slider en la fila 1 y columna 0

#LABEL
lb = Label(fm, textvariable=etiqueta, height=2)
lb.grid(row=2, column=0)

w.mainloop()
