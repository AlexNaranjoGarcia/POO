
from conexionBD import *
import hashlib
import datetime


class Usuario:
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        try:
            
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre,apellidos,email,hashlib.sha256(password.encode()).hexdigest(),fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
            return None         

    @staticmethod
    def nombre_apellidos(id):
        try:
            cursor.execute(
                "select nombre, apellidos from usuarios where id=%s",
                (id,)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
            return None       
