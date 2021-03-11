import random
# lista liczb do zbadania:

def losowe_liczby_jasia_i_malgosi(ile_m, ile_j):
    wynik = []
    for i in range(ile_m):
        wynik.append(random.randint(1,1000)*2+1)
    for i in range(ile_j):
        wynik.append(random.randint(1,1000)*2)
    return wynik
#A = [7, 5, 9, 13, 11, 17, 21, 23, 42, 44, 80, 90, 2]

A = losowe_liczby_jasia_i_malgosi(100000, 200000)

# uwaga! to jest notacja pythona, gdzie listy indeksujemy od 0 do n-1
# w pseudokodzie należałoby napisać p=1 k=n -- zgodnie z treścią zadania
poczatek = 0
koniec = len(A) - 1

# złożoność O(log n)

#while True:
print(A)
#for _ in range(8):
while True:
    srodek = (poczatek + koniec) // 2
    print(f"Element środkowy z [{poczatek}..{koniec}]:  {srodek} wynosi: {A[srodek]}")
    if A[srodek] % 2 == 1:
#        print("nieparzysty")
        poczatek = srodek + 1
    else:
#        print("parzysty")
        koniec = srodek
    if poczatek == koniec:
        w = A[srodek]
        break

print(f"Pierwsza liczba parzysta to: {w}")
