#!/usr/bin/env python3
# by neloduka_sobe
### Funkcje
# Funkcja rekurencyjna
def fibo_rek(n):
    if n == 1 or n == 0:
        return 1
    return fibo_rek(n-1) + fibo_rek(n-2)

# Funkcja iteracyjna
def fibo_it(n):
    a = 1
    v = 1
    for i in range(2,n+1):
        v, a = a+v, v
    return v


### Sprawdzenie
if __name__ == "__main__":
    for i in range(25):
        print(f"{i=} {fibo_rek(i)=}; {fibo_it(i)=}")
