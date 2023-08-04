import tkinter
import time

def cambio(valor):
    etiqueta.set(valor)
    time.sleep(0.2)

w = tkinter.Tk()
etiqueta = tkinter.StringVar()
etiqueta.set(0)
fm = tkinter.Frame(w)
fm.grid(row=0,column=0)
sl = tkinter.Scale(fm,from_=0,to=20,orient=tkinter.HORIZONTAL,length=200,command=cambio)
sl.grid(row=1,column=0)
lb = tkinter.Label(fm,textvariable=etiqueta,height=2)
lb.grid(row=2,column=0)

w.mainloop()