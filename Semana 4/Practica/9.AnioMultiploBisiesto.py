import os

def main():
    os.system("cls")
    
    anio = int(input("Ingrese un año: "))
    if anio > 0:

        siglo = anio

        if esBisiesto(anio):
            print(f"El año {anio} es bisiesto.")
        else:
            print(f"El año {anio} no es bisiesto.")

def esBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()