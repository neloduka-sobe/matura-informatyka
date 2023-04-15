#!/usr/bin/env python3

dane = []

with open('NM_DANE_PR/pomiary.txt', 'r') as f:
	for i in f:
		if i.startswith('data;godzina;czujnik1;czujnik2;czujnik3;czujnik4;czujnik5;czujnik6;czujnik7;czujnik8;czujnik9;czujnik10'):
			continue
		dane.append(i.strip().split(';'))
# 5.1
ilosc_pomiarow1 = 0
suma1 = 0
for i in dane:
	if 5 <= int(i[1][:2]) <= 12:
		if int(i[1][:2]) == 12 and int(i[1][3:]) != 0:
			continue
		suma1 += float(i[6].replace(',','.'))
		ilosc_pomiarow1 += 1

print(f"5.1: {round((suma1/ilosc_pomiarow1),2)}")
