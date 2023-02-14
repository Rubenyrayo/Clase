fichero=open("Programacion/Pruebaexamenes/agua.txt", "r")
datos=fichero.read()
palabras=datos.split()

linias=0

for linea in fichero:
    linias+=1
    linea.split(" ")

print("palabras:",len(palabras))
print("lineas:",linias)


fichero.close()