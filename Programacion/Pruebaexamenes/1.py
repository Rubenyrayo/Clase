palabra=input("introdueix una paraula: ")
palindrom=palabra[::-1]

if palabra==palindrom:
    print("Es un palindrom")
else:
    print("No es un palindrom")
