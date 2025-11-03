from conexionBD import *
import hashlib
import datetime

class Usuarios:

    @staticmethod
    def registrar(nombre,apellidos,email,password):
        try:
            fecha=datetime.datetime.now()
            password=hashlib.sha256(password.encode()).hexdigest()
            cursor.execute(
                "insert into usuarios values (NULL,%s,%s,%s,%s,%s)",(nombre,apellidos,email,password,fecha)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def iniciar_sesion(email,password):
        try:
            password=hashlib.sha256(password.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",(email,password)
            )
            return cursor.fetchone()
        except:
            return False
