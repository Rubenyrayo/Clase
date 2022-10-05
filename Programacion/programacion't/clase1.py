"""
Aixo es el primer codi per l'exercici previament dictat de Adrian Merinas

@Autor: Ruben Delgado
@Mail: Lawlietor03@gmail.com
@Data de creació: 21/09/2022
@Data de modificació: 21/09/2022
@Versio 1.0

"""


#Codi definitiu -->

productes=["teclat", "ratoli","monitor"]
preus=["20€", "25€", "100€"]

print("Que productes vols?")
print("0. teclat")
print("1. ratoli")
print("2. monitor")

numero=int(input(("Posa el seu numero:")))


print(productes[numero]+" "+preus[numero])

input("Premi qualsevol botó")

    