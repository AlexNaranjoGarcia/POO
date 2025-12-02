import tkinter as tk
class Vista:
    def __init__(self, window):
        window.geometry("800x600")
        window.title("Coches")
        Vista.menu_principal(window)
    
    @staticmethod
    def borrar_pantalla(window):
        for widget in window.winfo_children():
            widget.destroy()
    @staticmethod
    def menu_principal(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text="Menu Principal")
        lbl_titulo.pack(pady=10)
        
        btn_coche = tk.Button(window, text="Coches", command=lambda:Vista.menu_acciones(window, "Coches"))
        btn_coche.pack(pady=10)
        
        btn_camionetas = tk.Button(window, text="Camionetas", command=lambda:Vista.menu_acciones(window, "Camionetas"))
        btn_camionetas.pack(pady=10)
        
        btn_camiones = tk.Button(window, text="Camiones", command=lambda:Vista.menu_acciones(window, "Camiones"))
        btn_camiones.pack(pady=10)
        
        btn_salir = tk.Button(window, text="Salir", command=window.quit)
        btn_salir.pack(pady=20)
    
    @staticmethod
    def menu_acciones(window, tipo):
        Vista.borrar_pantalla(window)
        global global_tipo
        global_tipo = tipo
        if tipo == "Coches":
            lbl_titulo = tk.Label(window, text=f"Menu de {tipo}")
            lbl_titulo.pack(pady=10)
            
            btn_insertar = tk.Button(window, text="Insertar", command=lambda:Vista.insertar_autos(window))
            btn_insertar.pack(pady=10)
            
            btn_consultar = tk.Button(window, text="Consultar", command=lambda:Vista.consultar_autos(window))
            btn_consultar.pack(pady=10)
            
            btn_actualizar = tk.Button(window, text="Actualizar", command=lambda:Vista.buscar_auto(window, "cambiar"))
            btn_actualizar.pack(pady=10)
            
            btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:Vista.buscar_auto(window, "borrar"))
            btn_eliminar.pack(pady=10)
        elif tipo == "Camionetas":
            lbl_titulo = tk.Label(window, text=f"Menu de {tipo}")
            lbl_titulo.pack(pady=10)
            
            btn_insertar = tk.Button(window, text="Insertar", command=lambda:Vista.insertar_autos(window))
            btn_insertar.pack(pady=10)
            
            btn_consultar = tk.Button(window, text="Consultar", command=lambda:Vista.consultar_autos(window))
            btn_consultar.pack(pady=10)
            
            btn_actualizar = tk.Button(window, text="Actualizar", command=lambda:Vista.buscar_auto(window, "cambiar"))
            btn_actualizar.pack(pady=10)
            
            btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:Vista.buscar_auto(window, "borrar"))
            btn_eliminar.pack(pady=10)
        elif tipo == "Camiones":
            lbl_titulo = tk.Label(window, text=f"Menu de {tipo}")
            lbl_titulo.pack(pady=10)
            
            btn_insertar = tk.Button(window, text="Insertar", command=lambda:Vista.insertar_autos(window))
            btn_insertar.pack(pady=10)
            
            btn_consultar = tk.Button(window, text="Consultar", command=lambda:Vista.consultar_autos(window))
            btn_consultar.pack(pady=10)
            
            btn_actualizar = tk.Button(window, text="Actualizar", command=lambda:Vista.buscar_auto(window, "cambiar"))
            btn_actualizar.pack(pady=10)
            
            btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:Vista.buscar_auto(window, "borrar"))
            btn_eliminar.pack(pady=10)
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_principal(window))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def insertar_autos(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Datos del Auto")
        lbl_titulo.pack(pady=10)
        #Variables
        marca = tk.StringVar()
        color = tk.StringVar()
        modelo = tk.StringVar()
        velocidad = tk.StringVar()
        caballaje = tk.StringVar()
        plazas = tk.StringVar()
        
        lbl_marca = tk.Label(window, text="Marca:").pack(pady=8)
        txt_marca = tk.Entry(window, textvariable=marca).pack(pady=4)
        
        lbl_color = tk.Label(window, text="Color:").pack(pady=8)
        txt_color = tk.Entry(window, textvariable=color).pack(pady=4)
        
        lbl_modelo = tk.Label(window, text="Modelo:").pack(pady=8)
        txt_modelo = tk.Entry(window, textvariable=modelo).pack(pady=4)
        
        lbl_velocidad = tk.Label(window, text="Velocidad:").pack(pady=8)
        txt_velocidad = tk.Entry(window, textvariable=velocidad).pack(pady=4)
        
        lbl_caballaje = tk.Label(window, text="Caballaje:").pack(pady=8)
        txt_caballaje = tk.Entry(window, textvariable=caballaje).pack(pady=4)
        
        lbl_plazas = tk.Label(window, text="Plazas:").pack(pady=8)
        txt_plazas = tk.Entry(window, textvariable=plazas).pack(pady=4)
        
        btn_guardar = tk.Button(window, text="Guardar", command=lambda:"")
        btn_guardar.pack(pady=20)

        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def consultar_autos(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Registros de Autos")
        lbl_titulo.pack(pady=10)
        
        registros = "funciones"
        
        texto_notas = ""
        for i, fila in enumerate(registros, 1):
            texto_notas += f"Auto #{i}:\nID: {fila[0]} Marca: {fila[1]}. Color: {fila[2]}.\nModelo: {fila[3]}. Velocidad: {fila[4]}\nCaballaje: {fila[5]}. Plazas: {fila[6]}\n{'-'*30}\n"
        
        lbl_registros = tk.Label(window, text=texto_notas, justify="center").pack(pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def buscar_auto(window, tipo):
        Vista.borrar_pantalla(window)
        id = tk.IntVar()
        
        lbl_titulo = tk.Label(window, text=f"Buscar una Operacion")
        lbl_titulo.pack(pady=10)
        
        lbl_id = tk.Label(window, text="ID de la operacion a buscar:").pack(pady=5)
        txt_id = tk.Entry(window, textvariable=id, justify="right", width=5)
        txt_id.focus()
        txt_id.pack(pady=5)
        
        if tipo == "cambiar":
            tk.Button(window, text="Buscar", command=lambda:Vista.cambiar_auto(window, id.get())).pack()
        elif tipo =="borrar":
            tk.Button(window, text="Buscar", command=lambda:Vista.eliminar_auto(window, id.get())).pack()
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
        
    @staticmethod
    def cambiar_auto(window, id_consultado):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        marca = tk.StringVar()
        color = tk.StringVar()
        modelo = tk.StringVar()
        velocidad = tk.StringVar()
        caballaje = tk.StringVar()
        plazas = tk.StringVar()
        
        tk.Label(window, text=f"Actualizar Auto", font=("Arial", 14)).pack(pady=10)
        txt_id = tk.Entry(window, textvariable=id, justify="right", state="readonly")
        id.set(id_consultado)
        txt_id.pack(pady=5)
        
        lbl_marca = tk.Label(window, text="Marca:").pack(pady=8)
        txt_marca = tk.Entry(window, textvariable=marca)
        txt_marca.focus()
        txt_marca.pack(pady=4)
        
        lbl_color = tk.Label(window, text="Color:").pack(pady=8)
        txt_color = tk.Entry(window, textvariable=color).pack(pady=4)
        
        lbl_modelo = tk.Label(window, text="Modelo:").pack(pady=8)
        txt_modelo = tk.Entry(window, textvariable=modelo).pack(pady=4)
        
        lbl_velocidad = tk.Label(window, text="Velocidad:").pack(pady=8)
        txt_velocidad = tk.Entry(window, textvariable=velocidad).pack(pady=4)
        
        lbl_caballaje = tk.Label(window, text="Caballaje:").pack(pady=8)
        txt_caballaje = tk.Entry(window, textvariable=caballaje).pack(pady=4)
        
        lbl_plazas = tk.Label(window, text="Plazas:").pack(pady=8)
        txt_plazas = tk.Entry(window, textvariable=plazas).pack(pady=4)
        
        tk.Button(window, text="Guardar", command=lambda:"").pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)
    
    @staticmethod
    def eliminar_auto(window, id_consultado):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        
        tk.Label(window, text=f"Eliminar Auto", font=("Arial", 14)).pack(pady=10)
        txt_id = tk.Entry(window, textvariable=id, justify="right", state="readonly")
        id.set(id_consultado)
        txt_id.pack(pady=5)
        
        
        tk.Button(window, text="Eliminar", command=lambda:"").pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)

