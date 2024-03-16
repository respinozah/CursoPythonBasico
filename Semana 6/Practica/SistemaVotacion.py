import os

diccionarioVotos = {"Candidato A":0, "Candidato B":0, "Candidato C":0, "Candidato D":0}

def main():
    os.system("cls")
    print("Sistema de votacion \nSeleccione una opcion:\n1) Votar\n2) Ver resultados\n3)Salir\n")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        votar()
    elif opcion == 2:
        verResultados()
    elif opcion == 3:
        os.system("cls")
        exit

def votar():
    input("\n\nPresione enter para continuar")
    main()

def verResultados():
    input("\n\nPresione enter para continuar")
    main()

if __name__ == "__main__":
    main()