import os

def main():
    os.system("cls")
    
    numero = int(input("Ingrese un numero: "))
    tipoNatural = ""
    contadorDivisores = 0

    if numero >= 0:
        for i in range(1, numero + 1):
            residuo = numero % i
            #print(f"El residuo de {numero} entre {i} es igual a {residuo}")
            if residuo == 0:
                contadorDivisores = contadorDivisores + 1

        if contadorDivisores == 2:
            tipoNatural = "es primo"
        else:
            tipoNatural = "no es primo"


    print(f"El número {numero} {tipoNatural}.")

if __name__ == "__main__":
    main()