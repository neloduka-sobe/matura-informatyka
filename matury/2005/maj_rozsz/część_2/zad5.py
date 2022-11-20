#!/usr/bin/env python3


def naj_sum(arr):
    m = arr[0] + arr[1]
    for x in range(0, len(arr)):
        s = 0
        for y in range(0, len(arr)-x):
            s += arr[x+y]    
            if s > m:
                m = s
    return m


if __name__ == "__main__":
    ### Wczytywanie danych
    dane1 = []
    with open("DANE/dane5-1.txt", 'r') as f:
        for line in f:
            dane1.append(int(line))
    dane2 = []
    with open("DANE/dane5-2.txt", 'r') as f:
        for line in f:
            dane2.append(int(line))
    dane3 = []
    with open("DANE/dane5-3.txt", 'r') as f:
        for line in f:
            dane3.append(int(line))

    print(naj_sum([1, -2, 6, -5, 7, -3]))
    print(naj_sum(dane1))
    print(naj_sum(dane2))
    print(naj_sum(dane3))
