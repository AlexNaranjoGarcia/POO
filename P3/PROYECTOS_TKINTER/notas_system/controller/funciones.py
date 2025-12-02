from model import usuario, nota
from tkinter import messagebox
from view import view1

class Controlador:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message="Accion realizada con exito")
        else:
            messagebox.showinfo(message="No fue posible realizar la accion")

    @staticmethod
    def registrar_usuario(window, nombre, apellidos, email, password):
        respuesta =  usuario.Usuario.registrar(nombre, apellidos, email, password)
        if respuesta:
            messagebox.showinfo("Registro Exitoso", f"{nombre} {apellidos} registrado correctamente")
            view1.Vista.login(window)
        else:
            messagebox.showerror("Error", "No se pudo registrar")
    
    @staticmethod
    def login(window, email, password):
        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo("Logueo Exitoso", f"{registro[1]} {registro[2]}, se ha logueado correctamente")
            view1.Vista.menu_notas(window,registro[0],registro[1], registro[2])
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    @staticmethod
    def crear_nota(usuario_id, titulo, descripcion):
        respuesta =  nota.Nota.crear(usuario_id, titulo, descripcion)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def mostrar_notas(usuario_id):
        respuesta = nota.Nota.mostrar(usuario_id)
        if len(respuesta)>0:
            return respuesta
        else:
            messagebox.showinfo(message="No fue posible realizar la accion")
            return respuesta
    
    @staticmethod
    def eliminar_nota(nota_id):
        respuesta =  nota.Nota.eliminar(nota_id)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def actualizar_nota(nota_id, titulo, desc):
        respuesta = nota.Nota.actualizar(nota_id, titulo, desc)
        Controlador.respuesta_sql(respuesta)