import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sanja051/",
    database="Proyect_Pet"
)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM clients')

registros = cursor.fetchall()

for registro in registros:
    print(registro)

conexion.close()