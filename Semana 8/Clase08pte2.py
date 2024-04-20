################################################################
# Lectura
# r
#abrir un archivo para que pueda ser leido
archivo_python = open ("ruta del archivo datos.txt", "r") # "r" para poder leer

#lectura
lectura_archivo = archivo_python.read()
print("lineas del archivo")
print(lectura_archivo)

archivo_python.close()

################################################################
# Escritura
# w
archivo_python = open ("ruta del archivo datos.txt", "w") # "w" para poder escribir
archivo_python.write("Bienvenidos\nHola")
archivo_python.write("Mas valores")
archivo_python.close()

################################################################
# Append
# a
archivo_python = open ("ruta del archivo datos.txt", "a") # "a" para poder agregar al final del archivo
archivo_python.write("Esto se añadira al archivo")
archivo_python.close()

################################################################
# leer y escribir
# r+
archivo_python = open ("ruta del archivo datos.txt", "r+") # "r+" para poder leer y actualizar el archivo
lectura_archivo = archivo_python.read()
print("leer el contenido del archivo")
print(lectura_archivo)
# escribir desde el inicio del archivo
archivo_python.write("adiciono mas contenido en el archivo.")

archivo_python.seek(0)
#The seek() method sets the current file position in a file stream.
#The seek() method also returns the new postion.

nuevo_contenido_archivo = archivo_python.read()
print("Archivo actualizado")
print(nuevo_contenido_archivo)

nuevo_contenido_archivo.close()

################################################################
# leer y sobreescribir
# w+
with open ("ruta del archivo", "w+") as puntero: # "w+" para poder leer y sobreescribir el archivo
    puntero.write("Sobreescribir el archivo")
    puntero.seek(0)
    archivo_Actualizado = puntero.read()
    print("Archivo actualizado")

################################################################
# agregar y leer
# a+
with open("ruta del archivo", "a+") as puntero:
    puntero.write("Nuevo Elemento")
    puntero.seek(0)
    informacion = puntero.read()
    print(informacion)


################################################################
# lectura y escritura binaria
# wb+
with open ("ruta del archivo", "wb+") as archivo_nuevo:
    archivo_nuevo.write(b"Informacion del archivo binario")
    archivo_nuevo.seek(0)
    informacion_Archivo = archivo_nuevo.read()
    print(informacion_Archivo)


################################################################
# lectura y agregar a archivo binaria
# ab+
with open ("ruta del archivo", "wb+") as archivo_nuevo:
    archivo_nuevo.write(b"Agregar informacion al archivo binario")
    archivo_nuevo.seek(0)
    informacion = archivo_nuevo.read()
    print("Contenido del nuevo archivo binario, adicionando una fila", informacion)


################################################################
# crea archivo para escribirlo y si esciste un archivo como tal falla o lo podemos capturar ese error con FileExistsError
# x
try:
    with open("ruta del archivo", "x") as archivo_empleados:
        archivo_empleados.write("Juan de Costa Rica")
        print("El archivo se almaceno en la ubicacion especificada")
except FileExistsError:
    print("No podemos crear el archivo, ya que el mismo esta en la ubicacion.")


################################################################
# Calculos matematicos y guardarlos en un archivo
# 
def calculadora (archivo_Calculadora):
    numero1 = 30
    numero2 = 50

    suma = numero1 + numero2
    resta = numero2 - numero1
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    with open(archivo_Calculadora, "w") as calculadora:
        calculadora.write(f"Suma: {suma}")
        calculadora.write(f"Resta: {resta}")
        calculadora.write(f"Multiplicacion: {multiplicacion}")
        calculadora.write(f"Division: {division}")

    print("Los calculos fueron guardados exitosamente", archivo_Calculadora)

archivo_Calculadora = "Calculadora.txt"
calculadora(archivo_Calculadora)


################################################################
# Lectura de ubicacion de un archivo
# 
import os

def buscar_ruta_archivo(nombre_imagen):
    directorio = os.path.dirname(__file__)
    imagen_direccion = os.path.join(directorio, nombre_imagen)
    return imagen_direccion

nombre_imagen = "python.jpg"
ruta_imagen = buscar_ruta_archivo(nombre_imagen)
print ("Mi ruta de archivo de imagenes la siguiente: ", ruta_imagen)


################################################################
# Ejercicio
#
print("Alamcenar una lista de palabras")

palabra1 = "Perro"
palabra2 = "Canasta"
palabra3 = "Silla"
palabra4 = "Flores"
palabra5 = "Lampara"

try:
    with open("listaPalabras.txt", "w") as archivo:
        archivo.write("Palabra 1: ", palabra1)
        archivo.write("Palabra 2: ", palabra2)
        archivo.write("Palabra 3: ", palabra3)
        archivo.write("Palabra 4: ", palabra4)
        archivo.write("Palabra 5: ", palabra5)

    print("Palabras guardadas en el archivo.")
except FileNotFoundError:
    print("El archivo de palabras no existe.")


################################################################
# consola de windows (instruccion: pip install pillow)
#
from PIL import Image

def lectura_de_imagen (imagen_ruta):
    try:
        imagen = Image.open(imagen_ruta)
        print("Informacion de la imagen")
        print("Formato: ", imagen.format)
        print("Dimensiones: ", imagen.size)
        imagen.show()
    except FileNotFoundError:
        print("No se encuentra ese archivo en la ubicacion", imagen_ruta)
    except Exception as e:
        print("Existe un error al consultar la imagen.", e)
        
imagen_ruta = "C:\gitcourses\python\Semana 8\Python-logo-notext.svg.png"
lectura_de_imagen(imagen_ruta)

################################################################
# mover imagen entre directorios o sobreescribirla
#
from PIL import Image

def moverImagen(ruta_archivo, ruta_nueva):
    try:
        imagen = Image.open(ruta_archivo)
        imagen.save(ruta_nueva)
        print("Image guardada existosamente en", ruta_nueva)
    except FileNotFoundError:
        print("archivo no encontrado", ruta_archivo)
    except Exception as e:
        print("Ocurrio un error")

imagen_ruta = "C:\gitcourses\python\Semana 8\Python-logo-notext.svg.png"
ruta_nueva = "C:\gitcourses\python\Semana 8\nuevaRuta\Python.svg.png"
moverImagen(imagen_ruta, ruta_nueva)