def czy_pierwsza( n ):
    for i in range( 2, n ):
        #print( f"{n} modulo {i} = {n % i} ")
        if n % i == 0:
            return False
    return True

liczba = 127
if czy_pierwsza( liczba ):
    print("Liczba jest pierwsza")
else:
    print("Liczba jest zlozona")
