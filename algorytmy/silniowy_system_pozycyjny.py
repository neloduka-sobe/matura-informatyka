#!/usr/bin/env python3

# Zamiana z silniowego systemu pozycyjnego na dziesiętny
def siln_na_dzies(liczba):
    wynik = 0  # Zmienna przechowywająca wynik
    liczba = str(liczba) # Potrzebujemy str jako typ zmiennej, gdyż będziemy po niej iterować
    silnia = 1 # Zmienna przechwywająca wartości kolejnych pozycji systemu silniowego

    for i in range(1, len(liczba)+1):
        silnia *= i # Obliczanie wartości silni z i 
        wynik += (int(liczba[-i]) * silnia) # Dodawanie do wyniku iloczynu watrości pozycji w systemie pozycyjnym i liczby na danej pozycji

    return wynik # Zwracanie wyniku działania funkcji


# Zamiana z dziesiętnego na silniowy
def dzies_na_siln(liczba):
    silnia = 1 # Zmienna przechowywająca wartość silni
    n = 1 # Zmienna przechowywająca liczbę z której policzona jest silnia

    # Pętla służąca do znalezienia największej silni mieszczącej się w liczbie
    while silnia <= liczba:
        n += 1
        silnia *= n
    silnia //= n
    n -= 1
    
    wynik = '' # Zmienna przechowywająca wynik
    while n > 0:
        wynik += str(int(liczba // silnia) ) # Dodawanie do wyniku całkowitej ilości wartości silni możliwych do zmieszczenia w liczbie
        liczba %= silnia # Przypisywanie do zmiennej liczba reszty z dzielenia przez silnię
        silnia //= n # Dekrementacja wartości silni z n! do (n-1)!
        n -= 1 # Zmniejszanie n, aby odpowiadała wartości silni

    return wynik # Zwracanie wyniku


# Testy
war = [i for i in range(1000)]
for i in war:
    if i != siln_na_dzies(dzies_na_siln(i)):
        print(i)
