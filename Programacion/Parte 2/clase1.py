"""
Calculador de notes
    
@Autor: Ruben Delgado
@Mail: Lawlietor03@gmail.com
@Data de creació: 26/10/2022
@Data de modificació: 26/10/2022
@Versio 0.1
"""

# Variables para guardar la info

from os import link
from timeit import repeat


tasques=[]
treballs=[]
examen=[]

notatasques=0
notatreballs=0
notaexamen=0
# Menu per accedir a cada part

while True:
    print("Apartats")
    print("\n""1. Tasques", "\n" "2. Treballs", "\n" "3. Treballs","\n" "4. Salir", "\n")
    menus=int(input("A que part vols entrar? "))
    print("\n")

    #Menu de tasques
    if menus==1:
        print("Menu de tasques","\n")
        print("Notes de tasques dipositades = ", tasques)
        while True:
            notatasques=float(input("Posa nota per nota les notes corresponents (per sortir escriu 100)= "))
            if notatasques==100:
                break
            else:
                tasques.append(notatasques)
                
    #Menu de treballs
    elif menus==2:
        print("Menu de treballs","\n")
        print("Notes de treballs dipositades = ", treballs)
        while True:
            notatreballs=float(input("Posa nota per nota les notes corresponents (per sortir escriu 100) = "))
            if notatreballs==100:
                break
            else:
                treballs.append(notatreballs)
    #Menu de examen
    elif menus==3:
        print("Menu de treballs","\n")
        print("Notes de examens dipositades = ", examen)
        while True:
            notaexamen=float(input("Posa nota per nota les notes corresponents (per sortir escriu 100) = "))
            if notaexamen==100:
                break
            else:
                treballs.append(notaexamen)

    #Finalizar
    elif menus==4:
        break
print("nota tasques", tasques)
print ("nota treballs", treballs)
print ("nota examen", examen, "\n")

input("Per sorti premi un botó")

