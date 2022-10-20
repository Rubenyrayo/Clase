"""
Treure productes del fitxer    

@Autor: Ruben Delgado
@Mail: Lawlietor03@gmail.com
@Data de creació: 28/09/2022
@Data de modificació: 03/10/2022
@Versio 1.0

"""

#Obre els arxius

prod=open("Programacion/programacion't/listas/productes.txt","r")
preu=open("Programacion/programacion't/listas/preus.txt","r")

#S'encarrega de llegir totes les lineas de l'arixiu
listadepreu = preu.read()
listadeprod = prod.read()

#aplico les lineas del arxiu a les llistes
arr1=listadeprod.split()
arr2=listadepreu.split()


#Bucle per mostrar la llista de articles
for prod in arr1:
    print(prod)

#Salt de linea
print("\n")

#input per emmegatzemar el numero per despres mostrar el producte i el preu en el print
seleccionador=int(input("Que objeto quiere? (Empezando por 0) "))

print(arr1[seleccionador] + " " + arr2[seleccionador] + "€") 

#input per no sortir del programa y poder veure el resultat

input("Premi un boto per sortir del programa")
