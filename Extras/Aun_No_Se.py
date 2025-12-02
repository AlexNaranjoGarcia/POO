import tkinter as tk
from tkinter import messagebox

class AplicacionCalculadora(tk.Tk):
    
    def __init__(self):
        """
        Constructor de la clase. Se llama al crear una nueva instancia.
        Aquí configuramos la ventana y creamos los widgets.
        """
        
        super().__init__()
        
        self.title("Mi Aplicación POO") 
        self.geometry("600x450")      
        self.resizable(False, False)  
        
        self.crear_menu()
        self.crear_calculadora()

    def crear_menu(self):
        """
        Crea la barra de menú superior con las opciones "Operaciones".
        """
        
        # 1. Crear la barra de menú principal
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu) # Asignamos la barra a la ventana

        # 2. Crear el menú desplegable "Operaciones" (como en la imagen)
        # tearoff=0 quita una línea punteada que aparece por defecto
        menu_operaciones = tk.Menu(barra_menu, tearoff=0)
        
        # 3. Añadir el menú "Operaciones" a la barra principal
        barra_menu.add_cascade(label="Operaciones", menu=menu_operaciones)

        # 4. Añadir los comandos (items) al menú "Operaciones"
        # Cada comando llama a un método (función dentro de la clase)
        menu_operaciones.add_command(label="Agregar", command=self.funcion_placeholder)
        menu_operaciones.add_command(label="Consultar", command=self.funcion_placeholder)
        menu_operaciones.add_command(label="Cambiar", command=self.funcion_placeholder)
        menu_operaciones.add_command(label="Borrar", command=self.funcion_placeholder)
        menu_operaciones.add_separator() # Una línea divisoria
        menu_operaciones.add_command(label="Salir", command=self.salir)

    def crear_calculadora(self):
        """
        Crea el widget de la calculadora básica en la ventana principal.
        """
        
        # Usamos un Frame para agrupar todos los widgets de la calculadora
        frame_principal = tk.Frame(self, pady=15)
        frame_principal.pack(expand=True, fill=tk.BOTH)

        # Título "Calculadora Básica"
        label_titulo = tk.Label(frame_principal, text="Calculadora Básica", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=10)

        # Campo de entrada (Entry) donde el usuario escribe
        # Guardamos la referencia en 'self.entry_numero' para poder acceder a él
        # desde otros métodos (ej. realizar_operacion)
        self.entry_numero = tk.Entry(frame_principal, font=("Arial", 14), justify="right")
        self.entry_numero.pack(pady=5, padx=25, fill=tk.X)
        self.entry_numero.insert(0, "0") # Valor inicial como en la imagen

        # Etiqueta para mostrar el resultado (el "0" de abajo)
        # También la guardamos en 'self.label_resultado' para poder modificarla
        self.label_resultado = tk.Label(frame_principal, text="0", font=("Arial", 14, "bold"),
                                          relief="sunken", borderwidth=2, anchor="e", padx=10)
        self.label_resultado.pack(pady=10, padx=25, fill=tk.X, ipady=5)

        # Frame para agrupar los botones de operaciones
        frame_botones = tk.Frame(frame_principal)
        frame_botones.pack(pady=5)

        # --- Botones de operación ---
        # Usamos 'lambda' para poder pasar un argumento (el símbolo de la operación)
        # a nuestro método 'realizar_operacion' cuando se presiona el botón.
        
        btn_sumar = tk.Button(frame_botones, text="+", width=5, font=("Arial", 12),
                              command=lambda: self.realizar_operacion("+"))
        btn_sumar.pack(pady=3, fill=tk.X)

        btn_restar = tk.Button(frame_botones, text="-", width=5, font=("Arial", 12),
                               command=lambda: self.realizar_operacion("-"))
        btn_restar.pack(pady=3, fill=tk.X)

        btn_multi = tk.Button(frame_botones, text="x", width=5, font=("Arial", 12),
                              command=lambda: self.realizar_operacion("*"))
        btn_multi.pack(pady=3, fill=tk.X)

        btn_dividir = tk.Button(frame_botones, text="/", width=5, font=("Arial", 12),
                                command=lambda: self.realizar_operacion("/"))
        btn_dividir.pack(pady=3, fill=tk.X)

        # Botón de Salir (el de abajo)
        btn_salir_inferior = tk.Button(frame_principal, text="Salir", command=self.salir)
        btn_salir_inferior.pack(pady=20)

    def realizar_operacion(self, operacion):
        """
        Se llama al presionar un botón de operación (+, -, x, /).
        Toma el número del entry, lo opera con el resultado actual y actualiza.
        """
        try:
            # 1. Obtener el número ingresado por el usuario (del Entry)
            numero_ingresado = float(self.entry_numero.get())
            
            # 2. Obtener el total actual (guardado en el Label)
            total_actual = float(self.label_resultado["text"])

            # 3. Realizar la operación correspondiente
            nuevo_total = 0
            if operacion == "+":
                nuevo_total = total_actual + numero_ingresado
            elif operacion == "-":
                nuevo_total = total_actual - numero_ingresado
            elif operacion == "*": # La imagen dice 'x' pero la operación es '*'
                nuevo_total = total_actual * numero_ingresado
            elif operacion == "/":
                if numero_ingresado == 0:
                    # Validación de división por cero
                    messagebox.showerror("Error", "No se puede dividir por cero.")
                    return # Detenemos la ejecución aquí
                nuevo_total = total_actual / numero_ingresado

            # 4. Actualizar la etiqueta de resultado
            # Formateamos para que muestre un entero si no tiene decimales
            if nuevo_total == int(nuevo_total):
                self.label_resultado.config(text=str(int(nuevo_total)))
            else:
                self.label_resultado.config(text=f"{nuevo_total:.4f}") # Mostrar máx. 4 decimales

            # 5. Resetear el campo de entrada a "0"
            self.entry_numero.delete(0, tk.END)
            self.entry_numero.insert(0, "0")

        except ValueError:
            # Manejo de error si el usuario no ingresa un número válido
            messagebox.showerror("Error", "Entrada inválida. Por favor, ingrese un número.")
            self.entry_numero.delete(0, tk.END)
            self.entry_numero.insert(0, "0")

    def funcion_placeholder(self):
        """
        Función temporal para los botones del menú que no están implementados.
        Muestra un simple mensaje informativo.
        """
        messagebox.showinfo("Información", "Esta función (Agregar, Consultar, etc.) no está implementada en este ejemplo.")

    def salir(self):
        """
        Cierra la aplicación.
        Es llamado tanto por el menú "Salir" como por el botón "Salir".
        """
        self.destroy()

if __name__ == "__main__":
    # 1. Creamos una instancia de nuestra clase de aplicación
    app = AplicacionCalculadora()
    
    # 2. Iniciamos el bucle principal de eventos de tkinter (mainloop)
    # Esto mantiene la ventana abierta y esperando interacciones del usuario.
    app.mainloop()

En este punto no  se que chingados poner ya que nmms estoy probando el git y no se que mas poner aqui son puras mafufadas para llenar el archivo y probar el git lol