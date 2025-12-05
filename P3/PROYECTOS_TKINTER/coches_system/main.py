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

2 Diciembre
    1)Interfaces:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()
    
    Productos Entregables:
    **Interaccion con todas las interfaces
    **Nombre del Commit: "commit_02_12_25"

3 Diciembre
    1) Controlador:
        1.1 menu_principal()
        1.2 menu_acciones()
        1.3 insertar_autos()
        1.4 consultar_autos()
        1.5 cambiar_autos()
        1.6 borrar_autos()
    
    Productos Entregables:
    **Interaccion con la funcionalidad (controlador) de las interfaces anteriores
    ** Nombre del Commit: "commit_03_12_25"

4 Diciembre
    1) Controlador:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas
    Productos Entregables:
    **Interaccion con la funcionalidad (controlador) de las interfaces anteriores
    ** Nombre del Commit: "commit_04_12_25"
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