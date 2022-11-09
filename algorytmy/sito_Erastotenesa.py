#!/usr/bin/env python3
# by neloduka_sobe

# Krótka
def sito_1(n):
    ret = [i for i in range(2, n+1)]
    for index, war in enumerate(ret):
        if war != 0:
            for y in range(index+war, len(ret), war):
                ret[y] = 0
    return [a for a in ret if a != 0]


# wersja druga
def sito_2(n):

    ret = []
    for i in range(2, n+1):
        ret.append(i)

    for index in range(int(n ** 0.5) - 2):
        if ret[index] != 0:
            for y in range(index + ret[index], len(ret), ret[index]):
                ret[y] = 0

    ret = set(ret)
    ret.remove(0)
    return ret


# Dla purystów
def sito_3(n):

    # Stworzenie tablicy zawierającej liczby z przedziału [2;n]
    arr = []
    for i in range(n+1):
        arr.append(i)

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] != 0:
            for y in range(i*i, n+1, i):
                arr[y] = 0

    ret = [] 
    for i in range(2,n+1):
        if arr[i] != 0:
            ret.append(arr[i])

    return ret

print(sito_1(100))
print(sito_2(100))
print(sito_3(1024))
