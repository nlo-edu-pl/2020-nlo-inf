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
    _imie = None
    _nazwisko = None
    _oceny = None
    _adres = None

u1 = Uczen("Marcin", "xxxx", [3,5,4,3])
u2 = Uczen("Karol", "yyyyy", [3,3,3,3,3])
u3 = Uczen( "Ania", "Xyz", [3,4,5,6,6,6,5,6,5] )
u1.powitanie()
u2.powitanie()
u3.powitanie()

for u in ( u1, u2, u3 ):
    u.wyswietl_ucznia()

