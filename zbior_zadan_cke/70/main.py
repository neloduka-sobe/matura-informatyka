#!/usr/bin/env python3

### Funkcje
def f(x):
    return (x**4/(500)) - (x**2/(200)) - (3/250)

def g(x):
    return -(x**3/30) + (x/20) + (1/6)

### Zadanie 70.1
pole_pros = 8*(32+(2/3)+19+(61/125))

powierzchnia_zas = 0
for x in range(2*100000, 10*100000+1):
    x /= 100000
    powierzchnia_zas += (abs(f(x))*0.00001)
    powierzchnia_zas += (abs(g(x))*0.00001)

print("Zadanie 70.1")
print("Powierzchia zasłony: ", round(powierzchnia_zas, 3))
print("Powierzchia pozostałego materiału: ", round(pole_pros - powierzchnia_zas, 3))

### Zadanie 70.2
def odl(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5
obw = 8*2 + 32+(2/3)+19+(61/125)
for x in range(2000, 10000, 8):
    x /= 1000
    obw += odl(x+0.008, f(x+0.008), x, f(x))
    obw += odl(x+0.008, g(x+0.008), x, g(x))

print(f"\nZadanie 70.2\nNależy kupić: {int(obw)+1} m taśmy")

### Zadanie 70.3
zad3 = 0
BOK = 32+(2/3)+19+(61/125)
for x in range(975, 2*100 , -25):
    x /= 100
    zad3 += int(abs(g(x)) + abs(f(x)))
    
print(f"\nZadanie 70.3:\nDługość pasów jest równa: {zad3} m")
