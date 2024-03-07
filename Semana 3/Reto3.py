def main():
    print("Login\n")

    user = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
    secondFA = int(input("Ingrese su token: "))

    if((user == "osvaldo" and password == "pass1") or (user == "david" and password == "pass2")):
        if((user == "osvaldo" and secondFA == 111) or (user == "david" and secondFA == 222)):
            print("Bienvenido. Tiene acceso a toda la información.")
        else:
            print("Token invalido")
    else:
        print("Hubo un error de los datos suministrados, favor volver a intentar.")

if __name__ == "__main__":
    main()
