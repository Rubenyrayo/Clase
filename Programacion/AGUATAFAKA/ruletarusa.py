from ast import Break
import random

bala = random.randint(1,6)

for i in range (1,7):
    input("Presiona enter para disparar")
    if i == bala:
        print ("Te has disparado")
        Break