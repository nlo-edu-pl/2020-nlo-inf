# Zaimplementować funkcję przeliczającą temperatury obsłgującą 4 skale:
# - Celsjusza
# - Kelvina
# - Fahrenheita
# - Rankine'a

def przelicz_C_na_K( tC ):
    return tC + 273.15

def przelicz_K_na_C( tK ):
    return tK - 273.15

def przelicz_C_na_F( tC ):
    return 1.8 * tC + 32

def przelicz_F_na_C( tF ):
    return ( tF - 32 ) / 1.8

def przelicz_F_na_K( tF ):
    return przelicz_C_na_K( przelicz_F_na_C( tF ) )

def przelicz_R_na_K( tR ):
    return tR / 1.8

def przelicz_K_na_F( tK ):
    return przelicz_C_na_F( przelicz_K_na_C( tK ))

def przelicz_K_na_R( tK ):
    return tK * 1.8

def przelicz_temp( t, a, b ):
    if a == b:
        return t

    if a == "K":
        tK = t
    elif a == "C":
        tK = przelicz_C_na_K( t )
    elif a == "F":
        tK = przelicz_F_na_K( t )
    elif a == "R":
        tK = przelicz_R_na_K( t )
    
    # w tym momencie mamy temp w Kelvinach w zmiennej tK

    if b == "K":
        tW = tK
    elif b == "C":
        tW = przelicz_K_na_C( tK )
    elif b == "F":
        tW = przelicz_K_na_F( tK )
    elif b == "R":
        tW = przelicz_K_na_R( tk )

    return tW

x = przelicz_temp( 0, "C", "F" )
print( f"{x} = 32")
# powinno wyjsc 32

x = przelicz_temp( 100, "C", "F" )
print(f"{x} = 212")
# powinno wyjsc 212

x = przelicz_temp( 0, "K", "C" )
print(f"{x} = -273.15")
# powinno wyjsc -273.15

x = przelicz_temp( 0, "C", "C" )
print(f"{x} = 0")
