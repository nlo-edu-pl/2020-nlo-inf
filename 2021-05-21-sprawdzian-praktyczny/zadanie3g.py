#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Jaki procent wszystkich kandydatów stanowią kandydaci noszący jedno z nazwisk: 'NOWAK', 'KOWALSKI', 'KOWALSKA', 'WÓJCIK'?")
sql = """
    Select 100.0 * (
        Select count(*)
        From kandydat
        Where nazwisko in ('NOWAK', 'KOWALSKI', 'KOWALSKA', 'WÓJCIK')
    ) / (
        Select count(*)
        From kandydat
    )
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x:.2f}%")

print("Jaki procent wszystkich kandydatów stanowią kandydaci noszący jedno z nazwisk: 'NOWAK', 'KOWALSKI', 'KOWALSKA', 'WÓJCIK'?")
sql = """
    Select 100.0 * Sum(nazwisko in ('NOWAK', 'KOWALSKI', 'KOWALSKA', 'WÓJCIK'))/Sum(1)
    From kandydat
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x:.2f}%")