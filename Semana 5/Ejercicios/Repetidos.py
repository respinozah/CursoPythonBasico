import os

def main():
    os.system("cls")

    listaCantidadesRepetidos = []
    listaValoresRepetidos = []
    listaNumeros = (5, 8, 3, 1, 5, 7, 8, 2, 2, 5, 1, 0, 3, 7, 6, 4, 8, 9, 8)

    print(f"Tenemos una lista con los siguientes valores: {listaNumeros}\n\nEn esa lista sabemos que:")

    for numero in listaNumeros:
        if(listaNumeros.count(numero) > 1):
            if (numero in listaValoresRepetidos) == False:
                listaValoresRepetidos.append(numero)
                listaCantidadesRepetidos.append(listaNumeros.count(numero))

    for i in range(0, len(listaValoresRepetidos), 1):
        print(f"El numero {listaValoresRepetidos[i]} está repetido {listaCantidadesRepetidos[i]} veces.")

if __name__ == "__main__":
    main()