"""
Programa que demana una paraula i comprova si hi ha nombres i si hi ha majuscules i minúscules
    
@Autor: Ruben Delgado
@Mail: neburyj4@gmail.com
@Data de creació: 15/03/2023
@Data de modificació: 15/03/2023
@Versio 1.0
"""
import string 

word = input("Inserte una contraseña: ")

#comprovo que hi ha mayuscules amb el .ascii_uppercase i faig un if per donar les dos posibilitats

if not any(c in string.ascii_uppercase for c in word):
    print("Ingrese una mayúscula.")
else:
    print("tiene mayusculas")
    
#comprovo que hi ha numeros amb el .digits i faig un if per donar les dos posibilitats    

if not any(c in string.digits for c in word):
    print("Ingrese un número.")
else:
    print("tiene numeros")


