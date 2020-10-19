def odleglosc( x1, y1, x2, y2 ):
    a = ( x1 - x2 )
    b = ( y1 - y2 )
    return ( a**2 + b**2 ) ** 0.5

mieszkancy = []
sklepy = []
licznik_mieszkancow = []

with open("mieszkancy.txt","r") as f:
    for linia in f:
        x, y = linia.strip().split(" ")
        x = int(x)
        y = int(y)
        mieszkancy.append( [x,y] )

with open("sklepy.txt","r") as f:
    for linia in f:
        x, y = linia.strip().split(" ")
        x = int(x)
        y = int(y)
        sklepy.append( [x,y] )
        licznik_mieszkancow.append( 0 )

for nm, m in enumerate( mieszkancy ):
    print(f"Mieszkaniec numer {nm} {m}:")
    smin = None
    odlmin = None
    for ns, s in enumerate( sklepy ):
        odl = odleglosc( m[0], m[1], s[0], s[1] )
        if smin == None or odl < odlmin:
            smin = ns
            odlmin = odl
        #print(f"   Sklep numer {ns}: {s}: {odl}")
    print(f"Najbliższy sklep ma numer {smin} i jest w odległości {odlmin}")  
    licznik_mieszkancow[ smin ] += 1

for ns, ile in enumerate( licznik_mieszkancow ):
    print( f"Sklep #{ns} : {ile}" )
