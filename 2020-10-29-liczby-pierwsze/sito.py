zakres = 100000

liczby = ( zakres + 1 ) * [ True ]

for biezaca in range( 2, zakres + 1):
    if liczby[ biezaca ] == True:
        # ta liczba jest pierwsza:
        # - zostawiamy ja
        # - wykreslamy wszystkie wielokrotnosci
        for i in range( 2, zakres ):
            if biezaca * i > zakres:
                break
            liczby[ biezaca * i ] = False

for n in range( 2, zakres + 1 ):
    if liczby[n] == True:
        print( n )
