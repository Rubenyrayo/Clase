"""
 Joc del pica pared
 
 Autor: Ruben Delgado
 Data de creació: 7/12/22
 Data de modificació: 7/12/22
"""
import random

print("Introduce 'mover' si quieres moverte, de lo contrarió introduce 'quieto', si cuando te mueves, la maquina dice pica pared, quedas automaticamente eliminado")

values = list("1,2,3,picapared")
L1= random.choice(values)
values.remove(L1)

quehace= print(input("Que vols fer? ('quieto' o 'mover')"))

while True:
    if quehace=="mover":
        print(L1)
        
    else quehace=="quieto"
        print(L1)
    
        


