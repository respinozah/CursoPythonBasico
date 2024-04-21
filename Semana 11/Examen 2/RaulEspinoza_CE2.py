import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv

ARCHIVO_ESTUDIANTES = "estudiantes.txt"
FOLDER_CARNES = r"Semana 11\Examen 2"
ARCHIVO_CURSOS = "cursos.txt"
ARCHIVO_MATRICULA = ""
ARCHIVO_REPORTE = "reporte_matricula.pdf"

####################################################################################################
# CRUD Estudiantes
####################################################################################################
def crearEstudiante(carne, nombre, rutacarne):
    try:
        with open(ARCHIVO_ESTUDIANTES, "a") as archivoEstudiantes:
            archivoEstudiantes.write(f"{carne},{nombre},{(f"{FOLDER_CARNES}/carne{nombre}.jpg")}\n")
            shutil.copy(rutacarne, (f"{FOLDER_CARNES}/carne{nombre}.jpg"))
    except Exception as e:
        messagebox.showerror(title="Error registrando estudiante", message=(f"No fue posible registrar el estudiante {nombre}. Razon: {e}"))

def actualizarEstudiante(carnep, nombrep):
    try:
        with open(ARCHIVO_ESTUDIANTES, "r") as archivo:
            estudiantes = archivo.readlines()
        with open(ARCHIVO_ESTUDIANTES, "w") as archivo:
            for linea in estudiantes:
                carne, nombre, ruta = linea.strip().split(",")
                if carne == carnep:
                    archivo.write(f"{carne},{nombrep},{ruta}\n")
                else:
                    archivo.write(linea)
    except Exception as e:
        messagebox.showerror(title="Error actualizando estudiante", message=(f"No fue posible actualizar el estudiante. Razon: {e}"))

def getNombreDesdeCarne(carnep):
    try:
        with open(ARCHIVO_ESTUDIANTES, "r") as archivo:
            estudiantes = archivo.readlines()
        for estudiante in estudiantes:
            carne, nombre, ruta = estudiante.strip().split(",")
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
def crearCurso(valorCodigop, valorNombrep):
    try:
        with open(ARCHIVO_CURSOS, "a") as archivoCursos:
            archivoCursos.write(f"{valorCodigop},{valorNombrep}\n")
    except Exception as e:
        messagebox.showerror(title="Error registrando curso", message=(f"No fue posible registrar el curso {valorNombrep}. Razon: {e}"))

def actualizarCurso(codigop, nombrep):
    try:
        with open(ARCHIVO_CURSOS, "r") as archivo:
            cursos = archivo.readlines()
        with open(ARCHIVO_CURSOS, "w") as archivo:
            for linea in cursos:
                codigo, nombre = linea.strip().split(",")
                if codigo == codigop:
                    archivo.write(f"{codigo},{nombrep}\n")
                else:
                    archivo.write(linea)
    except Exception as e:
        messagebox.showerror(title="Error actualizando curso", message=(f"No fue posible actualizar el curso. Razon: {e}"))

def getNombreDesdeCodigo(codigop):
    try:
        with open(ARCHIVO_CURSOS, "r") as archivo:
            cursos = archivo.readlines()
        for curso in cursos:
            codigo, nombre = curso.strip().split(",")
            if codigo == str(codigop):
                return nombre
        return (f"No fue encontrado un curso con el código {codigop}")
    except Exception as e:
        messagebox.showerror(title="Error obteniendo nombre", message=(f"No fue posible obtener el nombre del curso. Razón: {e}"))

