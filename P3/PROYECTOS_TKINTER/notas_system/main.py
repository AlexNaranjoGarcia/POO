"""
    1.- Implementacion MVC
    2.- Paradigma POO
    3.- App de escritorio con interfaz grafica
"""
import tkinter as tk
from view import view1

class App:
    def __init__(self, window):
        view = view1.Vista(window)

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()