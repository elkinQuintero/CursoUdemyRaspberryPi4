import socket
import mysql.connector as mysql

db = mysql.connect(host="192.168.0.68", user="excelec", passwd="1234", database="test")
cursor = db.cursor()

s = socket.socket()
s.bind(("192.168.0.68",2020))
s.listen(10)
query = "INSERT INTO prueba1 (v1,v2,v3) VALUES(%s,%s,%s)"
print("Esperando conexiones...")
while True:
    (sc,addrc) = s.accept()
    print("Cliente conectado ", addrc)
    continuar = True
    while continuar:
        data = sc.recv(64)
        if not data:
            continuar = False
        else:
            print(data)
            valores = [data[0],data[1],data[2]]
            cursor.execute(query,valores)
            db.commit()
cursor.close()
db.close()
s.close()
print("Fin de programa")
