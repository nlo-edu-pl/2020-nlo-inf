# Praca domowa

Napisać program, który wczyta zawartość pliku tekstowego i wyświetli ile razy pojawiła się jaka litera z przedziału od `a` do `z` i `A` do `Z`.

## Przykład

Plik wejściowy:

```
Ala ma kota a kot ma psa.
Tra la la la la
```

Wynik:

```
A: 1
B: 0
C: 0
    ...
T: 1
    ...
Z: 0
a: 11
b: 0
c: 0
d: 0
    ...
k:  1
l:  5
m:  2
    ...itd aż do z
```

(Opcjonalnie, litery występujące 0 razy można pominąć.)

Najlepiej użyć list (`list`) lub słowników (`dict`)

Pomoc:
- https://docs.python.org/3/tutorial/datastructures.html
- https://www.w3schools.com/python/python_lists.asp
- https://www.programiz.com/python-programming/list
