def suma(numero1, numero2):
    return numero1 + numero2

resultadosuma = suma(60, 7)
print(f"La suma es {resultadosuma}.")




def funcionQueAplica(cuadrado, valor):
    return cuadrado(valor)
    
def cuadrado (numero):
    return numero ** 2



def encontrarNumeroMayor (numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2



def realizarSaludo (nombrePersona, saludar="Hola, Bievenido al sistema"):
    print(f"{saludar} {nombrePersona}")

realizarSaludo("Beto")