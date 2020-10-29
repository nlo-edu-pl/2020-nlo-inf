liczba = 5 ** 4 * 2 ** 8 * 11 * 17

dz = 2

while liczba > 1:
    while liczba % dz == 0:
        print ( f"{liczba}   {dz}")
        liczba = liczba // dz
    dz = dz + 1
