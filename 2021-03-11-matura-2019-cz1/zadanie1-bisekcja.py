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

A = losowe_liczby_jasia_i_malgosi(1000000,7)

#print(A)
for liczba in A:
    if liczba % 2 == 0:
        w = liczba
        break

print(w)

