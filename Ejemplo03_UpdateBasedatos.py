import mysql.connector as mysql

db = mysql.connect(host="192.168.0.65", user="excelec",passwd="1234",database="test")
cursor = db.cursor()
query = "UPDATE prueba SET valor1=%s, valor2=%s WHERE id=%s"
valores = (5,6,10)
cursor.execute(query,valores)

db.commit()
cursor.close()
db.close()
print("Fin del programa")