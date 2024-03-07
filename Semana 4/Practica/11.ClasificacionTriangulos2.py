import os

def main():
    os.system("cls")
    
    print("-Clasificacion de triangulos 2-")
    
    ladoA = float(input("Ingrese la medida del lado A: "))
    ladoB = float(input("Ingrese la medida del lado B: "))
    ladoC = float(input("Ingrese la medida del lado C: "))
    
    ladoaAlCuadrado = ladoA ** 2
    ladobAlCuadrado = ladoB ** 2
    ladocAlCuadrado = ladoC ** 2

    if ladoaAlCuadrado + ladobAlCuadrado == ladocAlCuadrado or ladobAlCuadrado + ladocAlCuadrado == ladoaAlCuadrado or ladoaAlCuadrado + ladocAlCuadrado == ladobAlCuadrado:
        clasificacion = "Rectangulo"
    elif ladoaAlCuadrado + ladobAlCuadrado < ladocAlCuadrado or ladobAlCuadrado + ladocAlCuadrado < ladoaAlCuadrado or ladoaAlCuadrado + ladocAlCuadrado < ladobAlCuadrado:
        clasificacion = "Obtusangulo"
    else:
        clasificacion = "Acutangulo"

    print(f"El triangulo con las medidas {ladoA}, {ladoB} y {ladoC} es un triangulo {clasificacion}.")
    

if __name__ == "__main__":
    main()