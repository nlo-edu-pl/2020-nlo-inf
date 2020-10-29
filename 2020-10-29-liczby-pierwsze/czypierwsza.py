def czy_pierwsza( n ):
    for i in range( 2, n ):
        #print( f"{n} / {i} = { n / i } (reszta {n % i}) ")
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True

liczba = 4083668327423
if czy_pierwsza( liczba ):
    print("Liczba jest pierwsza")
else:
    print("Liczba jest zlozona")
