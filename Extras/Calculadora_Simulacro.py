from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class CalculadoraApp:
    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Gestor de Operaciones Matemáticas")
        self.ventana.geometry("600x500")
        self.ventana.resizable(False, False)

        self.historial = [] 
        self.contador_id = 1

        self.frame_menu = Frame(self.ventana, bg="#ddd", height=50)
        self.frame_menu.pack(side="top", fill="x")

        self.frame_contenido = Frame(self.ventana)
        self.frame_contenido.pack(side="top", fill="both", expand=True, pady=10)

        self.crear_menu_navegacion()
        self.mostrar_calcular()

    def crear_menu_navegacion(self):
        btn_calc = Button(self.frame_menu, text="Calcular", command=self.mostrar_calcular)
        btn_calc.pack(side="left", padx=10, pady=10)

        btn_ver = Button(self.frame_menu, text="Ver Operaciones", command=self.mostrar_ver)
        btn_ver.pack(side="left", padx=10, pady=10)

        btn_cambiar = Button(self.frame_menu, text="Cambiar Operación", command=self.mostrar_cambiar_paso1)
        btn_cambiar.pack(side="left", padx=10, pady=10)

        btn_borrar = Button(self.frame_menu, text="Borrar Operación", command=self.mostrar_borrar)
        btn_borrar.pack(side="left", padx=10, pady=10)

        btn_salir = Button(self.frame_menu, text="Salir", command=self.ventana.quit, bg="#ffcccc")
        btn_salir.pack(side="right", padx=10, pady=10)

    def limpiar_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()


    def mostrar_calcular(self):
        self.limpiar_contenido()
        
        Label(self.frame_contenido, text="Nueva Operación", font=("Arial", 14, "bold")).pack(pady=10)

        n1 = StringVar()
        n2 = StringVar()
        signo_var = StringVar()

        Label(self.frame_contenido, text="Número 1:").pack()
        Entry(self.frame_contenido, textvariable=n1, justify="center").pack(pady=5)

        Label(self.frame_contenido, text="Signo (+, -, x, /):").pack()
        Entry(self.frame_contenido, textvariable=signo_var, justify="center", width=5).pack(pady=5)

        Label(self.frame_contenido, text="Número 2:").pack()
        Entry(self.frame_contenido, textvariable=n2, justify="center").pack(pady=5)

        def procesar():
            try:
                val1 = float(n1.get())
                val2 = float(n2.get())
                signo = signo_var.get()
                result = 0
                
                if signo not in ["+", "-", "x", "/"]:
                    messagebox.showerror("Error", "Signo inválido. Use +, -, x o /")
                    return

                if signo == "+": result = val1 + val2
                elif signo == "-": result = val1 - val2
                elif signo == "x": result = val1 * val2
                elif signo == "/": 
                    if val2 == 0:
                        messagebox.showerror("Error", "No se puede dividir por cero")
                        return
                    result = val1 / val2

                # Guardar
                nueva_op = {
                    'id': self.contador_id,
                    'n1': val1,
                    'n2': val2,
                    'signo': signo,
                    'res': result
                }
                self.historial.append(nueva_op)
                messagebox.showinfo("Resultado", f"ID: {self.contador_id}\n{val1} {signo} {val2} = {result}\n\n¡Guardado!")
                self.contador_id += 1
                
                n1.set("")
                n2.set("")
                signo_var.set("")

            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese números válidos")


        Button(self.frame_contenido, text="Calcular y Guardar", command=procesar, bg="#ccffcc", height=2, width=20).pack(pady=20)

    def mostrar_ver(self):
        self.limpiar_contenido()
        Label(self.frame_contenido, text="Historial de Operaciones", font=("Arial", 14, "bold")).pack(pady=10)

        columnas = ("id", "n1", "signo", "n2", "igual", "res")
        tabla = ttk.Treeview(self.frame_contenido, columns=columnas, show="headings", height=15)
        
        tabla.heading("id", text="ID"); tabla.column("id", width=50, anchor="center")
        tabla.heading("n1", text="Num 1"); tabla.column("n1", width=80, anchor="center")
        tabla.heading("signo", text="Op"); tabla.column("signo", width=50, anchor="center")
        tabla.heading("n2", text="Num 2"); tabla.column("n2", width=80, anchor="center")
        tabla.heading("igual", text="="); tabla.column("igual", width=30, anchor="center")
        tabla.heading("res", text="Resultado"); tabla.column("res", width=100, anchor="center")

        tabla.pack(pady=10, padx=20)

        for op in self.historial:
            tabla.insert("", "end", values=(op['id'], op['n1'], op['signo'], op['n2'], "=", op['res']))


    def mostrar_cambiar_paso1(self):
        self.limpiar_contenido()
        Label(self.frame_contenido, text="Modificar Operación - Paso 1", font=("Arial", 14, "bold")).pack(pady=10)

        Label(self.frame_contenido, text="Ingrese el ID de la operación a cambiar:").pack(pady=5)
        id_var = IntVar(value=0)
        Entry(self.frame_contenido, textvariable=id_var).pack(pady=5)

        def buscar_y_avanzar():
            id_buscado = id_var.get()
            operacion_encontrada = None
            for op in self.historial:
                if op['id'] == id_buscado:
                    operacion_encontrada = op
                    break
            
            if operacion_encontrada:
                self.mostrar_cambiar_paso2(operacion_encontrada)
            else:
                messagebox.showerror("Error", f"No se encontró ninguna operación con ID {id_buscado}")

        Button(self.frame_contenido, text="Buscar ID", command=buscar_y_avanzar).pack(pady=10)

    def mostrar_cambiar_paso2(self, op_data):
        """Paso 2: Mostrar datos. El ID se muestra pero NO se puede editar."""
        self.limpiar_contenido()
        Label(self.frame_contenido, text="Modificar Operación - Paso 2", font=("Arial", 14, "bold")).pack(pady=10)


        var_id = StringVar(value=str(op_data['id']))
        nuevo_n1 = StringVar(value=op_data['n1'])
        nuevo_n2 = StringVar(value=op_data['n2'])
        nuevo_signo = StringVar(value=op_data['signo'])

        Label(self.frame_contenido, text="ID (No editable):").pack()
        Entry(self.frame_contenido, textvariable=var_id, state='readonly', justify='center').pack(pady=5)


        Label(self.frame_contenido, text="Primer Número:").pack()
        Entry(self.frame_contenido, textvariable=nuevo_n1).pack(pady=5)

        Label(self.frame_contenido, text="Signo (+, -, *, /):").pack()
        Entry(self.frame_contenido, textvariable=nuevo_signo).pack(pady=5)
        
        Label(self.frame_contenido, text="Segundo Número:").pack()
        Entry(self.frame_contenido, textvariable=nuevo_n2).pack(pady=5)

        def guardar_cambios():
            try:
                v1 = float(nuevo_n1.get())
                v2 = float(nuevo_n2.get())
                s = nuevo_signo.get()

                if s not in ["+", "-", "*", "/"]:
                    messagebox.showerror("Error", "Signo inválido. Use +, -, * o /")
                    return

                res = 0
                if s == "+": res = v1 + v2
                elif s == "-": res = v1 - v2
                elif s == "*": res = v1 * v2
                elif s == "/": 
                    if v2 == 0:
                        messagebox.showerror("Error", "División por cero")
                        return
                    res = v1 / v2

                op_data['n1'] = v1
                op_data['n2'] = v2
                op_data['signo'] = s
                op_data['res'] = res

                messagebox.showinfo("Éxito", "Operación actualizada correctamente")
                self.mostrar_ver()

            except ValueError:
                messagebox.showerror("Error", "Los números no son válidos")

        Button(self.frame_contenido, text="Guardar Cambios", command=guardar_cambios, bg="#ccffcc").pack(pady=20)
        Button(self.frame_contenido, text="Cancelar", command=self.mostrar_cambiar_paso1).pack()


    def mostrar_borrar(self):
        self.limpiar_contenido()
        Label(self.frame_contenido, text="Borrar Operación", font=("Arial", 14, "bold")).pack(pady=10)

        Label(self.frame_contenido, text="Ingrese el ID a borrar:").pack(pady=5)
        id_borrar = IntVar(value=0)
        Entry(self.frame_contenido, textvariable=id_borrar).pack(pady=5)

        def ejecutar_borrado():
            id_b = id_borrar.get()
            encontrado = False
            for i, op in enumerate(self.historial):
                if op['id'] == id_b:
                    del self.historial[i]
                    encontrado = True
                    break
            
            if encontrado:
                messagebox.showinfo("Borrado", f"La operación ID {id_b} ha sido eliminada.")
                self.mostrar_ver()
            else:
                messagebox.showerror("Error", "ID no encontrado")

        Button(self.frame_contenido, text="Borrar Definitivamente", command=ejecutar_borrado, bg="#ffaaaa").pack(pady=10)

if __name__ == "__main__":
    ventana = Tk()
    app = CalculadoraApp(ventana)
    ventana.mainloop()