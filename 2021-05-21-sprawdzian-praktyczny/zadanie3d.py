#!/usr/bin/python3

# Autor: Mateusz Adamowski
# Email: mateusz.adamowski@nlo.edu.pl

import sqlite3

BAZA = "kandydaci.db"

db = sqlite3.connect(BAZA)

print("Ile miał lat najstarszy kandydat w roku, w którym zakończyła się II Wojna Światowa?")
sql = """
    Select max(1945 - rok_ur)
    From kandydat
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")

print("Ile miał lat najstarszy kandydat w roku, w którym zakończyła się II Wojna Światowa?")
sql = """
    Select 1945 - min(rok_ur)
    From kandydat
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")

print("Ile miał lat najstarszy kandydat w roku, w którym zakończyła się II Wojna Światowa?")
sql = """
    Select 1945 - rok_ur
    From kandydat
    Order By rok_ur
    Limit 1
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")

print("Ile miał lat najstarszy kandydat w roku, w którym zakończyła się II Wojna Światowa?")
sql = """
    Select 1945 - (Select min(rok_ur) From kandydat)
"""
print(sql)
for wiersz in db.execute(sql):
    (x,) = wiersz
    print(f"{x}")