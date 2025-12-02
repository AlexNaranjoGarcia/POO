import tkinter as tk

def CambiarTexto():
    label_cambiante.config(text="Nuevo valor", bg="blue")

def RegresarTexto():
    label_cambiante.config(text="Original", bg="red")

def AbrirVentanaSesion():
    ventana_sesion = tk.Toplevel(window)
    ventana_sesion.title("Sesión iniciada")
    ventana_sesion.geometry("300x150")
    ventana_sesion.config(bg="lightgreen")

    label_sesion = tk.Label(ventana_sesion, text="¡Has iniciado sesión!", font=("Arial", 14), bg="lightgreen")
    label_sesion.pack()

    boton_cerrar = tk.Button(ventana_sesion, text="Cerrar", command=ventana_sesion.destroy)
    boton_cerrar.pack(pady=10)

# Ventana principal
window = tk.Tk()
window.title("Uso de botones")
window.geometry("800x600")

frame_principal = tk.Frame(window, bg="Silver", width=800, height=50, border=2, relief="groove")
frame_principal.propagate(False)
frame_principal.pack(pady=10)

label_titulo = tk.Label(frame_principal, text="Uso de botones", bg="silver", width=20)
label_titulo.pack()

label_cambiante = tk.Label(window, text="Original")
label_cambiante.pack(pady=10)

button_cambiar = tk.Button(window, text="Cambiar Texto", command=CambiarTexto)
button_cambiar.pack(pady=5)

button_regresar = tk.Button(window, text="Regresar Texto", command=RegresarTexto)
button_regresar.pack(pady=5)


frame_secundario = tk.Frame(window, bg="Pink", width=800, height=100, border=2, relief="groove")
frame_secundario.propagate(False)
frame_secundario.pack(pady=10)

label_usuario = tk.Label(frame_secundario, text="Usuario", bg="pink", width=20)
label_usuario.pack()

label_psw = tk.Label(frame_secundario, text="Password")
label_psw.pack(pady=10)

# Botón que abre la nueva ventana
button_sesion = tk.Button(window, text="Iniciar Sesión", command=AbrirVentanaSesion, bg="lightblue")
button_sesion.pack(pady=10)

window.mainloop()
