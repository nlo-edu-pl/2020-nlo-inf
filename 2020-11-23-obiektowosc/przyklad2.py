class Uczen:
    def __init__(self, imie, nazwisko, oceny):
        self._imie = imie
        self._nazwisko = nazwisko
        self._oceny = oceny
        print(f"Utworzono nowego ucznia ({imie})!")
    def powitanie(self):
        print(f"Dzien dobry, nazywam sie {self._imie} {self._nazwisko} {self._oceny}")
    def policz_srednia(self):
        return sum(self._oceny)/len(self._oceny)
    def wyswietl_ucznia(self):
        srednia = self.policz_srednia()
        if srednia > 4.7:
            pasek = "czerwony pasek"
        else:
            pasek = ""
        print(f"{self._imie} {self._nazwisko} srednia: {srednia} {pasek}")
    def __repr__(self):
        return f"Uczen({repr(self._imie)}, {repr(self._nazwisko)}, {repr(self._oceny)})"
    _imie = None
    _nazwisko = None
    _oceny = None
    _adres = None

class Nauczyciel:
    def __init__(self, imie, nazwisko, uczniowie=[]):
        self._imie = imie
        self._nazwisko = nazwisko
        self._uczniowie = uczniowie
    def dodaj_ucznia(self, uczen):
        self._uczniowie.append(uczen)
    def przedstaw_sie(self):
        print(f"Nazywam sie {self._imie} {self._nazwisko}.")
        print(f"Moi uczniowie to:")
        for u in self._uczniowie:
            print(f"* {u}")
    def __repr__(self):
        return f"Nauczyciel({repr(self._imie)}, {repr(self._nazwisko)}, {repr(self._uczniowie)})"

u1 = Uczen("Marcin", "xxxx", [3,5,4,3])
n = Nauczyciel("Jan","Kowalski", [ u1 ] )
u2 = Uczen("Karol", "yyyyy", [3,3,3,3,3])
u3 = Uczen( "Ania", "Xyz", [3,4,5,6,6,6,5,6,5] )
n.dodaj_ucznia(u2)
n.dodaj_ucznia(u3)

#n.przedstaw_sie()

print(n)

#u2 = Uczen("Karol", "yyyyy", [3,3,3,3,3])
#u3 = Uczen( "Ania", "Xyz", [3,4,5,6,6,6,5,6,5] )

#for u in ( u1, u2, u3 ):
#    print(u)

