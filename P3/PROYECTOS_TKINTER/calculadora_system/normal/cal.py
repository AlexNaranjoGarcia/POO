"""

Crear una Calculadora:
1.- Dos Campos de texto
2.- 4 Botones con las Operaciones
3.- Mostrar el resultado con una Alerta
"""

import tkinter as tk
from tkinter import messagebox

def suma(num1, num2):
    messagebox.showinfo(message=f"{num1} + {num2} = {num1 + num2}")

def resta(num1, num2):
    messagebox.showinfo(message=f"{num1} - {num2} = {num1 - num2}")

def division(num1, num2):
    if num2 == 0:
        messagebox.showerror(message="No se puede dividir entre 0")
    else:
        messagebox.showinfo(message=f"{num1} / {num2} = {num1 / num2}")

def multiplicacion(num1, num2):
    messagebox.showinfo(message=f"{num1} x {num2} = {num1 * num2}")


window = tk.Tk()
window.title("Calculadora")
window.geometry("800x600")

frame_valores = tk.Frame(window, bg="skyblue")
frame_valores.propagate(False)
frame_valores.pack(pady=20)

lbl_1 = tk.Label(frame_valores, text="Ingrese el primer numero:")
lbl_1.grid(column=0, row=0, padx=10, pady=10)

lbl_2 = tk.Label(frame_valores, text="Ingrese el segundo numero:")
lbl_2.grid(column=0, row=1, padx=10, pady=10)

num1 = tk.IntVar()
num2 = tk.IntVar()

entry_1 = tk.Entry(frame_valores, textvariable=num1)
entry_1.grid(column=1, row=0, padx=10, pady=10)

entry_2 = tk.Entry(frame_valores, textvariable=num2)
entry_2.grid(column=1, row=1, padx=10, pady=10)

frame_botones = tk.Frame(window, width=400, height=80, bg="red")
frame_botones.propagate(False)
frame_botones.pack(pady=20)

btn_suma = tk.Button(frame_botones, text="SUMA", command=lambda:suma(num1.get(), num2.get()))
btn_suma.grid(row=0, column=0, padx=[5,0])

btn_resta = tk.Button(frame_botones, text="RESTA", command=lambda:resta(num1.get(), num2.get()))
btn_resta.grid(row=0, column=1, padx=5)

btn_div = tk.Button(frame_botones, text="DIVISION", command=lambda:division(num1.get(), num2.get()))
btn_div.grid(row=0, column=2, padx=5)

btn_mult = tk.Button(frame_botones, text="MULTIPLICACION", command=lambda:multiplicacion(num1.get(), num2.get()))
btn_mult.grid(row=0, column=3, padx=[0,5])

btn_salir = tk.Button(window, text="Salir", command=window.quit)
btn_salir.pack(pady=10)






window.mainloop()