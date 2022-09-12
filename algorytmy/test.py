import math #importujemy biblioteke potrzebna do pierwiastkowania i jego zaokgraglania


print("Program znajdujacy liczby pierwsze z przedzialu <2,n>.")
print("Podaj liczbę n: ")
n = int(input())
liczby = [True] * (n+1) #tworzymy n+1 elementowa tablice
for i in range(2, int(math.ceil(math.sqrt(n)))): #iterujemy poprzez nia, zaczynajac od 2, a konczac na zaokraglonym do gory pierwiastkiem z n
    if liczby[i]: #jezeli liczba jest pierwsza
        for k in range(i*i, n+1, i): #oznacz wszystkie jej wielokrotnosci jako liczby zlozone
            liczby[k] = False
print("Liczby pierwsze z przedzialu <2," + str(n) + "> : ")
for i in range(2, n+1): #wypisujemy elementy utworzonej tablicy
    if liczby[i]:
        print(str(i), end=" | ")
