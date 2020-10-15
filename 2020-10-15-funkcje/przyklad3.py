def przelicz_C_na_F( tC ):
    tempF = 1.8 * tC + 32
    return tempF

temperaturyC = [ -10, -5, 0, 5, 10, 15, 20, 25 ]

for tempC in temperaturyC:
    tempF = przelicz_C_na_F( tempC )
    tempK = 222
    print(f" {tempC}°C = {tempF}°F = {tempK}°K ")
