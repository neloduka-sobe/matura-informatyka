#!/usr/bin/env python3

### Wczytywanie danych
dane = []
with open('DANE/dane.txt', 'r') as f:
    for line in f:
        dane.append(line.strip())

### Zad 6 a)
slowa = dict()

for i in dane:
    if i in slowa.keys():
        slowa[i] += 1
    else:
        slowa[i] = 1

print("Zadanie 6 a)")
m = max(slowa, key=lambda x: slowa[x])
ile = sum(1 for i in slowa.values() if i > 1)
print(f"Powtarza się {ile} słów.")
print(f"Najczęściej powtarza się słowo {m}: {slowa[m]} razy.")

### Zad 6 b)

ile = 0
parz_kon = ('2','4','6','8','0','A', 'C', 'E')
for i in dane:
    if i[-1] in parz_kon:
        ile += 1
print("Zadanie 6 b)")
print(f"Ilość liczb parzystych w pliku: {ile}")


### Zad 6 c)

ile_c = 0

for i in dane:
    if i == i[::-1]:
        ile_c+=1

print("Zadanie 6 c)")
print(f"Ilość palindromów w pliku: {ile_c}")
