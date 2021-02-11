# Tabela ASCII: https://en.wikipedia.org/wiki/ASCII


napis = "Cbudib Zfkrgcd GR VCDIB"
wynik = ""

for x in napis:
    if x.isalpha():
        kodlitery = ord(x)
        if kodlitery >= 65 and kodlitery <= 90:
            numerlitery = kodlitery - 65
            numerliterysz = numerlitery - 3
            if numerliterysz < 0:
                numerliterysz = numerliterysz + 26
            kodliterysz = numerliterysz + 65
        else:
            numerlitery = kodlitery - 97
            numerliterysz = numerlitery - 3
            if numerliterysz < 0:
                numerliterysz = numerliterysz + 26
            kodliterysz = numerliterysz + 97
        literasz = chr(kodliterysz)
        #print(x, kodlitery, numerlitery, numerliterysz, kodliterysz, literasz)
        wynik = wynik + literasz
    else:
        wynik = wynik + x

print(wynik)
