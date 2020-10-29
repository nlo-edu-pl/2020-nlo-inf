def czy_pierwsza( n ):
    for i in range( 2, n ):
        #print( f"{n} / {i} = { n / i } (reszta {n % i}) ")
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True

for i in range( 2, 1000000 ):
    if czy_pierwsza( i ):
        print(i)