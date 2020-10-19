def odleglosc( x1, y1, x2, y2 ):
    a = ( x1 - x2 )
    b = ( y1 - y2 )
    return ( a**2 + b**2 ) ** 0.5

mieszkancy = []
sklepy = []

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

for nm, m in enumerate( mieszkancy ):
    print(f"Mieszkaniec numer {nm} {m}:")
    smin = None
    odlmin = None
    ile_blisko = 0
    for ns, s in enumerate( sklepy ):
        odl = odleglosc( m[0], m[1], s[0], s[1] )
        if odl < 200:
            ile_blisko += 1
    print(f"Sklepow w promieniu 200: {ile_blisko}")
