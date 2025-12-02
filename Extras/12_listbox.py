from tkinter import *

def mostrar_seleccion():
    valor=box.curselection()
    Selection.config(text=f"Seleccionaste:{valor}")

ventana = Tk()
ventana.title("ListBox")
ventana.geometry("500x500")

box=Listbox(ventana, width=50, height=20, selectmode='single')
box.pack()

opciones=["Azul", "Rojo", "Negro", "Amarillo"]

for opcion in opciones:
    box.insert(END, opcion)

boton=Button(ventana, text="Mostrar Seleccion del Usuario")
boton.pack()

Selection=Label(ventana, text="")
Selection.pack()

ventana.mainloop()