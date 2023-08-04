import tkinter
import socket

class Numero:
    def __init__(self):
        self.contador=0

def disminuir():
    print("disminuir")
    conta.contador=conta.contador-1
    etiqueta.set(conta.contador)
    s.send("b".encode())
    
def aumentar():
    print("aumentar")
    conta.contador=conta.contador+1
    etiqueta.set(conta.contador)
    s.send("a".encode())

s = socket.socket()

w = tkinter.Tk()
w.title("Demo")
etiqueta=tkinter.StringVar()
conta=Numero()
etiqueta.set("0")
fm = tkinter.Frame(w)
fm.grid(row=0,column=0)

bt1 = tkinter.Button(fm,text="Apagar",command=disminuir,height=2,width=20)
bt1.grid(row=1,column=0)
bt2 = tkinter.Button(fm,text="Prender",command=aumentar,height=2,width=20)
bt2.grid(row=1,column=1)
lb = tkinter.Label(fm,textvariable=etiqueta,height=2)
lb.grid(row=2,column=0,columnspan=2)

s.connect(("192.168.0.65",2020))

w.mainloop()