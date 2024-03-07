import os


def main():
    os.system("cls")

    calificacion = float(input("Conversion de calificaciones\nIngrese la calificacion (Un valor del 1 al 100): "))
    calificacionEnLetra = ""

    if (calificacion >= 0) and (calificacion <= 100):
        if (calificacion >= 93 and calificacion <= 100):
            calificacionEnLetra = "A"
        elif (calificacion >= 90 and calificacion <= 92.99):
            calificacionEnLetra = "A-"
        elif (calificacion >= 87 and calificacion <= 89.99):
            calificacionEnLetra = "B+"
        elif (calificacion >= 83 and calificacion <= 86.99):
            calificacionEnLetra = "B"
        elif (calificacion >= 80 and calificacion <= 82.99):
            calificacionEnLetra = "B-"
        elif (calificacion >= 77 and calificacion <= 79.99):
            calificacionEnLetra = "C+"
        elif (calificacion >= 73 and calificacion <= 76.99):
            calificacionEnLetra = "C"
        elif (calificacion >= 70 and calificacion <= 72.99):
            calificacionEnLetra = "C-"
        elif (calificacion >= 67 and calificacion <= 69.99):
            calificacionEnLetra = "D+"
        elif (calificacion >= 60 and calificacion <= 66.99):
            calificacionEnLetra = "D"
        elif (calificacion >= 0 and calificacion <= 59.99):
            calificacionEnLetra = "F"
        print(f"La calificacion por letra es {calificacionEnLetra}.")
    else:
        print("-Valor invalido, la calificacion debe ser un numero entre 1 y 100.")

if __name__ == "__main__":
    main()