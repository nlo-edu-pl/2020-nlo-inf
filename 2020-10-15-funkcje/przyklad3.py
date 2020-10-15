def przelicz_C_na_K( tC ):
    return tC + 273.15

def przelicz_C_na_F( tC ):
    return 1.8 * tC + 32

def przelicz_F_na_C( tF ):
    return ( tF - 32 ) / 1.8

def przelicz_F_na_K( tF ):
    return przelicz_C_na_K( przelicz_F_na_C( tF ) )

temperaturyC = [ -10, -5, 0, 5, 10, 15, 20, 25 ]

for tempC in temperaturyC:
    tempF = przelicz_C_na_F( tempC )
    tempK = przelicz_C_na_K( tempC )
    print(f"{tempC:8.1f}°C = {tempF:8.1f}°F = {tempK:8.2f}°K ")

# dopisać brakujący kod przeliczający F na C i K

temperaturyF = [ -2, 0, 2, 8, 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100 ]

for tempF in temperaturyF:
    tempC = przelicz_F_na_C( tempF )
    tempK = przelicz_F_na_K( tempF )
    print(f"{tempF:8.1f}°F = {tempC:8.1f}°C = {tempK:8.2f}°K ")