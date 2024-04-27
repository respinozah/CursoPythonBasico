import Usuario
import Puesto
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#####################################################
# Ventana Lista de usuarios
#####################################################
def abrirVentanaListaUsuarios():

    idSeleccionado = 0
    
    def seleccionarId(event, treeview):
        nonlocal idSeleccionado
        fila = treeview.selection()[0]
        idSeleccionado = treeview.item(fila, "text")

    try:
        ventanaListaUsuarios = tk.Tk()
        ventanaListaUsuarios.title("Inventario suministros - Usuarios registrados")
        ventanaListaUsuarios.geometry("1050x400+600+300")
        ventanaListaUsuarios.resizable(False, False)

        treeview = ttk.Treeview(ventanaListaUsuarios, height=15)
        def cargarLista():
            treeview.delete(*treeview.get_children())
            treeview["columns"] = ("Nombre", "Apellido", "Usuario", "Puesto")
            treeview.heading("#0", text="ID")
            treeview.heading("Nombre", text="Nombre")
            treeview.heading("Apellido", text="Apellido")
            treeview.heading("Usuario", text="Usuario")
            treeview.heading("Puesto", text="Puesto")
            treeview.grid(row=0, column=0, sticky="nsew")

            scrollbar = ttk.Scrollbar(ventanaListaUsuarios, orient="vertical", command=treeview.yview)
            scrollbar.grid(row=0, column=5, sticky="ns")
            treeview.configure(yscrollcommand=scrollbar.set)

            usuarios_activos = Usuario.getUsuariosActivos()
            for usuario in usuarios_activos:
                treeview.insert("", tk.END, text=usuario["id"], values=(usuario["nombre"], usuario["apellido"], usuario["usuario"], Puesto.getNombrePuesto(usuario["puesto"])))

            treeview.grid(row=0, column=0, columnspan=4, sticky="nsew")
    
            primerRow = treeview.get_children()[0]
            treeview.selection_set(primerRow)

        cargarLista()

        labelSeparador = tk.Label(ventanaListaUsuarios, text="")
        labelSeparador.grid(row=1, column=0)
        #Agregar
        btnAgregarUsuario = tk.Button(ventanaListaUsuarios, text="Agregar usuario", command=lambda: abrirVentanaDetallesUsuario("agregar", 0))
        btnAgregarUsuario.grid(row=2, column=0)
        #Refrescar Lista
        btnRefrescarLista = tk.Button(ventanaListaUsuarios, text="Refrescar", command=cargarLista)
        btnRefrescarLista.grid(row=2, column=1)
        #Actualizar
        btnActualizarUsuario = tk.Button(ventanaListaUsuarios, text="Actualizar usuario", command=lambda: abrirVentanaDetallesUsuario("actualizar", idSeleccionado))
        btnActualizarUsuario.grid(row=2, column=2)
        #Cerrar
        btnCerrar = tk.Button(ventanaListaUsuarios, text="Cerrar", command=ventanaListaUsuarios.destroy)
        btnCerrar.grid(row=2, column=3)

        treeview.bind("<ButtonRelease-1>", lambda event: seleccionarId(event, treeview))

    except Exception as e:
        messagebox.showerror(title="Error", message=("Error cargando los usuarios registrados. Error: ", e))

