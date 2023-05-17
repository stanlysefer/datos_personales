# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# abrir toplevel notas
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_salud = Toplevel()
    toplevel_salud.title("notas")
    toplevel_salud.resizable(False, False)
    toplevel_salud.geometry("300x200")
    toplevel_salud.config(bg="blue")
    
    #titulo 
    frame_titulo = Frame(toplevel_notas, width=290 , heigth=290)
    frame_titulo.config(bg="white", width=200, height=280)
    frame_titulo.place(x=10, y=10)

#toplevel notas
def ir_toplevel_salud():
    pass

#toplevel salud
def abrir_toplevel_salud():
    global toplevel_salud
    toplevel_salud = Toplevel()
    toplevel_salud.title("salud")
    toplevel_salud.resizable(False, False)
    toplevel_salud.geometry("300x200")
    toplevel_salud.config(bg="red")
    
    #titulo 
    frame_titulo = Frame(toplevel_notas, width=290 , heigth=290)
    frame_titulo.config(bg="white", width=200, height=280)
    frame_titulo.place(x=10, y=10)

#toplevel salud
def ir_toplevel_salud():
    pass

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("datos personales ")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# color de fondo de la ventana
ventana_principal.config(bg="blue")

#---------------------------
Grado = StringVar()
Nombre = StringVar()

#variablesprincipales
global salud
global notas

#-----------------------------------
# Entrada datos
#-----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="ivory3", width=480, height=180)
frame_entrada.place(x=10, y=10)


# etiqueta para nombre
lb_c = Label(frame_entrada, text = "Nombre = ")
lb_c.config(bg="ivory3", fg="blue", font=("Helvetica", 18))
lb_c.place(x=20, y=40)

# caja de texto para nombre
entry_c = Entry(frame_entrada, textvariable= Nombre)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=28)
entry_c.focus_set()
entry_c.place(x=130,y=39)

# etiqueta para grado
lb_c = Label(frame_entrada, text = "Grado = ")
lb_c.config(bg="ivory3", fg="blue", font=("Helvetica", 18))
lb_c.place(x=20, y=80)

# caja de texto para grado
entry_c = Entry(frame_entrada, textvariable= Grado)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=28)
entry_c.focus_set()
entry_c.place(x=130,y=80)

#----------------
#framemedio------
#----------------
#-----------------------------------
frame_medio = Frame(ventana_principal)
frame_medio.config(bg="ivory3", width=480, height=180)
frame_medio.place(x=10, y=200)

#imagenes delos botones
salud=PhotoImage(file="img/salud.png")
notas=PhotoImage(file="img/notas.png")

#boton sobre la salud
bt_saud= Button(frame_medio,image=salud, command=abrir_toplevel_salud)
bt_saud.place(x=60, y=220 , width=30, height=30,)
bt_saud.config(bg="red")

#boton para academico
bt_notas= Button(frame_medio,image=notas, command=abrir_toplevel_notas)
bt_notas.place(x=150, y=220 , width=80, height=80,)
bt_notas.config(bg="coral1")

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()