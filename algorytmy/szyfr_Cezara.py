#!/usr/bin/env python3
# by neloduka_sobe
# ord('a') = 97
# ord('z') = 122

def szyfr(text, n):
    """Funkcja szyfrująca za pomocą szyfru Cezara wiadomości zapisane znakami w alfabecie abcdefghijklmnopqrstuvwxyz"""
    n = n % 26 # Reszta z dzielenia przez długość alfabetu to rzeczywiste przesunięcie liter
    ret = '' # Wynik działania algorytmu
    for litera in text:
        if ord(litera) + n > 122: # Jeżeli nowa liczba przekracza zakres alfabetu z prawej strony
            ret += chr(ord(litera) + n - 26) # Dodawanie zaszyfrowanego znaku do wyniku
        elif ord(litera) + n < 97: # Pętla potrzebna przy rozszyfrowywaniu, gdy nowa liczba przekracza zakres alfabetu z lewej strony
            ret += chr(ord(litera) + n + 26) # Dodawanie zaszyfrowanego znaku do wyniku
        else: # Gdy nowy kod mieści się w zakresie alfabetu
            ret += chr(ord(litera) + n) # Dodawanie zaszyfrowanego znaku do wyniku
    return ret


def szyfr_2(alfabet, text, n):
    """Funkcja szyfrująca za pomocą szyfru Cezara wiadomości zapisane znakami w podanym alfabecie """
    n = n % len(alfabet) # Reszta z dzielenia przez długość alfabetu to rzeczywiste przesunięcie liter
    ret = ''
    for litera in text:
        if alfabet.index(litera) + n > len(alfabet):
            ret += alfabet[alfabet.index(litera) + n - len(alfabet)]
        else:
            ret += alfabet[alfabet.index(litera) + n]

    return ret


print(szyfr('testz', 400))
print(szyfr_2('abcdefghijklmnopqrstuvwxyz', 'testz', 400))
print(szyfr('docdj', -400))
print(szyfr_2('abcdefghijklmnopqrstuvwxyz', 'docdj', -400))
