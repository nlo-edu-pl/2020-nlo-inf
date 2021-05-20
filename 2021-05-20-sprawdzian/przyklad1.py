#!/usr/bin/python3

import sqlite3
import urllib.request
import os

URL = "https://github.com/mateusza2/2020-nlo-inf/raw/master/2021-05-20-sprawdzian/kandydaci.db"
BAZA = "kandydaci.db"

if not os.path.exists(BAZA):
    print(f"Pobieram {URL}...")
    urllib.request.urlretrieve(URL, BAZA)

db = sqlite3.connect(BAZA)

print("Przykład 1 - jeden wiersz, jedna kolumna:")
sql = """
    Select count(*)
    From kandydat
    Where nazwisko Like 'E%'
"""
print(sql)
for wiersz in db.execute(sql):
    (n,) = wiersz
    print(f"Liczba kandydatów: {n}")
print("----------");

print("Przykład 2 - jeden wiersz, kilka kolumn:")
sql = """
    Select min(wiek), max(wiek)
    From kandydat
    Where imie = 'ALFRED'
"""
print(sql)
for wiersz in db.execute(sql):
    wiek_min, wiek_max = wiersz
    print(f"Przedział wieku: {wiek_min}-{wiek_max}")
print("----------");

print("Przykład 3 - wiele wierszy, wiele kolumn:")
sql = """
    Select imie, nazwisko, rok_ur
    From kandydat
    Where
        wiek > 40
        And wiek < 45
        And imie in ('BORYS', 'ANGELIKA')
    Order By nazwisko
"""
print(sql)
for wiersz in db.execute(sql):
    imie, nazwisko, rok = wiersz
    print(f"* {nazwisko} {imie} ({rok})")
print(f"----------");

