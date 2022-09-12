#!/usr/bin/env python3
# by neloduka_sobe

# Dla nominałów posortowanych rosnąco
def wydawanie_reszty(kwota, nominaly):
    """
        kwota - int; kwota reszty do wydania
        nominaly [int]; nominały pieniędzy posortowane malejąco
    """
    wydane_nominaly = []
    ind = 0
    while kwota >= nominaly[-1]:
        if nominaly[ind] <= kwota:
            wydane_nominaly.append(nominaly[ind])
            kwota -= nominaly[ind]
        else:
            ind += 1
    return wydane_nominaly

# Dla nominałów posortowanych malejąco
def wydawanie_reszty_1(kwota, nominaly):
    """
        kwota - int; kwota reszty do wydania
        nominaly [int]; nominały pieniędzy posortowane rosnąco
    """
    wydane_nominaly = []
    ind = len(nominaly)-1
    while kwota >= nominaly[0]:
        if nominaly[ind] <= kwota:
            wydane_nominaly.append(nominaly[ind])
            kwota -= nominaly[ind]
        else:
            ind -= 1
    return wydane_nominaly

print(wydawanie_reszty(13.5, [100,50,20,10,5,2,1,0.5]))
print(wydawanie_reszty_1(13.5, [0.5,1,2,5,10,20,50,100]))
