#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Jak ma na imię jedyny kandydat o nazwisku 'PIPAŁA'?")
sql = """
    Select imie
    From kandydat
    Where nazwisko Like 'PIPAŁA'
"""
print(sql)
for wiersz in db.execute(sql):
    (imie,) = wiersz
    print(f"{imie}")
