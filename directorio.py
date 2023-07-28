#------------------------------
# Diccionario Estudiantes
#------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#------------------------------
# funciones de la app
#------------------------------

# borrar
def borrar():
    messagebox.showinfo("Diccionario Estudiantes", "Los datos serán borrados")

# salir
def salir():
    messagebox.showinfo("Diccionario Estudiantes", "La app se va a cerrar")
    ventana_principal.destroy()

#------------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Diccionario Estudiantes")

# tamaño de la ventana
ventana_principal.geometry("600x500")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame entrada
#------------------------------
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg="thistle", width=600, height=500)
frame_entrada.place(x=0, y=0)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=580, height=480)
frame_blanco.place(x=10, y=10)

#------------------------------
# frame thistle
#------------------------------
frame_thistle= Frame(ventana_principal)
frame_thistle.config(bg="thistle", width=560, height=60)
frame_thistle.place(x=20, y=20)

#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar", command=borrar)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Menú", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

# titulo de la app
titulo = Label(frame_thistle, text="Diccionario Estudiantes")
titulo.config(bg = "thistle",fg="white", font=("Helvetica", 30))
titulo.place(x=70,y=13)

# boton para borrar
bt_borrar = Button(frame_blanco, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()