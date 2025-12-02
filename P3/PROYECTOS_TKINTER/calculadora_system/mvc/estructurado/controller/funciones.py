import tkinter as tk
from tkinter import messagebox

def operaciones(num1, num2, simbolo):
    if simbolo == "+":
        op = num1 + num2
        tipo = "SUMA"
    elif simbolo == "-":
        op = num1 - num2
        tipo = "RESTA"
    elif simbolo == "x":
        op = num1 * num2
        tipo = "MULTIPLICACION"
    elif simbolo == "/":
        if num2 == 0:
            messagebox.showerror(message="No se puede dividir entre 0")
            op = "ERROR"
        else:
            op = num1 / num2
            tipo = "DIVISION"
    if op == "ERROR":
        pass
    else:
        messagebox.showinfo(message=f"{num1} {simbolo} {num2} = {op}", title=tipo)