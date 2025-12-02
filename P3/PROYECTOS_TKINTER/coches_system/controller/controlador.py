from model import coches, camiones, camionetas
from tkinter import messagebox
class Funciones:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message="Operacion realizada con exito")
        else:
            messagebox.showerror(message="Error al realizar la operacion")