napis = "ALA MA KOTA, A KOT NAZYWA SIE PUSZEK"

for x in napis:
    if x.isalpha():
        kodlitery = ord(x)
        numerlitery = kodlitery - 65
        numerliterysz = numerlitery + 3
        if numerliterysz > 25:
            numerliterysz = numerliterysz - 26
        kodliterysz = numerliterysz + 65
        literasz = chr(kodliterysz)
        #print(x, kodlitery, numerlitery, numerliterysz, kodliterysz, literasz)
        print(literasz)
    else:
        print(x)
