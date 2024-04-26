import csv
import os

ARCHIVO_USUARIOS = r"Proyecto\sum_usuarios.csv"

def getUsuariosActivos():
    # Verificar si el archivo csv existe
    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "w") as archivo:
            nuevoArchivo = csv.writer(archivo)
            nuevoArchivo.writerow(["id", "usuario", "password", "nombre", "apellido", "puesto", "estado"])
        return []

    # Crear lista de usuarios activos
    usuarios_activos = []
    with open(ARCHIVO_USUARIOS, "r") as archivo:
        usuarios = csv.DictReader(archivo)
        for usuario in usuarios:
            if usuario["estado"] == "activo":
                usuarios_activos.append({
                    "id": usuario["id"],
                    "nombre": usuario["nombre"],
                    "apellido": usuario["apellido"],
                    "usuario": usuario["usuario"],
                    "puesto": usuario["puesto"]
                })
    return usuarios_activos
