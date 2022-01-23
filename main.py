"""
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál, és ezeket a listákat egy 'tarolo' nevű listába helyezi. A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
"""

import random

tarolo = []
for i in range(4):
    lista = []
    tarolo.append(lista)
    for i in range(3):
        randszam = random.randint(0,25)
        lista.append(randszam)


print(tarolo)
    