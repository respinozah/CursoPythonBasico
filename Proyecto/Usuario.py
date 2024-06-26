import csv
import os

ARCHIVO_USUARIOS = r"Proyecto\sum_usuarios.csv"

def login(usuariop, passwordp):
    autenticado = False
    with open(ARCHIVO_USUARIOS, "r") as archivo:
        usuarios = csv.DictReader(archivo)
        for usuario in usuarios:
            if usuario["usuario"] == usuariop and usuario["password"] == passwordp and usuario["estado"] == "activo":
                autenticado = True
    return autenticado


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

def crearUsuario(usuariop):
    #Calcular el siguiente Id
    siguienteId = 0
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            usuarios = csv.DictReader(archivo)
            for usuario in usuarios:
                siguienteId = max(siguienteId, int(usuario["id"]))
    siguienteId = siguienteId + 1

    #Agregar el nuevo usuario al archivo CSV
    with open(ARCHIVO_USUARIOS, "a", newline='') as archivo:
        nuevoUsuario = csv.writer(archivo)
        nuevoUsuario.writerow([siguienteId, usuariop["usuario"], usuariop["password"], usuariop["nombre"], usuariop["apellido"], usuariop["puesto"], "activo"])

def actualizarUsuario(idUsuario, datosUsuario):
    usuariosActualizados = []

    with open(ARCHIVO_USUARIOS, "r") as archivo:
        usuarios = csv.DictReader(archivo)
        for usuario in usuarios:
            if usuario["id"] == idUsuario:
                usuario.update(datosUsuario)
            usuariosActualizados.append(usuario)

    with open(ARCHIVO_USUARIOS, "w", newline='') as archivo:
        escritor = csv.DictWriter(archivo, ["id", "usuario", "password", "nombre", "apellido", "puesto", "estado"])
        escritor.writeheader()
        escritor.writerows(usuariosActualizados)


def consultarUsuario(idUsuario):
    usuarioConsultado = {}
    with open(ARCHIVO_USUARIOS, "r") as archivo:
        usuarios = csv.DictReader(archivo)
        for usuario in usuarios:
            if usuario["id"] == idUsuario:
                usuarioConsultado = {"id": usuario["id"],"nombre": usuario["nombre"],"apellido": usuario["apellido"],"usuario": usuario["usuario"],"password": usuario["password"],"puesto": usuario["puesto"],"estado": usuario["estado"]}
                break

    return usuarioConsultado