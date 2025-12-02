import tkinter as tk
from controller import funciones
from tkinter import ttk

class Vista:
    def __init__(self, window):
        window.title("Calculadora")
        window.geometry("1024x768")
        window.resizable(False, False)
        Vista.interfaz_principal(window)
    
    @staticmethod
    def borrarPantalla(window):
        for widget in window.winfo_children():
            if widget != window.nametowidget(window.cget("menu")):
                widget.destroy()
    
    @staticmethod
    def menuPrincipal(window):
        menubar = tk.Menu(window)
        window.config(menu=menubar)
        menu_operaciones = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operaciones", menu=menu_operaciones)
        menu_operaciones.add_command(label="Agregar", command=lambda:Vista.interfaz_principal(window))
        menu_operaciones.add_command(label="Consultar", command=lambda:Vista.interfazConsultar(window))
        menu_operaciones.add_command(label="Cambiar", command=lambda:Vista.consultarActualizar(window))
        menu_operaciones.add_command(label="Borrar", command=lambda:Vista.interfazBorrar(window))
        menu_operaciones.add_separator()
        menu_operaciones.add_command(label="Salir", command=window.quit)
    
    @staticmethod
    def interfaz_principal(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        frame_valores = tk.Frame(window, bg="skyblue")
        frame_valores.propagate(False)
        frame_valores.pack(pady=20)
        
        lbl_1 = tk.Label(frame_valores, text="Ingrese el primer numero:")
        lbl_1.grid(column=0, row=0, padx=10, pady=10)
        
        lbl_2 = tk.Label(frame_valores, text="Ingrese el segundo numero:")
        lbl_2.grid(column=0, row=1, padx=10, pady=10)
        
        num1 = tk.IntVar()
        num2 = tk.IntVar()
        
        entry_1 = tk.Entry(frame_valores, textvariable=num1, justify="right")
        entry_1.focus()
        entry_1.grid(column=1, row=0, padx=10, pady=10)
        
        entry_2 = tk.Entry(frame_valores, textvariable=num2, justify="right")
        entry_2.grid(column=1, row=1, padx=10, pady=10)
        
        frame_botones = tk.Frame(window, width=400, height=80, bg="red")
        frame_botones.propagate(False)
        frame_botones.pack(pady=20)
        
        btn_suma = tk.Button(frame_botones, text="SUMA", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "+"))
        btn_suma.grid(row=0, column=0, padx=[5,0])
        
        btn_resta = tk.Button(frame_botones, text="RESTA", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "-"))
        btn_resta.grid(row=0, column=1, padx=5)
        
        btn_div = tk.Button(frame_botones, text="DIVISION", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "/"))
        btn_div.grid(row=0, column=2, padx=5)
        
        btn_mult = tk.Button(frame_botones, text="MULTIPLICACION", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "x"))
        btn_mult.grid(row=0, column=3, padx=[0,5])
        
        btn_salir = tk.Button(window, text="Salir", command=window.quit)
        btn_salir.pack(pady=10)

    @staticmethod
    def interfazBorrar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        lbl_1 = tk.Label(window, text="Borrar una Operacion")
        lbl_1.pack()
        lbl_id = tk.Label(window, text="ID de la Operacion: ")
        lbl_id.pack()
        
        id = tk.IntVar()
        
        entry_1 = tk.Entry(window, textvariable=id, justify="right")
        entry_1.focus()
        entry_1.pack()
        
        btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:funciones.Funciones.borrar(id.get()))
        btn_eliminar.pack(pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=10)
    
    @staticmethod
    def interfazConsultar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        
        lbl_titulo = tk.Label(window, text=".::Listado de Operaciones::.", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)
        
        registros = funciones.Funciones.consultar()
        cadena=""
        contador=1
        for registro in registros:
            cadena+=f"Operacion {contador} ID: {registro[0]} Fecha de Creacion: {registro[1]}\nOperacion: {registro[2]} {registro[4]} {registro[3]} = {registro[5]}\n"
            contador+=1
        lbl_registros = tk.Label(window, text=cadena)
        lbl_registros.pack()
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultarActualizar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        lbltit=tk.Label(ventana,text=".::Cambiar una Operacion::.")
        lbltit.pack(pady=5)
        id=tk.IntVar()
        lblind=tk.Label(ventana,text="ID de la operacion ")
        lblind.pack(pady=5)
        caja0=tk.Entry(ventana,textvariable=id,width=5, justify="right")
        caja0.focus()
        caja0.pack(pady=5)
        
        
        
        btngua=tk.Button(ventana,text="Buscar",command=lambda:funciones.Funciones.consultar_id(ventana,id.get()))      
        btngua.pack(pady=5)
        btnvolv=tk.Button(ventana,text="Volver",command=lambda:Vista.interfaz_principal(ventana))
        btnvolv.pack(pady=10)
    
    @staticmethod
    def interfazAcualizar(ventana, registro):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        
        registro_id = registro[0]
        id_v = registro_id[0]
        num1_v = registro_id[2]
        num2_v = registro_id[3]
        simb_v = registro_id[4]
        res_v = registro_id[5]

        print(registro)
        lbltit=tk.Label(ventana,text="Cambiar una Operacion")
        lbltit.pack(pady=5)
        caja0=tk.Entry(ventana,width=5, justify="right")
        caja0.insert(0,id_v)
        caja0.config(state="readonly")
        caja0.pack(pady=5)

        lblnum1=tk.Label(ventana,text="Nuevo numero 1:")
        lblnum1.pack(pady=5)
        caja1=tk.Entry(ventana,width=6, justify="right")
        caja1.insert(0, num1_v)
        caja1.pack(pady=5)
        lblnum2=tk.Label(ventana,text="Nuevo numero 2:")
        lblnum2.pack(pady=5)
        caja2=tk.Entry(ventana,width=6, justify="right")
        caja2.insert(0, num2_v)
        caja2.pack(pady=5)
        lblsimb=tk.Label(ventana,text="Nuevo simbolo:")
        lblsimb.pack(pady=5)
        caja3=tk.Entry(ventana,width=4, justify="center")
        caja3.insert(0, simb_v)
        caja3.pack(pady=5)
        lblres=tk.Label(ventana,text="Nuevo resultado:")
        lblres.pack(pady=5)
        caja4=tk.Entry(ventana,width=6, justify="right")
        caja4.insert(0, res_v)
        caja4.pack(pady=10)

        btngua=tk.Button(ventana,text="Guardar",command=lambda:funciones.Funciones.actualizar(caja1.get(),caja2.get(),caja3.get(),caja4.get(),caja0.get()))      
        btngua.pack(pady=5)
        btnvolv=tk.Button(ventana,text="Volver",command=lambda:Vista.interfaz_principal(ventana))
        btnvolv.pack(pady=10)