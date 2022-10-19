from audioop import reverse


palabras=[]

while True:
    palabra=input("Quina paraula vols?")
    if palabra == " ":
        break
    else:
        palabras.append(palabra)
    
for x in reversed(palabras):
    print(x)
    