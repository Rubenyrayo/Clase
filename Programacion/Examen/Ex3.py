"""
Restar anys de vida
    
@Autor: Ruben Delgado
@Mail: neburyj4@gmail.com
@Data de creació: 15/03/2023
@Data de modificació: 15/03/2023
@Versio 1.0
"""

#bucle while que agafa l'edad de la variable esperanzavida i resta o suma depenent de la activitat
esperanzavida=86
while True:
    activitat=input("que actividad haces(exercici, dormir, fumar, beure, programar) per acabar posa sortir: ")
    if activitat=="exercici":
        esperanzavida=esperanzavida + 2
    elif activitat=="fumar":
        esperanzavida=esperanzavida-3
    elif activitat=="beure":
        esperanzavida=esperanzavida-2
    elif activitat=="programar":
        esperanzavida=esperanzavida-10
    elif activitat=="dormir":
        esperanzavida=esperanzavida+1
    else:
        break
print("viuras:", esperanzavida)

