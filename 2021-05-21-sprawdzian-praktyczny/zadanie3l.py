#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Ilu jest kandydatów o nazwisku 'NOWAK' w każdym roczniku?")
sql = """
    Select rok_ur, count(*)
    From kandydat
    Where nazwisko = 'NOWAK'
    Group By rok_ur
    Order By rok_ur
"""
print(sql)
for wiersz in db.execute(sql):
    (rok, ile) = wiersz
    print(f"{rok}: {ile}")
