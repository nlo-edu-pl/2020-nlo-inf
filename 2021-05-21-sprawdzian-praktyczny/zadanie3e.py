#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Ilu jest kandydatów zamieszkałych w Józefosławiu?")
sql = """
    Select count(*)
    From kandydat
    Where zamieszk = 'JÓZEFOSŁAW'
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")

print("Ilu jest kandydatów zamieszkałych w Józefosławiu?")
sql = """
    Select count(*)
    From kandydat
    Where zamieszk = 'Józefosław'
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")

print("Ilu jest kandydatów zamieszkałych w Józefosławiu?")
sql = """
    Select count(*)
    From kandydat
    Where zamieszk = 'Józefosław' Or zamieszk = 'JÓZEFOSŁAW'
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")


print("Ilu jest kandydatów zamieszkałych w Józefosławiu?")
sql = """
    Select count(*)
    From kandydat
    Where zamieszk in ('Józefosław', 'JÓZEFOSŁAW')
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")
