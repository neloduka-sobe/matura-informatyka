#!/usr/bin/env python3
# by neloduka_sobe


# Wersja iteracyjna
def wyszukiwanie_binarne(tab, lewy, prawy, szukany):

    while lewy < prawy:
        
        # Wyznaczamy środek szukanego obszaru
        srodek = (lewy+prawy) // 2

        # Jeżeli znaleźliśmy szukaną liczbę
        if tab[srodek] == szukany:
            return srodek
        
        # Jeżeli szukana liczba znajduje się w prawej części
        elif szukany > tab[srodek]:
            lewy = srodek + 1

        # Jeżeli szukana liczba znajduje się w lewej części
        elif szukany < tab[srodek]:
            prawy = srodek

    return -1


# Wersja rekurencyjna 1
def wyszukiwanie_binarne_1(tab, lewy, prawy, szukany):

    if prawy >= lewy:

        srodek = lewy + ((prawy-lewy) // 2) # Wyznaczanie środka
        if srodek > len(tab) - 1:
            return -1
        
        # Jeśli szukany jest na środku danego przedziału
        if tab[srodek] == szukany:
            return srodek
        
        # Jeśli element szukany jest mniejszy od środka (znajduje się po lewej stronie)
        elif tab[srodek] > szukany:
            return wyszukiwanie_binarne_1(tab, lewy, srodek-1, szukany)

        # Jeśli element szukany jest większy od środka (znajduje się po prawej stronie)
        else:
            return wyszukiwanie_binarne_1(tab, srodek+1, prawy, szukany)

    else:
        return -1


# Wersja rekurencyjna 2
def wyszukiwanie_binarne_2(tab, szukany, ind=0):
    srodek = (len(tab)-1) // 2

    if len(tab) == 1 and tab[0] != szukany:
        return -1

    elif tab[srodek] == szukany:
        return  ind + srodek

    elif tab[srodek] < szukany:
        return wyszukiwanie_binarne_2(tab[srodek+1:], szukany, ind+srodek+1)

    else:
        return wyszukiwanie_binarne_2(tab[:srodek], szukany, ind)


### TESTY 1
tab1 = [2,5,6,7,145,3754,3457347,74547357]
tab2 = [1,2,5,6,7,145,3754,3457347,74547357]

print(wyszukiwanie_binarne(tab1, 0, len(tab1), 74547357))
print(wyszukiwanie_binarne(tab2, 0, len(tab2), 3754))
print(wyszukiwanie_binarne_2(tab1, 74547357))
print(wyszukiwanie_binarne_2(tab2, 3754))
print(wyszukiwanie_binarne_1(tab1, 0, len(tab1), 74547357))
print(wyszukiwanie_binarne_1(tab2, 0, len(tab2), 3754))

### TESTY 2

print(wyszukiwanie_binarne([1, 2, 3, 4],0,4,4) == 3)
print(wyszukiwanie_binarne_1([1, 2, 3, 4],0,4,4) == 3)
print(wyszukiwanie_binarne_2([1, 2, 3, 4], 4) == 3)

print(wyszukiwanie_binarne([1, 2, 3, 4],0,4,1) == 0)
print(wyszukiwanie_binarne_1([1, 2, 3, 4],0,4,1) == 0)
print(wyszukiwanie_binarne_2([1, 2, 3, 4], 1) == 0)

print(wyszukiwanie_binarne([1, 2, 3, 4],0,4,3) == 2)
print(wyszukiwanie_binarne_1([1, 2, 3, 4],0,4,3) == 2)
print(wyszukiwanie_binarne_2([1, 2, 3, 4], 3) == 2)

print(wyszukiwanie_binarne([1, 2, 3, 4, 5],0,5,3) == 2)
print(wyszukiwanie_binarne_1([1, 2, 3, 4, 5],0,5,3) == 2)
print(wyszukiwanie_binarne_2([1, 2, 3, 4, 5], 3) == 2)

print(wyszukiwanie_binarne([1, 2, 3, 4],0,4,3) == 2)
print(wyszukiwanie_binarne_1([1, 2, 3, 4],0,4,3) == 2)
print(wyszukiwanie_binarne_2([1, 2, 3, 4], 3) == 2)

print(wyszukiwanie_binarne([1, 2],0,2,3) == -1)
print(wyszukiwanie_binarne_1([1, 2],0,2,3) == -1)
print(wyszukiwanie_binarne_2([1, 2], 3) == -1)
