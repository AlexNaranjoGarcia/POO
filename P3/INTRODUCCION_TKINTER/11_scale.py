import tkinter as tk

def mostrarValor():
    lbl_mostrar.config(
        text=f"Valor seleccionado por el usuario: {valor.get()}"
    )

window = tk.Tk()
window.geometry("500x500")
window.title("Scale")

valor = tk.IntVar()
scale = tk.Scale(window, orient="horizontal", variable=valor, to=100, from_=0)
scale.pack()

btn_mostrar = tk.Button(window, text="Mostrar Valor", command=mostrarValor)
btn_mostrar.pack()

lbl_mostrar = tk.Label(window, text="")
lbl_mostrar.pack()

window.mainloop()