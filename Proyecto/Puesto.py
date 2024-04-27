import csv
import os

ARCHIVO_PUESTOS = r"Proyecto\sum_puestos.csv"

def getPuestos():
    # Verificar si el archivo csv existe
    if not os.path.exists(ARCHIVO_PUESTOS):
        with open(ARCHIVO_PUESTOS, "w") as archivo:
            nuevoArchivo = csv.writer(archivo)
            nuevoArchivo.writerow(["id", "nombre", "estado"])
        return []

    # Crear lista de puestos activos
    puestos_activos = []
    with open(ARCHIVO_PUESTOS, "r") as archivo:
        puestos = csv.DictReader(archivo)
        for puesto in puestos:
            if puesto["estado"] == "activo":
                puestos_activos.append({
                    "id": puesto["id"],
                    "nombre": puesto["nombre"],
                    "estado": puesto["estado"]
                })
    return puestos_activos

def getNombrePuesto(idPuesto):
    with open(ARCHIVO_PUESTOS, "r") as archivo:
        puestos = csv.DictReader(archivo)
        for puesto in puestos:
            if puesto["id"] == idPuesto:
                return puesto["nombre"]

def getIdPuesto(nombrePuesto):
    with open(ARCHIVO_PUESTOS, "r") as archivo:
        puestos = csv.DictReader(archivo)
        for puesto in puestos:
            if puesto["nombre"] == nombrePuesto:
                return puesto["id"]

def existePuesto(nombrePuesto):
    existe = False
    with open(ARCHIVO_PUESTOS, "r") as archivo:
        puestos = csv.DictReader(archivo)
        for puesto in puestos:
            if puesto["nombre"] == nombrePuesto:
                existe = True
    return existe
