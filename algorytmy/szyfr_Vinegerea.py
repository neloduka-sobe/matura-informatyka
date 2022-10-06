#!/usr/bin/env python3
# by neloduka_sobe

def szyfruj(tekst_jawny, klucz, alfabet_jawny):
    alfabety_szyfrowe = []

    slowo_kluczowe = ''
    for i in range(len(klucz)):
        if klucz[i] not in klucz[:i] + ' ':
            slowo_kluczowe += klucz[i]
    
    for i in slowo_kluczowe:
        y = alfabet_jawny.index(i)
        a = ''
        while len(a) < len(alfabet_jawny):
            a += alfabet_jawny[y]
            y += 1
            y %= len(alfabet_jawny)
        alfabety_szyfrowe.append(a)

    ret = ''
    spacje = 0
    for ind, i in enumerate(tekst_jawny):
        if i == ' ':
            spacje += 1
            ret += ' '
            continue
        ind -= spacje
        ret += alfabety_szyfrowe[ind%len(slowo_kluczowe)][alfabet_jawny.index(i)]
    return ret

def deszyfruj(tekst, klucz, alfabet_jawny):
    alfabety_szyfrowe = []

    slowo_kluczowe = ''
    for i in range(len(klucz)):
        if klucz[i] not in klucz[:i] + ' ':
            slowo_kluczowe += klucz[i]
    
    for i in slowo_kluczowe:
        y = alfabet_jawny.index(i)
        a = ''
        while len(a) < len(alfabet_jawny):
            a += alfabet_jawny[y]
            y += 1
            y %= len(alfabet_jawny)
        alfabety_szyfrowe.append(a)

    ret = ''
    spacje = 0
    for ind, i in enumerate(tekst):
        if i == ' ':
            spacje += 1
            ret += ' '
            continue
        ind -= spacje
        ret += alfabet_jawny[alfabety_szyfrowe[ind%len(slowo_kluczowe)].index(i)]
    return ret

if __name__ == '__main__':
    print(szyfruj("NIEOBECNY SAM SOBIE SZKODZI", "TELEFON", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print(deszyfruj('GMPTPRVRJ XOZ LSMNS FSOZINV' ,"TELEFON", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
