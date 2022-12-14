"""
 Joc del pica pared
 
 Autor: Ruben Delgado
 Data de creació: 7/12/22
 Data de modificació: 13/12/22
"""
import random

frase = ["1," , "2," , "3," , "pica" , "pared"]
def partirfrase(frase):
    L1= random.randint(1,3)
    print(frase[0:L1])
    return

print("\n""Introduce 'mover' si quieres moverte, de lo contrarió introduce 'quieto', si cuando te mueves, la maquina dice pica pared, quedas automaticamente eliminado""\n")

print(partirfrase(frase))

while True:
    quehace=input("Que vols fer? ('quieto', 'mover' o 'salir')")
    if quehace=="mover" or "quieto":
        print(L1)
    
    elif quehace=="salir":
        break
    
    elif quehace!="mover" or "quieto" or "salir":
        print("Debes de introducir una accion permitida")
        


