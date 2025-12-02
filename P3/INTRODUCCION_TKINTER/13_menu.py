import tkinter as tk

def mensaje(tipo):
    resultado.config(
        text=f"{tipo}"
    )


window = tk.Tk()
window.geometry("500x500")
window.title("Menu")

menuBar = tk.Menu(window)
window.config(menu=menuBar)


archivoMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo", command=lambda:mensaje("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo", command=lambda:mensaje("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=window.quit)

edicionMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edicion", menu=edicionMenu)
edicionMenu.add_command(label="Copiar", command=lambda:mensaje("Copiar"))
edicionMenu.add_command(label="Guardar Archivo", command=lambda:mensaje("Guardar Archivo"))
edicionMenu.add_separator()
edicionMenu.add_command(label="Salir", command=window.destroy)

resultado = tk.Label(window, text="")
resultado.pack()



window.mainloop()