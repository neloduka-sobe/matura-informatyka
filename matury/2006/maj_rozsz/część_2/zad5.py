#!/usr/bin/env python3

def f(x):
    return -1*(x**2/50)

def g(x):
    return 1 + (x**2/100) - (x/200)

### a)
# Z metody trapezów
# Podział pola na trapezy o wysokości 0.01 i równolegóych bokach  f(x)+g(x) i f(x+0.01) + g(x+0.01)
pole = 0
for i in range(0, 1000):
    i /= 100
    a = abs(f(i)) + g(i)
    b = abs(f(i+0.01)) + g(i+0.01)
    pole += (0.01 * (a+b)) / 2

print("Zadanie 5 a)")
print(f"{pole=}")

### b)
print("Zadanie 5 b)")
i = 0
while True:
    if (int(abs(f(i))) + int(abs(g(i)))) > 26:
        print("Współrzędne")
        print(f"{i}, {int(g(i))}")
        print(f"{i}, {int(g(i))-26}")
        print(f"{i+100}, {int(g(i))}")
        print(f"{i+100}, {int(g(i))-26}")
        break
    i += 1