def removerCursoDelArchivo(codigop):
    try:
        with open(ARCHIVO_CURSOS, "r") as archivo:
            cursos = archivo.readlines()
        cursosActualizados = []
        for curso in cursos:
            codigo, nombre = curso.strip().split(",")
            if codigo != codigop:
                cursosActualizados.append(curso)
        with open(ARCHIVO_CURSOS, "w") as archivo:
            for curso in cursosActualizados:
                archivo.write(curso)
    except Exception as e:
        messagebox.showerror(title="Error removiendo curso", message=f"No fue posible remover el curso. Razon: {e}")

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
# Gestion de Cursos
#####################################################
def gestionarCurso(accion):
    #Ventana emergente curso
    ventanaCurso = tk.Toplevel(ventanaPrincipal)
    ventanaCurso.title("Detalles del curso")
    ventanaCurso.geometry("500x300")

    #Label de instrucciones
    labelTitulo = tk.Label(ventanaCurso)
    labelTitulo.grid(row=0, columnspan=3, sticky=tk.W)
    def cambiarInstrucciones(accion):
        if accion == "Agregar":
            textoLabel = "Completar la informacion del curso (código y nombre) por agregar."
        elif accion == "Consultar":
            textoLabel = "Ingrese el numero de código y haga click en Consultar."
        elif accion == "Actualizar":
            textoLabel = "Actualice el nombre y haga click en Actualizar."
        elif accion == "Remover":
            textoLabel = "Indique el numero de código y haga click en Remover."
        labelTitulo.config(text=textoLabel)
    cambiarInstrucciones(accion)

    #Seccion carne
    labelCodigo = tk.Label(ventanaCurso, text="Código:")
    labelCodigo.grid(row=1, column=0, sticky=tk.W)
    textBoxCodigo = tk.Text(ventanaCurso, height=1, width=12)
    textBoxCodigo.grid(row=1, column=1, sticky=tk.W)

    #Seccion nombre
    labelNombre = tk.Label(ventanaCurso, text="Nombre:")
    labelNombre.grid(row=2, column=0, sticky=tk.W)
    textBoxNombre = tk.Text(ventanaCurso, height=1, width=25)
    textBoxNombre.grid(row=2, column=1, sticky=tk.W)

    #Gestion de curso
    def gestionarValores():
        valorCodigo = textBoxCodigo.get("1.0", "end-1c")
        valorNombre = textBoxNombre.get("1.0", "end-1c")

        if accion == "Consultar":
            try:
                if valorCodigo != "":
                    try:
                        textBoxNombre.delete("1.0","end-1c")
                        textBoxNombre.insert("1.0", getNombreDesdeCodigo(int(valorCodigo)))
                    except ValueError:
                        messagebox.showerror(title="Campo requerido", message="El número de código debe ser un número.")
                else:
                    messagebox.showerror(title="Valor requerido", message="Se necesita un número de código para poder consultar un curso.")
            except Exception as e:
                messagebox.showerror(title="Error consultando curso", message=("No fue posible consultar curso: ", e))

        elif accion == "Actualizar":
            try:
                if valorCodigo != "" or valorNombre != "":
                    if validarEsEntero(valorCodigo):
                        actualizarCurso(valorCodigo, valorNombre)
                        messagebox.showinfo(title="Curso actualizado", message=f"Curso {valorCodigo} {valorNombre} fue actualizado en el sistema.")
                        ventanaCurso.destroy
                    else:
                        messagebox.showerror(title="Valor invalido", message="El número de código debe ser un valor númerico.")#
                else:
                    messagebox.showerror(title="Campo requerido", message="Favor revisar que los campos esten completos.")
            except Exception as e:
                messagebox.showerror(title="Error actualizando curso", message=("No fue posible actualizar la informacion del curso: ", e))

        elif accion == "Agregar":
            try:
                if valorCodigo != "" or valorNombre != "":
                    if validarEsEntero(valorCodigo):
                        crearCurso(valorCodigo, valorNombre)
                        messagebox.showinfo(title="Curso creado", message=f"Curso {valorNombre} fue creado en el sistema.")
                        ventanaCurso.destroy
                    else:
                        messagebox.showerror(title="Valor invalido", message="El número de código debe ser un valor númerico.")
                else:
                    messagebox.showerror(title="Campos requeridos", message="Favor revisar que los campos esten completos.")
            except Exception as e:
                messagebox.showerror(title="Error guardando curso", message=("No fue posible guardar el curso: ", e))

    def removerCurso():
        valorCodigo = textBoxCodigo.get("1.0", "end-1c")
        confirmacion = messagebox.askyesno(title="Por favor confirmar", message=(f"¿Estás seguro de que desea remover el curso {getNombreDesdeCodigo(valorCodigo)}?"))
        if confirmacion:
            try:
                if valorCodigo != "":
                    if validarEsEntero(valorCodigo):
                        removerCursoDelArchivo(valorCodigo)
                        messagebox.showinfo(title="Curso removido", message=f"Curso fue removido del sistema.")
                        ventanaCurso.destroy
                    else:
                        messagebox.showerror(title="Valor invalido", message="El número de código debe ser un valor númerico.")
                else:
                    messagebox.showerror(title="Campos requeridos", message="Favor revisar que el numero de carne.")
            except Exception as e:
                messagebox.showerror(title="Error removiendo curso", message=("No fue posible remover el curso: ", e))

    #Boton consultar
    btnConsultar = tk.Button(ventanaCurso, text="Consultar", command=gestionarValores)
    btnConsultar.grid(row=3, column=0)

    #Boton guardar
    btnGuardar = tk.Button(ventanaCurso, text="Guardar", command=gestionarValores)
    btnGuardar.grid(row=3, column=1)

    #Boton remover
    btnRemover = tk.Button(ventanaCurso, text="Remover", command=removerCurso)
    btnRemover.grid(row=3, column=2)

    #Boton cancelar
    btnCancelar = tk.Button(ventanaCurso, text="Cancelar", command=ventanaCurso.destroy)
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
        valorRutaCarne = textBoxRutaCarne.get("1.0", "end-1c")

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
                if valorCarne != "" or valorNombre != "" or valorRutaCarne != "":
                    if validarEsEntero(valorCarne):
                        crearEstudiante(valorCarne, valorNombre, valorRutaCarne)
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

    def generarRutaCarne():
        try:
            rutaCarne = filedialog.askopenfilename()
            textBoxRutaCarne.delete("1.0","end-1c")
            textBoxRutaCarne.insert("1.0", rutaCarne)
            if rutaCarne != "":
                return rutaCarne
            else:
                return ""
        except Exception as e:
            messagebox.showerror(title="Error seleccionando carné", message=f"No se pudo seleccionar el archivo del carné. {e}")
            return ""

    #Seccion archivo carné
    labelCarne = tk.Label(ventanaEstudiante, text="Foto carné:")
    labelCarne.grid(row=3, column=0, sticky=tk.W)
    textBoxRutaCarne = tk.Text(ventanaEstudiante, height=1, width=25)
    textBoxRutaCarne.grid(row=3, columnspan=2, column=1, sticky=tk.W)
    btnRutaCarne = tk.Button(ventanaEstudiante, text="...", command=generarRutaCarne)
    btnRutaCarne.grid(row=3, column=3)

    #Boton consultar
    btnConsultar = tk.Button(ventanaEstudiante, text="Consultar", command=gestionarValores)
    btnConsultar.grid(row=4, column=0)

    #Boton guardar
    btnGuardar = tk.Button(ventanaEstudiante, text="Guardar", command=gestionarValores)
    btnGuardar.grid(row=4, column=1)

    #Boton remover
    btnRemover = tk.Button(ventanaEstudiante, text="Remover", command=removerEstudiante)
    btnRemover.grid(row=4, column=2)

    #Boton cancelar
    btnCancelar = tk.Button(ventanaEstudiante, text="Cancelar", command=ventanaEstudiante.destroy)
    btnCancelar.grid(row=4, column=3)

    if accion == "Agregar":
        btnRemover.config(state="disabled")
        btnConsultar.config(state="disabled")
    elif accion == "Consultar":
        btnGuardar.config(state="disabled")
        btnRemover.config(state="disabled")
    elif accion == "Actualizar":
        btnConsultar.config(state="disabled")

