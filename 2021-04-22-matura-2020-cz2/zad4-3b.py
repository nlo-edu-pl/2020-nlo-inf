"""
Para (liczba1, słowo1) jest mniejsza od pary (liczba2, słowo2), gdy:
– liczba1 < liczba2,
albo
– liczba1 = liczba2 oraz słowo1 jest leksykograficznie (w porządku alfabetycznym)
mniejsze od słowo2.
"""

def porownaj_pary(p1, p2):
    liczba1, slowo1 = p1
    liczba2, slowo2 = p2
 
    if liczba1 == liczba2:
        return slowo1 < slowo2
    return liczba1 < liczba2

para_min = None

with open('pary.txt', 'r') as fin, open('wyniki4-3.txt', 'w') as fout:
    for linia in fin:
        # print(f"Linia: {linia}")
        liczba, slowo = linia.split(" ")
        slowo = slowo.strip()
        liczba = int(liczba)

        if len(slowo) != liczba:
            continue
        para = (liczba, slowo)
        
        # print(f"Najmniejsza para: {para_min}  vs  {para}")
        if para_min == None or porownaj_pary(para, para_min):
            para_min = para
    # print(f"Najmniejsza para: {para_min}")
    liczba_min, slowo_min = para_min
    fout.write(f"{liczba_min} {slowo_min}")
