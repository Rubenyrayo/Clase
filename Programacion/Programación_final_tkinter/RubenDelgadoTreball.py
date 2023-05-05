"""
Calculadora avançada

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

#Aqui genero definiciones para poder utilizar el programa las quales mostraran las operaciones y numeros que se añaden
def añadirValores(tecla):
    if tecla >= '0'  and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
        
        
        
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == '**':
        if tecla =='*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        elif tecla == '**':
            entrada1.set(entrada2.get() + '**')
        
        entrada2.set('')
    
    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
        
def añadirValoresConTeclado(event):

#Es exactamente igual que la definicion añadirValores pero en este caso genero un evento con la caracteristica ".char" que lo que hace es que cada
#vez que el programa detecte una entrada del ordenador en question la tenga en cuenta    

    tecla= event.char
    
    if tecla >= '0'  and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
        
        
        
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla =='*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        
        entrada2.set('')
    
    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def radianes():
    
    entrada1.set('')
    resultado = math.radians(float(entrada2.get()))
    entrada2.set(resultado)

def raizCuadrada():
    
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
    
def borrar():
    inicio = 0
    final = len(entrada2.get())
    
    #Aqui hago dos variables para saber desde el caracter 0 que seria el primer numero de todos, hasta el ultimo caracter
    #gracias a la variable final que recoge el total de caracteres que hay, entonces gracias a eso lo que hago a continuacion es decirle
    #que entre 0 i la longitud del numero en question elimine 1
    
    entrada2.set(entrada2.get()[inicio:final - 1])
            
def borrarTodo():
    
    #Aqui simplemente no asigno nada, entonces al presionar el boton "C" hace que se actualice con esta definicion y se quede en blanco
    
    entrada1.set('')
    entrada2.set('')    
    
#Aqui es donde se guardan la configuración para generar la ventada del programa
w=Tk()
w.configure(bg='#262626')
w.resizable(0,0)
w.title('Calculadora Cientifica')

pantalla1= ttk.Frame(w, style="estilo1.TFrame")
pantalla1.grid(column=0,row=0)

#Hago el estilo para que todo siempre ocupe el mismo espacio
estilo1= ttk.Style()
estilo1.theme_use('clam')
estilo1.configure('estilo1.TFrame', background="#dcdad5")

#hago los estilos donde se mostraran las operaciones
estilo_entrada1= ttk.Style()
estilo_entrada1.configure('estilo_entrada1.TLabel', font="arial 15", anchor="e")

estilo_entrada2= ttk.Style()
estilo_entrada2.configure('estilo_entrada2.TLabel', font="arial 35", anchor="e")

#Genero un widget del propio tkinter que lo que hace és que según el valor de la variable entrada1 se vera reflejada en el Label
entrada1= StringVar()
Label_entrada1= ttk.Label(pantalla1, textvariable=entrada1, style="estilo_entrada1.TLabel")
Label_entrada1.grid (column=0, row=0, columnspan=4, sticky=(W, N, E, S))

#Genero lo mismo otra vez para la segunda entrada 
entrada2= StringVar()
Label_entrada2= ttk.Label(pantalla1, textvariable=entrada2, style="estilo_entrada2.TLabel")
Label_entrada2.grid (column=0, row=1, columnspan=4, sticky=(W, N, E, S))

#Estilo para botones
estilo_numeros=ttk.Style()
estilo_numeros.configure('Numeros.TButton', font="arial 16", width=5, background="#FFFFFF", relief="flat")
estilo_numeros.map('Numeros.TButton', background=[('active', '#CFCFCF')])

estilo_operaciones=ttk.Style()
estilo_operaciones.configure('Operaciones.TButton', font="arial 16", width=5, background="#CFCFCF", relief="flat")

#Hago los botones de numero
boton0= ttk.Button(pantalla1, text="0", style=("Numeros.TButton"), command=lambda: añadirValores('0'))
boton1= ttk.Button(pantalla1, text="1", style=("Numeros.TButton"), command=lambda: añadirValores('1'))
boton2= ttk.Button(pantalla1, text="2", style=("Numeros.TButton"), command=lambda: añadirValores('2'))
boton3= ttk.Button(pantalla1, text="3", style=("Numeros.TButton"), command=lambda: añadirValores('3'))
boton4= ttk.Button(pantalla1, text="4", style=("Numeros.TButton"), command=lambda: añadirValores('4'))
boton5= ttk.Button(pantalla1, text="5", style=("Numeros.TButton"), command=lambda: añadirValores('5'))
boton6= ttk.Button(pantalla1, text="6", style=("Numeros.TButton"), command=lambda: añadirValores('6'))
boton7= ttk.Button(pantalla1, text="7", style=("Numeros.TButton"), command=lambda: añadirValores('7'))
boton8= ttk.Button(pantalla1, text="8", style=("Numeros.TButton"), command=lambda: añadirValores('8'))
boton9= ttk.Button(pantalla1, text="9", style=("Numeros.TButton"), command=lambda: añadirValores('9'))

#Genero los botones de opciones basicas
boton_borrar= ttk.Button(pantalla1, text=chr(9003), style=("Operaciones.TButton"), command=lambda: borrar())
boton_C= ttk.Button(pantalla1, text="C", style=("Operaciones.TButton"), command=lambda: borrarTodo())
boton_abrirparentesis= ttk.Button(pantalla1, text="(", style=("Operaciones.TButton"), command=lambda: añadirValores('('))
boton_cerrarparentesis= ttk.Button(pantalla1, text=")", style=("Operaciones.TButton"), command=lambda: añadirValores(')'))
boton_coma= ttk.Button(pantalla1, text=",", style=("Operaciones.TButton"), command=lambda: añadirValores('.'))

#Genero botones de operaciones basicas
boton_division= ttk.Button(pantalla1, text=chr(247), style=("Operaciones.TButton"), command=lambda: añadirValores('/'))
boton_multiplicacion= ttk.Button(pantalla1, text="x", style=("Operaciones.TButton"), command=lambda: añadirValores('*'))
boton_resta= ttk.Button(pantalla1, text="-", style=("Operaciones.TButton"), command=lambda: añadirValores('-'))
boton_suma= ttk.Button(pantalla1, text="+", style=("Operaciones.TButton"), command=lambda: añadirValores('+'))
boton_raizcuadrada= ttk.Button(pantalla1, text=chr(8730), style=("Operaciones.TButton"), command=lambda: raizCuadrada())
boton_igual= ttk.Button(pantalla1, text="=", style=("Operaciones.TButton"), command=lambda: añadirValores('='))
boton_radianes= ttk.Button(pantalla1, text="rad", style=("Operaciones.TButton"), command=lambda: radianes())
boton_potencia= ttk.Button(pantalla1, text="^", style=("Operaciones.TButton"), command=lambda: añadirValores('**'))

#poner los botones en pantalla
boton_C.grid(column=0, row=2, sticky=(W, N, E, S))
boton_abrirparentesis.grid(column=1,row=2, sticky=(W, N, E, S))
boton_cerrarparentesis.grid(column=2,row=2, sticky=(W, N, E, S))
boton_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

#linea 2
boton1.grid(column=0, row=3, sticky=(W, N, E, S))
boton2.grid(column=1, row=3, sticky=(W, N, E, S))
boton3.grid(column=2, row=3, sticky=(W, N, E, S))
boton_division.grid(column=3, row=3, sticky=(W, N, E, S))

#linea 3
boton4.grid(column=0, row=4, sticky=(W, N, E, S))
boton5.grid(column=1, row=4, sticky=(W, N, E, S))
boton6.grid(column=2, row=4, sticky=(W, N, E, S))
boton_suma.grid(column=3, row=4, sticky=(W, N, E, S))

#linea 4
boton7.grid(column=0, row=5, sticky=(W, N, E, S))
boton8.grid(column=1, row=5, sticky=(W, N, E, S))
boton9.grid(column=2, row=5, sticky=(W, N, E, S))
boton_resta.grid(column=3, row=5, sticky=(W, N, E, S))

#linea 5
boton0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
boton_coma.grid(column=2, row=6, sticky=(W, N, E, S))
boton_multiplicacion.grid(column=3, row=6, sticky=(W, N, E, S))

#linea 6
boton_radianes.grid(column=0, row=7, sticky=(W, N, E, S))
boton_potencia.grid(column=1, row=7, sticky=(W, N, E, S))
boton_raizcuadrada.grid(column=2, row=7, sticky=(W, N, E, S))
boton_igual.grid(column=3, row=7, sticky=(W, N, E, S))

#Añado una separación entre cada boton
for espacio in pantalla1.winfo_children():
    espacio.grid_configure(ipady=5, padx=1, pady=1)

#asigno que el programa detecte los botones del teclado (el botó enter no el compte com igual i el borrar no el detecta)

w.bind('<Key>', añadirValoresConTeclado) 

w.mainloop() 