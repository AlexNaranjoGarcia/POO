from conexionBD import *
import datetime

class Notas:
    
    @staticmethod
    def insertar(usuario_id,titulo,descripcion):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into notas values (NULL,%s,%s,%s,%s)",(usuario_id,titulo,descripcion,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def mostrar(usuario_id):
        try:
            cursor.execute(
                "select * from notas where usuario_id=%s",(usuario_id,)
            )
            return cursor.fetchall()
        except:
            return False
    
    @staticmethod
    def actualizar(titulo,descripcion,id):
        try:
            cursor.execute(
                "update notas set titulo=%s, descripcion=%s where id=%s",(titulo,descripcion,id)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from notas where id=%s",(id,)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def check(id):
        try:
            cursor.execute(
                "select * from notas where id=%s",(id,)
            )
            return cursor.fetchall()
        except:
            return False