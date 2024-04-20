import tkinter as tk
from tkinter import messagebox
from tkinter import font

ARCHIVO_ESTUDIANTES = "estudiantes.txt"
ARCHIVO_CURSOS = ""
ARCHIVO_MATRICULA = ""

####################################################################################################
# CRUD Estiantes
####################################################################################################

def crearEstudiante(carne, nombre):
    try:
        with open(ARCHIVO_ESTUDIANTES, "a") as archivoEstudiantes:
            archivoEstudiantes.write(f"{carne},{nombre}\n")
    except Exception as e:
        messagebox.showerror(title="Error registrando estudiante", message=(f"No fue posible registrar el estudiante {nombre}. Razon: {e}"))
    

def actualizarEstudiante(carnep, nombrep):
    try:
        with open(ARCHIVO_ESTUDIANTES, "r") as archivo:
            estudiantes = archivo.readlines()

        with open(ARCHIVO_ESTUDIANTES, "w") as archivo:
            for linea in estudiantes:
                carne, nombre = linea.strip().split(",")
                if carne == carnep:
                    archivo.write(f"{carne},{nombrep}\n")
                else:
                    archivo.write(linea)
    except Exception as e:
        messagebox.showerror(title="Error actualizando estudiante", message=(f"No fue posible actualizar el estudiante. Razon: {e}"))
    

def getNombreDesdeCarne(carnep):
    try:
        with open(ARCHIVO_ESTUDIANTES, "r") as archivo:
            estudiantes = archivo.readlines()
        for estudiante in estudiantes:
            carne, nombre = estudiante.strip().split(",")
            if carne == str(carnep):
                return nombre
        return (f"No fue encontrado un estudiante con el carné {carnep}")

    except Exception as e:
        messagebox.showerror(title="Error obteniendo nombre", message=(f"No fue posible obtener el nombre del estudiante. Razón: {e}"))

def removerEstudianteDelArchivo(carnep):
    try:
        with open(ARCHIVO_ESTUDIANTES, "r") as archivo:
            estudiantes = archivo.readlines()
        estudiantesActualizados = []
        for estudiante in estudiantes:
            carne, nombre = estudiante.strip().split(",")
            if carne != carnep:
                estudiantesActualizados.append(estudiante)

        with open(ARCHIVO_ESTUDIANTES, "w") as archivo:
            for estudiante in estudiantesActualizados:
                archivo.write(estudiante)
    except Exception as e:
        messagebox.showerror(title="Error removiendo estudiante", message=f"No fue posible remover el estudiante. Razon: {e}")
####################################################################################################
# CRUD Cursos
####################################################################################################

####################################################################################################
# CRUD Matricula
####################################################################################################

####################################################################################################
# Util
####################################################################################################
def validarEsEntero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

####################################################################################################
# Seguridad
####################################################################################################

####################################################################################################
# Tkinter
####################################################################################################

