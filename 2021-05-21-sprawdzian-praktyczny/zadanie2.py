#!/usr/bin/python3

# autor: Mateusz Adamowski
# email: mateusz.adamowski@nlo.edu.pl

with open("slowa.txt", encoding="UTF-8") as plik:
    for linia in plik:
        slowo = linia.strip()
        if len(slowo) >= 6:
            ile_kropek = len(slowo) - 4 
            print(f"{slowo[0:4]}{'.' * ile_kropek}")
