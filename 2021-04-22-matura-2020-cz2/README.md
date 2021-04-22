# Zadania

## Zadanie 4.1

Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą dwóch nieparzystych liczb pierwszych.

Przykład:

Mamy liczbę 24.
* jest większa od 4 ✅
* jest parzysta ✅

Parzystość przy dodawaniu:
```
P + P = P
P + N = N
N + N = P
```

Problem: **czy liczba jest sumą dwóch liczb pierwszych?**

badana liczba: `24`

liczby pierwsze bez 2: `3, 5, 7, 11, 13, 17, 19, 23, 29` itd.

| badana liczba | liczba pierwsza | druga        | werdykt | różnica | uwagi |
|---------------|-----------------|--------------|---------|-------|-------|
|            24 |               3 | 24 - 3 = 21  |   ❌    |       |       |
|            24 |               5 | 24 - 5 = 19  |   ✅    | **14**|       |
|            24 |               7 | 24 - 7 = 17  |   ✅    | 10    |       |
|            24 |              11 | 24 - 11 = 13 |   ✅    |  2    |       |
|            24 |              13 | 24 - 13 = 11 |   ✅    |  2    | od tego momentu będzie się powtarzać |
|            24 |              17 | 24 - 17 = 7  |   ✅    | 10    |       |
|            24 |              19 | 24 - 19 = 5  |   ✅    | 14    |       |
|            24 |              23 | 24 - 23 = 1  |   ❌    |       |       |
|            24 |              29 | 24 - 29 = -5 |   ❌    | KONIEC |       |

Pary liczb spełniających tę własność to:
* 5 i 19
* 7 i 17
* 11 i 13
* 13 i 11
* 17 i 7
* 19 i 5

Największa różnica to pierwsza para: `5, 19`

### Algorytm wyszukiwania par liczb pierwszych sumujących się do wskazanej liczby

```python
for p in range(3, badana_liczba // 2):
    if not czy_pierwsza(p):
        continue
    q = badana_liczba - p
    if not czy_pierwsza(q):
        continue
    print(f"{p} {q}")
```

## Zadanie 4.2

Mamy jakiś napis: `aaaaavbbbxbbcdddddxxxyyyyzzzz`

Napis składa się ze spójnych fragmentów złożonego z identycznych liter:

| fragment  | długość |
|-----------|---------|
| `aaaaa`   | **5**   |
| `v`       | 1       |
| `bbb`     | 3       |
| `x`       | 1       |
| `bb`      | 2       |
| `c`       | 1       |
| `ddddd`   | 5       |
| `xxx`     | 3       |
| `yyyy`    | 4       |
| `zzzz`    | 4       |

## Zadanie 4.3

Mamy pary liczba-słowo:
- `(1, bbbb)`
- `(2, aaa)`
- `(3, aaa)`