import mysql.connector as mysql
import matplotlib.pyplot as plt

ejex = []
ejev1 = []
ejev2 = []
db = mysql.connect(host="192.168.1.7",user="roger",passwd="1234",database="test")
cursor = db.cursor()

query = "SELECT * FROM prueba"
cursor.execute(query)
resultado = cursor.fetchall()
db.commit()

for x in resultado:
    ejex.append(x[0])
    ejev1.append(x[1])
    ejev2.append(x[2])

plt.plot(ejex,ejev1,label="valor1")
plt.plot(ejex,ejev2,label="valor2")
plt.legend()
plt.xlabel("id")
plt.ylabel("Valores")
plt.title("Seleccion")
plt.show()
cursor.close()
db.close()
print("Fin de programa")