class Kwadrat:
    def __init__(self, bok):
        self._bok = bok
    def obwod(self):
        return self._bok * 4
    def pole(self):
        return self._bok**2

kw = Kwadrat(4.5)
p = kw.pole()
obw = kw.obwod()

print(f"Kwadrat ma pole={p} i obwód={obw}")