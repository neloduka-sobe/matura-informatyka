#!/usr/bin/env python3

# Wczytywanie danych
dane = []
with open('Dane/anagram.txt', 'r') as f:
	for i in f:
		dane.append(i.strip().split())

# a)
with open('odp_4a.txt', 'w') as f:
	for i in dane:
		if len(set(len(i[y]) for y in range(5))) == 1:
			f.write(' '.join(i) + '\n')

# b)
with open('odp_4b.txt', 'w') as f:
	for i in dane:
		if len(set(''.join(sorted(i[y])) for y in range(5))) == 1:
			f.write(' '.join(i) + '\n')
