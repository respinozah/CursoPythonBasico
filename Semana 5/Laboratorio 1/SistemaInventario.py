import os
import pwinput

#Usuarios
usuarioAuthenticado = ""
usuarios = []
passwords = []
pin = []
rolesAsignados = []
roles = ("Administrador", "Almacen", "Cliente", "Proveedor")

#Inventario
articulosNombre = []
articulosCantidad = []

def main():
    os.system("cls")
    print(f"Sistema de inventario\n----------------------------\nBienvenid@ {usuarioAuthenticado}")

    if tienePermisoElUsuario(usuarioAuthenticado, "Agregar articulo"):
        print("1) Agregar articulo")
    
    if tienePermisoElUsuario(usuarioAuthenticado, "Actualizar articulo"):
        print("2) Actualizar articulo")

    if tienePermisoElUsuario(usuarioAuthenticado, "Eliminar articulo"):
        print("3) Eliminar articulo")

    if tienePermisoElUsuario(usuarioAuthenticado, "Imprimir inventario"):
        print("4) Imprimir el inventario completo")

    if tienePermisoElUsuario(usuarioAuthenticado, "Gestion de usuarios"):
        print("5) Gestion de usuarios")

    print("6) Salir\n")

    funcion = int(input("\nSeleccione una opcion: "))
    if funcion == 1:
        agregarAInventario()
    elif funcion == 2:
        actualizarCantidad()
    elif funcion == 3:
        removerDeInventario()
    elif funcion == 4:
        imprimirInventario()
    elif funcion == 5:
        gestionUsuarios()
    elif funcion == 6:
        os.system("cls")
        exit

def gestionUsuarios():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nGestion de usuarios\n")
    print("1) Agregar usuario\n2) Consultar usuarios\n3) Modificar rol de un usuario\n4) Eliminar usuario\n")
    funcion = int(input("\nSeleccione una opcion: "))

    if funcion == 1:
        agregarUsuario()
    elif funcion == 2:
        consultarUsuarios()
    elif funcion == 3:
        modificarRol()
    elif funcion == 4:
        eliminarUsuario()

    main()

def agregarUsuario():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nGestion de usuarios - Agregar usuario\n")
    usuario = str(input("Ingrese el usuario: "))
    password = str(input("Ingrese la contraseña: "))
    pinNuevo = int(input("Ingrese el pin: "))
    rol  = str(input("Ingrese el rol (Administrador, Almacen, Cliente, Proveedor): "))
    if not existeUsuario(usuario):
        usuarios.append(usuario)
        passwords.append(password)
        pin.append(pinNuevo)
        rolesAsignados.append(roles.index(rol))
        print(f"El usuario {usuario} con el rol {rol} fue agregado al sistema.")
    else:
        print(f"El usuario {usuario} ya existe, no se puede agregar.")
    input("\n\nPresione enter para continuar")

def consultarUsuarios():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nGestion de usuarios - Consulta de usuarios\n")
    print("Usuario    Rol")
    for indice, usuario in enumerate (usuarios):
        print(f"-{usuario}    {roles[rolesAsignados[indice]]}    ")
    print("----------------------------\n")
    input("\n\nPresione enter para continuar")

def modificarRol():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nGestion de usuarios - Modificar rol\n")
    usuario = str(input("Ingrese el usuario al que se le va a modificar su rol: "))
    if existeUsuario(usuario):
        rolSeleccionado = int(input(f"El usuario {usuario} tiene el rol {roles[rolesAsignados[usuarios.index(usuario)]]}.\nSeleccione el nuevo rol del usuario (1- Administrador, 2- Almacen, 3-Cliente, 4-Proveedor): "))
        if rolSeleccionado >= 1 or rolSeleccionado >= 4:
            rolesAsignados[usuarios.index(usuario)] = rolSeleccionado - 1
            print(f"El usuario {usuario} ahora tiene el rol de {roles[rolesAsignados[usuarios.index(usuario)]]}.")
        else:
            print("Seleccion invalida")
    else:
        print(f"El usuario usuario no existe en el sistema.")    
    input("\n\nPresione enter para continuar")

def eliminarUsuario():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nGestion de usuarios - Eliminar usuario\n")
    usuario = str(input("Ingrese el usuario que se va a eliminar: "))
    global usuarioAuthenticado
    if existeUsuario(usuario):
        if not usuario == usuarioAuthenticado:
            indice = usuarios.index(usuario)
            usuarios.pop(indice)
            passwords.pop(indice)
            pin.pop(indice)
            rolesAsignados.pop(indice)
            print(f"El usuario {usuario} ha sido eliminado del sistema.")
        else:
            print(f"El usuario authenticado no puede eliminarse a si mismo.")
    else:
        print(f"El usuario usuario no existe en el sistema.")    
    input("\n\nPresione enter para continuar")

def existeUsuario(usuario):
    existe = False
    for valor in usuarios:
        if valor == usuario:
            existe = True
            break
    return existe

def validarPassword(usuario, password):
    passwordValido = False
    if existeUsuario(usuario):
        if password == passwords[usuarios.index(usuario)]:
            passwordValido = True
    return passwordValido

