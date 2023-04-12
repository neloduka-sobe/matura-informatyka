#!/usr/bin/env python3
import math

tj = []
klucze1 = []
klucze2 = []
sz = []

### Wczytywanie danych
with open("Dane/tj.txt","r") as f:
	for i in f:
		tj.append(i.strip())

with open("Dane/sz.txt","r") as f:
	for i in f:
		sz.append(i.strip())

with open("Dane/klucze1.txt","r") as f:
	for i in f:
		klucze1.append(i.strip())

with open("Dane/klucze2.txt","r") as f:
	for i in f:
		klucze2.append(i.strip())

def szyfruj(tekst, klucz):
	if len(klucz) < len(tekst):
		klucz *= math.ceil(len(tekst)//len(klucz)+1)
	ret = ''
	for ind,i in enumerate(tekst):
		nowa = ord(i) + (ord(klucz[ind])-64)
		while nowa > 90:
			nowa -= 26
		ret += chr(nowa)
	return ret
		
def deszyfruj(tekst, klucz):
	if len(klucz) < len(tekst):
		klucz *= math.ceil(len(tekst)//len(klucz)+1)
	ret = ''
	for ind,i in enumerate(tekst):
		nowa = ord(i) - (ord(klucz[ind])-64)
		while nowa < 65:
			nowa += 26
		ret += chr(nowa)
	return ret

# a)
with open('wynik4a.txt','w') as f:
	for x,y in zip(tj,klucze1):
		f.write(f"{szyfruj(x,y)}\n")

# b)
with open('wynik4b.txt','w') as f:
	for x,y in zip(sz,klucze2):
		f.write(f"{deszyfruj(x,y)}\n")
