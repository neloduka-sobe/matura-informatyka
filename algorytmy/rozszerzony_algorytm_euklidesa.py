#!/usr/bin/env python3
'''
link: https://www.youtube.com/watch?v=YcLfSRK70R4&list=PLpEP9TjZ__-Ff6YYZSZ0EAd54AdVFXOf5&index=29
Wersja podstawowa:
nwd(a,b) = {
        nwd(b, a%b) dla b > 0
        a dla b = 0
        }

Wersja rozszerzona:
    x*a + y*b = NWD(a,b)
    x,y całkowite
    x = ypoprzedni
    y = xpoprzedni - a//b * ypoprzedni
'''

p_y=0
y=0
x=0
def nwd(a,b):
    global x,y,p_y
    if b != 0 :
        nwd(b,a%b) 
        p_y = y
        y = x - a//b*p_y
        x = p_y

if __name__ == "__main__":
    x = 1
    y = 0
    nwd(23,13)
    print(x,y)
