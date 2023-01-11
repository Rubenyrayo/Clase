#from audioop import reverse
#
#
#palabras=[]
#
#while True:
#    palabra=input("Quina paraula vols?")
#    if palabra == " ":
#        break
#    else:
#        palabras.append(palabra)
#    
#for x in reversed(palabras):
#    print(x)
celsius = int(input())

def conv(c):
    #your code goes here
    grados = 1.8 * c + 32

    return grados

fahrenheit = conv(celsius)
print(fahrenheit)