"""
Fes un programa que calculi el sou mensual d’un comercial. El sou base és de 1000 € i rep una comissió del 5% dels contractes que firmi.
"""

def multiplicacion(multiplicador,multiplicador1):
    return multiplicador*multiplicador1

def division(dividiendo, divisor):
    return dividiendo/divisor

def suma(suma,suma1):
    return suma+suma1

def comissió(porcentage, contratos, cien):
    return porcentage * contratos/cien

soubase=1000
contratobase=200

contratosfirmados=int(input("Quantos contratos has firmado? "))

preucontracte=multiplicacion(contratobase,contratosfirmados)

comisión=comissió(5,preucontracte)

nousou=suma(soubase,comisión)

print(nousou)