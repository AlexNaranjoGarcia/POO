from conexionBD import *

class Autos: 
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            cursor.execute("Insert into coches values(Null, %s, %s, %s, %s, %s, %s)",(marca, color, modelo, velocidad, caballaje, plazas))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from coches")
            return cursor.fetchall()
        except:
            return []
    
    @staticmethod
    def consultar_id(id):
        try:
            cursor.execute("Select * from coches where id = %s", (id,))
            return cursor.fetchone()
        except:
            return []
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        try:
            cursor.execute("Update coches set marca = %s, color= %s, modelo = %s, velocidad = %s, caballaje = %s, plazas = %s where id =%s",(marca, color, modelo, velocidad, caballaje, plazas, id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id =%s",(id,))
            conexion.commit()
            return True
        except:
            return False


