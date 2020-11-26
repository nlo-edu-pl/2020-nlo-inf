napis = "Litwo, ojczyzno moja, ty jestes"

klucz = 3

for litera in napis:
    kod_litery = ord( litera )

    if ord("A") <= kod_litery <= ord("Z"):
        numer_litery = kod_litery - ord("A")
        numer_litery_zaszyfr = ( numer_litery + klucz ) % 26
        kod_litery_zaszyfr = numer_litery_zaszyfr + ord("A")
        litera_zaszyfrowana = chr(kod_litery_zaszyfr)
        print(litera, kod_litery, numer_litery, numer_litery_zaszyfr, kod_litery_zaszyfr, litera_zaszyfrowana)
    elif ord("a") <= kod_litery <= ord("z"):
        numer_litery = kod_litery - ord("a")
        numer_litery_zaszyfr = ( numer_litery + klucz ) % 26
        kod_litery_zaszyfr = numer_litery_zaszyfr + ord("a")
        litera_zaszyfrowana = chr(kod_litery_zaszyfr)
        print(litera, kod_litery, numer_litery, numer_litery_zaszyfr, kod_litery_zaszyfr, litera_zaszyfrowana)
    else:
        print(litera)
