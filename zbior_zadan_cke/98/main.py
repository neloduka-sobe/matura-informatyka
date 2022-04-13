#!/usr/bin/env python3


### 98.1
klasy = dict()
with open("dane/uczniowie.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")

        if line[3] not in klasy.keys():
            klasy[line[3]] = [0,0]

        if line[1][-1] == 'a':
            klasy[line[3]][0] = klasy[line[3]][0] + 1
        else:
            klasy[line[3]][1] = klasy[line[3]][1] + 1


print("Zadanie 98.1")
for i in klasy.keys():
    if klasy[i][0] > klasy[i][1]:
        print("Klasa: {}, Ilość: {}".format(i, klasy[i]))



### 98.2
oceny = dict()

with open('dane/oceny.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')

        data = line[1]
        if data not in oceny.keys():
            oceny[data] = 0

        if line[4] == '1':
            oceny[data] = oceny[data] + 1


print("Zadanie 98.2")
for i in oceny.keys():
    if oceny[i] > 10:
        print("Data: {}".format(i))


### 98.3
id_uczniow = dict()
id_j_pol = 1
klasy = dict()

with open("dane/uczniowie.txt", 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        id_uczniow[line[0]] = line[3]

with open("dane/oceny.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        
        line[2] = id_uczniow[line[2]]
        if line[2] not in klasy.keys():
            klasy[line[2]] = [0,0]

        if line[3] == '1':
            klasy[line[2]][0], klasy[line[2]][1] = klasy[line[2]][0]+1, klasy[line[2]][1]+int(line[4])


print("Zadanie 98.3")
for i in klasy.keys():
    if i[:2] == 'IV':
        print("Klasa: {}, srednia: {}".format(i, round(klasy[i][1]/klasy[i][0],2)))


### 98.4
piatki = dict()
przedmioty = dict()

with open("dane/przedmioty.txt", "r") as f:
    for line in f:
       line = line.strip().split("\t") 
       przedmioty[line[0]] = line[1]

with open("dane/oceny.txt", "r") as f:
    for line in f:
        line = line.strip().split("\t")
        mies = int(line[1][5:7]) - 9
        if line[4] == '5':
            
            if przedmioty[line[3]] not in piatki.keys():
                piatki[przedmioty[line[3]]] = [0,0,0,0]
            
            piatki[przedmioty[line[3]]][mies] = piatki[przedmioty[line[3]]][mies] + 1

print("Zadanie 98.4")
for i in piatki.keys():
    print("Ilość: {}, Przedmiot: {}".format(piatki[i],i))



### 98.5
klasa = 'II A'
uczniowie = dict()
with open('dane/uczniowie.txt', 'r') as f:
    for line in f:
        line = line.strip().split("\t")
        if line[3] == "II A":
            uczniowie[line[0]] = line[1:3]


with open('dane/oceny.txt', 'r') as f:
    for line in f:
        line = line.strip().split("\t")
        if line[2] in uczniowie.keys() and line[3] == '21':
            del uczniowie[line[2]]

print("Zadanie 98.5")
for i in uczniowie.keys():
    print(uczniowie[i][0], uczniowie[i][1])
