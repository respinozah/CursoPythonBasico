import math
import os

def main():
    os.system("cls")
    cantEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))

    aprobados = 0
    reprobados = 0
    notaMayor = 0
    notaMenor = 0

    for i in range(1, (cantEstudiantes + 1)):
        notaEstudiante = int(input(f"Ingrese la nota del estudiante {i}: "))

        if notaEstudiante >= 70:
            aprobados += 1
        else:
            reprobados += 1

        if notaEstudiante > notaMayor:
            notaMayor = notaEstudiante

        if notaEstudiante < notaMenor or notaMenor == 0:
            notaMenor = notaEstudiante

    print(f"La cantidad de estudiantes aprobados es: {aprobados}.")
    print(f"La cantidad de estudiantes reprobados es: {reprobados}.")
    print(f"La nota mayor es: {notaMayor}.")
    print(f"La nota menos es: {notaMenor}.")

def login():
    os.system("cls")
    print("Login\n-------")
    user = str(input("Usuario: "))
    password = str(input("Password: "))
    pin = int(input("Pin: "))
    if user == "profesor" and password == "123" and pin == 1:
        return True

def cargarTestData():
    print("")

if __name__ == "__main__":
    if login():
        main()