import tkinter as tk
from controller import funciones

def interfaz_principal():
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

    btn_suma = tk.Button(frame_botones, text="SUMA", command=lambda:funciones.operaciones(num1.get(), num2.get(), "+"))
    btn_suma.grid(row=0, column=0, padx=[5,0])

    btn_resta = tk.Button(frame_botones, text="RESTA", command=lambda:funciones.operaciones(num1.get(), num2.get(), "-"))
    btn_resta.grid(row=0, column=1, padx=5)

    btn_div = tk.Button(frame_botones, text="DIVISION", command=lambda:funciones.operaciones(num1.get(), num2.get(), "/"))
    btn_div.grid(row=0, column=2, padx=5)

    btn_mult = tk.Button(frame_botones, text="MULTIPLICACION", command=lambda:funciones.operaciones(num1.get(), num2.get(), "x"))
    btn_mult.grid(row=0, column=3, padx=[0,5])

    btn_salir = tk.Button(window, text="Salir", command=window.quit)
    btn_salir.pack(pady=10)


    window.mainloop()