#####################################################
# Gestion de Estudiantes
#####################################################
def gestionarEstudiante(accion):
    #Ventana emergente estudiante
    ventanaEstudiante = tk.Toplevel(ventanaPrincipal)
    ventanaEstudiante.title("Detalles del estudiante")
    ventanaEstudiante.geometry("500x300")

    #Label de instrucciones
    labelTitulo = tk.Label(ventanaEstudiante)
    labelTitulo.grid(row=0, columnspan=3, sticky=tk.W)
    def cambiarInstrucciones(accion):
        if accion == "Agregar":
            textoLabel = "Completar la informacion del estudiante (carne y nombre) por agregar."
        elif accion == "Consultar":
            textoLabel = "Ingrese el numero de carne y haga click en Consultar."
        elif accion == "Actualizar":
            textoLabel = "Actualice el nombre y haga click en Actualizar."
        elif accion == "Remover":
            textoLabel = "Indique el numero de carne y haga click en Remover."
        labelTitulo.config(text=textoLabel)
    cambiarInstrucciones(accion)

    #Seccion carne
    labelCarne = tk.Label(ventanaEstudiante, text="Carne:")
    labelCarne.grid(row=1, column=0, sticky=tk.W)
    textBoxCarne = tk.Text(ventanaEstudiante, height=1, width=12)
    textBoxCarne.grid(row=1, column=1, sticky=tk.W)

    #Seccion nombre
    labelNombre = tk.Label(ventanaEstudiante, text="Nombre:")
    labelNombre.grid(row=2, column=0, sticky=tk.W)
    textBoxNombre = tk.Text(ventanaEstudiante, height=1, width=25)
    textBoxNombre.grid(row=2, column=1, sticky=tk.W)

    #Gestion de estudiante
    def gestionarValores():
        valorCarne = textBoxCarne.get("1.0", "end-1c")
        valorNombre = textBoxNombre.get("1.0", "end-1c")

        if accion == "Consultar":
            try:
                if valorCarne != "":
                    try:
                        textBoxNombre.delete("1.0","end-1c")
                        textBoxNombre.insert("1.0", getNombreDesdeCarne(int(valorCarne)))
                    except ValueError:
                        messagebox.showerror(title="Campo requerido", message="El número de carné debe ser un número.")
                else:
                    messagebox.showerror(title="Valor requerido", message="Se necesita un número de carné para poder consultar un estudiante.")
            except Exception as e:
                messagebox.showerror(title="Error consultando estudiante", message=("No fue posible consultar estudiante: ", e))

        elif accion == "Actualizar":
            try:
                if valorCarne != "" or valorNombre != "":
                    if validarEsEntero(valorCarne):
                        actualizarEstudiante(valorCarne, valorNombre)
                        messagebox.showinfo(title="Estudiante actualizado", message=f"Estudiante {valorCarne} {valorNombre} fue actualizado en el sistema.")
                        ventanaEstudiante.destroy
                    else:
                        messagebox.showerror(title="Valor invalido", message="El número de carné debe ser un valor númerico.")#
                else:
                    messagebox.showerror(title="Campo requerido", message="Favor revisar que los campos esten completos.")
            except Exception as e:
                messagebox.showerror(title="Error actualizando estudiante", message=("No fue posible actualizar la informacion del estudiante: ", e))

        elif accion == "Agregar":
            try:
                if valorCarne != "" or valorNombre != "":
                    if validarEsEntero(valorCarne):
                        crearEstudiante(valorCarne, valorNombre)
                        messagebox.showinfo(title="Estudiante creado", message=f"Estudiante {valorNombre} fue creado en el sistema.")
                        ventanaEstudiante.destroy
                    else:
                        messagebox.showerror(title="Valor invalido", message="El número de carné debe ser un valor númerico.")
                else:
                    messagebox.showerror(title="Campos requeridos", message="Favor revisar que los campos esten completos.")
            except Exception as e:
                messagebox.showerror(title="Error guardando estudiante", message=("No fue posible guardar el estudiante: ", e))

    def removerEstudiante():

        valorCarne = textBoxCarne.get("1.0", "end-1c")
        confirmacion = messagebox.askyesno(title="Por favor confirmar", message=(f"¿Estás seguro de que desea remover el estudiante {getNombreDesdeCarne(valorCarne)}?"))
        if confirmacion:
            try:
                if valorCarne != "":
                    if validarEsEntero(valorCarne):
                        removerEstudianteDelArchivo(valorCarne)
                        messagebox.showinfo(title="Estudiante removido", message=f"Estudiante fue removido del sistema.")
                        ventanaEstudiante.destroy
                    else:
                        messagebox.showerror(title="Valor invalido", message="El número de carné debe ser un valor númerico.")
                else:
                    messagebox.showerror(title="Campos requeridos", message="Favor revisar que el numero de carne.")
            except Exception as e:
                messagebox.showerror(title="Error removiendo estudiante", message=("No fue posible remover el estudiante: ", e))

    #Boton consultar
    btnConsultar = tk.Button(ventanaEstudiante, text="Consultar", command=gestionarValores)
    btnConsultar.grid(row=3, column=0)

    #Boton guardar
    btnGuardar = tk.Button(ventanaEstudiante, text="Guardar", command=gestionarValores)
    btnGuardar.grid(row=3, column=1)

    #Boton remover
    btnRemover = tk.Button(ventanaEstudiante, text="Remover", command=removerEstudiante)
    btnRemover.grid(row=3, column=2)

    #Boton cancelar
    btnCancelar = tk.Button(ventanaEstudiante, text="Cancelar", command=ventanaEstudiante.destroy)
    btnCancelar.grid(row=3, column=3)

    if accion == "Agregar":
        btnRemover.config(state="disabled")
        btnConsultar.config(state="disabled")
    elif accion == "Consultar":
        btnGuardar.config(state="disabled")
        btnRemover.config(state="disabled")
    elif accion == "Actualizar":
        btnConsultar.config(state="disabled")


#####################################################
# Ventana Principal
#####################################################
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de matricula")
ventanaPrincipal.geometry("1000x600")
ventanaPrincipal.resizable(False, False)

#Menu Archivo
menuArchivo = tk.Menu(ventanaPrincipal, tearoff=0)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=ventanaPrincipal.quit)

#Menu Estudiantes
menuEstudiantes = tk.Menu(ventanaPrincipal, tearoff=0)
menuEstudiantes.add_command(label="Nuevo estudiante", command=lambda: gestionarEstudiante("Agregar"))
menuEstudiantes.add_command(label="Consultar estudiante", command=lambda: gestionarEstudiante("Consultar"))
menuEstudiantes.add_command(label="Actualizar estudiante", command=lambda: gestionarEstudiante("Actualizar"))

#Barra Menu
barraMenu = tk.Menu(ventanaPrincipal)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Estudiantes", menu=menuEstudiantes)
ventanaPrincipal.config(menu=barraMenu)

#Boton cerrar DEBE SER BORRADO
btnCerrar = tk.Button(ventanaPrincipal, text="Cerrar", command=ventanaPrincipal.quit)
btnCerrar.pack()





#####################################################
# Ejecucion del sistema
#####################################################
ventanaPrincipal.mainloop()