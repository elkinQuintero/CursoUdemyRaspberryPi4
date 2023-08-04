import tkinter
import time
import threading as th
def aumentar():
    contador = 0
    while True:
        time.sleep(1)
        etiqueta2.set(contador)
        contador= contador+1

def cambio(valor):
    etiqueta1.set(valor)

w = tkinter.Tk()
etiqueta1 = tkinter.StringVar()
etiqueta1.set(0)
etiqueta2 = tkinter.StringVar()
etiqueta2.set(0)
hilo = th.Thread(target = aumentar)
hilo.start()
fm = tkinter.Frame(w)
fm.grid(row=0,column=0)
sl = tkinter.Scale(fm,from_=0,to=20,orient=tkinter.HORIZONTAL,length=200,command=cambio)
sl.grid(row=1,column=0)
lb1 = tkinter.Label(fm,textvariable=etiqueta1,height=2)
lb1.grid(row=2,column=0)
lb2 = tkinter.Label(fm,textvariable=etiqueta2,height=2)
lb2.grid(row=3,column=0)

w.mainloop()