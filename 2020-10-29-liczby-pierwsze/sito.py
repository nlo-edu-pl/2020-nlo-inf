zakres = 1000000

liczby = ( zakres + 1 ) * [ True ]

for biezaca in range( 2, zakres + 1):
    if liczby[ biezaca ] == True:
        # ta liczba jest pierwsza:
        # - zostawiamy ja
        # - wykreslamy wszystkie wielokrotnosci
        #   zaczynajac od kwadratu biezacej liczby
        for i in range( biezaca, zakres ):
            if biezaca * i > zakres:
                break
            liczby[ biezaca * i ] = False
    if biezaca ** 2 > zakres:
        break

for n in range( 2, zakres + 1 ):
    if liczby[n] == True:
        print( n )
