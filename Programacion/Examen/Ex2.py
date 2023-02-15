"""
Diccionari de sinonims
    
@Autor: Ruben Delgado
@Mail: neburyj4@gmail.com
@Data de creació: 15/03/2023
@Data de modificació: 15/03/2023
@Versio 1.0
"""
import requests
from bs4 import BeautifulSoup
url='https://www.wordreference.com/sinonimos/'
enlace=input("palabra a buscar: ")
buscar=url+enlace
resp=requests.get(buscar)
bs=BeautifulSoup(resp.text)
lista=bs.find_all(class_='trans clickable')
for sin in lista:
    sino=sin.find_all('li')
    for fin in sino:
        print(fin.next_element)
