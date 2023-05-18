# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Toplevel

#definición para notas
# salir
def salir():
    messagebox.showinfo("Datos personales", "La app se va a cerrar")
    ventana_principal.destroy()

# abrir toplevel notas
def abrir_toplevel_notas():
    global toplevel_notas
    global log0
    toplevel_notas = Toplevel()
    toplevel_notas.title("notas")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("400x300")
    toplevel_notas.config(bg="white")
 
    #titulo 
    frame_titulo = Frame(toplevel_notas)
    frame_titulo.config(bg="white", width=295, height=280)
    frame_titulo.place(x=10, y=10)
    
    # salir
    def salir():
        messagebox.showinfo("Notas", "La ventana se va a cerrar")
        toplevel_notas.destroy()

    # menu salir
    barra_menu = Menu()
    toplevel_notas.config(menu=barra_menu)
    menu_salir = Menu(tearoff=0)
    menu_salir.add_command(label="Salir", command=salir)
    barra_menu.add_cascade(label="Salir", menu=menu_salir)


    # texto procedimental
    proce=Label(toplevel_notas, text="Nota_procedimental=")
    proce.config(bg="white", fg="blue", font=("Helvetica",20))
    proce.place(x=20,y=30)

    # caja de texto para procedimental
    entry_proce=Entry(toplevel_notas)
    entry_proce.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=5)
    entry_proce.focus_set()
    entry_proce.place(x=280 , y=30)

    # texto cognitivo
    cog=Label(toplevel_notas, text="Nota_cognitiva =   ")
    cog.config(bg="white", fg="blue", font=("Helvetica",20))
    cog.place(x=20,y=70)

    # caja de texto para cognitivo
    entry_cog=Entry(toplevel_notas)
    entry_cog.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=5)
    entry_cog.focus_set()
    entry_cog.place(x=280 , y=70)

    # texto autoevaluacion
    auto=Label(toplevel_notas, text="Nota_autoevaluacion=")
    auto.config(bg="white", fg="blue", font=("Helvetica",19))
    auto.place(x=20,y=110)

    # caja de texto para autoevaluacion
    entry_auto=Entry(toplevel_notas)
    entry_auto.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=5)
    entry_auto.focus_set()
    entry_auto.place(x=280 , y=110)

    # texto actitudinal
    acti=Label(toplevel_notas, text="Nota_actitudinal= ")
    acti.config(bg="white", fg="blue", font=("Helvetica",20))
    acti.place(x=20,y=150)

    # caja de texto para actitudinal
    entry_acti=Entry(toplevel_notas)
    entry_acti.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=5)
    entry_acti.focus_set()
    entry_acti.place(x=280 , y=150)

    # texto bimestral
    bime=Label(toplevel_notas, text="Nota_bimestral = ")
    bime.config(bg="white", fg="blue", font=("Helvetica",20))
    bime.place(x=20,y=190)

    # caja de texto para bimestral
    entry_bime=Entry(toplevel_notas)
    entry_bime.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=5)
    entry_bime.focus_set()
    entry_bime.place(x=280 , y=190)
    
    # logo de la app
    logo=PhotoImage(file="img/22.png")
    lb_logo = Label(toplevel_notas, image=logo, bg="white")
    lb_logo.place(x=300,y=200)
    
    # boton para borrar
    bt_borrar = Button(toplevel_notas, text="calcular")
    bt_borrar.place(x=190, y=35, width=100, height=30)
    


   

#toplevel notas
def ir_toplevel_notas():
    pass

#toplevel salud
def abrir_toplevel_salud():
    global toplevel_salud
    toplevel_salud = Toplevel()
    toplevel_salud.title("Salud")
    toplevel_salud.resizable(False, False)
    toplevel_salud.geometry("300x200")
    toplevel_salud.config(bg="white")

    # salir
    def salir():
        messagebox.showinfo("Salud", "La ventana se va a cerrar")
        toplevel_salud.destroy()

    # menu salir
    barra_menu = Menu()
    toplevel_salud.config(menu=barra_menu)
    menu_salir = Menu(tearoff=0)
    menu_salir.add_command(label="Salir", command=salir)
    barra_menu.add_cascade(label="Salir", menu=menu_salir)

    # texto altura
    altura=Label(toplevel_salud, text="Altura =")
    altura.config(bg="white", fg="blue", font=("Helvetica",20))
    altura.place(x=20,y=30)

    # caja de texto para altura
    entry_altura=Entry(toplevel_salud)
    entry_altura.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=6)
    entry_altura.focus_set()
    entry_altura.place(x=140 , y=30)

    # texto Peso
    peso=Label(toplevel_salud, text="Peso =")
    peso.config(bg="white", fg="blue", font=("Helvetica",20))
    peso.place(x=20,y=70)

    # caja de texto Peso
    entry_peso=Entry(toplevel_salud)
    entry_peso.config(bg="ivory3", fg="black",font=("Time New Roman",16), width=6)
    entry_peso.focus_set()
    entry_peso.place(x=140 , y=70)

    

#toplevel salud
def ir_toplevel_salud():
    pass

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Datos personales ")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# color de fondo de la ventana
ventana_principal.config(bg="blue")

#---------------------------
Grado = StringVar()
Nombre = StringVar()
Especialidad = StringVar()

#variablesprincipales
global salud
global notas
global cuaderno
toplevel_notas=StringVar
toplevel_salud=StringVar


#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_separator()

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

#-----------------------------------
# Entrada datos
#-----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="ivory3", width=480, height=180)
frame_entrada.place(x=10, y=10)


# titulo de la app
titulo = Label(frame_entrada, text="Consula De Datos Personales")
titulo.config(bg = "ivory3",fg="navy", font=("Helventica", 20))
titulo.place(x=60,y=4)

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

# etiqueta para la especiaidad
lb_c = Label(frame_entrada, text = "Especialidad = ")
lb_c.config(bg="ivory3", fg="blue", font=("Helvetica", 18))
lb_c.place(x=20, y=125)

# caja de texto para la especialidad
entry_c = Entry(frame_entrada, textvariable= Especialidad)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=28)
entry_c.focus_set()
entry_c.place(x=180,y=120)

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
bt_saud.place(x=80, y=10 , width=130, height=125)
bt_saud.config(bg="indianred1")

#boton para notas
bt_notas= Button(frame_medio,image=notas, command=abrir_toplevel_notas)
bt_notas.place(x=280, y=10 , width=130, height=130,)
bt_notas.config(bg="white")

#ventana de notas


# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()