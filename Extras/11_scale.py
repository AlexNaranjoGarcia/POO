from tkinter import *

def mostrar_valor():
    respuesta.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

ventana = Tk()
ventana.title("Escalar")
ventana.geometry("500x500")

valor=IntVar()
escala=Scale(ventana, from_=0, to=100, orient=HORIZONTAL, length=400, variable=valor)
escala.pack()

boton=Button(ventana, text="Mostrar valor", command=mostrar_valor)
boton.pack()

respuesta=Label(ventana, text="")
respuesta.pack()

ventana.mainloop()

