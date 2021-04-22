min_liczba = None
min_slowo = None

with open('pary.txt', 'r') as fin, open('wyniki4-3.txt', 'w') as fout:
    for linia in fin:
        liczba, slowo = linia.split(' ')

        # czyszczenie i konwertowanie danych
        liczba = int(liczba)    # konwersja na int()
        slowo = slowo.strip()   # usunięcie znaku końca linii (entera)

        if liczba != len(slowo):
            continue
        if liczba == min_liczba:
            if min_slowo == None or slowo < min_slowo:
                min_slowo = slowo
        if min_liczba == None or liczba < min_liczba:
            min_liczba = liczba
            min_slowo = slowo

    fout.write(f"{min_liczba} {min_slowo}")