#!/usr/bin/env python3

# IMPORTS
import sys

# CONSTANTS
LENGTH = 107

# VARIABLES
# uruchomić `python3 main.py zadx` aby uruchomić zadanie nr x
zad1 =  sys.argv[1] == 'zad1'
zad2 =  sys.argv[1] == 'zad2'
zad3 =  sys.argv[1] == 'zad3'
zad4 =  sys.argv[1] == 'zad4'
zad5 =  sys.argv[1] == 'zad5'

electric_speed = 4 if not zad5 else 4*0.9
gas_speed = 10 if not zad5 else 10*0.9
general_dist = 0


# FUNCTIONS
def write_to_file(day, value):
    with open("wykres.csv", 'a') as f:
        line = f"{day}, {value}\n"
        f.write(line)

# MAIN
if __name__ == '__main__':
    for day in range(1, LENGTH+1):

        ### 87.1
        if electric_speed < 3 and zad1:
            print(f"Zadanie 87.1: {day}")
            zad1 = False

        electric_hours = 20
        gas_hours = 4
        electric_dist = 0
        gas_dist = 0
        day_dist = 0

        if day % 7 == 4 and day != 4 and zad5:
            electric_hours = 18
            gas_hours = 4

        elif day == 73 and not zad5:
            electric_hours = 0
            gas_hours = 0

        elif day == 106 and not zad5:
            gas_hours = 9
            electric_hours = 0

        elif day >= 74 and not zad4 and not zad5:
            electric_hours = 0
            gas_hours = 11
        
        
        gas_dist = gas_hours * gas_speed
        electric_dist = electric_hours * electric_speed
        day_dist = gas_dist + electric_dist
        general_dist += day_dist

        ### 87.4
        if zad4 and general_dist >= 7701.09:
            print(f"Zadanie 87.4: {day}")
            break

        write_to_file(day, day_dist)
        electric_speed *= 0.99 if not zad5 else 0.997
        gas_speed *= 0.99 if not zad5 else 0.997

### 87.2
if zad2:
    print(f"Zadanie 87.2: {round(general_dist, 1)}")

### 87.3
if zad3:
    print("Zadani3 87.3 w pliku wykres.csv")

### 87.5
if zad5:
    print(f"Zadanie 87.5: {round(general_dist, 1)}")
