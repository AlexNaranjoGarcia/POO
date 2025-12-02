
import tkinter as tk

def mostrar():
    lbl_2.config(
        text=f"Comentario: {caja.get(1.0,tk.END)}"
    )

window = tk.Tk()
window.geometry("800x600")

lbl_1 = tk.Label(window, text="Escriba su comentario:")
lbl_1.pack()

caja = tk.Text(window, width=40, height=5)
caja.pack()

bt = tk.Button(window, text="Mostrar Comentario", command=mostrar)
bt.pack()

lbl_2 = tk.Label(window, text="")
lbl_2.pack()


window.mainloop()