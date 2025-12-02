
import tkinter as tk

def haz_click():
    lbl_titulo.config(
    text="POO con Python",
    bg="green",
    fg="red", 
    font=("Arial", 30, "bold"),
    border=2,
    relief="groove"
    )

def regresar_click():
    lbl_titulo.config(
    text="Bienvenidos a Tkinter",
    bg="lightblue",
    fg="darkblue", 
    width=50,
    height=4,
    font=("Helvetica", 30, "italic"),
    border=2,
    relief="groove"
    )

window = tk.Tk()
window.title("Personalizar Widgets")
window.geometry("800x600")

lbl_titulo = tk.Label(window, text="Bienvenidos a Tkinter")
lbl_titulo.config(
    bg="lightblue",
    fg="darkblue", 
    width=50,
    height=4,
    font=("Helvetica", 30, "italic"),
    border=2,
    relief="groove"
    )
lbl_titulo.propagate(False)
lbl_titulo.pack(pady=30)

btn_1 = tk.Button(window, text="Haz click aqui", command=haz_click)
btn_1.config(
    fg="White",
    activeforeground="yellow",
    width=15,
    font=("Arial", 20, "bold")
)
btn_1.pack(pady=5)

btn_2 = tk.Button(window, text="Regresa click aqui", command=regresar_click)
btn_2.config(
    fg="black",
    activeforeground="red",
    width=15,
    font=("Arial", 20, "bold")
)
btn_2.pack(pady=5)

window.mainloop()