import os

def main():
    os.system("cls")

    print("-Clasificacion de triangulos-")
    
    base = float(input("Ingrese la medida de la base: "))
    altura = float(input("Ingrese la medida de la altura: "))
    clasificacion = "Escaleno"

    if (base == altura):
        clasificacion = "Equilatero"
    elif (altura >= base):
        clasificacion = "Isosceles"
    
    print(f"\n- El triango con base {base} y altura {altura} es un triangulo {clasificacion}.")

if __name__ == "__main__":
    main()