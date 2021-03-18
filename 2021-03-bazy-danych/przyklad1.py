import sqlite3

db = sqlite3.connect('2021-03-bazy-danych/firma.db')

x = db.execute("Select * From samochody")

for samochod in x:
    nr, tab, marka, model, rocznik, kolor = samochod
    print(f"{tab}: {marka} {model} ({rocznik})")
