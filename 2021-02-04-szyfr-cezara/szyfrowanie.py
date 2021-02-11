# Tabela ASCII: https://en.wikipedia.org/wiki/ASCII


napis = "Zyrafy Wchodza DO SZAFY"
wynik = ""

for x in napis:
    if x.isalpha():
        kodlitery = ord(x)
        # sprawdzamy, czy mamy mala czy wielka litere
        # sprawdzić, czy kod litery >= 65 oraz <= 90
        if kodlitery >= 65 and kodlitery <= 90:
            numerlitery = kodlitery - 65
            numerliterysz = numerlitery + 3
            if numerliterysz > 25:
                numerliterysz = numerliterysz - 26
            kodliterysz = numerliterysz + 65
        else:
            numerlitery = kodlitery - 97
            numerliterysz = numerlitery + 3
            if numerliterysz > 25:
                numerliterysz = numerliterysz - 26
            kodliterysz = numerliterysz + 97
            
        literasz = chr(kodliterysz)
        #print(x, kodlitery, numerlitery, numerliterysz, kodliterysz, literasz)
        wynik = wynik + literasz
    else:
        wynik = wynik + x

print(wynik)
