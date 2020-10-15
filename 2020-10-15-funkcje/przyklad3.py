def przelicz_C_na_K( tC ):
    return tC + 273.15

def przelicz_C_na_F( tC ):
    return 1.8 * tC + 32

temperaturyC = [ -10, -5, 0, 5, 10, 15, 20, 25 ]

for tempC in temperaturyC:
    tempF = przelicz_C_na_F( tempC )
    tempK = przelicz_C_na_K( tempC )
    print(f"{tempC:8.1f}°C = {tempF:8.1f}°F = {tempK:8.2f}°K ")

# dopisać brakujący kod przeliczający F na C i K

temperaturyF = [ -2, 0, 2, 8, 10, 20, 25, 30, 40, 50, 60, 70 ]
