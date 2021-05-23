#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Ilu jest kandydatów o nazwisku 'WÓJCIK'?")
sql = """
    Select count(*)
    From kandydat
    Where nazwisko = 'WÓJCIK'
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")
