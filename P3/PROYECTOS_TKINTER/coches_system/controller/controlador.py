from view import vista
from model import coches, camiones, camionetas
from tkinter import messagebox
class Funciones:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message="Operacion realizada con exito")
        else:
            messagebox.showerror(message="Error al realizar la operacion")
    
    @staticmethod
    def insertar_autos(marca, color, modelo, velocidad, caballaje, plazas):
        respuesta = coches.Autos.insertar(marca, color, modelo, velocidad, caballaje, plazas)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def get_id_auto(window, id, tipo):
        registro = coches.Autos.consultar_id(id)
        if registro == None:
            messagebox.showerror(title="Error", message="No existe ese ID")
            return
        if tipo == "cambiar":
            vista.Vista.cambiar_auto(window, registro)
        if tipo == "borrar":
            vista.Vista.eliminar_auto(window, registro)
    
    @staticmethod
    def consultar_autos():
        registros = coches.Autos.consultar()
        if len(registros)==0:
            messagebox.showerror(title="Error", message="No hay registros de Autos")
        return registros
    
    @staticmethod
    def cambiar_auto(marca, color, modelo, velocidad, caballaje, plazas, id):
        respuesta = coches.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas, id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def eliminar_auto(id):
        respuesta = coches.Autos.eliminar(id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def insertar_camionetas(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        respuesta = camionetas.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def get_id_camioneta(window, id, tipo):
        registro = camionetas.Camionetas.consultar_id(id)
        if registro == None:
            messagebox.showerror(title="Error", message="No existe ese ID")
            return
        if tipo == "cambiar":
            vista.Vista.cambiar_camionetas(window, registro)
        if tipo == "borrar":
            vista.Vista.eliminar_camionetas(window, registro)
    
    @staticmethod
    def consultar_camionetas():
        registros = camionetas.Camionetas.consultar()
        if len(registros)==0:
            messagebox.showerror(title="Error", message="No hay registros de Camionetas")
        return registros
    
    @staticmethod
    def cambiar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada,id):
        respuesta = camionetas.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def eliminar_camionetas(id):
        respuesta = camionetas.Camionetas.eliminar(id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def insertar_camiones(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad):
        respuesta = camiones.Camion.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def get_id_camion(window, id, tipo):
        registro = camiones.Camion.consultar_id(id)
        if registro == None:
            messagebox.showerror(title="Error", message="No existe ese ID")
            return
        if tipo == "cambiar":
            vista.Vista.cambiar_camiones(window, registro)
        if tipo == "borrar":
            vista.Vista.eliminar_camiones(window, registro)
    
    @staticmethod
    def consultar_camiones():
        registros = camiones.Camion.consultar()
        if len(registros)==0:
            messagebox.showerror(title="Error", message="No hay registros de Camiones")
        return registros
    
    @staticmethod
    def cambiar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad, id):
        respuesta = camiones.Camion.actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidad, id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def eliminar_camion(id):
        respuesta = camiones.Camion.eliminar(id)
        Funciones.respuesta_sql(respuesta)