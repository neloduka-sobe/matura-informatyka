#!/usr/bin/env python3

# Stałe
CENA_PASZY = 1.9
PASZA_PER_KURA = 0.2
DLUGOSC = 180
CENA_JAJKA = 0.9
CENA_KURY = 18

# Zmienne
ilosc_kur = 200
pieniadze = 0
suma_karmienie = 0
realny_zysk = 0

with open("wykres.csv", 'w') as f:
	f.write(f"Dzień,dzienny przychód,dzienny koszt\n")


for nr_dnia in range(1, DLUGOSC+1):
	dzien_tyg = nr_dnia % 7 # 0 - niedziela

	'''
	# a)
	if nr_dnia != 1 and ilosc_kur == 200:
		print(f"Rano przed kupieniem {nr_dnia} dnia")
		break
	'''

	### Rano
	koszt = 0
	if nr_dnia % 30 == 0:
		kupione = int(ilosc_kur*0.2)
		koszt = kupione*CENA_KURY
		pieniadze -= koszt
		ilosc_kur += kupione

		'''
		# a)
		if nr_dnia != 1 and ilosc_kur == 200:
			print(f"Rano po kupieniu {nr_dnia} dnia")
			break
		'''

	karmienie = PASZA_PER_KURA * ilosc_kur
	cena_karmienia = karmienie*CENA_PASZY
	pieniadze -= cena_karmienia
	suma_karmienie += cena_karmienia


	### Południe
	pieniadze_z_jajek = 0
	if dzien_tyg:
		pieniadze_z_jajek = (ilosc_kur*CENA_JAJKA)
		pieniadze += pieniadze_z_jajek



	### Wieczór
	if nr_dnia % 2 == 1:
		ilosc_kur -= 2
		
		'''
		# a)
		if nr_dnia != 1 and ilosc_kur == 200:
			print(f"Wieczorem po wizycie lisa {nr_dnia} dnia")
			break
		'''

	dzienny_zysk = pieniadze_z_jajek - koszt - cena_karmienia
	realny_zysk += dzienny_zysk
	with open("wykres.csv", 'a') as f:
		f.write(f"{nr_dnia},{round(pieniadze_z_jajek,2)},{round(koszt+cena_karmienia,2)}\n")
	
	'''
	# c)
	if realny_zysk > 1500:
		print("c)")
		print(nr_dnia)
		break
	'''

print("b)")
print(round(suma_karmienie,2))
print("c)")
print(realny_zysk)
