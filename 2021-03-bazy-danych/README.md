# SQL

## DB Browser for SQLite:

* https://sqlitebrowser.org/

## Podstawy SQL

### Zapytania:

Wyświetla wszystkich pracowników:
```sql
SELECT * FROM pracownicy;
```


Wyświetla wszystkich pracowników z pensją niższą niż 3300.

```sql
SELECT * FROM pracownicy WHERE pensja < 3300;
```

Wyszukiwanie po imieniu:

```sql
SELECT * FROM pracownicy WHERE imie = 'Mariusz'
```

Jeżeli kolumna ma nazwę ze spacją lub nazwę będącą słowem kluczowym, nazwą funkcji itp, zapisujemy ją w cudzysłowie:

```sql
SELECT * FROM pracownicy WHERE "numer pracownika" > 1000
```

Lub w kwadratowych nawiasach:

```sql
SELECT * FROM pracownicy WHERE [numer pracownika] > 1000
```

Uwaga! W innych dialektach SQL będzie używana inna składnia, np. w `MySQL` używa się odwrotnych apostrofów:

```sql
SELECT * FROM pracownicy WHERE `numer pracownika` > 1000
```

Wybieranie konkretnych kolumn (np. `imie` i `nazwisko`):

```sql
Select imie, nazwisko
From pracownicy
Where staz > 5
```

Wyliczanie wyrażeń: (np. dwunastokrotność pensji)

```sql
Select imie, nazwisko, pensja * 12
From pracownicy
Where staz > 5
```

Nadawanie nazw wyliczonym kolumnom:

```sql
Select
    imie,
    nazwisko,
    pensja * 12 as "pensja roczna"
From pracownicy
Where staz > 5
```

#### Zliczanie wierszy

Sprawdzenie ile jest wierszy w tabelce:

```sql
Select Count(*) From uczniowie;
```

Sprawdzenie ile wierszy spełnia dany warunek (np. *imie* to `Marcin`):

```sql
Select count(*) from uczniowie where imie = 'Marcin';
```

#### Grupowanie wierszy

Liczenie uczniów wg klas:
```
select klasa, count(*) as "liczba uczniów"
from uczniowie
group by klasa
```

|klasa     |liczba uczniów|
|----------|--------------|
|A         | 9            |
|B         | 10           |
|C         | 11           |

Liczenie uczniów spełniających jakiś warunek, wg klas:

```sql
select
	klasa,
	count(*) as "ile uczniów"
from uczniowie
where imie like 'M%'
group by klasa
```
|klasa     |liczba uczniów|
|----------|--------------|
|A         | 4            |
|B         | 3            |
|C         | 5            |

Aby przefiltrować wiersze wynikowe:

```sql
select
	imie,
	count(*)
from uczniowie
group by imie
having count(*) > 2
```

|imie      |count(*)      |
|----------|--------------|
|Marcin    | 3            |


Wyliczanie statystyk wieku wg klas:
```sql
select
	klasa,
	 min(wiek), max(wiek), avg(wiek)
from uczniowie
group by klasa
```
|klasa|min(wiek)|max(wiek)|avg(wiek)|
|-----|---------|---------|---------|
| A   |15       |17       |15.4444  |
| B   |14       |17       |15.6     |
| C   |14       |16       |15.2727  |


**Uwaga, błędne zapytanie**

```sql
select
	klasa,
	imie,
	min(wiek), max(wiek), avg(wiek)
from uczniowie
group by klasa
```
|klasa|imie     |min(wiek)|max(wiek)|avg(wiek)|
|-----|---------|---------|---------|---------|
| A   |Stanisław|15       |17       |15.4444  |
| B   |Filip    |14       |17       |15.6     |
| C   |Kacper   |14       |16       |15.2727  |

**Imiona w powyższym zbiorze wynikowym nie mają żadnego sensu.**

Inne bazy danych (np. Postgresql) mogą w ogóle uznać takie zapytanie za błędne.

Pobranie wszystkich imion jako jeden napis:

```sql
select
	klasa,
	group_concat(imie, ', ') as imiona,
	min(wiek), max(wiek), avg(wiek)
from uczniowie
group by klasa
```
Uwaga:
- nie mamy wpływu na kolejność imion
- funkcja `group_concat()` jest specyficzna dla niektórych dialektów SQL, w Postgresie będzie to `string_agg()`

#### Łączenie tabel

Najprostszy *iloczyn kartezjański*
```sql
select nazwa, imie, nazwisko
from nauczyciele Join klasy
```

Iloczyn kartezjański + filtrowanie wierszy:
```sql
select nazwa, imie, nazwisko
from nauczyciele Join klasy
Where nauczyciele.id = klasy.wychowawca;
```

`Left Join` - dopasowanie do **wszystkich** wierszy z lewej tabelki. (tutaj: `klasy`)
Jeżeli do danego wiersza nie pasuje żaden inny - wyświetla się `NULL`
```sql
select nazwa, imie, nazwisko
from klasy Left Join nauczyciele
On ( nauczyciele.id = klasy.wychowawca );
```

Inne bazy danych mają też `Right Join`, który działa dosłownie symetrycznie do `Left`. W przypadku `SQLite` funkcjonalność `Right Join` uzyskujemy poprzez zamianę miejscami tabelek.

Join trzech tabelek:
```sql
Select
	uczniowie.imie || ' ' || uczniowie.nazwisko As "imie i nazwisko",
	nazwa As klasa,
	nauczyciele.imie || ' ' || nauczyciele.nazwisko As "wychowawca"
From uczniowie
Join klasy On uczniowie.id_klasy = klasy.id
Join nauczyciele On klasy.id_wychowawcy = nauczyciele.id
```
(Przy okazji łączenie tekstów - Uwaga - w różnych silnikach bazd danych będzie to inna składnia.) https://www.oreilly.com/library/view/sql-in-a/9780596155322/re92.html


### Modyfikowanie danych

#### Dodawanie wierszy

```sql
Insert Into pracownicy Values(7777, 'Jan', 'Kowalski', 1.0, 2500 )
```

Lista wartości w `Values()` musi się zgadzać z kolumnami danej tabelki!

#### Kasowanie wierszy

```sql
Delete From pracownicy Where imie = 'Mariusz'
```

Uwaga, poniższe polecenie skasuje **wszystkie** wiersze z tabelki (brak `WHERE`):
```
Delete From pracownicy
```

#### Aktualizacja wierszy

```sql
Update pracownicy
Set pensja = 10000
Where nazwisko = 'Nowak'
```
(Ustawi pensję 10000 wszystkim pracownikom o nazwisku Nowak)

Uwaga, podobnie jak `Delete`, brak `Where` powoduje, że polecenie działa dla **wszystkich** wierszy:
```sql
Update pracownicy
Set pensja = 1000
```

Update może zmienić więcej niż jedną kolumnę:

```sql
Update pracownicy
Set
	imie = 'Kazik',
	nazwisko = 'Nowaczek'
Where "numer pracownika" = 7499
```

Update może wyliczyć wartość względem wartości bieżącej:

```sql
Update pracownicy
Set pensja = pensja * 1.2
Where staz > 10
```
## Tworzenie tabel
```sql
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
```sql
drop table samochody;
```
