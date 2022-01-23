"""
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál, és ezeket a listákat egy 'tarolo' nevű listába helyezi. A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
"""

import random

tarolo = []
szamlalo = 0
while True:
    lista = []
    lista1 = []
    lista2 = []
    lista3 = []
    if szamlalo == 0:
        tarolo.append(lista1)
    elif szamlalo == 1:
        tarolo.append(lista2)
    elif szamlalo == 2:
        tarolo.append(lista3)
    if szamlalo == 3:
        tarolo.append(lista)
    elif szamlalo == 5:
        break
    for i in range(3):
        if szamlalo == 0:
            random_szamok = random.randint(0,25)
            lista1.append(random_szamok)
        elif szamlalo == 1:
            random_szamok = random.randint(0,25)
            lista2.append(random_szamok)
        elif szamlalo == 2:
            random_szamok = random.randint(0,25)
            lista3.append(random_szamok)
        elif szamlalo == 3:
            random_szamok = random.randint(0,25)
            lista.append(random_szamok)
    szamlalo += 1
print(tarolo)
    