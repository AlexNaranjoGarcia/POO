from conexionBD import *
import datetime


def registrar_usuario(nombre, apellidos, email, password):
    try:
        fecha=datetime.datetime.now()
        sql="insert into usuarios(nombre, apellidos, email, password, fecha) values(%s, %s, %s, %s, %s)"
        val=(nombre, apellidos, email, password, fecha)
        cursor.execute(sql,val )
        conexion.commit()
        print(f"\n \t \t Usuario {nombre} {apellidos} registrado correctamente")
        return True
    except:
        return False
    
def login_usuario(email, password):
    try:
        sql="select * from usuarios where email=%s and password=%s"
        val=(email, password)
        cursor.execute(sql, val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            print("\n \t \t Usuario o contraseña incorrectos.")
            return None
    except Error as e:
        print(f"\n \t \t Error al intentar iniciar sesión: {e}")
        return None
 