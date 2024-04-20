import tkinter as tk
from tkinter import ttk

def opcionSeleccionada(ListboxSelect):
    indice_seleccion = listaDeProgramas.curselection()
    if indice_seleccion:
        opcionSeleccionada = listaDeProgramas.get(indice_seleccion)
        print(f"Opcion seleccionada es: ", opcionSeleccionada)

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Lenguajes de programación")

listaDeProgramas = tk.Listbox(ventanaPrincipal)
listaDeProgramas.pack(pady=10)

listaDeProgramas.insert(1, "C#")
listaDeProgramas.insert(2, "Python")
listaDeProgramas.insert(3, "Java")
listaDeProgramas.insert(4, "Ruby")

listaDeProgramas.bind("<<ListboxSelect>>", opcionSeleccionada)

ventanaPrincipal.mainloop()