#####################################################
# Gestion de Matricula
#####################################################
def gestionarMatricula(accion):
    print()

#####################################################
# Reportes
#####################################################
def generarReporteEstudiantesPdf(nombreArchivo, datos):
    c = canvas.Canvas(nombreArchivo, pagesize=letter)
    c.setFont("Helvetica", 12)

    for dato in datos:
        c.drawString(100, 750, f"Id: {dato[0]} - Nombre: {dato[1]}")
        c.drawString(100, 730, f"Ruta de imagen: {dato[2]}")
        c.showPage()
    
    c.save()

def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r', newline='', encoding='utf-8') as archivo:
        leer_csv = csv.reader(archivo)
        datos = list(leer_csv)
    return datos

def generarReporteEstudiantes():
    estudiantes = leerArchivo(ARCHIVO_ESTUDIANTES)
    generarReporteEstudiantesPdf("ReporteEstudiantes.pdf", estudiantes)
    
def generarReporteCursos():
    cursos = leerArchivo(ARCHIVO_CURSOS)



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

#Menu Cursos
menuCursos = tk.Menu(ventanaPrincipal, tearoff=0)
menuCursos.add_command(label="Nuevo curso", command=lambda: gestionarCurso("Agregar"))
menuCursos.add_command(label="Consultar curso", command=lambda: gestionarCurso("Consultar"))
menuCursos.add_command(label="Actualizar curso", command=lambda: gestionarCurso("Actualizar"))

#Menu Matricula
menuMatricula = tk.Menu(ventanaPrincipal, tearoff=0)
menuMatricula.add_command(label="Matricular curso", command=lambda: gestionarMatricula("Agregar"))
menuMatricula.add_command(label="Consultar matricula", command=lambda: gestionarMatricula("Consultar"))
menuMatricula.add_command(label="Actualizar matricula", command=lambda: gestionarMatricula("Actualizar"))

#Menu Reporte
menuReporte = tk.Menu(ventanaPrincipal, tearoff=0)
menuReporte.add_command(label="Generar reporte estudiantes", command=lambda: generarReporteEstudiantes)
menuReporte.add_command(label="Generar reporte cursos", command=lambda: generarReporteCursos)

#Barra Menu
barraMenu = tk.Menu(ventanaPrincipal)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Estudiantes", menu=menuEstudiantes)
barraMenu.add_cascade(label="Cursos", menu=menuCursos)
barraMenu.add_cascade(label="Matricula", menu=menuMatricula)
barraMenu.add_cascade(label="Reportes", menu=menuReporte)
ventanaPrincipal.config(menu=barraMenu)

#Boton cerrar DEBE SER BORRADO
btnCerrar = tk.Button(ventanaPrincipal, text="Cerrar", command=ventanaPrincipal.quit)
btnCerrar.pack()





#####################################################
# Ejecucion del sistema
#####################################################
ventanaPrincipal.mainloop()