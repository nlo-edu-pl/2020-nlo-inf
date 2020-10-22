# Info o formacie NetPBM:
# https://en.wikipedia.org/wiki/Netpbm


width = 90
height = 60
plik = "francja.ppm"

with open( plik ,"w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")
    for y in range(height):
        for x in range(width):
            if x < width/3:
                r, g, b = ( 0, 85, 164 )
            elif x < width * 2/3:
                r, g, b = ( 255, 255, 255 )
            else:
                r, g, b = ( 239, 65, 53 ) 

            f.write(f"{r} {g} {b}\n")
