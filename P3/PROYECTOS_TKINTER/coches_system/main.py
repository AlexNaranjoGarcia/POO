'''
1ER Diciembre
    1) Implementacion de MVC
    2)Paradigma de POO
    3) Interfaces:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
Productos Entregables:
    *Estructura del proyecto basado en MVC
    *Modulo principal "main"
    *Interaccion con las interfaces
**Nombre del commit: "commit_01_12_25"
'''
import tkinter as tk
from view import vista

class App:
    def __init__(self, window):
        view = vista.Vista(window)

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()