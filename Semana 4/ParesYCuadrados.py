import math

def main():
    print("Numeros del 20 al 40 y sus cuadrados")
    for i in range(20,41):
        if es_par(i):
            print(f"El numero {i} es par y el cuadrado es {math.pow(i, 2)}.")

def es_par(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    main()