try:
    print(estudiantes)
except NameError as e:
    print("Variable no esta definida", e)


try:
    empleados=[1,2,3,4]
    print(empleados[3])
except IndexError as e:
    print("Indice fuera de rango", e)


#Diccionarios
try:
    diccionario_libros={"abc":1, "english":2}
    print(diccionario_libros["historia"])
except KeyError as e:
    print("Indice invalido", e)

#TypeError
try:
    "2" + 2
except TypeError as e:
    print("Diferentes tipos de dato", e)


#Value Error
try:
    int("estudiantes")
except ValueError as e:
    print("No se puede convertir string a entero", e)


#FileNotFound
try:
    open ("python.txt")
except FileNotFoundError as e:
    print("No existe el archivo")


#ZeroDivisionError
try:
    resultado = 2 / 0
except ZeroDivisionError as e:
    print("No se puede dividir por cero.")


#OverflowError
try:
    import math
    math.exp(10000)
except OverflowError as e:
    print("Operacion muy grande")


#ConectionError
try:
    import requests
    requests.get("url_estudiantes_python")
except ConnectionError as e:
    print("URL invalida")