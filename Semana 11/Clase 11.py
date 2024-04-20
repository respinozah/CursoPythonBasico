import tkinter as tk
from tkinter import messagebox

def guardar_archivo():
    contenido_archivo = texto.get("1.0", "end-1c")
    if contenido_archivo.strip():
        try:
            with open ("archivo.txt", "w") as archivo_estudiante:
                archivo_estudiante.write(contenido_archivo)
                messagebox.showinfo("El estudiante se guardo con exito.")
        except Exception as error:
            messagebox.showerror(f"El estudiante no pudo ser guardado. Error: {error}")
    else:
        messagebox.showwarning("El archivo esta vacio, valide nuevamente.")

def leer_archivo():
    try:
        with open("archivo.txt" ,"r") as archivo_estudiante:
            contenido_archivo = archivo_estudiante.read()
        texto.delete("1.0","end-1c")
        texto.insert("1.0", contenido_archivo)
    except FileNotFoundError:
        messagebox.showerror("El archivo no existe.")

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Informacion de estudiante")

texto = tk.Text(ventanaPrincipal, width=40, height=10)
texto.pack(padx=10, pady=5)

frameBotones = tk.Frame(ventanaPrincipal)
frameBotones.pack(pady=10)

btnGuardar = tk.Button(frameBotones, text="Guardar", command=guardar_archivo)
btnGuardar.pack(side="left", padx=10)

btnLeer = tk.Button(frameBotones, text="Leer", command=leer_archivo)
btnLeer.pack(side="left", padx=10)

ventanaPrincipal.mainloop()