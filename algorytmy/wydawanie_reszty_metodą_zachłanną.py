#!/usr/bin/env python3
# by neloduka_sobe

# Dla nominałów posortowanych malejąco
def wydawanie_reszty(kwota, nominaly):
    """
        kwota - int; kwota reszty do wydania
        nominaly [int]; nominały pieniędzy posortowane malejąco
    """
    wydane_nominaly = [] # lista zawierająca wydane nominały
    ind = 0

    while kwota >= nominaly[-1]: # dopóki kwota jest większa od najmniejszego dostępnego nominału

        if nominaly[ind] <= kwota: # Jeśli nominał mieści się w kwocie
            # Wydaj nominał
            wydane_nominaly.append(nominaly[ind])
            kwota -= nominaly[ind]

        else: # W przeciwnym wypadku
            # Zmień nominał na mniejszy
            ind += 1

    return wydane_nominaly # Zwróć wydane nominały

# Dla nominałów posortowanych rosnąco
def wydawanie_reszty_1(kwota, nominaly):
    """
        kwota - int; kwota reszty do wydania
        nominaly [int]; nominały pieniędzy posortowane rosnąco
    """

    wydane_nominaly = [] # lista zawierająca wydane nominały
    ind = len(nominaly)-1

    while kwota >= nominaly[0]: # dopóki kwota jest większa od najmniejszego dostępnego nominału

        if nominaly[ind] <= kwota: # Jeśli nominał mieści się w kwocie
            # Wydaj nominał
            wydane_nominaly.append(nominaly[ind])
            kwota -= nominaly[ind]

        else: # W przeciwnym wypadku
            # Zmień nominał na mniejszy
            ind -= 1

    return wydane_nominaly # Zwróć wydane nominały

print(wydawanie_reszty(13.5, [100,50,20,10,5,2,1,0.5]))
print(wydawanie_reszty_1(13.5, [0.5,1,2,5,10,20,50,100]))
