import os

class Empleado:
    def __init__(self, idEmpleado, nombre, puesto, salario):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    
    def __str__(self):
        return f"ID:{self.idEmpleado}, Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}."

class SistemaEmpleados:
    def __init__(self):
        self.empleados=[]
        self.archivo_empleados="empleados.txt"

    def cargarEmpleados(self):
        try:
            with open (self.archivo_empleados, "r") as archivo:
                for linea in archivo:
                    idEmpleado, nombre, puesto, salario = linea.strip().split(",")
                    empleado = Empleado(idEmpleado, nombre, puesto, salario)
                    self.empleados.append(empleado)
        except FileNotFoundError:
            open("empleados.txt", "x")
            print("El archivo no se encuentra. Se creara uno nuevo.")

    def guardarEmpleados(self):
        try:
            with open(self.archivo_empleados, "w") as archivo:
                for empleado in self.empleados:
                    archivo.write(f"{empleado.idEmpleado},{empleado.nombre},{empleado.puesto},{empleado.salario}\n")
        except FileNotFoundError:
            print("El archivo no se encuentra. Se creara uno nuevo.")

    def buscarEmpleado(self, idEmpleadop):
        encontrado= False
        for empleado in self.empleados:
            if empleado.idEmpleado == idEmpleadop:
                encontrado = True
                print(f"Se encontro el empleado {idEmpleadop}.")
                print("Los detalles del empleado son ", empleado)
                break
        
        if not encontrado:
            print(f"No existe el empleado {idEmpleadop}.")

    def actualizarEmpleado (self, idEmpleadop, nombrep, puestop, salariop):
        encontrado = False
        for empleado in self.empleados:
            if empleado.idEmpleado == idEmpleadop:
                print(f"Empleado {empleado.idEmpleado} fue encontrado.")
                empleado.nombre = nombrep
                empleado.puesto = puestop
                empleado.salario= salariop
                self.guardarEmpleados()
                print(f"El empleado {empleado.idEmpleado} fue actualizado.")
                encontrado = True
                break
        if not encontrado:
            print(f"El empleado {idEmpleadop} no existe.")

    def eliminarEmpleado(self, idEmpleadop):
        eliminado = False
        for empleado in self.empleados:
            if empleado.idEmpleado == idEmpleadop:
                confirmacion=input(f"Esta seguro que desea eliminar el empleado {empleado.nombre}? (S/N)")
                if confirmacion.lower() == "s":
                    self.empleados.remove(empleado)
                    self.guardarEmpleados()
                    print(f"El empleado {empleado.idEmpleado} {empleado.nombre} ha sido eliminado.")
                    eliminado = True
                    break
                else:
                    print("Solicitud de eliminacion cancelada")
            #if not eliminado:
            #    print(f"El empleado {empleado.idEmpleado} no ha sido encontrado.")

    def registrarEmpleado(self, idEmpleadop, nombrep, puestop, salariop):
        nuevoEmpleado = Empleado(idEmpleadop, nombrep, puestop, salariop)
        self.empleados.append(nuevoEmpleado)
        self.guardarEmpleados()
        print(f"El empleado {idEmpleadop} ha sido registrado.")

class Usuario:
    def __init__(self, usuariop, passwordp, pinp):
        self.usuario = usuariop
        self.password = passwordp
        self.pin = pinp
        self.archivo_usuarios="usuarios.txt"

    def login(usuariop, passwordp, pinp):
        return True

    

def menu():
    #os.system("cls")
    print("\n Menu de Sistema de empleados: ")
    print("1.Registrar nuevo empleado")
    print("2.Consultar empleados")
    print("3.Buscar empleado")
    print("4.Actualizar un empleado")
    print("5.Eliminar un empleado")
    print("6.Salir\n")
    opcion = int(input("Ingrese la opcion que desea: "))
    print("\n")
    return opcion
    
def main():
    sistema = SistemaEmpleados()
    sistema.cargarEmpleados()
    
    username = str(input("Ingrese su usuario: "))
    password = str(input("Ingrese su password: "))
    pin = int(input("Ingrese su pin: "))
    usuario = Usuario(username, password, pin)

    if usuario.login():
        while True:
            opcion = menu()
            #os.system("cls")
            if opcion == 1:
                print("Registrar un nuevo empleado:")
                idEmpleado = input("Ingrese el Id del empleado: ")
                nombre = input("Ingrese el nombre del empleado: ")
                puesto = input("Ingrese el puesto del empleado: ")
                salario = input("Ingrese el salario del empleado: ")
                sistema.registrarEmpleado(idEmpleado, nombre, puesto, salario)
            
            elif opcion == 2:
                print("Los empleados en el sistema son:")
                for empleado in sistema.empleados:
                    print(empleado)

            elif opcion == 3:
                idBusqueda = input("Ingrese el Id del empleado que desea buscar: ")
                sistema.buscarEmpleado(idBusqueda)
            
            elif opcion == 4:
                idActualizar = input("Ingrese el id de empleado que desea actualizar: ")
                nuevoNombre = input("Ingrese el nuevo nombre del empleado: ")
                nuevoPuesto = input("Ingrese el nuevo puesto del empleado: ")
                nuevoSalario = input("Ingrese el nuevo salario del empleado: ")
                sistema.actualizarEmpleado(idActualizar, nuevoNombre, nuevoPuesto, nuevoSalario)
            
            elif opcion == 5:
                idEliminar = input("Ingrese el id de empleado que desea eliminar: ")
                sistema.eliminarEmpleado(idEliminar)

            elif opcion == 6:
                print("Saliendo del sistema.")
                break
            else:
                print("Opcion invalida")
    else:
        print("Usuario invalido.")

if __name__ == "__main__":
    main()