#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("W ktorym roku urodził się najstarszy kandydat?")
sql = """
    Select min(rok_ur)
    From kandydat
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")

print("W ktorym roku urodził się najstarszy kandydat?")
sql = """
    Select rok_ur
    From kandydat
    Order By rok_ur
    Limit 1
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")
