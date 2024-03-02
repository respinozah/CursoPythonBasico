nombrePoducto = input("Ingrese su producto deseado: ")
cantProducto = int(input("Ingrese la cantidad de unidades que desea adquirir: "))
precioProducto = float(input("Ingrese el precio unitario del producto: "))
totalCuenta = precioProducto*cantProducto

if totalCuenta > 1000:
    totalCuenta = totalCuenta-(totalCuenta*0.15)

print("La cuenta por la compra de ", cantProducto, " unidades de ", nombrePoducto, " es de ", totalCuenta, ".")