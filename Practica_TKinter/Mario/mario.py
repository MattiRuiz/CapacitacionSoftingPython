from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.font import BOLD
from PIL import Image, ImageTk
import io

#Interface
root=Tk()
root.title("Mario a traves de los años")
root.geometry("325x325")
root.resizable(width=None, height=None)
root.config(bg="red")
root.iconbitmap("mario.ico")

#Variables
miAnio=StringVar()

#Funciones
def conexionBBDD():
    try:
        miConexion=sqlite3.connect("datamario.db")
        miCursor=miConexion.cursor()
        messagebox.showinfo("Conexión", "Conexión exitosa con la base de datos")
    except:
        messagebox.showerror("Conexión fallida", "No se pudo conectar a la base de datos")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
    if valor=="yes":
        root.destroy()
    else:
        pass

def acercaDe():
    acerca='''
    APP DE PRUEBA
    Última modificación: 18/01
    Versión 0.8 alfa-omega-epsilon
    Python - Tkinter - Sqlite3
    '''
    messagebox.showinfo(title="Información de la app", message=acerca)

def buscar():
    miConexion=sqlite3.connect("datamario.db")
    miCursor=miConexion.cursor()

    global portada

    dato=miAnio.get()

    try:
        parametro = miCursor.execute("SELECT * FROM marios WHERE lanzamiento=?",(dato,))
        if miCursor.execute("SELECT * FROM marios WHERE lanzamiento=?",(dato,)):
            bandera=0
            for row in parametro:
                jueguito=Label(marco, text="{}".format(row[1]))
                jueguito.place(x=5, y=5)
                jueguito.config(bg="white", fg="red", font=("Arial", 11, BOLD))

                consola=Label(marco, text="{} - ({})".format(row[2], row[0]))
                consola.place(x=8, y=25)
                consola.config(bg="white", font=("Arial", 8))

                foto=Image.open(io.BytesIO(row[3]))
                width, height= foto.size
                newHeight=height/140
                newWidth=width/newHeight
                fotoResize=foto.resize((int(newWidth),140))
                
                portada=ImageTk.PhotoImage(fotoResize)
                portadaLabel = Label(marco, image=portada, bg="white")
                portadaLabel.place(x=8, y=45)
                portadaLabel.config(width=295, height=140)

                bandera = 1
            if bandera==0:
                messagebox.showinfo("GAME OVER", "No se encontraron coincidencias")
                limpiarCampos()
               
    except:
        messagebox.showerror("Error", "Hubo un error en la busqueda")
        

def limpiarCampos():
    miAnio.set("")


#Menu
menubar=Menu(root)
menuPrincipal=Menu(menubar, tearoff=0)
menuPrincipal.add_command(label="Conectar Base de Datos", command=conexionBBDD)
menuPrincipal.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menuPrincipal)

menuAyuda=Menu(menubar, tearoff=0)
menuAyuda.add_command(label="Acerca de...", command=acercaDe)
menubar.add_cascade(label="Ayuda", menu=menuAyuda)

#Widgets
marco=Frame(root)
marco.config(bg="white", width=305, height=200, relief=RIDGE, borderwidth=1)
marco.place(x=10, y=45)

titulo=Label(root, text="¿Qué juego de Mario salió cuando naciste?")
titulo.place(x=5, y=10)
titulo.config(font=("Arial", 11, BOLD), bg="red", fg="white")

etiqueta=Label(root, text="Año :")
etiqueta.place(x=25, y=265)
etiqueta.config(font=("Arial", 11, BOLD), bg="red", fg="white")

entrada=Entry(root, textvariable=miAnio, width=15)
entrada.place(x=70, y=267)
entrada.config(justify=RIGHT, font=("Arial", 10, BOLD))

botonBusqueda=Button(root, text="Buscar", command=buscar)
botonBusqueda.place(x=200, y=263)
botonBusqueda.config(font=("Arial", 10, BOLD), bg="red", fg="white", padx=10, pady=2)





#Finalización del código
root.config(menu=menubar)
root.mainloop()

    