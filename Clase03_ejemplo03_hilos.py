import threading as th
import time

def paralelo():
    global contador
    global conti
    contador=0
    conti=True
    while conti:
        time.sleep(1)
        contador=contador+1
    print("Fin del Hilo")

print("Inicio del programa")
hilo = th.Thread(target=paralelo)
hilo.start()
continuar = True
while continuar:
    dato = input("Digite algo: ")
    if dato == "a":
        print(contador)
    elif dato == "z":
        continuar=False
        conti=False
    else:
        print(dato)
print("Fin de programa principal")