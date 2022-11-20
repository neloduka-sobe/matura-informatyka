#!/usr/bin/env python3

# Złożoność liniowa O(n)
def najp(arr):
    naj = dict()
    for i in arr:
        if i not in naj.keys():
            naj[i] = 1
        else:
            naj[i] += 1
    return max(naj, key=lambda x: naj[x])

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

    print(najp(dane1))
    print(najp(dane2))
    print(najp(dane3))
