import os

diccionarioPalabras = {}

def main():
    os.system("cls")

    texto = str(input("Ingrese el text a evaluar: "))

    listaPalabras = texto.split()

    for indice, palabra in enumerate (listaPalabras):
        if existePalabraEnDiccionario(palabra):
            diccionarioPalabras[palabra] = diccionarioPalabras[palabra] + 1
        else:
            diccionarioPalabras.update({palabra:1})
    
    printConteoPalabras()

def printConteoPalabras():
    for indice, palabra in enumerate (diccionarioPalabras):
        print(f"La palabra {palabra} aparece {diccionarioPalabras[palabra]} veces en el texto")

def existePalabraEnDiccionario(palabra):
    if palabra in diccionarioPalabras:
        return True
    else:
        return False

if __name__ == "__main__":
    main()