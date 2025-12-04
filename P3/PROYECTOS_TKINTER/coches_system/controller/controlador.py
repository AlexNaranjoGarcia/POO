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
        if len(registro)==0:
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