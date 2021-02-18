import szyfry

with open("2021-02-18-szyfr-cezara-cd/tekst1.txt", encoding="UTF-8") as f:
    wiadomosc = f.read()

with open("2021-02-18-szyfr-cezara-cd/tekst1-tajny.txt", "w", encoding="UTF-8") as f2:
    f2.write(szyfry.szyfr_cezara(3, wiadomosc))


