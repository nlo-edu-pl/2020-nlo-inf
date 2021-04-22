def znajdz_najdluzszy_podciag(napis):
    max_dlug = 0
    lit_max = None
    poprzednia = None
    for litera in napis:
        if litera == poprzednia:
            licznik = licznik + 1
        else:
            licznik = 1
        if licznik > max_dlug:
            max_dlug = licznik
            lit_max = litera
        # print(f"{litera} {poprzednia} {licznik}")
        poprzednia = litera
    # print(f"Najdłuższy podciąg miał długość: {max_dlug} i składał się z liter: {lit_max}")
    return max_dlug, lit_max * max_dlug

with open('pary.txt', 'r') as fin, open('wyniki4-2.txt', 'w') as fout:
    for linia in fin:
        liczba, slowo = linia.split(' ')
        dlug, litera = znajdz_najdluzszy_podciag(slowo)
        fout.write(f"{litera} {dlug}\n")
