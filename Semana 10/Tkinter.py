import tkinter as tk
import tkinter as ttk
#from tkinter import messagebox
from tkinter import*

###########################
# Una ventana simple
###########################
Ventana_principal = tk.Tk()
Ventana_principal.title("Curso de Python Entry Level")
Ventana_principal.geometry("400x300")

###########################
# Frame
###########################
frame = tk.Frame(Ventana_principal, padx=10, pady=10)
frame.pack()

nombre = tk.Label(frame, text="estudiantesdeprogramacion")
nombre.grid(row=0, column=0)

puesto = tk.Label(frame, text="estudiantesdeprogramacion")
puesto.grid(row=1, column=0)

salario = tk.Label(frame, text="estudiantesdeprogramacion")
salario.grid(row=2, column=0)

Ventana_principal.mainloop()

###########################
# Ventanas secundarias
###########################
def abrirVentanaSecundaria():
    ventana_secundaria = tk.Toplevel(Ventana_principal)
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.geometry("300x200")

    etiqueta=ttk.Label(ventana_secundaria, text="Es una ventana secundaria")
    etiqueta.pack(pady=20)
    bnt_cerrar = ttk.Button(ventana_secundaria, text="Cierre esta ventana", command=ventana_secundaria.destroy)

btn_abrir = ttk.Button(Ventana_principal, text="Abrir ventana secundaria", command=abrirVentanaSecundaria())
btn_abrir.pack(pady=50)

###########################
# Message o ventanas emergentes de informacion
###########################
def mostrar_mensaje():
    messagebox.showinfo("Hay examen la proxima semana.")

btn_mostrarmensaje = tk.Button(Ventana_principal, text="Mostrar mensaje", command=mostrar_mensaje())
btn_mostrarmensaje.pack()

###########################
# spinbox
###########################
valores=("C#", "Java", "Python")
spinbox = tk.Spinbox(Ventana_principal, values=valores)
spinbox.pack()

###########################
# combobox o seleccion
###########################
seleccion = ttk.Combobox(Ventana_principal, values=valores)
seleccion.pack()

###########################
# radio button
###########################
def seleccion_unica():
    opcion_seleccionada = boton_seleccionado.get()
    print("Su opcion seleccionada fue la siguiente: ", opcion_seleccionada)

boton_seleccionado = tk.StringVar()
boton_seleccionado.set("Opcion 1")

btn_seleccion1=ttk.Radiobutton(Ventana_principal, variable=boton_seleccionado, value="opcion1", command=seleccion_unica())
btn_seleccion1.pack(pady=5)
btn_seleccion2=ttk.Radiobutton(Ventana_principal, variable=boton_seleccionado, value="opcion2", command=seleccion_unica())
btn_seleccion2.pack(pady=5)


###################################################
Ventana_principal.mainloop()