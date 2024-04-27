import UsuarioGestion
import Usuario
import ArticuloGestion
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#####################################################
# Ventana autenticacion
#####################################################
def autenticar():
    try:
        if Usuario.login(textBoxUsuario.get(), textBoxPassword.get()):
            ventanaLogin.destroy()
            abrirVentanaPrincipal()
        else:
            messagebox.showerror(title="Error en autenticacion", message="Credenciales invalidos.")
    except Exception as e:
        messagebox.showerror(title="Error en autenticacion", message=("Error en autenticacion. Error: ", e))

ventanaLogin = tk.Tk()
ventanaLogin.title("Inventario suministros - Autenticacion")
ventanaLogin.geometry("300x80+600+300")
ventanaLogin.resizable(False, False)
labelUsuario = tk.Label(ventanaLogin, text="Usuario:")
labelUsuario.grid(row=1, column=0, sticky=tk.W)
textBoxUsuario = tk.Entry(ventanaLogin, width=25)
textBoxUsuario.grid(row=1, column=1, sticky=tk.W)
labelPassword = tk.Label(ventanaLogin, text="Contraseña:")
labelPassword.grid(row=2, column=0, sticky=tk.W)
textBoxPassword = tk.Entry(ventanaLogin, width=25, show="*")
textBoxPassword.grid(row=2, column=1, sticky=tk.W)
btnLogin = tk.Button(ventanaLogin, text="Ingresar", command=autenticar)
btnLogin.grid(row=3, column=1)
btnCancelar = tk.Button(ventanaLogin, text="Cancelar", command=ventanaLogin.quit)
btnCancelar.grid(row=3, column=2)

#####################################################
# Ventana principal
#####################################################
def abrirVentanaPrincipal():
    try:
        ventanaPrincipal = tk.Tk()
        ventanaPrincipal.title("Inventario suministros")
        ventanaPrincipal.geometry("300x400+600+300")
        ventanaPrincipal.resizable(False, False)
        espacioEntreBotones = 10
        indentacionBotones = 50
        anchoBotones = 28
        # Boton de Gestión de usuarios 1
        btnUsuarios = tk.Button(ventanaPrincipal, text="Gestión de usuarios", width=anchoBotones, command=UsuarioGestion.abrirVentanaListaUsuarios)
        btnUsuarios.grid(row=1, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton de Gestión de artículos 2
        btnArticulos = tk.Button(ventanaPrincipal, text="Gestión de artículos", width=anchoBotones, command=ArticuloGestion.abrirVentanaListaArticulos)
        btnArticulos.grid(row=2, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton de Ingreso en inventario 3
        btnIngresoArticulos = tk.Button(ventanaPrincipal, text="Ingreso en inventario", width=anchoBotones)
        btnIngresoArticulos.grid(row=3, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton de Salida de inventario 4
        btnSalidaArticulos = tk.Button(ventanaPrincipal, text="Salida de inventario", width=anchoBotones)
        btnSalidaArticulos.grid(row=4, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton de Merma de inventario 5
        btnMermaArticulos = tk.Button(ventanaPrincipal, text="Merma en inventario", width=anchoBotones)
        btnMermaArticulos.grid(row=5, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton de Consulta de movimientos 6
        btnConsultaMovimientos = tk.Button(ventanaPrincipal, text="Consulta de movimientos", width=anchoBotones)
        btnConsultaMovimientos.grid(row=6, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton de Reporte de saldos 7
        btnReporteDeSaldos = tk.Button(ventanaPrincipal, text="Reporte de saldos", width=anchoBotones)
        btnReporteDeSaldos.grid(row=7, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        # Boton Salir 8
        btnSalir = tk.Button(ventanaPrincipal, text="Salir", width=anchoBotones, command=ventanaPrincipal.destroy)
        btnSalir.grid(row=8, column=0, padx=indentacionBotones, pady=espacioEntreBotones)
        ventanaPrincipal.mainloop()
    except Exception as e:
        messagebox.showerror(title="Error", message=("Error inicializando el sistema. Error: ", e))

#####################################################
ventanaLogin.mainloop()