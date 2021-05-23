#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Ile lat ma w tym roku jedyny kandydat o imieniu 'JOE'?")
sql = """
    Select 2021 - rok_ur
    From kandydat
    Where imie = 'JOE'
"""
print(sql)
for wiersz in db.execute(sql):
    (wiek,) = wiersz
    print(f"{wiek}")
