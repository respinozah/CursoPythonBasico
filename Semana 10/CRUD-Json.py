from tkinter import Canvas
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

ARCHIVO_EMPLEADOS = "empleados.json"
ARCHIVO_REPORTE = "reporte_empleados.pdf"

def cargar_empleados():
    try:
        with open (ARCHIVO_EMPLEADOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_empleados(empleados):
    try:
        with open(ARCHIVO_EMPLEADOS, "w") as archivo:
            json.dump(empleados, archivo, indent=4)
    except FileNotFoundError:
        return []

def validar_id(id_empleado, empleados):
    if not id_empleado.isdigit():
        raise ValueError("El Id debe ser un numero entero")
    
    for empleado in empleados:
        if empleado["id"] == id_empleado:
            raise ValueError("El id ya esta en uso, no se puede utilizar")
    
    return id_empleado

def validar_salario(salariop):
    try:
        salario = float(salariop)
        if salario < 0:
            raise ValueError("El salario ingresado no puede ser negativo.")
        return salario
    except ValueError:
        raise ValueError("El salario no es valido")

def agregar_empleado():
    empleados =  cargar_empleados()
    empleado = {}
    while True:
        try:
            empleado["id"] = validar_id(input("Ingrese el Id del empleado: "), empleados)
            empleado["Nombre"] = input("Ingrese el nombre del empleado: ")
            empleado["Puesto"] = input("Ingrese el cargo del empleado: ")
            empleado["Salario"] = validar_salario(input("Ingrese el salario del empleado: "))
            break
        except ValueError as e:
            print(e)
    
    empleados.append(empleado)
    guardar_empleados(empleados)
    print("Los datos se han guardado de manera exitosa")

def listar_empleados():
    empleados = cargar_empleados()
    for empleado in empleados:
        print(f"ID:{empleado['id']}, Nombre: {empleado['Nombre']}, Puesto: {empleado['Puesto']}, Salario: {empleado['Salario']}")

def actualizar_empleado():
    id_empleado = input("Ingrese el Id del empleado que desea actualizar: ")
    empleados = cargar_empleados()
    for empleado in empleados:
        if empleado["id"] == id_empleado:
            print("Si no desea actualizar un campo especifico, dejelo en blanco.")
            empleado["Nombre"] = input(f"Ingrese el nuevo nombre ({empleado['Nombre']}): ")
            empleado["Puesto"] = input(f"Ingrese el nuevo puesto ({empleado['Puesto']}): ")
            try:
                nuevo_salario = input(f"Ingrese el nuevo salario ({empleado['Salario']}): ")
                empleado["Salario"] = validar_salario(nuevo_salario)
            except ValueError as excepcion:
                print(excepcion)
            guardar_empleados(empleados)
            print("El empleado fue actualizado.")
            return
        else:
            print("Empleado no encontrado")

def eliminar_empleado():
    id_empleado = input("Ingrese el Id del empleado que desea eliminar: ")
    empleados = cargar_empleados()
    encontrado= False
    for empleado in empleados:
        if empleado["id"] == id_empleado:
            encontrado = True
        confirmacion = input("Esta segurio de eliminar ese empleado? (s/n):").lower()
        if confirmacion == "s":
            empleados.remove(empleado)
            guardar_empleados(empleados)
        else:
            print("Se cancela la operacion")
        break

    if not encontrado:
        print("El empleado no se encontró.")

def buscar_empleado():
    campo_busqueda = input("Ingrese el Id o el nombre que desea buscar: ")
    empleados = cargar_empleados()
    encontrados = []
    for empleado in empleados:
        if campo_busqueda.lower() in empleado['nombre'].lower() or campo_busqueda == empleado["id"]:
            encontrados.append(empleado)
        if encontrados:
            print("No se encontraron empleados")
            for empleado in encontrados:
                print(f"ID:{empleado['id']}, Nombre: {empleado['Nombre']}, Puesto: {empleado['Puesto']}, Salario: {empleado['Salario']}")
        else:
            print("El empleado no se encuentra.")

def generarReportePDF():
    empleados = cargar_empleados()
    dataTabla = [["ID", "Nombre", "Puesto", "Salario"]]
    for empleado in empleados:
        dataTabla.append([
            str(empleado["id"]),
            empleado["Nombre"],
            str(empleado["Puesto"]),
            empleado["Salario"]
        ])
    
    #estilos de la tabla
    estilo_encabezado = [
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1, 0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ]
    estilo_celda = [
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]

    #crear canvas para el pdf
    c = canvas.Canvas(ARCHIVO_REPORTE, pagesize=letter)

    #Definir la tabla y aplicar estilos
    tabla = Table(dataTabla)
    tabla.setStyle(TableStyle(estilo_encabezado + estilo_celda))

    #Coordenadas para dibujar la tabla en el lienzo
    x = 50
    y = 750

    #Dibujar la tabla en el lienzo
    tabla.wrapOn(c, 400, 600) # Ancho y alto del area donde se ajustara la tabla
    tabla.drawOn(c, x, y)

    #Guardar el PDF
    c.save()





# hacer un menu
# Hacer un reporte en pdf, encabezado, filas y columnas y guardar ese archivo en la maquina.
# 2 funciones que considere que se deben agregar