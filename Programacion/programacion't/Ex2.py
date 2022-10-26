"""
Fes un programa que calculi el sou mensual d’un comercial. El sou base és de 1000 € i rep una comissió del 5% dels contractes que firmi.
"""

soubase=(1000)
contratobase=(200)

contratosfirmados=int(input("Quantos contratos has firmado? "))
nuevocontratobase=(contratobase * contratosfirmados)

porcentage= 5 * nuevocontratobase/100

nousou=(soubase + porcentage)

print(nousou)
