"""
Calculador de notes
    
@Autor: Ruben Delgado
@Mail: Lawlietor03@gmail.com
@Data de creació: 26/10/2022
@Data de modificació: 26/10/2022
@Versio 0.1
"""

# Variables para guardar la info

tasques=[]
treballs=[]
examen=[]

# Valors per iniciar els bucles

notatasques=()

# Menu per accedir a cada part

print("Apartats")
print("\n""1. Tasques", "\n" "2. Treballs", "\n" "3. Treballs","\n")
menus=int(input("A que part vols entrar? "))
print("\n")

#Menu de tasques
if menus==1:
    print("Menu de tasques","\n")
    print("Notes de tasques dipositades = ", tasques)
    while True:
        notatasques=float(input("Posa nota per nota les notes corresponents = "))
        if notatasques==1:
            break
        else:
            tasques.append(notatasques)
            
    print(notatasques, tasques)

#Menu de treballs





