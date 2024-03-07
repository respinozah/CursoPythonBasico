def main():
    numero1 = float(input("Insgrese el primer numero: "))
    numero2 = float(input("Insgrese el primer numero: "))
    operacion = int(input("Las operaciones disponibles son:\n1 - Suma\n2 - Resta\n3 - Multiplicacion\n4 - Division\n5 - Division entera\n6 - Potencia\nPor favor seleccionar una operacion: "))
    nombreOperacion = ""
    resultadoOperacion = 0
    
    if operacion == 1: #suma
        nombreOperacion = "suma"
        resultadoOperacion = numero1 + numero2
    elif operacion == 2: #resta
        nombreOperacion = "resta"
        resultadoOperacion = numero1 - numero2
    elif operacion == 3: #multiplicacion
        nombreOperacion = "multiplicacion"
        resultadoOperacion = numero1 * numero2
    elif operacion == 4: #division
        nombreOperacion = "division"
        resultadoOperacion = numero1 / numero2
    elif operacion == 5: #division entera
        nombreOperacion = "division entera"
        resultadoOperacion = numero1 // numero2
    elif operacion == 6: #potencia
        nombreOperacion = "potencia"
        resultadoOperacion = numero1 ** numero2
    else:
        print("Operacion invalida")

    if(operacion >= 1 and operacion <= 6):
        print(f"El resultado de la {nombreOperacion} es {resultadoOperacion}.")

if __name__ == "__main__":
    main()