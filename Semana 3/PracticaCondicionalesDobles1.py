precioEntrada = 1600
print(f"Compra de entradas para parques nacionales. El valor de la entrada para adultos es de ${precioEntrada}")

edad = int(input("Por favor indicar su edad: "))

if (edad >= 18):
    print(f"El monto a pagar es ${precioEntrada}")
else:
    print("Los niños no pagan entrada.")
