#!/usr/bin/python3

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

##########################################################

print("Przykład 1 - jeden wiersz, jedna kolumna:")

sql1 = """
    Select count(*)
    From kandydat
"""

for wiersz in db.execute(sql1):
    (n,) = wiersz
    print(f"Liczba kandydatów: {n}")

##########################################################

print("Przykład 2 - jeden wiersz, kilka kolumn:")

sql2 = """
    Select min(wiek), max(wiek)
    From kandydat
"""

for wiersz in db.execute(sql2):
    wiek_min, wiek_max = wiersz
    print(f"Przedział wieku: {wiek_min}-{wiek_max}")

##########################################################

print("Przykład 3 - wiele wierszy, wiele kolumn:")

sql3 = """
    Select imie, nazwisko, rok_ur
    From kandydat
    Where
        wiek > 40
        And wiek < 45
        And imie in ('BORYS', 'ANGELIKA')
"""

for wiersz in db.execute(sql3):
    imie, nazwisko, rok = wiersz
    print(f"* {nazwisko} {imie} ({rok})")