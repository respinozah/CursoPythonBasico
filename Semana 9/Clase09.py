import csv

lista = [
    ["Nombre", "Edad", "Correo"]
    ["Juan", 30, "juan@mail.com"]
    ["Maria", 25, "maria@mail.com"]
]

with open ("informacion.csv", "w", newline="") as archivo:
    escritura_csv = csv.writer(archivo_csv)
    for registro in archivo:
        escritura_csv.writerow(registro)

with open ("informacion.csv", "r") as archivo:
    lectura = csv.reader(archivo)
    for registro in lectura:
        print(registro)

#------------------------------------------------------------------------------
#Escribir informacion en un archivo csv desde un diccionario
import csv

informacion_empleados = [
    {"Nombre":"Vane", "Edad":30},
    {"Nombre":"Juan", "Edad":35},
    {"Nombre":"Andrea", "Edad":17}
]

with open ("informacion_empleados.csv", "w", newline="") as archivo:
    encabezado = ["Nombre", "Edad"]
    empleados = csv.DictWriter (archivo, fieldnames=encabezado)
    empleados.writeheader()
    empleados.writerow(informacion_empleados)


#------------------------------------------------------------------------------
#JSON - crud
#------------------------------------------------------------------------------

#Escritura
import json

empleados = {
    "Nombre":"Ricardo",
    "Edad":25,
    "correo":"ricardo@mail.com"
}

with open ("empleados.json", "w") as archivo:
    json.dump(empleados, archivo)

#Lectura
import json

with open("empleados.json", "r") as archivo:
    lectura_archivo = json.load(archivo)
    print(lectura_archivo)

#Conversion de diccionario a json y viceversa
#diccionario -> json
diccionario = {"Nombre": "Vane", "Edad":20}
convertir_diccionario = json.dumps(diccionario)
print(convertir_diccionario)

#json -> diccionario
informacion_json = '{"Nombre": "Vane", "Edad":20}'
diccionario = json.load(informacion_json)
print(diccionario)


#------------------------------------------------------------------------------
#OS - crud
#------------------------------------------------------------------------------
import os

archivo="archivo.txt"
os.remove(archivo)
print(f"Archivo {archivo} eliminado")

#variables de entorno
#=variables_entorno= = os.environ 

#cambiar el directorio
import os

archivo_viejo ="archivo.txt"
nuevo_archivo="empleados.txt"
os.rename(archivo_viejo, nuevo_archivo)
