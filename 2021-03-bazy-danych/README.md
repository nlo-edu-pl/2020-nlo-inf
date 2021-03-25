# SQL

## DB Browser for SQLite:

* https://sqlitebrowser.org/

## Podstawy SQL

### Zapytania:

Wyświetla wszystkich pracowników:
```
SELECT * FROM pracownicy;
```


Wyświetla wszystkich pracowników z pensją niższą niż 3300.

```
SELECT * FROM pracownicy WHERE pensja < 3300;
```

Wyszukiwanie po imieniu:

```
SELECT * FROM pracownicy WHERE imie = 'Mariusz'
```

Jeżeli kolumna ma nazwę ze spacją lub nazwę będącą słowem kluczowym, nazwą funkcji itp, zapisujemy ją w cudzysłowie:

```
SELECT * FROM pracownicy WHERE "numer pracownika" > 1000
```

Lub w kwadratowych nawiasach:

```
SELECT * FROM pracownicy WHERE [numer pracownika] > 1000
```

Uwaga! W innych dialektach SQL będzie używana inna składnia, np. w `MySQL` używa się odwrotnych apostrofów:

```
SELECT * FROM pracownicy WHERE `numer pracownika` > 1000
```

Wybieranie konkretnych kolumn (np. `imie` i `nazwisko`):

```
Select imie, nazwisko
From pracownicy
Where staz > 5
```

Wyliczanie wyrażeń: (np. dwunastokrotność pensji)

```
Select imie, nazwisko, pensja * 12
From pracownicy
Where staz > 5
```

Nadawanie nazw wyliczonym kolumnom:

```
Select
    imie,
    nazwisko,
    pensja * 12 as "pensja roczna"
From pracownicy
Where staz > 5
```

#### Zliczanie wierszy

Sprawdzenie ile jest wierszy w tabelce:

```
Select Count(*) From uczniowie;
```

Sprawdzenie ile wierszy spełnia dany warunek (np. *imie* to `Marcin`):

```
Select count(*) from uczniowie where imie = 'Marcin';
```

### Modyfikowanie danych

#### Dodawanie wierszy

```
Insert Into pracownicy Values(7777, 'Jan', 'Kowalski', 1.0, 2500 )
```

Lista wartości w `Values()` musi się zgadzać z kolumnami danej tabelki!

#### Kasowanie wierszy

```
Delete From pracownicy Where imie = 'Mariusz'
```

Uwaga, poniższe polecenie skasuje **wszystkie** wiersze z tabelki (brak `WHERE`):
```
Delete From pracownicy
```

#### Aktualizacja wierszy

```
Update pracownicy
Set pensja = 10000
Where nazwisko = 'Nowak'
```
(Ustawi pensję 10000 wszystkim pracownikom o nazwisku Nowak)

Uwaga, podobnie jak `Delete`, brak `Where` powoduje, że polecenie działa dla **wszystkich** wierszy:
```
Update pracownicy
Set pensja = 1000
```

Update może zmienić więcej niż jedną kolumnę:

```
Update pracownicy
Set
	imie = 'Kazik',
	nazwisko = 'Nowaczek'
Where "numer pracownika" = 7499
```

Update może wyliczyć wartość względem wartości bieżącej:

```
Update pracownicy
Set pensja = pensja * 1.2
Where staz > 10
```
## Tworzenie tabel
```
CREATE TABLE "samochody" (
	"nr_s"	INTEGER,
	"tablica rejestracyjna"	TEXT UNIQUE,
	"marka"	TEXT,
	"model"	TEXT,
	"rocznik"	INTEGER,
	"kolor"	TEXT
)
```

### Kasowanie
```
drop table samochody;
```
