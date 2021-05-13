# Tematy i przykłady zadań na sprawdzianie

## Część teoretyczne (na papierze, bez komputera, z notatkami, z prostym kalkulatorem, bez telefonu)

### Systemy liczbowe
- Przeliczanie wartości z dowolnego systemu na dziesiętny
- Przeliczanie wartości z systemu dziesiętnego na dowolny
- Wykonywanie operacji dodawania w innych systemach.

#### Przykładowe zadania

* Przeliczyć liczbę `103` (dziesiętną) na system o podstawie `9`. 
* Przeliczyć liczbę `205` (w systemie o podstawie `7`) na system dziesiętny.
* Przeliczyć liczbę `121112` (w systemie trójkowym) na system dziesiętny.
* Czy liczba `1357` jest poprawną liczbą w systemie piątkowym?
    * odp: NIE, bo w systemie piątkowym mamy tylko cyfry: `0, 1, 2, 3, 4`
* Wykonać obliczenie w systemie czwórkowym: `1302 + 2111`
```
system czwórkowy: 0 1 2 3

    1302            2*1 + 0*4 + 3*4*4 + 1*4*4*4 = 114 dec
+   2111            1*1 + 1*4 + 1*4*4 + 2*4*4*4 = 149 dec
---------
   10013            112 + 149 = 263 dec => 10013 (czwórkowy)
```

### Funkcje i pętle w pythonie
- Znajomość składni funkcji
- Umiejętność rozpisania na kartce sposobu działania funkcji
- Funkcje rekurencyjne - badanie złożoności i całkowitej liczby wywołań

#### Przykładowe zadania:
```python
# mamy dwie funkcje

def abc(a, b):
    return 3*a + 2*b

def xyz(a):
    return a - 7

# napisać co wyświetli poniższy program
                            # odpowiedzi:
print(xyz(10))              # 3
print(abc(10, 2))           # 34
print(abc(1, 1) + xyz(80))  # 78
print(abc(xyz(8), xyz(10))) # 9

for x in [10, 11, 12, 13]:  # 30 35 40 45
    print(abc(x, x-10))

for x in range(8):          # 0 5 6 11 12 17 18 23
    print(abc(x, x%2))

for x in range(8, 16):      # 1 3 4 6 7
    if x % 3 == 0:
        continue
    print(xyz(x))
```

### Liczby pierwsze
- Algorytm Sito Eratostenesa

### Szyfr Cezara
- Zaszyfrować i odszyfrować napis na kartce (przyjmując alfabet amerykański: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`)

### SQL
- Zapytania SQL

#### Przykładowe zadanie
Mamy daną tabelę `ludzie`
| imie     | nazwisko   | waga | wzrost |
|----------|------------|------|--------|
| Zygmunt  | Iksiński   | 80   | 1.76   |
| Zbigniew | Iksiński   | 81   | 1.86   |
| Zenon    | Igrekowski | 84   | 1.72   |
| Marian   | Zetowski   | 76   | 1.79   |

Podać wynik następujących zapytań:
- `select "nazwisko" from "ludzie" where "waga" < 80`  (odp: "Zetowski")
- `select count(*) from "ludzie" where "wzrost" > 1.8`  (odp: 1)
- `select sum(waga) from "ludzie" where "nazwisko" = 'Iksiński'` (odp: 161)
- `select * from "ludzie" where "imie" = 'Zenon'` (odp: "Zenon", "Igrekowski", 84, 1.72)
- `select "imie" from "ludzie" where "waga" > 80` (odp: "Zbigniew", "Zenon")
- `select 100*wzrost from "ludzie" where "waga" = 80` (odp: 176)
- **itd**

Oprócz tego, mogą pojawić się:
- `Distinct`
- `Order By`
- `Join` (co implikuje drugą tabelkę)

## Algorytmy sortowania
* Algorytmy:
    * QuickSort
    * MergeSort
    * bąbelkowe
    * przez wstawianie
    * przez zliczanie
* zagadnienia:
    * złożoność

## Część praktyczna (przy komputerze, python, sql)

### Python - zagadnienia:
- pobieranie danych od użytkownika `input()`
- wczytywanie danych z pliku `open()` a potem `.read()` lub pętla `for linia in plik:`
- zapisywanie danych do pliku `.write()`
- konwersja typów `int()`, `float()`
- porównywanie wartości: `==`, `>`, `>=`, `!=`
- bloki warunkowe: `if warunek:` oraz opcjonalnie `else:`
- pętle `for x in lista:`
- pętle `while warunek:`
- sterowanie pętlą: `break` i `continue`
- operacje na tekście:
    - podział na listę kawałków: `.split()`
    - wyciąganie fragmentów: `[4:10]`
    - łączenie: `imie + " " + nazwisko`
    - formatowanie: `f"zawodnik: {imie} {nazwisko} ({wiek})"`
- importowanie modułów: `import random`
- liczby losowe: `random.randint(1, 10)`

### Python problemy:
- Umiejętność zaimplementowania funkcji na podstawie opisu słownego, opisu matematycznego lub pseudokodu
- Umiejętność przetwarzania danych z plików wejściowych

### Python przykładowe zadania

#### zadanie

Mając dany plik wejściowy `samochody.txt` o zawartości:
```
Toyota Corolla 23000.00
Fiat Panda 34000.00
Opel Corsa 3999.99
Opel Astra 15399.00
```

wygenerować plik wynikowy `wynik1.txt` zawierający:
- sumaryczną wartość wszystkich samochodów:
```
76398.98999999999
```
- listę zawierającą tylko Ople:
```
Opel Corsa 3999.99
Opel Astra 15399.00
```
- liczbę samochodów o cenach poniżej 20000.00:
```
2
```
- listę samochodów o cenach powyżej 30000:
```
Fiat Panda 34000.00
```
- listę samochodów, których model zaczyna się na `C`:
```
Toyota Corolla 23000.00
Opel Corsa 3999.99
```
- listę cen, których model jest na 5 liter:
```
34000.00
3999.99
15399.00
```

(wzorować się na pliku [zad4-3.py](../2021-04-22-matura-2020-cz2/zad4-3.py))

### SQL - zapytania
- Wykonywanie zapytań SQL w otrzymanej bazie danych.


