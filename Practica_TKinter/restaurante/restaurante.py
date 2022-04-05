from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from tkinter.font import BOLD

# --- Interface ---
root=Tk()
root.title("Gestor restaurante")
root.geometry("800x600")
root.resizable(width=None, height=None)
root.config(bg="#f7f7f7")
root.iconbitmap("restorant.ico")

# --- Variables ---
miProducto=StringVar()
miCantidad=StringVar()
miPrecio=StringVar()
miTotal=StringVar()

# --- Funciones ---
def conexionBBDD():
    try:
        miConexion=sqlite3.connect("cartaProductos.db")
        miCursor=miConexion.cursor()
        messagebox.showinfo("Conexión", "Conexión exitosa con la base de datos")
    except:
        messagebox.showerror("Conexión fallida", "No se pudo conectar a la base de datos")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Está seguro que desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()
    else:
        pass

def acercaDe():
    acerca='''
    App de prueba para la capacitación de Python
    Alumno: Matias Ruiz

    Última modificiación 31/01
    Versión 0.9
    Python - Tkinter - Sqlite3
    '''
    messagebox.showinfo(title="Información del programa", message=acerca)

def limpiarProducto():
    miProducto.set("")
    miCantidad.set("")
    miPrecio.set("")

def mostrarProducto(producto):
    miConexion=sqlite3.connect("cartaProductos.db")
    miCursor=miConexion.cursor()
    registros=treePrecios.get_children()
    for elemento in registros:
        treePrecios.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM listaProductos WHERE categoria=?",(producto,))
        for row in miCursor:
            treePrecios.insert("",0, text=row[1], values=(row[2], row[0]))
    except:
        messagebox.showerror("Error", "No se pudo buscar el producto en la BBDD")

# --- Menú ---
menubar=Menu(root)
menuPrincipal=Menu(menubar, tearoff=0)
menuPrincipal.add_command(label="Conectar Base de Datos", command=conexionBBDD)
menuPrincipal.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menuPrincipal)

menuAyuda=Menu(menubar, tearoff=0)
menuAyuda.add_command(label="Acerca de...", command=acercaDe)
menubar.add_cascade(label="Ayuda", menu=menuAyuda)

# --- Widgets ---
cabecera=Label(root, text="Restaurante Pepito - Facturación")
cabecera.place(x=10, y=10)
cabecera.config(font=("Tahoma", 12, BOLD), bg="#f7f7f7", fg="#051456")

tituloProductos=Label(root, text="Productos:")
tituloProductos.place(x=10, y=45)
tituloProductos.config(font=("Tahoma", 10, BOLD), bg="#f7f7f7", fg="#444")

#Botones
botonParrilla=Button(root, text="Parrilla", command=lambda:mostrarProducto("parrilla"))
botonParrilla.place(x=10, y=75)
botonParrilla.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

botonPasta=Button(root, text="Pastas", command=lambda:mostrarProducto("pasta"))
botonPasta.place(x=100, y=75)
botonPasta.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

botonGuarnicion=Button(root, text="Guarnición", command=lambda:mostrarProducto("guarnicion"))
botonGuarnicion.place(x=187, y=75)
botonGuarnicion.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

botonEntradas=Button(root, text="Entrada", command=lambda:mostrarProducto("entrada"))
botonEntradas.place(x=297, y=75)
botonEntradas.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

botonTradicionales=Button(root, text="Tradicionales", command=lambda:mostrarProducto("tradicionales"))
botonTradicionales.place(x=392, y=75)
botonTradicionales.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

botonBebidas=Button(root, text="Bebidas", command=lambda:mostrarProducto("bebidas"))
botonBebidas.place(x=520, y=75)
botonBebidas.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

botonPostres=Button(root, text="Postres", command=lambda:mostrarProducto("postres"))
botonPostres.place(x=616, y=75)
botonPostres.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)

#Tablas
tituloListaPrecios=Label(root, text="Lista de precios:")
tituloListaPrecios.place(x=10, y=120)
tituloListaPrecios.config(font=("Tahoma", 10, BOLD), bg="#f7f7f7", fg="#444")

framePrecios=Frame(root)
framePrecios.place(x=10, y=150)
framePrecios.config(width=350, height=288, relief=RIDGE, borderwidth=1)
treePrecios=ttk.Treeview(framePrecios, height=13, columns=('#0', '#1'))
treePrecios.place(x=0, y=0)
treePrecios.column('#0', width=270)
treePrecios.heading('#0', text="Producto", anchor=CENTER)
treePrecios.column('#1', width=80)
treePrecios.heading('#1', text="Precio", anchor=CENTER)

tituloPedido=Label(root, text="Pedido:")
tituloPedido.place(x=400, y=120)
tituloPedido.config(font=("Tahoma", 10, BOLD), bg="#f7f7f7", fg="#444")

