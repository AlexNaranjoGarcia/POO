from tkinter import *

def entrar():
    lbl_resultado.config(
    text=f"BIENVENDIO {nombre.get()}",
    bg="silver",
    fg="white",
    width=50,
    height=4,
    font=("Arial", 30, "bold"),
    border=2,
    relief="groove"
    )

def borrar():
    lbl_resultado.config(text="")
    txt_nombre.delete(0,END)
    txt_password.delete(0,END)
    txt_nombre.focus()
    #limpiar inputs xt_password.delete(0,END)
    #obtener valor de input txt_nombre.get()
    lbl_resultado.destroy()

def salir():
    ventana.quit()

ventana=Tk()

ventana.geometry("500x500")
ventana.title("ENTRY")


lbltit=Label(ventana,text="ACCESO AL SISTEMA")
lbltit.config(background="light blue",foreground="dark blue",width=50,height=4,font=("helvetica",30,"italic"),border=2,relief="groove")
lbltit.pack(pady=[10,5])

frame_main = Frame(ventana, width=800, height=300, bg="silver")
frame_main.pack()



lbl_nombre=Label(frame_main,text="INGRESE EL NOMBRE:")
lbl_nombre.grid(row=0, column=0, padx=5, pady=5)

nombre = StringVar()
txt_nombre=Entry(frame_main,width=30, textvariable=nombre)
txt_nombre.focus()
txt_nombre.grid(row=0, column=1, padx=5, pady=5)

lbl_password=Label(frame_main,text="INGRESE LA CONTRASEÑA:")
lbl_password.grid(row=1, column=0, padx=5, pady=5)


txt_password=Entry(frame_main,width=30,show="*")
txt_password.grid(row=1, column=1, padx=5, pady=5)


frame_button = Frame(ventana, width=800, height=100, bg="silver")
frame_button.pack()

btn_entrar=Button(frame_button,text="ENTRAR",command=entrar)
btn_entrar.grid(row=2, column=0, padx=5, pady=5)

btn_borrar=Button(frame_button,text="BORRAR",command=borrar)
btn_borrar.grid(row=2, column=1, padx=5, pady=5)

btn_salir=Button(frame_button,text="Salir",command=salir)
btn_salir.grid(row=2, column=3, padx=5, pady=5)

#etiqueta bienvenido y quien entro
lbl_resultado=Label(ventana,text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()