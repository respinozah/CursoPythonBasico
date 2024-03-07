import os

def main():
    os.system("cls")
    tuplaLibros = ("Cien años de soledad", "Ejercicios de algebra", "Recetas de Tia Florita", "Historia natural", "Novela epica", "Poemas volados", "Coaching for coaches",)
    
    print("Biblioteca\n\nLos libros disponibles son:")
    for i in range(0, len(tuplaLibros), 1):
        print(f" {i+1} - {tuplaLibros[i]}")

    libroSeleccionado = int(input("\n\nPor favor selecione un libro de la lista: "))
    print(f"-Usted ha seleccionado el libro: {tuplaLibros[libroSeleccionado-1]}.\n Gracias\n")

def login():
    os.system("cls")
    validLogin = False
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
    pin = int(input("Ingrese su pin de seguridad: "))
    if ((user == "user") and (password == "1111")):
        if(pin == 22):
            validLogin = True
    return validLogin

if __name__ == "__main__":
    if login() == True:
        main()
    else:
        print("Usuario o contraseña invalidos.")