#!/usr/bin/python3

# autor: Mateusz Adamowski
# email: mateusz.adamowski@nlo.edu.pl

import math

r = float(input("Podaj promień podstawy: "))
H = float(input("Podaj wysokość: "))

P = math.pi * r**2
V = 1/3 * P * H
l = (H**2 + r**2)**(1/2)

kat = math.degrees(math.atan2(H, r))

print("Wynik")
print(f"Pole podstawy: {P:.2f}")
print(f"Objętość: {V:.2f}")
print(f"Tworząca: {l:.2f}")
print(f"Kąt: {kat:.1f}°")
