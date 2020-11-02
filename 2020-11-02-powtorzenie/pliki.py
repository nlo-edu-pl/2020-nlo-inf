liczby = [ 2,3,5,7,11,13,17 ]

f = open("wynik.txt","w")

for liczba in liczby:
    f.write( f"Tralalalalala {liczba} hihihihi\n" )

f.close()

f = open("tabliczka-mnozenia.txt","w")

for a in range(1,16):
    for b in range(1,16):
        f.write( f"{a*b:4} ")
    f.write("\n")    