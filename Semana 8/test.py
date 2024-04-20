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