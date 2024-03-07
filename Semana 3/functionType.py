def main():
    numero = 5
    print(type(numero))

    nombre = "Pepe"
    print(type(nombre))

    listaObjetos=[1,2,3]
    print(type(listaObjetos))

    x = type("Practica", (object,), {"atributos":""})
    print(type(x))

if __name__ == "__main__":
    main()
