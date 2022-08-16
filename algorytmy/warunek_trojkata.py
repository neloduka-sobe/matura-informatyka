#!/usr/bin/env python3
# Algorytm sprawdzajączy czy z podanych boków można utworzyć trójkąt
# Link: https://www.algorytm.edu.pl/algorytmy-maturalne/nierownosc-trojkata.html

def warunek_trojkata(a,b,c):
    return a + b > c and a + c > b and c + b > a

if __name__ == '__main__':
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    print(warunek_trojkata(a,b,c))

