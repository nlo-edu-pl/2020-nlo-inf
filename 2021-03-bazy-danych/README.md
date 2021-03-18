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
