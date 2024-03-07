import os

def main():
    clear()
    print("Bienvenid@\n\n--Menu principal")
    sistemaSeleccionado = int(input("\nSeleccione una opcion:\n  1) Plan de dietas\n  2) Casino\n  3) Venta de repuestos\n  4) Salir\n\n Opcion: "))
    if sistemaSeleccionado == 1:
        planDietas()
    elif sistemaSeleccionado == 2:
        casino()
    elif sistemaSeleccionado == 3:
        ventaRepuestos()
    elif sistemaSeleccionado == 4:
        exit

def login():
    clear()
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
    if ((user == "user") and (password == "1111")):
        return True
    else:
        return False

def planDietas():
    clear()
    print("--Plan de dietas\n")
    diaDeLaSemana = str(input("Por favor indicar que dia es hoy: "))
    if diaDeLaSemana == "lunes":
        print("El desayuno del lunes es: Avena y frutas tropicales")
    elif diaDeLaSemana == "lartes":
        print("El desayuno del martes es: Yogurt y frutas secas")
    elif diaDeLaSemana == "miercoles":
        print("El desayuno del miércoles es: Café y galletas saladas")
    elif diaDeLaSemana == "jueves":
        print("El desayuno del jueves es: Barra energética y jugo de naranja")
    else:
        print("El día es incorrecto")
    
    input("\n\nPresione enter para continuar")
    main()

def casino():
    clear()
    print("--Casino\n")
    reto1 = False
    reto2 = False
    reto3 = False
    reto4 = False
    reto5 = False

    respuesta = int(input("Cuanto es 3 * 9? ")) #Reto 1
    if (reto(3, 9, "multiplicacion", respuesta)):
        reto1 = True
        print("Primer reto ganado.\n")
        respuesta = int(input("Cuanto es 2 + 6? ")) #Reto 2
        if (reto(2, 6, "suma", respuesta)):
            reto2 = True
            print("Segundo reto ganado.\n")
            respuesta = int(input("Cuanto es 4 - 3? ")) #Reto 3
            if (reto(4, 3, "resta", respuesta)):
                reto3 = True
                print("Tercer reto ganado.\n")
                respuesta = int(input("Cuanto es 18 / 3? ")) #Reto 4
                if (reto(18, 3, "division", respuesta)):
                    reto4 = True
                    print("Cuarto reto ganado.\n")
                    respuesta = int(input("Cuanto es 10 + 3? ")) #Reto 5
                    if (reto(10, 3, "suma", respuesta)):
                        reto5 = True
                        print("Quinto reto ganado.\n")
                    else:
                        print("Realice de nuevo el reto # 5.")
                        exit
                else:
                    print("Realice de nuevo el reto # 4.")
                    exit
            else:
                print("Realice de nuevo el reto # 3.")
                exit
        else:
            print("Realice de nuevo el reto # 2.")
            exit
    else:
        print("Realice de nuevo el reto # 1.")
        exit

    if reto1 == True and reto2 == True and reto3 == True and reto4 == True and reto5 == True:
        print("Siguiente Nivel!")

    input("\n\nPresione enter para continuar")
    main()

def reto(valor1, valor2, operacion, respuesta):
    retoGanado = False
    if(operacion == "suma" and (respuesta == (valor1 + valor2))):
        retoGanado = True
    if(operacion == "resta" and (respuesta == (valor1 - valor2))):
        retoGanado = True
    if(operacion == "multiplicacion") and (respuesta == (valor1 * valor2)):
        retoGanado = True
    if(operacion == "division" and (respuesta == (valor1 / valor2))):
        retoGanado = True
    return retoGanado

def ventaRepuestos():
    clear()
    print("--Venta de repuestos\n  ¡Hoy promociones de aniversario!")

    sistemaSeleccionado = int(input("\nSeleccione una opcion:\n  1) Repuestos para el motor\n  2) Repuestos accesorios\n  3) Repuestos para limpieza del auto\n  4) Repuestos para frenos\n\n Opcion: "))
    montoCompra = 0
    descuento = 0
    tipo = ""
    if sistemaSeleccionado == 1:
        print("Los repuestos para el motor tienen un 15% de descuento.")
        descuento = 15
        tipo = "repuestos para el motor"
    elif sistemaSeleccionado == 2:
        print("Los repuestos para accesorios tienen un 10% de descuento.")
        descuento = 10
        tipo = "repuestos para accesorios"
    elif sistemaSeleccionado == 3:
        print("Los repuestos para limpieza del auto tienen un 5% de descuento.")
        descuento = 5
        tipo = "repuestos para limpieza del auto"
    elif sistemaSeleccionado == 4:
        print("Los repuestos para frenos tienen un 3% de descuento.")
        descuento = 3
        tipo = "repuestos para frenos"

    montoCompra = float(input(f"-Ingrese el monto de la compra de {tipo}:"))
    montoCompra = calcularDescuento(montoCompra, descuento)
    print(f"El monto de la compra de {tipo} con descuento es de {montoCompra}.")

    input("\n\nPresione enter para continuar")
    main()

def calcularDescuento(montoCompra, descuento):
    totalCuentaConDescuento = montoCompra - ((montoCompra * descuento)/100)
    return totalCuentaConDescuento

def clear():
    os.system("cls")

if __name__ == "__main__":
    if login() == True:
        main()
    else:
        print("Usuario o contraseña invalidos.")