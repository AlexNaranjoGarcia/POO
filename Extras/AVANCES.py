"""
1ER DICIEMBRE
    1)Implementacion de MVC
    2)POO
    3)INTERFACES:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insetar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()

    Productos Entregables:
        Estructura del proyecto basada en MVC
        Modulo principal "main
        Interaccion con las interfaces
        Nombre del 
        
"""

from  tkinter import *
from tkinter import messagebox

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Coches System")
        ventana.geometry("400x300")
        ventana.resizable(0,0)
        self.menu_principal(ventana)
        ventana.pack()
        mainloop()

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        Vista.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Menu Principal", font=("Arial", 16))
        lbl_titulo.pack(pady=20)
        lbl_opcion = Label(ventana, text="Seleccione una opcion:")
        lbl_opcion.pack(pady=10)
        btn_autos = Button(ventana, text="Autos", command=lambda: Vista.menu_acciones(ventana))
        btn_autos.pack(pady=10)
        btn_camionetas = Button(ventana, text="Camionetas", command=lambda: messagebox.showinfo("Camionetas", "Funcionalidad en desarrollo"))
        btn_camionetas.pack(pady=10)
        btn_camiones = Button(ventana, text="Camiones", command=lambda: messagebox.showinfo("Camiones", "Funcionalidad en desarrollo"))
        btn_camiones.pack(pady=10)

    @staticmethod
    def menu_acciones(ventana):
        Vista.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Menu Acciones - Autos", font=("Arial", 16))
        lbl_titulo.pack(pady=20)
        btn_insertar = Button(ventana, text="Insertar Autos", command=lambda: Vista.insertar_autos(ventana))
        btn_insertar.pack(pady=10)
        btn_volver = Button(ventana, text="Volver al Menu Principal", command=lambda: Vista.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def insertar_autos(ventana):
        Vista.borrarPantalla(ventana)
        Label(ventana, text="Insertar Autos", font=("Arial", 16)).pack(pady=20)

        Label(ventana, text="Color:").pack()
        entrada_color = Entry(ventana)
        entrada_color.pack()

        Label(ventana, text="Marca:").pack()
        entrada_marca = Entry(ventana)
        entrada_marca.pack()

        Label(ventana, text="Modelo:").pack()
        entrada_modelo = Entry(ventana)
        entrada_modelo.pack()

        Label(ventana, text="Año:").pack()
        entrada_año = Entry(ventana)
        entrada_año.pack()

        def guardar_auto():
            marca = entrada_marca.get()
            modelo = entrada_modelo.get()
            año = entrada_año.get()
            messagebox.showinfo("Auto Guardado", f"Auto guardado:\nMarca: {marca}\nModelo: {modelo}\nAño: {año}")

        Button(ventana, text="Guardar Auto", command=guardar_auto).pack(pady=10)
        Button(ventana, text="Volver al Menu Acciones", command=lambda: Vista.menu_acciones(ventana)).pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):
        Vista.borrarPantalla(ventana)


    @staticmethod
    def cambiar_autos(ventana):
        Vista.borrarPantalla(ventana)
        