#!/usr/bin/env python3
# by neloduka_sobe

wartosci_rzym = ('I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M')
wartosci_dzies = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)

# Rzymski na dziesięty
def rzym_na_dzies(s):
    '''
    Wytłumczenie:
        https://onestepcode.com/roman-decimal-converter/
    ''' 
    global wartosci_rzym
    global wartosci_dzies
    ret = 0
    r = wartosci_dzies[wartosci_rzym.index((s[-1]))]
    for i in s[::-1]:
        l = wartosci_dzies[wartosci_rzym.index(i)]
        if l < r:
            ret -= l
        else:
            ret += l
        r = l
    return ret

# Dziesiętny na rzymski
def dzies_na_rzym(n):
    pass


### Wywołanie
if __name__ == "__main__":
    print(rzym_na_dzies('MCDXLIX'))
