import socket
import random
import time

s=socket.socket()
s.connect(("192.168.0.65", 2020))
data = [0,0,0]
for i in range(100):
    data[0] = random.randint(10,30)
    data[1] = random.randint(15,45)
    data[2] = random.randint(10,25)
    s.send(bytes(data))
    time.sleep(1)

s.close()
print("Data enviada")
print("Fin del programa")
