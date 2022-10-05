from codeop import CommandCompiler
from distutils.cmd import Command
from tkinter import *
from turtle import bgcolor

#configurar ventana
Calculadora=Tk() #crear ventana
Calculadora.title("Calculadora") #Nombre de ventana
Calculadora.geometry('300x400') #ancho x alto
Calculadora.resizable(False, False) #que las dimenciones no se cambien
Calculadora.configure(bg="white") #configurar color fondo
##############################################################################################
#                                        Parte Logica                                        #
##############################################################################################
########Recoge los botones que va pulsando el usuario########
def envia_boton(valor):
    anterior = Ecuacion.get()
    Ecuacion.delete(0, END)
    Ecuacion.insert(0, str(anterior) + str(valor))
########Botones de operaciones########
def resta():
    global num1
    global operacion
    num1 = Ecuacion.get()
    num1 = float(num1)
    Ecuacion.delete(0,END)
    operacion = "-"

def suma():
    global num1
    global operacion
    num1 = Ecuacion.get()
    num1 = float(num1)
    Ecuacion.delete(0,END)
    operacion = "+"

def multiplicar():
    global num1
    global operacion
    num1 = Ecuacion.get()
    num1 = float(num1)
    Ecuacion.delete(0,END)
    operacion = "*"

def dividir():
    global num1
    global operacion
    num1 = Ecuacion.get()
    num1 = float(num1)
    Ecuacion.delete(0,END)
    operacion = "/"

def igual():
    global num2
    num2 = Ecuacion.get()
    Ecuacion.delete(0, END)
    
    if operacion == "+":
        Ecuacion.insert(0, num1 + float(num2))
    if operacion == "-":
        Ecuacion.insert(0, num1 - float(num2))
    if operacion == "*":
        Ecuacion.insert(0, num1 * float(num2))
    if operacion == "/":
        Ecuacion.insert(0, num1 / float(num2))

def despejar():
    Ecuacion.delete(0, END)
##############################################################################################
#                                        Parte Grafica                                       #
##############################################################################################
###############Text Box###############
Ecuacion = Entry(Calculadora,
                bg="#b5bebe",
                borderwidth=1,
                font=('arial', 22, 'bold'))
Ecuacion.place(width=290,
                height=40,
                x=5,
                y=1)


#configuracion de botones
Ancho_del_Boton = 50
Alto_del_Boton = 50

Boton_1 = Button(Calculadora,
                text="1",
                command=lambda: envia_boton(1)) 
Boton_1.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=5,
                y=110)


Boton_2 = Button(Calculadora,
                text="2",
                command=lambda: envia_boton(2)) 
Boton_2.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=65,
                y=110)


Boton_3 = Button(Calculadora,
                text="3",
                command=lambda: envia_boton(3)) 
Boton_3.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=125,
                y=110)


Boton_4 = Button(Calculadora,
                text="4",
                command=lambda: envia_boton(4)) 
Boton_4.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=185,
                y=110)

Boton_5 = Button(Calculadora,
                text="5",
                command=lambda: envia_boton(5)) 
Boton_5.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=245,
                y=110)


Boton_6 = Button(Calculadora,
                text="6",
                command=lambda: envia_boton(6)) 
Boton_6.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=5,
                y=170)


Boton_7 = Button(Calculadora,
                text="7",
                command=lambda: envia_boton(7)) 
Boton_7.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=65,
                y=170)


Boton_8 = Button(Calculadora,
                text="8",
                command=lambda: envia_boton(8)) 
Boton_8.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=125,
                y=170)


Boton_9 = Button(Calculadora,
                text="9",
                command=lambda: envia_boton(9)) 
Boton_9.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=185,
                y=170)


Boton_0 = Button(Calculadora,
                text="0",
                command=lambda: envia_boton(0)) 
Boton_0.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=245,
                y=170)
########Botones de operaciones########
Boton_menos = Button(Calculadora,
                text="-",
                bg="#F50743",
                command=resta)
Boton_menos.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=5,
                y=230)


Boton_mas = Button(Calculadora,
                text="+",
                bg="#F50743",
                command=suma)
Boton_mas.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=65,
                y=230)


Boton_mult = Button(Calculadora,
                text="x",
                bg="#F50743",
                command=multiplicar)
Boton_mult.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=125,
                y=230)


Boton_div = Button(Calculadora,
                text="/",
                bg="#F50743",
                command=dividir)
Boton_div.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=185,
                y=230)

Boton_limpiar = Button(Calculadora,
                text="limpiar",
                command=despejar)

Boton_limpiar.place(width=Ancho_del_Boton,
                height=Alto_del_Boton,
                x=245,
                y=230,)

Boton_Igual = Button(Calculadora,
                text="=",
                bg="#F50743",
                command=igual)
Boton_Igual.place(width=150,
                height=Alto_del_Boton,
                x=70,
                y=300)


######################################
Calculadora.mainloop() #cerrar ventana