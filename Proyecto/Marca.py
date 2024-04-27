import csv
import os

ARCHIVO_MARCAS = r"Proyecto\sum_marcas.csv"

def getMarcas():
    # Verificar si el archivo csv existe
    if not os.path.exists(ARCHIVO_MARCAS):
        with open(ARCHIVO_MARCAS, "w") as archivo:
            nuevoArchivo = csv.writer(archivo)
            nuevoArchivo.writerow(["id", "nombre", "estado"])
        return []

    # Crear lista de marcas activas
    marcas_activas = []
    with open(ARCHIVO_MARCAS, "r") as archivo:
        marcas = csv.DictReader(archivo)
        for marca in marcas:
            if marca["estado"] == "activo":
                marcas_activas.append({
                    "id": marca["id"],
                    "nombre": marca["nombre"],
                    "estado": marca["estado"]
                })
    return marcas_activas

def getNombreMarca(idMarca):
    with open(ARCHIVO_MARCAS, "r") as archivo:
        marcas = csv.DictReader(archivo)
        for marca in marcas:
            if marca["id"] == idMarca:
                return marca["nombre"]

def getIdMarca(nombreMarca):
    with open(ARCHIVO_MARCAS, "r") as archivo:
        marcas = csv.DictReader(archivo)
        for marca in marcas:
            if marca["nombre"] == nombreMarca:
                return marca["id"]

def existeMarca(nombreMarca):
    existe = False
    with open(ARCHIVO_MARCAS, "r") as archivo:
        marcas = csv.DictReader(archivo)
        for marca in marcas:
            if marca["nombre"] == nombreMarca:
                existe = True
    return existe
