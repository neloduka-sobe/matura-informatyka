#!/usr/bin/env python3
# by neloduka_sobe

def szyfr(tekst, alfabet_jawny, slowo_kluczowe):
    alfabet_szyfrowy = '' 
    for i in range(len(slowo_kluczowe)):
        if slowo_kluczowe[i] not in slowo_kluczowe[:i] + ' ':
            alfabet_szyfrowy += slowo_kluczowe[i]

    y = alfabet_jawny.index(alfabet_szyfrowy[-1]) + 1
    while len(alfabet_szyfrowy) < len(alfabet_jawny):
        i = alfabet_jawny[y]
        if i not in alfabet_szyfrowy:
            alfabet_szyfrowy += i
        y += 1
        y %= len(alfabet_jawny)
    
    ret = ''
    for i in tekst:
        if i == ' ':
            ret += ' '
        else:
            ret += alfabet_szyfrowy[alfabet_jawny.index(i)]

    return ret

if __name__ == "__main__":
    print(szyfr('PEWNEGO PRZYJACIELA POZNAJE SIE W NIEPEWNEJ SYTUACJI', "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "KRYPTOLOGIA I STEGANOGRAFIA"))
        
