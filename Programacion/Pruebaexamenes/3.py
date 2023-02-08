inicio=0
frase="Hola como estas"
final=len(frase)
vocal=input("¿Por que letra quieres sustituir las vocales?")
frasefinal=""
caracteres=""

while inicio < final:
    if frase[inicio] in "aeiou":
        caracter=vocal
    else:
        caracter=frase[inicio]
    frasefinal+=caracter
    inicio+=1
    
print(frase)
print(frasefinal)