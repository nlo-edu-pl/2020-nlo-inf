#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Jakie jest 5 najpopularniejszych nazwisk żeńskich pośród kandydatek mających 20-30 lat w dniu wyborów?")
sql = """
    Select nazwisko
    From kandydat
    Where plec = 'K' And wiek >= 20 And wiek <= 30
    Group By nazwisko
    Order By count(*) Desc
    Limit 5
"""
print(sql)
for wiersz in db.execute(sql):
    (nazw,) = wiersz
    print(f"{nazw}")
