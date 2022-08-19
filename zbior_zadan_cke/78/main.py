#!/usr/bin/env python3

### Wczytanie danych
wiadomosci = []
podpisy = []

with open('dane/podpisy.txt', 'r') as f:
    for line in f:
        podpisy.append([int(i) for i in line.strip().split(' ')])

with open('dane/wiadomosci.txt', 'r') as f:
    for line in f:
        wiadomosci.append(line.strip())

### Funkcje
def skrot(wiad):
    S = [ord(i) for i in "ALGORYTM"] # a)
    wiad += '.'*(8 - len(wiad) % 8) # b)

    # c)
    for porcja in [wiad[i:i+8] for i in range(0, len(wiad), 8)]:
        for j in range(0, 8):
            S[j] =  (S[j] + ord(porcja[j])) % 128

    # d)
    wynik = ''
    for j in range(0,8):
        wynik += chr(65 + S[j] % 26 )

    return len(wiad), S, wynik


def deszyfrowanie(wiad, d, n):
    wynik = ''
    for y in list(wiad):
        wynik += chr(y*d % n)
    return wynik


### Zadanie 78.1
print(f"Zadanie 78.1\na) {skrot(wiadomosci[0])[0]}\nb) {skrot(wiadomosci[0])[1]}\nc) {skrot(wiadomosci[0])[2]}\n")

### Zadanie 78.2
print("Zadanie 78.2")
d, n = 3, 200

for i in podpisy:
    print(deszyfrowanie(i, d, n))


### Zadanie 78.3
wiarygodne = []

for i in range(11):
    if deszyfrowanie(podpisy[i], d, n) == skrot(wiadomosci[i])[2]:
        wiarygodne.append(i+1)

print("\nZadanie 78.3")
print(*wiarygodne)
