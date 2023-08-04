import mysql.connector as mysql
import random

db = mysql.connect(host="192.168.0.68", user="excelec",passwd="1234",database="test")
cursor = db.cursor()
query = "INSERT INTO prueba1(v1,v2,v3) VALUES (%s,%s,%s)"
for i in range(5):
    valores = (random.randint(15,30),random.randint(15,30),random.randint(15,30))
    cursor.execute(query,valores)
    db.commit()

cursor.close()
db.close()
print("Fin de programa")
