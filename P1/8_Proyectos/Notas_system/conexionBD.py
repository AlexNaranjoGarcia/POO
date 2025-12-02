import mysql.connector
from mysql.connector import Error

try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_notas"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print(f"\n \t \t No se pudo conectar a la base de datos. Verifica que el servidor esté activo y la base de datos exista.") 


