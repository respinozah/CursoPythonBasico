import os

def existeArchivo(ruta):
    return os.path.exists(ruta)

def remover_comas(valor):
    return valor.replace(",", "")
