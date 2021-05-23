#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Jakie jest 5 najpopularniejszych imion męskich pośród wszystkich kandydatów (mężczyzn) i ilu kandydatów nosi każde z tych imion?")
sql = """
    Select imie, count(*)
    From kandydat
    Where plec = 'M'
    Group By imie
    Order By count(*) Desc
    Limit 5
"""
print(sql)
for wiersz in db.execute(sql):
    (imie, ile) = wiersz
    print(f"{imie}: {ile}")
