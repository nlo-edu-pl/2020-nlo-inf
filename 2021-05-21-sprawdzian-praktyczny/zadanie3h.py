#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Jakie jest 5 najpopularniejszych imion męskich pośród kandydatów (mężczyzn) urodzonych w latach 1970-1985?")
sql = """
    Select imie
    From kandydat
    Where rok_ur >= 1970 And rok_ur <= 1985 And plec = 'M'
    Group By imie
    Order By count(*) Desc
    Limit 5
"""
print(sql)
for wiersz in db.execute(sql):
    (imie, ) = wiersz
    print(f"{imie}")
