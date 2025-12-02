import tkinter as tk

def mostrarEstado():
    if opcion.get()==1:
        lbl_mostrar.config(
            text=f"Notificaciones Activadas"
        )
    else:
        lbl_mostrar.config(
            text=f"Notificaciones Desactivadas"
        )

window = tk.Tk()
window.geometry("500x500")
window.title("checkButton")

frame1 = tk.Frame(window, width=300, height=200)
frame1.pack()

opcion= tk.IntVar()
check_box = tk.Checkbutton(frame1, text="Desea recibir notificacoines?", height=2, variable=opcion, onvalue=1, offvalue=0)
check_box.pack()

btn_confirmar = tk.Button(frame1, text="Confirmar", command=mostrarEstado)
btn_confirmar.pack()

lbl_mostrar = tk.Label(window, text="")
lbl_mostrar.pack()

window.mainloop()