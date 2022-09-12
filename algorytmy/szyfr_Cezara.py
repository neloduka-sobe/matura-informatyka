#!/usr/bin/env python3
# by neloduka_sobe
# ord('a') = 97
# ord('z') = 122

def szyfr(text, n):
    """Funkcja szyfrująca za pomocą szyfru Cezara wiadomości zapisane znakami w alfabecie abcdefghijklmnopqrstuvwxyz"""
    ret = ''
    for litera in text:
        if ord(litera) + n > 122:
            ret += chr(ord(litera) + n - 26)
        elif ord(litera) + n < 97: # Pętla potrzebna przy rozszyfrowywaniu
            ret += chr(ord(litera) + n + 26)
        else:
            ret += chr(ord(litera) + n)
    return ret


def szyfr_2(alfabet, text, n):
    """Funkcja szyfrująca za pomocą szyfru Cezara wiadomości zapisane znakami w podanym alfabecie """
    ret = ''
    for litera in text:
        if alfabet.index(litera) + n > len(alfabet):
            ret += alfabet[alfabet.index(litera) + n - len(alfabet)]
        else:
            ret += alfabet[alfabet.index(litera) + n]

    return ret


print(szyfr('testz', 4))
print(szyfr_2('abcdefghijklmnopqrstuvwxyz', 'testz', 4))
print(szyfr('xiwxd', -4))
print(szyfr_2('abcdefghijklmnopqrstuvwxyz', 'xiwxd', -4))
