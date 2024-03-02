def main():
    #Nota del estudiante
    nota = int(input("Ingrese la nota: "))

    if nota >= 70:
        print("Aprobado")
        print("")
    elif nota <= 60:
        print("Aplazado")
    else:
        print("Reprobado")

    print("If anidado")

if __name__ == "__main__":
    main()