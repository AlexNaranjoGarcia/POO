import tkinter as tk
from tkinter import messagebox
from controller import funciones

class Vista:
    def __init__(self, window):
        self.window = window
        self.window.title("Sistema de Notas")
        self.window.geometry("800x600")
        self.menu_principal(window)
    
    @staticmethod
    def limpiar(window):
        for widget in window.winfo_children():
            if isinstance(widget, tk.Menu): continue
            widget.destroy()
    
    @staticmethod
    def menu_principal(window):
        Vista.limpiar(window)
        tk.Label(window, text=".:: Menu Principal ::.", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(window, text="1.- Registro", width=30, command=lambda:Vista.registro(window)).pack(pady=10)
        tk.Button(window, text="2.- Login", width=30, command=lambda:Vista.login(window)).pack(pady=10)
        tk.Button(window, text="3.- Salir", width=30, command=lambda:window.quit(window)).pack(pady=10)
    
    @staticmethod
    def registro(window):
        Vista.limpiar(window)
        nombre = tk.StringVar()
        apellidos = tk.StringVar()
        email = tk.StringVar()
        psw = tk.StringVar()
        
        tk.Label(window, text=".:: Registro ::.", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(window, text="¿Cuál es tu nombre?").pack()
        tk.Entry(window, textvariable=nombre).pack(pady=5)
        
        tk.Label(window, text="¿Cuáles son tus apellidos?").pack()
        tk.Entry(window, textvariable=apellidos).pack(pady=5)
        
        tk.Label(window, text="Ingresa tu email:").pack()
        tk.Entry(window, textvariable=email).pack(pady=5)
        
        tk.Label(window, text="Ingresa tu Contraseña:").pack()
        tk.Entry(window, textvariable=psw, show="*").pack(pady=5)
        
        tk.Button(window, text="Registrar", bg="green", fg="white", command=lambda:
            funciones.Controlador.registrar_usuario(window,nombre.get(),apellidos.get(),email.get(),psw.get()),
            ).pack(pady=20)
        tk.Button(window, text="Volver", command=Vista.menu_principal).pack(pady=5)
    
    @staticmethod
    def login(window):
        Vista.limpiar(window)
        email = tk.StringVar()
        psw = tk.StringVar()
        
        tk.Label(window, text=".:: Login ::.", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(window, text="Ingresa tu Email").pack()
        tk.Entry(window, textvariable=email).pack(pady=5)
        
        tk.Label(window, text="Ingresa tu Contraseña").pack()
        tk.Entry(window, textvariable=psw, show="*").pack(pady=5)
        
        tk.Button(window, text="Entrar", bg="blue", fg="white", command=lambda:
            funciones.Controlador.login(window,email.get(), psw.get())
            ).pack(pady=20)
        tk.Button(window, text="Volver", command=Vista.menu_principal).pack(pady=5)
    
    @staticmethod
    def menu_notas(window, id, nombre, apellidos):
        Vista.limpiar(window)
        global id_user, nom_user, ape_user
        id_user = id
        nom_user = nombre
        ape_user = apellidos

        tk.Label(window, text=f".:: Bienvenido {nom_user} {ape_user} ::.", font=("Arial", 12, "bold"), fg="darkblue").pack(pady=10)
        
        tk.Button(window, text="1.- Crear Nota", width=30, command=lambda:Vista.nota_crear(window)).pack(pady=5)
        tk.Button(window, text="2.- Mostrar Notas", width=30, command=lambda:Vista.nota_mostrar(window)).pack(pady=5)
        tk.Button(window, text="3.- Cambiar Nota", width=30, command=lambda:Vista.nota_cambiar(window)).pack(pady=5)
        tk.Button(window, text="4.- Eliminar Nota", width=30, command=lambda:Vista.nota_eliminar(window)).pack(pady=5)
        tk.Button(window, text="5.- Cerrar Sesión", width=30, bg="red", fg="white", command=lambda:Vista.menu_principal(window)).pack(pady=20)
    
    @staticmethod
    def nota_crear(window):
        Vista.limpiar(window)
        titulo = tk.StringVar()
        descr = tk.StringVar()
        
        tk.Label(window, text=".:: Crear Nota ::.", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(window, text="Titulo:").pack()
        tk.Entry(window, textvariable=titulo).pack(pady=5)
        
        tk.Label(window, text="Descripcion:").pack()
        tk.Entry(window, textvariable=descr).pack(pady=5)
        
        tk.Button(window, text="Guardar", command=lambda: funciones.Controlador.crear_nota(id_user, titulo.get(),descr.get())).pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_notas(window,id_user, nom_user, ape_user)).pack(pady=5)
    
    @staticmethod
    def nota_mostrar(window):
        Vista.limpiar(window)
        
        tk.Label(window, text=f"Notas de {nom_user} {ape_user}:", font=("Arial", 14)).pack(pady=10)
        
        # Simulamos una lista de LISTAS (como vendría de la BD)
        registros = funciones.Controlador.mostrar_notas(id_user)
        
        texto_notas = ""
        for i, fila in enumerate(registros, 1):
            # fila[0]=ID, fila[2]=Titulo, fila[3]=Desc, fila[4]=Fecha
            texto_notas += f"Nota {i}:\nID: {fila[0]} .-Título: {fila[2]}. Fecha de Creacion: {fila[4]}\nDescripcion: {fila[3]}\n{'-'*30}\n"
        
        tk.Label(window, text=texto_notas, justify="center").pack(pady=10)
        
        tk.Button(window, text="Volver", command=lambda:Vista.menu_notas(window,id_user, nom_user, ape_user)).pack(pady=10)
    
    @staticmethod
    def nota_cambiar(window):
        Vista.limpiar(window)
        id_nota = tk.StringVar()
        titulo = tk.StringVar()
        descr = tk.StringVar()
        
        tk.Label(window, text=f"{nom_user} {ape_user}, vamos a modificar una Nota", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(window, text="ID de la nota a cambiar::").pack()
        tk.Entry(window, textvariable=id_nota).pack(pady=5)
        
        tk.Label(window, text="Nuevo Titulo:").pack()
        tk.Entry(window, textvariable=titulo).pack(pady=5)
        
        tk.Label(window, text="Nueva Descripcion:").pack()
        tk.Entry(window, textvariable=descr).pack(pady=5)
        
        tk.Button(window, text="Guardar", command=lambda:funciones.Controlador.actualizar_nota(id_nota.get(), titulo.get(), descr.get())).pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_notas(window,id_user, nom_user, ape_user)).pack(pady=5)
    
    @staticmethod
    def nota_eliminar(window):
        Vista.limpiar(window)
        id_nota = tk.StringVar()
        
        tk.Label(window, text=f"{nom_user} {ape_user}, camos a eliminar una Nota", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(window, text="ID de la Nota:").pack()
        tk.Entry(window, textvariable=id_nota).pack(pady=5)
        
        tk.Button(window, text="Eliminar", bg="red", fg="white", command=lambda:funciones.Controlador.eliminar_nota(id_nota.get())).pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_notas(window,id_user, nom_user, ape_user)).pack(pady=5)