import Articulo
import Marca
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#####################################################
# Ventana Lista de articulos
#####################################################
def abrirVentanaListaArticulos():

    idSeleccionado = 0
    
    def seleccionarId(event, treeview):
        nonlocal idSeleccionado
        fila = treeview.selection()[0]
        idSeleccionado = treeview.item(fila, "text")

    try:
        ventanaListaArticulos = tk.Tk()
        ventanaListaArticulos.title("Inventario suministros - Articulos registrados")
        ventanaListaArticulos.geometry("1800x400+10+300")
        ventanaListaArticulos.resizable(False, False)

        treeview = ttk.Treeview(ventanaListaArticulos, height=15)
        def cargarLista():
            treeview.delete(*treeview.get_children())
            treeview["columns"] = ("Nombre", "Descripcion", "Marca", "Estado", "Presentacion", "Stock", "Costo Unitario", "Fecha Creacion", "Fecha Actualizacion")
            treeview.heading("#0", text="ID")
            treeview.heading("Nombre", text="Nombre")
            treeview.heading("Descripcion", text="Descripcion")
            treeview.heading("Marca", text="Marca")
            treeview.heading("Estado", text="Estado")
            treeview.heading("Presentacion", text="Presentacion")
            treeview.heading("Stock", text="Stock")
            treeview.heading("Costo Unitario", text="Costo Unitario")
            treeview.heading("Fecha Creacion", text="Fecha Creacion")
            treeview.heading("Fecha Actualizacion", text="Fecha Actualizacion")
            treeview.grid(row=0, column=0, sticky="nsew")

            scrollbar = ttk.Scrollbar(ventanaListaArticulos, orient="vertical", command=treeview.yview)
            scrollbar.grid(row=0, column=4, sticky="ns")
            treeview.configure(yscrollcommand=scrollbar.set)

            scrollbarh = ttk.Scrollbar(ventanaListaArticulos, orient="horizontal", command=treeview.xview)
            scrollbarh.grid(row=1, column=0, columnspan=5, sticky="ns")
            treeview.configure(xscrollcommand=scrollbar.set)

            articulos_activos = Articulo.getArticulos()
            for articulo in articulos_activos:
                treeview.insert("", tk.END, text=articulo["id"], values=(articulo["nombre"], articulo["descripcion"], Marca.getNombreMarca(articulo["idMarca"]), articulo["estado"], articulo["presentacion"], articulo["stock"], articulo["costoUnitario"], articulo["fechaCreacion"], articulo["fechaActualizacion"]))

            treeview.grid(row=0, column=0, columnspan=5, sticky="nsew")
    
            primerRow = treeview.get_children()[0]
            treeview.selection_set(primerRow)

        cargarLista()

        labelSeparador = tk.Label(ventanaListaArticulos, text="")
        labelSeparador.grid(row=1, column=0)
        #Agregar
        btnAgregarArticulo = tk.Button(ventanaListaArticulos, text="Agregar artículo", command=lambda: abrirVentanaDetallesArticulo("agregar", 0))
        btnAgregarArticulo.grid(row=2, column=0)
        #Refrescar Lista
        btnRefrescarLista = tk.Button(ventanaListaArticulos, text="Refrescar", command=cargarLista)
        btnRefrescarLista.grid(row=2, column=1)
        #Actualizar
        btnActualizarArticulo = tk.Button(ventanaListaArticulos, text="Actualizar artículo", command=lambda: abrirVentanaDetallesArticulo("actualizar", idSeleccionado))
        btnActualizarArticulo.grid(row=2, column=2)
        #Cerrar
        btnCerrar = tk.Button(ventanaListaArticulos, text="Cerrar", command=ventanaListaArticulos.destroy)
        btnCerrar.grid(row=2, column=3)

        treeview.bind("<ButtonRelease-1>", lambda event: seleccionarId(event, treeview))

    except Exception as e:
        messagebox.showerror(title="Error", message=("Error cargando los articulos registrados. Error: ", e))

