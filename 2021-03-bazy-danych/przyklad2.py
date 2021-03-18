import sqlite3

db = sqlite3.connect('2021-03-bazy-danych/firma.db')

x = db.execute("Insert into samochody([tablica rejestracyjna], marka) values('WX12345', 'Hyundai')")
db.commit()

