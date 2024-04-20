try:
    resultado = 5 / 0
except ZeroDivisionError:
    print("¡No puedes dividir entre cero!")


try:
    numero = int(input("Ingresa un numero: "))
except ValueError:
    print("Debes ingresar un numero valido.")


try:
    valor = int("hola")
except ValueError:
    print("No se peude convertir 'hola' a entero.")


lista = [1, 2, 3]
try:
    print(lista[4])
except IndexError:
    print("Indice fuera de rango")


diccionado = {"a":1, "b":2}
try:
    print(diccionado["c"])
except KeyError:
    print("La clave 'c' no existe en el diccionario.")


try:
    resultado = "a" + 5
except TypeError:
    print("Operacion no valida entre str e int.")


try:
    resultado = "a" / "b"
except TypeError:
    print("Operacion no valida entre str y str.")


try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")


try:
    import modulo_inexistente
except ImportError:
    print("El modulo no esta instalado o no se puede importar")


