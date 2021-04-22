# Zadania

## Zadanie 4

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
|            24 |              13 | 24 - 13 = 11 |   ✅    | od tego momentu będzie się powtarzać |
|            24 |              17 | 24 - 17 = 7  |   ✅    |       |       |
|            24 |              19 | 24 - 19 = 5  |   ✅    |       |       |
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










for p in pierwsze:
    druga_liczba = badana_liczba - p