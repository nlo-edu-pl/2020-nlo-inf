#!/usr/bin/python3

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True

badana_liczba = 2400

for p in range(3, badana_liczba // 2):
    if not czy_pierwsza(p):
        continue
    q = badana_liczba - p
    if not czy_pierwsza(q):
        continue
    print(f"{p} {q}")
