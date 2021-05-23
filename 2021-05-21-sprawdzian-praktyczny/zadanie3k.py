#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Jaki procent kandydatów to mężczyźni a jaki kobiety?")
sql = """
    Select
        100.0 * (Select Count(*) From kandydat Where plec = 'M')
        / Count(*),
        100.0 * (Select Count(*) From kandydat Where plec = 'K')
        / Count(*)
    From kandydat
"""
print(sql)
for wiersz in db.execute(sql):
    (m, k) = wiersz
    print(f"M:{m:.1f}%, K:{k:.1f}%")

print("Jaki procent kandydatów to mężczyźni a jaki kobiety?")
sql = """
    Select
        100.0 * Sum(plec = 'M') / Count(*),
        100.0 * Sum(plec = 'K') / Count(*)
    From kandydat
"""
print(sql)
for wiersz in db.execute(sql):
    (m, k) = wiersz
    print(f"M:{m:.1f}%, K:{k:.1f}%")