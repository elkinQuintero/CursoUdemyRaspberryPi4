from tkinter import *
import socket


def apagar():
    etiqueta.set("Apagado")
    s.send("apagar".encode())
def encender():
    etiqueta.set("Encendido")
    s.send("encender".encode())


s = socket.socket()
s.connect(("192.168.0.65",2020))

w = Tk()

etiqueta=StringVar()
etiqueta.set("Apagado")

fm = Frame(w)
fm.grid(row=0, column=0)

bt1 = Button(fm,text="Apagar",command=apagar,height=2,width=20)
bt1.grid(row=1,column=0)
bt2 = Button(fm,text="Encender",command=encender,height=2,width=20)
bt2.grid(row=1,column=1)
lb = Label(fm,textvariable=etiqueta,height=2)
lb.grid(row=2,column=0,columnspan=2)

w.mainloop()

s.close()
print("Fin del programa")