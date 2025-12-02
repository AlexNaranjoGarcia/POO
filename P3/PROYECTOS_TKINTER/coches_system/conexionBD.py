import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bd_coches"
    )
    cursor = conexion.cursor(buffered=True)
except:
    print("Error al conectar con la base de datos")