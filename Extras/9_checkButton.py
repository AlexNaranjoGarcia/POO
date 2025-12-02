from tkinter import *

def mostrar_estado():
    if opcion== 1:
        resultado.config(text="Has activado las notificaciones")
    else:
        resultado.config(text="Has desactivado las notificaciones")


ventana = Tk()
ventana.title("Check button")
ventana.geometry("500x500")

opcion=IntVar()
checkBoton=Checkbutton(ventana, text="¿Desea recibir notificaciones?", variable=opcion, onvalue=1, offvalue=0)
checkBoton.pack()


btn_confirmar=Button(ventana,text="Confirmar", command=mostrar_estado)
btn_confirmar.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()