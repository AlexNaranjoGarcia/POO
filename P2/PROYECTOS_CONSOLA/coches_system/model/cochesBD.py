from conexion_BD import *

class Autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    def insertar(self):
        try:
            cursor.execute(
                "insert into coches values (NULL,%s,%s,%s,%s,%s,%s)",(self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from coches"
            )
            return cursor.fetchall()
        except:
            return False
        
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
        try:
            cursor.execute(
                "update coches set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",(marca,color,modelo,velocidad,caballaje,plazas,id)
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
                "delete from coches where id=%s",(id,)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False
        


class Camionetas:
    @staticmethod
    #si es estatico el metodo se puede usar sin tener un objeto creado de esa clase y no se usa el self
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado):
        try:
            cursor.execute(
                "insert into camionetas values (NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from camionetas"
            )
            return cursor.fetchall()
        except:
            return False
        
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado,id):
        try:
            cursor.execute(
                "update camionetas set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,traccion=%s,cerrada=%s where id=%s",(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrado,id)
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
                "delete from camionetas where id=%s",(id,)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False

class Camiones:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad_carga):
        try:
            cursor.execute(
                "insert into camiones values (NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad_carga)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from camiones"
            )
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad_carga,id):
        try:
            cursor.execute(
                "update camiones set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidad_carga=%s where id=%s",(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad_carga,id)
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
                "delete from camiones where id=%s",(id,)
            )
            conexion.commit()
            if cursor.rowcount>0:
                return True
            else:
                return False
        except:
            return False