def tienePermisoElUsuario(usuarioAuthenticado, permiso):
    tienePermiso = False
    indice = usuarios.index(usuarioAuthenticado)
    rolAsignado = rolesAsignados[indice]

    if permiso == "Agregar articulo":
        if rolAsignado == 0 or rolAsignado == 1:
            tienePermiso = True
    elif permiso == "Actualizar articulo":
        if rolAsignado == 0 or rolAsignado == 1 or rolAsignado == 2 or rolAsignado == 3:
            tienePermiso = True
    elif permiso == "Eliminar articulo":
        if rolAsignado == 0 or rolAsignado == 1:
            tienePermiso = True
    elif permiso == "Imprimir inventario":
        if rolAsignado == 0 or rolAsignado == 1 or rolAsignado == 2 or rolAsignado == 3:
            tienePermiso = True
    elif permiso == "Gestion de usuarios":
        if rolAsignado == 0:
            tienePermiso = True

    return tienePermiso

def removerDeInventario():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nRemover articulo del inventario\n")
    articulo = str(input("Ingrese el articulo que va a ser removido del inventario: "))
    if existeArticulo(articulo):
        confirmacion = str(input(f"¿Desea realmente eliminar el articulo {articulo} del inventario? (y/n)"))
        if confirmacion == "y" or confirmacion == "yes":
            indice = articulosNombre.index(articulo)
            unidades = articulosCantidad[articulosNombre.index(articulo)]
            articulosNombre.pop(indice)
            articulosCantidad.pop(indice)
            print(f"{unidades} unidades de {articulo} han sido removidas del inventario")
    else:
        print(f"El articulo {articulo} no existe en inventario.")
    input("\n\nPresione enter para continuar")
    main()

def actualizarCantidad():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nActualizar existencia de articulo\n")
    articulo = str(input("Ingrese el nombre del articulo que va a actualizar: "))
    cantidad = int(input(f"Ingrese la nueva cantidad de {articulo} que va a exister en el sistema: "))
    if existeArticulo(articulo):
        articulosCantidad[articulosNombre.index(articulo)] = cantidad
        print(f"El articulo {articulo} ahora tiene una existencia de {cantidad}.")
    else:
        print(f"\nEl articulo {articulo} no existe en inventario. Use la funcion agregar articulo para crear en el sistema.")
    input("\n\nPresione enter para continuar")
    main()

def agregarAInventario():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nAgregar articulo\n")
    nombre = str(input("Ingrese el nombre del articulo que desea agregar: "))
    cantidad = int(input(f"Ingrese la cantidad de {nombre} que va a almacenar: "))

    if existeArticulo(nombre):
        print("\nArticulo ya existe, por favor usar la funcion de modificar cantidad.")
    else:
        articulosNombre.append(nombre)
        articulosCantidad.append(cantidad)
        print(f"Se agregaron {cantidad} unidades de {nombre} al invetario. Por favor usar la funcion de imprimir inventario para verificar.")

    input("\n\nPresione enter para continuar")
    main()

def existeArticulo(nombre):
    articuloEncontrado = False
    for articulo in articulosNombre:
        if articulo == nombre:
            articuloEncontrado = True
            break
    return articuloEncontrado

def imprimirInventario():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nInventario completo\n")
    print("Articulo    Cantidad disponible")
    for indice, valor in enumerate (articulosNombre):
        print(f"-{valor}    {articulosCantidad[indice]}")
    print("----------------------------\n")
    input("\n\nPresione enter para continuar")
    main()

def login():
    os.system("cls")
    print("Sistema de inventarios\n----------------------------\nAutenticación\n")
    usuario = input("Ingrese su usuario: ")
    password = pwinput.pwinput(prompt ="Ingrese su contraseña: ", mask="*")
    pin = pwinput.pwinput(prompt ="Ingrese su pin: ", mask="#")
    authenticado = False
    global usuarioAuthenticado
    for indice, valor in enumerate (usuarios):
        if usuario == valor:
            if password == passwords[indice]:
                if pin == pin[indice]:
                    usuarioAuthenticado = usuario
                    authenticado = True
                    break
    return authenticado

def cargarTestData():
    usuarios.append("administrador")
    usuarios.append("almacen")
    usuarios.append("cliente")
    usuarios.append("proveedor")
    passwords.append("pass")
    passwords.append("pass")
    passwords.append("pass")
    passwords.append("pass")
    pin.append(1)
    pin.append(2)
    pin.append(3)
    pin.append(4)
    rolesAsignados.append(0)
    rolesAsignados.append(1)
    rolesAsignados.append(2)
    rolesAsignados.append(3)
    #roles = ("Administrador", "Almacen", "Cliente", "Proveedor")
    articulosNombre.append("Bicicleta")
    articulosNombre.append("Pantalla")
    articulosNombre.append("Cafetera")
    articulosCantidad.append(8)
    articulosCantidad.append(5)
    articulosCantidad.append(16)    


if __name__ == "__main__":
    cargarTestData()

    if login() == True:
        main()
    else:
        print("Usuario o contraseña invalidos.")

    main()