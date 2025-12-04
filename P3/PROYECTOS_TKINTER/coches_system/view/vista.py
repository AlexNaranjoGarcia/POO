import tkinter as tk
from controller import controlador
class Vista:
    def __init__(self, window):
        window.geometry("800x800")
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
            
            btn_insertar = tk.Button(window, text="Insertar", command=lambda:Vista.insertar_camionetas(window))
            btn_insertar.pack(pady=10)
            
            btn_consultar = tk.Button(window, text="Consultar", command=lambda:Vista.consultar_camionetas(window))
            btn_consultar.pack(pady=10)
            
            btn_actualizar = tk.Button(window, text="Actualizar", command=lambda:Vista.buscar_camionetas(window, "cambiar"))
            btn_actualizar.pack(pady=10)
            
            btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:Vista.buscar_camionetas(window, "borrar"))
            btn_eliminar.pack(pady=10)
        elif tipo == "Camiones":
            lbl_titulo = tk.Label(window, text=f"Menu de {tipo}")
            lbl_titulo.pack(pady=10)
            
            btn_insertar = tk.Button(window, text="Insertar", command=lambda:Vista.insertar_camiones(window))
            btn_insertar.pack(pady=10)
            
            btn_consultar = tk.Button(window, text="Consultar", command=lambda:Vista.consultar_camiones(window))
            btn_consultar.pack(pady=10)
            
            btn_actualizar = tk.Button(window, text="Actualizar", command=lambda:Vista.buscar_camiones(window, "cambiar"))
            btn_actualizar.pack(pady=10)
            
            btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:Vista.buscar_camiones(window, "borrar"))
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
        
        btn_guardar = tk.Button(window, text="Guardar", command=lambda:controlador.Funciones.insertar_autos(marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get()))
        btn_guardar.pack(pady=20)

        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def consultar_autos(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Registros de Autos")
        lbl_titulo.pack(pady=10)
        
        registros = controlador.Funciones.consultar_autos()
        
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
            tk.Button(window, text="Buscar", command=lambda:controlador.Funciones.get_id_auto(window, id.get(), "cambiar")).pack()
        elif tipo =="borrar":
            tk.Button(window, text="Buscar", command=lambda:controlador.Funciones.get_id_auto(window, id.get(), "borrar")).pack()
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
        
    @staticmethod
    def cambiar_auto(window, registro):
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
        id.set(registro[0])
        txt_id.pack(pady=5)
        
        lbl_marca = tk.Label(window, text="Marca:").pack(pady=8)
        txt_marca = tk.Entry(window, textvariable=marca)
        txt_marca.focus()
        marca.set(registro[1])
        txt_marca.pack(pady=4)
        
        lbl_color = tk.Label(window, text="Color:").pack(pady=8)
        txt_color = tk.Entry(window, textvariable=color).pack(pady=4)
        color.set(registro[2])
        
        lbl_modelo = tk.Label(window, text="Modelo:").pack(pady=8)
        txt_modelo = tk.Entry(window, textvariable=modelo).pack(pady=4)
        modelo.set(registro[3])
        
        lbl_velocidad = tk.Label(window, text="Velocidad:").pack(pady=8)
        txt_velocidad = tk.Entry(window, textvariable=velocidad).pack(pady=4)
        velocidad.set(registro[4])
        
        lbl_caballaje = tk.Label(window, text="Caballaje:").pack(pady=8)
        txt_caballaje = tk.Entry(window, textvariable=caballaje).pack(pady=4)
        caballaje.set(registro[5])
        
        lbl_plazas = tk.Label(window, text="Plazas:").pack(pady=8)
        txt_plazas = tk.Entry(window, textvariable=plazas).pack(pady=4)
        plazas.set(registro[6])
        
        tk.Button(window, text="Guardar", command=lambda:controlador.Funciones.cambiar_auto(marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), id.get())).pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)
    
    @staticmethod
    def eliminar_auto(window, registro):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        
        tk.Label(window, text=f"Eliminar Auto", font=("Arial", 14)).pack(pady=10)
        txt_id = tk.Entry(window, textvariable=id, justify="right", state="readonly")
        id.set(registro[0])
        txt_id.pack(pady=5)
        
        
        tk.Button(window, text="Eliminar", command=lambda:controlador.Funciones.eliminar_auto(id.get())).pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)
    
    @staticmethod
    def insertar_camionetas(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Datos de la Camioneta")
        lbl_titulo.pack(pady=10)
        #Variables
        marca = tk.StringVar()
        color = tk.StringVar()
        modelo = tk.StringVar()
        velocidad = tk.StringVar()
        caballaje = tk.StringVar()
        plazas = tk.StringVar()
        traccion = tk.StringVar()
        cerrada = tk.StringVar()
        
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
        
        lbl_traccion = tk.Label(window, text="Traccion:").pack(pady=8)
        txt_traccion = tk.Entry(window, textvariable=traccion).pack(pady=4)
        
        lbl_cerrada = tk.Label(window, text="Cerrada:").pack(pady=8)
        txt_cerrada = tk.Entry(window, textvariable=cerrada).pack(pady=4)
        
        btn_guardar = tk.Button(window, text="Guardar", command=lambda:"")
        btn_guardar.pack(pady=20)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def consultar_camionetas(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Registros de Camionetas")
        lbl_titulo.pack(pady=10)
        
        registros = [(1, "BMW", "Rojo", "2020", "150", "200", "4", "Trasera", "1")]
        
        texto_notas = ""
        for i, fila in enumerate(registros, 1):
            if fila[8] == "1":
                cerrada = True
            else:
                cerrada = False
            texto_notas += f"Camioneta #{i}:\nID: {fila[0]} Marca: {fila[1]}. Color: {fila[2]}.\nModelo: {fila[3]}. Velocidad: {fila[4]}\nCaballaje: {fila[5]}. Plazas: {fila[6]}\nTraccion: {fila[7]}. Cerrada: {cerrada}\n{'-'*30}\n"
        
        lbl_registros = tk.Label(window, text=texto_notas, justify="center").pack(pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def buscar_camionetas(window, tipo):
        Vista.borrar_pantalla(window)
        id = tk.IntVar()
        
        lbl_titulo = tk.Label(window, text=f"Buscar una Camioneta")
        lbl_titulo.pack(pady=10)
        
        lbl_id = tk.Label(window, text="ID de la Camioneta a buscar:").pack(pady=5)
        txt_id = tk.Entry(window, textvariable=id, justify="right", width=5)
        txt_id.focus()
        txt_id.pack(pady=5)
        
        if tipo == "cambiar":
            tk.Button(window, text="Buscar", command=lambda:Vista.cambiar_camionetas(window, id.get())).pack()
        elif tipo =="borrar":
            tk.Button(window, text="Buscar", command=lambda:Vista.eliminar_camionetas(window, id.get())).pack()
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def cambiar_camionetas(window, id_consultado):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        marca = tk.StringVar()
        color = tk.StringVar()
        modelo = tk.StringVar()
        velocidad = tk.StringVar()
        caballaje = tk.StringVar()
        plazas = tk.StringVar()
        traccion = tk.StringVar()
        cerrada = tk.StringVar()
        
        tk.Label(window, text=f"Actualizar Camionetas", font=("Arial", 14)).pack(pady=10)
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
        
        lbl_traccion = tk.Label(window, text="Traccion:").pack(pady=8)
        txt_traccion = tk.Entry(window, textvariable=traccion).pack(pady=4)
        
        lbl_cerrada = tk.Label(window, text="Cerrada:").pack(pady=8)
        txt_cerrada = tk.Entry(window, textvariable=cerrada).pack(pady=4)
        
        tk.Button(window, text="Guardar", command=lambda:"").pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)
    
    @staticmethod
    def eliminar_camionetas(window, id_consultado):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        
        tk.Label(window, text=f"Eliminar Camionetas", font=("Arial", 14)).pack(pady=10)
        txt_id = tk.Entry(window, textvariable=id, justify="right", state="readonly")
        id.set(id_consultado)
        txt_id.pack(pady=5)
        
        
        tk.Button(window, text="Eliminar", command=lambda:"").pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)
    
    @staticmethod
    def insertar_camiones(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Datos del Camion")
        lbl_titulo.pack(pady=10)
        #Variables
        marca = tk.StringVar()
        color = tk.StringVar()
        modelo = tk.StringVar()
        velocidad = tk.StringVar()
        caballaje = tk.StringVar()
        plazas = tk.StringVar()
        eje = tk.StringVar()
        capacidad = tk.StringVar()
        
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
        
        lbl_eje = tk.Label(window, text="Eje:").pack(pady=8)
        txt_eje = tk.Entry(window, textvariable=eje).pack(pady=4)
        
        lbl_capacidad = tk.Label(window, text="Capacidad:").pack(pady=8)
        txt_capacidad = tk.Entry(window, textvariable=capacidad).pack(pady=4)
        
        btn_guardar = tk.Button(window, text="Guardar", command=lambda:"")
        btn_guardar.pack(pady=20)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def consultar_camiones(window):
        Vista.borrar_pantalla(window)
        lbl_titulo = tk.Label(window, text=f"Registros de Camiones")
        lbl_titulo.pack(pady=10)
        
        registros = [(1, "BMW", "Rojo", "2020", "150", "200", "4", "8", "1500")]
        
        texto_notas = ""
        for i, fila in enumerate(registros, 1):
            texto_notas += f"Camion #{i}:\nID: {fila[0]} Marca: {fila[1]}. Color: {fila[2]}.\nModelo: {fila[3]}. Velocidad: {fila[4]}\nCaballaje: {fila[5]}. Plazas: {fila[6]}\nEjes: {fila[7]}. Capacidad: {fila[8]}\n{'-'*30}\n"
        
        lbl_registros = tk.Label(window, text=texto_notas, justify="center").pack(pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
    
    @staticmethod
    def buscar_camiones(window, tipo):
        Vista.borrar_pantalla(window)
        id = tk.IntVar()
        
        lbl_titulo = tk.Label(window, text=f"Buscar un Camion")
        lbl_titulo.pack(pady=10)
        
        lbl_id = tk.Label(window, text="ID del Camion a buscar:").pack(pady=5)
        txt_id = tk.Entry(window, textvariable=id, justify="right", width=5)
        txt_id.focus()
        txt_id.pack(pady=5)
        
        if tipo == "cambiar":
            tk.Button(window, text="Buscar", command=lambda:Vista.cambiar_camiones(window, id.get())).pack()
        elif tipo =="borrar":
            tk.Button(window, text="Buscar", command=lambda:Vista.eliminar_camiones(window, id.get())).pack()
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo))
        btn_volver.pack(pady=20)
        
    @staticmethod
    def cambiar_camiones(window, id_consultado):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        marca = tk.StringVar()
        color = tk.StringVar()
        modelo = tk.StringVar()
        velocidad = tk.StringVar()
        caballaje = tk.StringVar()
        plazas = tk.StringVar()
        eje = tk.StringVar()
        capacidad = tk.StringVar()
        
        tk.Label(window, text=f"Actualizar Camion", font=("Arial", 14)).pack(pady=10)
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
        
        lbl_eje = tk.Label(window, text="Eje:").pack(pady=8)
        txt_eje = tk.Entry(window, textvariable=eje).pack(pady=4)
        
        lbl_capacidad = tk.Label(window, text="Capacidad:").pack(pady=8)
        txt_capacidad = tk.Entry(window, textvariable=capacidad).pack(pady=4)
        
        tk.Button(window, text="Guardar", command=lambda:"").pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)
    
    @staticmethod
    def eliminar_camiones(window, id_consultado):
        Vista.borrar_pantalla(window)
        #Variables
        id = tk.IntVar()
        
        tk.Label(window, text=f"Eliminar Camion", font=("Arial", 14)).pack(pady=10)
        txt_id = tk.Entry(window, textvariable=id, justify="right", state="readonly")
        id.set(id_consultado)
        txt_id.pack(pady=5)
        
        
        tk.Button(window, text="Eliminar", command=lambda:"").pack(pady=20)
        tk.Button(window, text="Volver", command=lambda:Vista.menu_acciones(window, global_tipo)).pack(pady=5)

