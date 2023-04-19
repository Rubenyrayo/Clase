"""
Novela grafica donde puedes tomar decisiones a parte, también añadir momentos de pelea donde puedas mejorar a tu personaje

@Autor: Ruben Delgado
@Mail: neburyj4@gmail.com
@Data de creació: 15/03/2023
@Data de modificació: 15/03/2023
@Versio 1.0

"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

#Aqui es donde se guardan la configuración para generar la ventada del programa
w=Tk()
w.configure(bg='#262626')
w.resizable(0,0)
w.title('Calculadora Cientifica')

pantalla1= ttk.Frame(w)
pantalla1.grid(column=0,row=0)

#Genero un widget del propio tkinter que lo que hace és que según el valor de la variable entrada1 se vera reflejada en el Label
entrada1= StringVar()
Label_entrada1= ttk.Label(pantalla1, textvariable=entrada1)
Label_entrada1.grid (column=0, row=0)

#Genero lo mismo otra vez para la segunda entrada 
entrada2= StringVar()
Label_entrada2= ttk.Label(pantalla1, textvariable=entrada2)

#Hago los botones de numero
boton0= ttk.Button(pantalla1, text="0")
boton1= ttk.Button(pantalla1, text="1")
boton2= ttk.Button(pantalla1, text="2")
boton3= ttk.Button(pantalla1, text="3")
boton4= ttk.Button(pantalla1, text="4")
boton5= ttk.Button(pantalla1, text="5")
boton6= ttk.Button(pantalla1, text="6")
boton7= ttk.Button(pantalla1, text="7")
boton8= ttk.Button(pantalla1, text="8")
boton9= ttk.Button(pantalla1, text="9")

#Genero los botones de opciones basicas
boton_borrar= ttk.Button(pantalla1, text=chr(9003))
boton_C= ttk.Button(pantalla1, text="C")
boton_abrirparentesis= ttk.Button(pantalla1, text="(")
boton_cerrarparentesis= ttk.Button(pantalla1, text=")")
boton_coma= ttk.Button(pantalla1, text=",")

#Genero botones de operaciones basicas
boton_division= ttk.Button(pantalla1, text=chr(247))
boton_multiplicacion= ttk.Button(pantalla1, text="x")
boton_resta= ttk.Button(pantalla1, text="-")
boton_suma= ttk.Button(pantalla1, text="+")
boton_raizcuadrada= ttk.Button(pantalla1, text=chr(8730))
boton_igual= ttk.Button(pantalla1, text="=")

#poner los botones en pantalla
boton_C.grid(column=0, row=2)
boton_borrar.grid(column=1, row=2)
boton_abrirparentesis.grid(column=2,row=2)
boton_cerrarparentesis.grid(column=3,row=2)
boton1.grid(column=0, row=3)
boton2.grid(column=1, row=3)
boton3.grid(column=2, row=3)
boton4.grid(column=0, row=4)
boton5.grid(column=1, row=4)
boton6.grid(column=2, row=4)
boton7.grid(column=0, row=5)
boton8.grid(column=1, row=5)
boton9.grid(column=2, row=5)



w.mainloop() 