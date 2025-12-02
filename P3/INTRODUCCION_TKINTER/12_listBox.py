import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("ListBox")

def mostrarOpcion():
    valor = list.get(list.curselection())
    lbl_mostrar.config(
        text=f"Seleccionaste: {valor}"
    )

list = tk.Listbox(window, width=50, height=5, selectmode="single")
list.pack()
Opciones = ["Azul", "Rojo", "Negro", "Amarillo"]
for opc in Opciones:
    list.insert(tk.END, opc)

btn_mostrar = tk.Button(window, text="Mostrar Resultado", command=mostrarOpcion)
btn_mostrar.pack()

lbl_mostrar = tk.Label(window, text="")
lbl_mostrar.pack()

window.mainloop()