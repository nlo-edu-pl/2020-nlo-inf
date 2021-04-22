#!/usr/bin/python3

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True

def znajdz_pare_liczb(n):    
    for p in range(3, n // 2 + 1):
        if not czy_pierwsza(p):
            continue
        q = n - p
        if not czy_pierwsza(q):
            continue
        return p, q

with open('pary.txt', 'r') as fin, open('wyniki4-1.txt', 'w') as fout:
    for linia in fin:
        liczba, napis = linia.split(' ')
        liczba = int(liczba) # konwersja stringa na liczbę
        if liczba % 2 == 1:
            continue
        p, q = znajdz_pare_liczb(liczba)
        fout.write(f"{liczba} {p} {q}\n")
