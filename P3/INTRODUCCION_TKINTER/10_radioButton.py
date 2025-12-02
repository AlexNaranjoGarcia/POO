import tkinter as tk

def mostrar_seleccion():
        lbl_resultado.config(
            text=f"Opcion Seleccionada: {opcion.get()}"
        )



window = tk.Tk()
window.geometry("500x500")
window.title("radioButton")

opcion = tk.StringVar()

rb_1 = tk.Radiobutton(window, text="Opcion 1", variable=opcion, value="Opcion 1")
rb_1.pack()

rb_2 = tk.Radiobutton(window, text="Opcion 2", variable=opcion, value="Opcion 2")
rb_2.pack()

rb_3 = tk.Radiobutton(window, text="Opcion 3", variable=opcion, value="Opcion 3")
rb_3.pack()

btn_mostrar = tk.Button(window, text="Mostrar Seleccion", command=mostrar_seleccion)
btn_mostrar.pack()

lbl_resultado = tk.Label(window, text="Opcion Seleccionada: ")
lbl_resultado.pack()

window.mainloop()