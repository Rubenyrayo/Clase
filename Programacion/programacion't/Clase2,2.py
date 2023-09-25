"""
Afegir mes productes y preus al .txt
    
@Autor: Ruben Delgado
@Mail: Lawlietor03@gmail.com
@Data de creació: 03/10/2022
@Data de modificació: 03/10/2022
@Versio 1.0
"""

#Obre els .txt
from fileinput import close


prod=open("Programacion/programacion't/listas/productes.txt","a")
preu=open("Programacion/programacion't/listas/preus.txt","a")
print("y tu madre como la chupa ??")
#Afegeix el producte amb un salt de linea a l'arxiu
addprod=input("Que producte vols afegir?")
prod.write("\n" + addprod)

#Afegeix el preu amb un salt de linea i una E a l'arxiu (ja que el simbol "€" no es pot reproduir)
addpreu=input("Quant costa? (nomes afegir numeros)")
preu.write("\n" + addpreu)

