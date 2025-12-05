from conexionBD import *

class Camion:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad):
        try:
            cursor.execute("insert into camiones values(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camiones")
            return cursor.fetchall()
        except:
            return []
    
    @staticmethod
    def consultar_id(id):
        try:
            cursor.execute("Select * from camiones where id = %s", (id,))
            return cursor.fetchone()
        except:
            return []
        
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad, id):
        try:
            cursor.execute("Update camiones set marca = %s, color= %s, modelo = %s, velocidad = %s, caballaje = %s, plazas = %s, eje = %s, capacidad_carga = %s where id =%s",(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad, id))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camiones where id =%s",(id,))
            conexion.commit()
            return True
        except:
            return False
