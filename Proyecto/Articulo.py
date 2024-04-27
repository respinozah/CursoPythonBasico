import csv
import Util

ARCHIVO_ARTICULOS = r"Proyecto\sum_articulos.csv"

def getArticulos():
    # Verificar si el archivo csv existe
    if not Util.existeArchivo(ARCHIVO_ARTICULOS):
        with open(ARCHIVO_ARTICULOS, "w") as archivo:
            nuevoArchivo = csv.writer(archivo)
            nuevoArchivo.writerow(["id", "nombre", "descripcion", "idMarca", "estado", "presentacion", "stock", "costoUnitario", "fechaCreacion", "fechaActualizacion"])
        return []

    # Crear lista de artículos activos
    articulos_activos = []
    with open(ARCHIVO_ARTICULOS, "r") as archivo:
        articulos = csv.DictReader(archivo)
        for articulo in articulos:
            if articulo["estado"] == "activo":
                articulos_activos.append({"id": articulo["id"],"nombre": articulo["nombre"],"descripcion": articulo["descripcion"],"idMarca": articulo["idMarca"],"estado": articulo["estado"],"presentacion": articulo["presentacion"],"stock": articulo["stock"],"costoUnitario": articulo["costoUnitario"],"fechaCreacion": articulo["fechaCreacion"],"fechaActualizacion": articulo["fechaActualizacion"]})
    return articulos_activos

def crearArticulo(articulop):
    # Calcular el siguiente Id
    siguienteId = 0
    if Util.existeArchivo(ARCHIVO_ARTICULOS):
        with open(ARCHIVO_ARTICULOS, "r") as archivo:
            articulos = csv.DictReader(archivo)
            for articulo in articulos:
                siguienteId = max(siguienteId, int(articulo["id"]))
    siguienteId = siguienteId + 1
    
    # Agregar el nuevo artículo al archivo CSV
    with open(ARCHIVO_ARTICULOS, "a", newline='') as archivo:
        nuevoArticulo = csv.writer(archivo)
        nuevoArticulo.writerow([siguienteId, articulop["nombre"], articulop["descripcion"], articulop["idMarca"], articulop["estado"], articulop["presentacion"], articulop["stock"], articulop["costoUnitario"], articulop["fechaCreacion"], articulop["fechaActualizacion"]])

def actualizarArticulo(idArticulo, datosArticulo):
    articulosActualizados = []

    with open(ARCHIVO_ARTICULOS, "r") as archivo:
        articulos = csv.DictReader(archivo)
        for articulo in articulos:
            if articulo["id"] == idArticulo:
                articulo.update(datosArticulo)
            articulosActualizados.append(articulo)

    with open(ARCHIVO_ARTICULOS, "w", newline='') as archivo:
        escritor = csv.DictWriter(archivo, ["id", "nombre", "descripcion", "idMarca", "estado", "presentacion", "stock", "costoUnitario", "fechaCreacion", "fechaActualizacion"])
        escritor.writeheader()
        escritor.writerows(articulosActualizados)

def consultarArticulo(idArticulo):
    articuloConsultado = {}
    with open(ARCHIVO_ARTICULOS, "r") as archivo:
        articulos = csv.DictReader(archivo)
        for articulo in articulos:
            if articulo["id"] == idArticulo:
                articuloConsultado = articulo
                break
    return articuloConsultado
