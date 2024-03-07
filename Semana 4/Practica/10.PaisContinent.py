import os

def main():
    os.system("cls")
    
    pais = str(input("Por favor ingrese el nombre del pais: "))
    continente = ""

    if pais == "Ecuador":
        continente = "América"
    elif pais == "Costa Rica":
        continente ="América"
    elif pais == "China":
        continente ="Asia"
    elif pais == "Italia":
        continente ="Europa"
    elif pais == "Australia":
        continente ="Oceanía"
    else:
        print(f"-El pais {pais} no esta registrado en el sistema.")
    
    if continente != "":
        print(f"El pais {pais} esta en el continente {continente}.")
    
if __name__ == "__main__":
    main()