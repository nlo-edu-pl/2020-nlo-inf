uczniowie = [
  { "imie" : "Katarzyna", "nazwisko" : "U.", "oceny" : "4 4 4 4 4 5 5 3 3 4 3 4" },
  { "imie" : "Małgorzata", "nazwisko" : "K.", "oceny" : "3 3 4 4 2 2 3 4 3 3 3 2" },
  { "imie" : "Wiktor", "nazwisko" : "J.", "oceny" : "4 3 4 3 3 4 4 3 3 3 3 3" },
  { "imie" : "Wiktor", "nazwisko" : "N.", "oceny" : "4 3 2 3 5 2 5 5 3 3 5 5" },
  { "imie" : "Gabrysia", "nazwisko" : "J.", "oceny" : "3 4 4 3 4 3 3 4 4 3 4 4" },
  { "imie" : "Katarzyna", "nazwisko" : "O.", "oceny" : "2 5 2 2 3 4 5 4 2 4 4 2" },
  { "imie" : "Jarema", "nazwisko" : "Z.", "oceny" : "4 3 4 1 2 3 4 5 5 2 2 4" },
  { "imie" : "Marek", "nazwisko" : "D.", "oceny" : "5 5 2 5 4 3 4 5 3 4 3 4" },
  { "imie" : "Marek", "nazwisko" : "D.", "oceny" : "5 5 4 3 4 4 4 3 3 3 5 3" },
  { "imie" : "Marek", "nazwisko" : "X.", "oceny" : "2 2 3 2 2 2 3 3 4 3 3 2" },
  { "imie" : "Marek", "nazwisko" : "B.", "oceny" : "6 4 5 4 5 5 4 6 4 3 5 4" },
  { "imie" : "Marek", "nazwisko" : "V.", "oceny" : "4 5 3 3 2 4 4 5 3 6 2 3" }
]

def wyswietl_ucznia( uczen ):
    print(f"{uczen['imie']} {uczen['nazwisko']} oceny: {uczen['oceny']}")

# napisac kod funkcji liczącej średnią ocen ucznia:

def policz_srednia( uczen ):
    pass



for u in uczniowie:
    wyswietl_ucznia( u )

