#!/usr/bin/env python3
# 21.02.2022 by neloduka_sobe

# Wczytywanie danych
dane = []
with open('dane/wspolrzedne.txt', 'r') as f:
    for line in f:
        dane.append(line.strip().split("\t"))

### 81.1
licznik = 0
for i in dane:
    teza = True
    for y in i:
        y = int(y)
        if y <= 0:
            teza = False
            break
    if teza:
        licznik += 1

print("Zadanie 81.1")
print(f"Ilość: {licznik}")


### 81.2
licznik2 = 0
for punkty in dane:
    x1, y1, x2, y2, x3, y3 = int(punkty[0]), int(punkty[1]),int(punkty[2]),int(punkty[3]),int(punkty[4]),int(punkty[5])
    a1 = (y1-y2) / (x1-x2) if x1-x2 != 0 else 0
    a2 = (y1-y3) / (x1-x3) if x1-x3 != 0 else 0
    if a1 == a2:
        licznik2 += 1
print("Zadanie 81.2")
print(f"Ilość: {licznik2}")


### 81.3
def oblicz_obwod(x1,y1,x2,y2,x3,y3):
    """Funkcja licząca obwód trójkąta o podanych wierzchołkach"""
    obw = 0
    obw += ((x1-x2)**2 + (y1-y2)**2)**0.5
    obw += ((x1-x3)**2 + (y1-y3)**2)**0.5
    obw += ((x2-x3)**2 + (y2-y3)**2)**0.5
    return obw

    

dane2 = []
maks = 0
wspol = []
with open("dane/wspolrzedneTR.txt", 'r') as f:
    for punkty in f:
        punkty = punkty.strip().split('\t')
        x1, y1, x2, y2, x3, y3 = int(punkty[0]), int(punkty[1]),int(punkty[2]),int(punkty[3]),int(punkty[4]),int(punkty[5])
        tmp = oblicz_obwod(x1,y1,x2,y2,x3,y3)
        if tmp > maks:
            maks = tmp
            wspol = [(x1,y1), (x2,y2), (x3, y3)]

print("Zadanie 81.3")
print(f"Maks: {maks}")
print(f"Współrzędne: {wspol}")

### 81.4
liczba = 0
def prostokatny(x1,y1,x2,y2,x3,y3):
    """Funkcja sprawdzająca, czy trójkąt o podanych wierzchołkach jest prostokątny"""
    arr = [((x1-x2)**2 + (y1-y2)**2),  ((x1-x3)**2 + (y1-y3)**2), ((x2-x3)**2 + (y2-y3)**2)]
    arr.sort()
    return arr[0] + arr[1] == arr[2]

# Wczytywanie danych
with open("dane/wspolrzedneTR.txt", 'r') as f:
    for punkty in f:
        punkty = punkty.strip().split('\t')
        x1, y1, x2, y2, x3, y3 = int(punkty[0]), int(punkty[1]),int(punkty[2]),int(punkty[3]),int(punkty[4]),int(punkty[5])
        if prostokatny(x1,y1,x2,y2,x3,y3):
            liczba += 1

print("Zadanie 81.4")
print(f"Liczba: {liczba}")

### 81.5
def wyznacz_punkt(ix1,iy1,ix2,iy2,ix3,iy3):
    """Funkcja wyznaczająca współrzędne czwartego punktu w równoległoboku"""
    v1 = [ix1-ix2, iy1-iy2]
    v2 = [ix1-ix3, iy1-iy3]
    return [ix3+v1[0], iy3+v1[1] ]

# Wczytywanie danych
with open("dane/wspolrzedneTR.txt", 'r') as f:
    for punkty1 in f:
        punkty1 = punkty1.strip().split('\t')
        x1, y1, x2, y2, x3, y3 = int(punkty1[0]), int(punkty1[1]),int(punkty1[2]),int(punkty1[3]),int(punkty1[4]),int(punkty1[5])
        x4, y4 = wyznacz_punkt(x1,y1,x2,y2,x3,y3)
        if x4 == y4:
            print(f"({x1}, {y1}) ({x2}, {y2}) ({x3}, {y3}) ({x4}, {y4})")