#####################################################
# Ventana detalle de usuarios
#####################################################
def abrirVentanaDetallesUsuario(accion, id):
    try:
        ventanaDetalleUsuarios = tk.Tk()
        ventanaDetalleUsuarios.title("Inventario suministros - Detalles de usuario")
        ventanaDetalleUsuarios.geometry("400x200+600+200")
        ventanaDetalleUsuarios.resizable(False, False)

        #ID
        labelId = tk.Label(ventanaDetalleUsuarios, text="ID:")
        labelId.grid(row=1, column=0, sticky=tk.W)
        labelValorId = tk.Label(ventanaDetalleUsuarios, text="--")
        labelValorId.grid(row=1, column=1, sticky=tk.W)
        #user
        labelUsername = tk.Label(ventanaDetalleUsuarios, text="Usuario:")
        labelUsername.grid(row=2, column=0, sticky=tk.W)
        textBoxUsername = tk.Entry(ventanaDetalleUsuarios, width=20)
        textBoxUsername.grid(row=2, column=1, sticky=tk.W)
        #password
        labelPassword = tk.Label(ventanaDetalleUsuarios, text="Password:")
        labelPassword.grid(row=3, column=0, sticky=tk.W)
        textBoxPassword = tk.Entry(ventanaDetalleUsuarios, width=20, show="*")
        textBoxPassword.grid(row=3, column=1, sticky=tk.W)
        #nombre
        labelNombre = tk.Label(ventanaDetalleUsuarios, text="Nombre:")
        labelNombre.grid(row=4, column=0, sticky=tk.W)
        textBoxNombre = tk.Entry(ventanaDetalleUsuarios, width=20)
        textBoxNombre.grid(row=4, column=1, sticky=tk.W)
        #apellido
        labelApellido = tk.Label(ventanaDetalleUsuarios, text="Apellido:")
        labelApellido.grid(row=5, column=0, sticky=tk.W)
        textBoxApellido = tk.Entry(ventanaDetalleUsuarios, width=20)
        textBoxApellido.grid(row=5, column=1, sticky=tk.W)
        #puesto
        labelPuesto = tk.Label(ventanaDetalleUsuarios, text="Puesto:")
        labelPuesto.grid(row=6, column=0, sticky=tk.W)
        opcionesPuestos = []
        puestosActivos = Puesto.getPuestos()
        for puesto in puestosActivos:
            opcionesPuestos.append(puesto["nombre"])
        comboPuesto = ttk.Combobox(ventanaDetalleUsuarios, values=opcionesPuestos, state="readonly")
        comboPuesto.grid(row=6, column=1, sticky=tk.W)
        #estado
        labelEstado = tk.Label(ventanaDetalleUsuarios, text="Estado:")
        labelEstado.grid(row=7, column=0, sticky=tk.W)
        opcionesEstados = ["activo", "inactivo"]
        comboEstado = ttk.Combobox(ventanaDetalleUsuarios, values=opcionesEstados, state="readonly")
        comboEstado.grid(row=7, column=1, sticky=tk.W)

        def cargarCampos():
            try:
                usuario = Usuario.consultarUsuario(id)
                labelValorId.config(text=usuario["id"])
                textBoxUsername.insert(0, usuario["usuario"])
                textBoxPassword.insert(0, usuario["password"])
                textBoxNombre.insert(0, usuario["nombre"])
                textBoxApellido.insert(0, usuario["apellido"])
                comboPuesto.set(Puesto.getNombrePuesto(usuario["puesto"]))
                comboEstado.set(usuario["estado"])
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Error cargando los campos con los valores del usuario. Error: {e}")

        if accion == "agregar":
            #Agregar
            def agregarUsuario():
                try:
                    Usuario.crearUsuario({"usuario": textBoxUsername.get(), "password": textBoxPassword.get(), "nombre": textBoxNombre.get(), "apellido": textBoxApellido.get(), "puesto": Puesto.getIdPuesto(comboPuesto.get())})
                    messagebox.showinfo(title="Info", message=f"Usuario de {textBoxNombre.get()} {textBoxApellido.get()} creado.")
                    ventanaDetalleUsuarios.destroy()
                except Exception as e:
                    messagebox.showerror(title="Error", message=("Error agregando usuario. Error: ", e))
            btnAgregar = tk.Button(ventanaDetalleUsuarios, text="Agregar", command=agregarUsuario)
            btnAgregar.grid(row=8, column=0)
        elif accion == "actualizar":
            #Actualizar
            def actualizarUsuario():
                try:
                    #print({"usuario": textBoxUsername.get(), "password": textBoxPassword.get(), "nombre": textBoxNombre.get(), "apellido": textBoxApellido.get(), "puesto": Puesto.getIdPuesto(comboPuesto.get()), "estado": comboEstado.get()})
                    Usuario.actualizarUsuario(id, {"usuario": textBoxUsername.get(), "password": textBoxPassword.get(), "nombre": textBoxNombre.get(), "apellido": textBoxApellido.get(), "puesto": Puesto.getIdPuesto(comboPuesto.get()), "estado": comboEstado.get()})
                    messagebox.showinfo(title="Info", message=f"Usuario de {textBoxNombre.get()} {textBoxApellido.get()} fue actualizado.")
                    ventanaDetalleUsuarios.destroy()
                except Exception as e:
                    messagebox.showerror(title="Error", message=("Error actualizando usuario. Error: ", e))
            cargarCampos()
            btnActualizar = tk.Button(ventanaDetalleUsuarios, text="Actualizar", command=actualizarUsuario)
            btnActualizar.grid(row=8, column=0)
        #Cerrar
        btnCerrar = tk.Button(ventanaDetalleUsuarios, text="Cerrar", command=ventanaDetalleUsuarios.destroy)
        btnCerrar.grid(row=8, column=1)

    except Exception as e:
        messagebox.showerror(title="Error", message=("Error cargando los detalles de un usuario. Error: ", e))