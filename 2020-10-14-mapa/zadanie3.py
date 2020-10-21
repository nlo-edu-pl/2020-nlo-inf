import random


def odleglosc( x1, y1, x2, y2 ):
    a = ( x1 - x2 )
    b = ( y1 - y2 )
    return ( a**2 + b**2 ) ** 0.5

W = 800
H = 800

mieszkancy = []
sklepy = []
kolorysklepow = []

piksele = W * H * [ None ]

with open("mieszkancy.txt","r") as f:
    for linia in f:
        x, y = linia.strip().split(" ")
        x = int(x)
        y = int(y)
        mieszkancy.append( [x,y] )
        numerpiksela = y * W + x
        piksele[ numerpiksela ] = "M"

with open("sklepy.txt","r") as f:
    for linia in f:
        x, y = linia.strip().split(" ")
        x = int(x)
        y = int(y)
        sklepy.append( [x,y] )
        kolorysklepow.append( ( random.randint( 0, 255 ), random.randint( 0, 255 ), random.randint( 0, 255 ) ) )
        numerpiksela = y * W + x
        piksele[ numerpiksela ] = "S"

with open("mapa.ppm", "w") as f:
    f.write("P3\n")
    f.write(f"{W} {H} 255\n")
    for y in range( H ):
        for x in range( W ):
            numerpiksela = y * W + x
            if piksele[ numerpiksela ] == "S":
                r,g,b = ( 30, 200, 30 )
            elif piksele[ numerpiksela ] == "M":
                r,g,b = ( 212, 30, 60 )
            else:
                # znalezc najblizszy sklep w tym punkcie
                # sprawdzic jego kolor i pokolorowac pixel na ten kolor
                r,g,b = ( 255, 255, 255 )
            f.write( f"{r} {g} {b}\n" )
