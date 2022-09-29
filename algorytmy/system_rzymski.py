#!/usr/bin/env python3
# by neloduka_sobe

wartosci_rzym = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
wartosci_dzies = (1, 5, 10, 50, 100, 500, 1000)

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
    ret = ''
    for ind, i in enumerate(str(n)[::-1]):
        wartosci = (
        ('I','II','III','IV','V','VI','VII','VIII','IX','X'),
        ('X','XX','XXX','XL','L','LX','LXX','LXXX','XC'),
        ('C','CC','CCC','CD','D','DC','DCC','DCCC', 'CM'),
        ('M','MM','MMM')
        )
        if int(i) != 0:
            ret = wartosci[ind][int(i)-1] + ret
    return ret

### Wywołanie
if __name__ == "__main__":
    for i in range(1,4000):
        # Testy
        if i != rzym_na_dzies(dzies_na_rzym(i)):
            print(dzies_na_rzym(i))
