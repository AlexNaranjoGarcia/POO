from conexionBD import *

class Camionetas:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            cursor.execute("insert into camionetas values(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("Select * from camionetas")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        try:
            cursor.execute("Update camionetas set marca = %s, color= %s, modelo = %s, velocidad = %s, caballaje = %s, plazas = %s, traccion = %s, cerrada = %s where id_camioneta =%s",(marca, color, modelo, velocidad, caballaje, plazas, traccion,cerrada, id))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camionetas where id_camioneta =%s",(id,))
            conexion.commit()
            return True
        except:
            return False