#####################################################
# Ventana detalle de articulo
#####################################################
def abrirVentanaDetallesArticulo(accion, id):
    try:
        ventanaDetallesArticulo = tk.Tk()
        ventanaDetallesArticulo.title("Inventario suministros - Detalles de articulo")
        ventanaDetallesArticulo.geometry("400x300+600+200")
        ventanaDetallesArticulo.resizable(False, False)

        #ID
        labelId = tk.Label(ventanaDetallesArticulo, text="ID:")
        labelId.grid(row=1, column=0, sticky=tk.W)
        labelValorId = tk.Label(ventanaDetallesArticulo, text="--")
        labelValorId.grid(row=1, column=1, sticky=tk.W)
        #Nombre
        labelNombre = tk.Label(ventanaDetallesArticulo, text="Nombre:")
        labelNombre.grid(row=2, column=0, sticky=tk.W)
        textBoxNombre = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxNombre.grid(row=2, column=1, sticky=tk.W)
        #Descripcion
        labelDescripcion = tk.Label(ventanaDetallesArticulo, text="Descripcion:")
        labelDescripcion.grid(row=3, column=0, sticky=tk.W)
        textBoxDescripcion = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxDescripcion.grid(row=3, column=1, sticky=tk.W)
        #Marca
        labelMarca = tk.Label(ventanaDetallesArticulo, text="Marca:")
        labelMarca.grid(row=4, column=0, sticky=tk.W)
        opcionesMarcas = []
        marcasActivas = Marca.getMarcas()
        for marca in marcasActivas:
            opcionesMarcas.append(marca["nombre"])
        comboMarca = ttk.Combobox(ventanaDetallesArticulo, values=opcionesMarcas, state="readonly")
        comboMarca.grid(row=4, column=1, sticky=tk.W)
        #estado
        labelEstado = tk.Label(ventanaDetallesArticulo, text="Estado:")
        labelEstado.grid(row=5, column=0, sticky=tk.W)
        opcionesEstados = ["activo", "inactivo"]
        comboEstado = ttk.Combobox(ventanaDetallesArticulo, values=opcionesEstados, state="readonly")
        comboEstado.grid(row=5, column=1, sticky=tk.W)
        #Presentacion
        labelPresentacion = tk.Label(ventanaDetallesArticulo, text="Presentacion:")
        labelPresentacion.grid(row=6, column=0, sticky=tk.W)
        textBoxPresentacion = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxPresentacion.grid(row=6, column=1, sticky=tk.W)
        #Stock
        labelStock = tk.Label(ventanaDetallesArticulo, text="Stock:")
        labelStock.grid(row=7, column=0, sticky=tk.W)
        textBoxStock = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxStock.grid(row=7, column=1, sticky=tk.W)
        #Costo Unitario
        labelCostoUnitario = tk.Label(ventanaDetallesArticulo, text="Costo unitario:")
        labelCostoUnitario.grid(row=8, column=0, sticky=tk.W)
        textBoxCostoUnitario = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxCostoUnitario.grid(row=8, column=1, sticky=tk.W)
        #Fecha creacion
        labelFechaCreacion = tk.Label(ventanaDetallesArticulo, text="Fecha de creación:")
        labelFechaCreacion.grid(row=9, column=0, sticky=tk.W)
        textBoxFechaCreacion = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxFechaCreacion.grid(row=9, column=1, sticky=tk.W)
        #Fecha modificacion
        labelFechaModificacion = tk.Label(ventanaDetallesArticulo, text="Fecha de modificacón:")
        labelFechaModificacion.grid(row=10, column=0, sticky=tk.W)
        textBoxFechaModificacion = tk.Entry(ventanaDetallesArticulo, width=20)
        textBoxFechaModificacion.grid(row=10, column=1, sticky=tk.W)        

        def cargarCampos():
            try:
                articulo = Articulo.consultarArticulo(id)
                labelValorId.config(text=articulo["id"])
                textBoxNombre.insert(0, articulo["nombre"])
                textBoxDescripcion.insert(0, articulo["descripcion"])
                comboMarca.set(Marca.getNombreMarca(articulo["idMarca"]))
                comboEstado.set(articulo["estado"])
                textBoxPresentacion.insert(0, articulo["presentacion"])
                textBoxStock.insert(0, articulo["stock"])
                textBoxCostoUnitario.insert(0, articulo["costoUnitario"])
                textBoxFechaCreacion.insert(0, articulo["fechaCreacion"])
                textBoxFechaModificacion.insert(0, articulo["fechaActualizacion"])
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Error cargando los campos con los valores del artículo. Error: {e}")

        if accion == "agregar":
            #Agregar
            def agregarArticulo():
                try:
                    Articulo.crearArticulo({"nombre": textBoxNombre.get(),"descripcion": textBoxDescripcion.get(),"idMarca": Marca.getIdMarca(comboMarca.get()),"estado": comboEstado.get(),"presentacion": textBoxPresentacion.get(),"stock": textBoxStock.get(),"costoUnitario": textBoxCostoUnitario.get(),"fechaCreacion": textBoxFechaCreacion.get(),"fechaActualizacion": textBoxFechaModificacion.get()})
                    messagebox.showinfo(title="Info", message=f"Articulo {textBoxNombre.get()} fue creado con {textBoxStock.get()} {textBoxPresentacion.get()}.")
                    ventanaDetallesArticulo.destroy()
                except Exception as e:
                    messagebox.showerror(title="Error", message=("Error agregando articulo. Error: ", e))
            btnAgregar = tk.Button(ventanaDetallesArticulo, text="Agregar", command=agregarArticulo)
            btnAgregar.grid(row=11, column=0)
        elif accion == "actualizar":
            #Actualizar
            def actualizarArticulo():
                try:
                    Articulo.actualizarArticulo(id, {"nombre": textBoxNombre.get(),"descripcion": textBoxDescripcion.get(),"idMarca": Marca.getIdMarca(comboMarca.get()),"estado": comboEstado.get(),"presentacion": textBoxPresentacion.get(),"stock": textBoxStock.get(),"costoUnitario": textBoxCostoUnitario.get(),"fechaCreacion": textBoxFechaCreacion.get(),"fechaActualizacion": textBoxFechaModificacion.get()})
                    messagebox.showinfo(title="Info", message=f"Artículo de {textBoxNombre.get()} fue actualizado.")
                    ventanaDetallesArticulo.destroy()
                except Exception as e:
                    messagebox.showerror(title="Error", message=("Error actualizando artículo. Error: ", e))
            cargarCampos()
            btnActualizar = tk.Button(ventanaDetallesArticulo, text="Actualizar", command=actualizarArticulo)
            btnActualizar.grid(row=11, column=0)
        #Cerrar
        btnCerrar = tk.Button(ventanaDetallesArticulo, text="Cerrar", command=ventanaDetallesArticulo.destroy)
        btnCerrar.grid(row=11, column=1)

    except Exception as e:
        messagebox.showerror(title="Error", message=("Error cargando los detalles de un artículo. Error: ", e))