## Import danych z pliku tekstowego (`.txt`) do bazy danych LibreOffice Base

### W LibreOffice Calc
1. Otworzyć plik `jezyki.txt`
2. Upewnić się, że ustawienia importu są poprawne (separatory itp)
3. Zaznaczyć całe kolumny z danymi i skopiować do schowka (`CTRL-C`)

### W LibreOffice Base
1. Utworzyć nową bazę danych
2. Na liście tabel (dotychczas pustej) wkleić zawartość schowka (`CTRL-V`)
3. W oknie importu:
    - Wpisać nazwę tabeli (uwaga! wielkość liter ma znaczenie)
    - [x] "użyj pierwszego wiersza jako nazw kolumn"
    - [x] utwórz klucz podstawowy o nazwie: `ID`
4. W imporcie kolumn wybieramy wszystkie
5. Ustawiamy typy kolumn
    - Jeżeli kolumna zawiera dane numeryczne - ustawiamy typ `DOUBLE`
6. 
