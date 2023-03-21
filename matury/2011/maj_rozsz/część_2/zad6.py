#!/usr/bin/env python3

dane = []

with open("Dane/liczby.txt", "r") as f:
	for i in f:
		dane.append(i.strip())

ile_a = 0
ile_c = 0
suma = 0
for i in dane:
	
	# a)
	if i[-1] == '0':
		ile_a += 1
	# c)
	if len(i) == 9:
		ile_c += 1
		suma += int(i,2)

print("Zadanie 6")
print(f"a) {ile_a}")
b = max(dane, key=lambda x: int(x,2))
print(f"b) binarnie: {b}; dziesiętnie: {int(b,2)}")
print(f"c) ilość: {ile_c}; suma: {bin(suma)[2:]}")