framePedido=Frame(root)
framePedido.place(x=400, y=150)
framePedido.config(width=350, height=288, relief=RIDGE, borderwidth=1)
treePedido=ttk.Treeview(framePedido, height=13, columns=('#0', '#1', '#2'))
treePedido.place(x=0, y=0)
treePedido.column('#0', width=50)
treePedido.heading('#0', text="Cant.", anchor=CENTER)
treePedido.column('#1', width=230)
treePedido.heading('#1', text="Producto", anchor=CENTER)
treePedido.column('#2', width=70)
treePedido.heading('#2', text="Precio", anchor=CENTER)

# --- Función tabla ---
def seleccionarUsandoClick(event):
    item=treePrecios.identify('item', event.x, event.y)
    miProducto.set(treePrecios.item(item, "text"))
    miCantidad.set(int(1))
    miPrecio.set(treePrecios.item(item, "values")[0])

treePrecios.bind("<Double-1>", seleccionarUsandoClick)

def agregarAlPedido():
    try:
        datos=miCantidad.get(),miProducto.get(),miPrecio.get()
        nuevoPrecio=int(datos[0])*int(datos[2])
        treePedido.insert("", 0, text=datos[0], values=(datos[1], nuevoPrecio))
        limpiarProducto()
        calcularTotal()
    except:
        messagebox.showerror("ADVERTENCIA", "No ha seleccionado ningún producto")

def borrarTodo():
    if messagebox.askyesno(message="¿Está seguro que quiere borrar todo?", title="ADVERTENCIA"):
        treePedido.delete(*treePedido.get_children())
        treePrecios.delete(*treePrecios.get_children())
        borrarTotal()
    else:
        pass

def calcularTotal():
    total=0
    for child in treePedido.get_children():
        total+= int(treePedido.item(child, 'values')[1])
        miTotal.set(total)

def borrarTotal():
    miTotal.set("")

def borrarItem():
    try:
        itemSeleccionado=treePedido.selection()[0]
        treePedido.delete(itemSeleccionado)
        calcularTotal()
    except:
        messagebox.showerror("ADVERTENCIA", "Seleccione un producto a borrar")

def imprimirTicket():
    messagebox.askyesno("IMPRIMIR", "¿Desea imprimir el ticket?")
    pass

#Parte inferior
tituloAgregar=Label(root, text="Agregar al pedido:")
tituloAgregar.place(x=10, y=450)
tituloAgregar.config(font=("Tahoma", 10, BOLD), bg="#f7f7f7", fg="#444")

labelProducto=Label(root, text="Producto:")
labelProducto.config(font=("Tahoma", 9), bg="#f7f7f7")
labelProducto.place(x=10, y=480)
entryProducto=Entry(root, width=40, textvariable=miProducto)
entryProducto.place(x=80, y=480)
labelCantidad=Label(root, text="Cantidad:")
labelCantidad.config(font=("Tahoma", 9), bg="#f7f7f7")
labelCantidad.place(x=10, y=510)
entryCantidad=Entry(root, width=6, textvariable=miCantidad)
entryCantidad.place(x=80, y=510)
labelPrecio=Label(root, text="Precio:")
labelPrecio.config(font=("Tahoma", 9), bg="#f7f7f7")
labelPrecio.place(x=170, y=510)
entryPrecio=Entry(root, width=12, textvariable=miPrecio)
entryPrecio.place(x=220, y=510)

botonAgregar=Button(root, text="Agregar", command=agregarAlPedido)
botonAgregar.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)
botonAgregar.place(x=55, y=545)
borrarProducto=Button(root, text="Borrar", command=limpiarProducto)
borrarProducto.config(font=("Tahoma", 10), bg="red", fg="white", padx=10, pady=2)
borrarProducto.place(x=170, y=545)

labelTotal=Label(root, text="Total:")
labelTotal.config(font=("Tahoma", 10, BOLD), bg="#f7f7f7", fg="#444")
labelTotal.place(x=600, y=455)
entryTotal=Entry(root, width=15, textvariable=miTotal)
entryTotal.place(x=650, y=455)
botonImprimir=Button(root, text="Imprimir pedido", command=imprimirTicket)
botonImprimir.config(font=("Tahoma", 10), padx=10, pady=2)
botonImprimir.place(x=450, y=500)
borrarArticulo=Button(root, text="Borrar producto", command=borrarItem)
borrarArticulo.config(font=("Tahoma", 10), bg="#eee", padx=10, pady=2)
borrarArticulo.place(x=600, y=500)
borrarPedido=Button(root, text="Borrar todo", command=borrarTodo)
borrarPedido.config(font=("Tahoma", 10), bg="red", fg="white", padx=10, pady=2)
borrarPedido.place(x=535, y=540)



# --- Finalización del código ---
root.config(menu=menubar)
root.mainloop()