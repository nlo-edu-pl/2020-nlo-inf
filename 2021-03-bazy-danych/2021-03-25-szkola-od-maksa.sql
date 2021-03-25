BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "uczniowie" (
	"imie"	TEXT,
	"nazwisko"	TEXT,
	"wiek"	INTEGER,
	"klasa"	TEXT
);
CREATE TABLE IF NOT EXISTS "nauczyciele" (
	"imie"	TEXT,
	"nazwisko"	TEXT,
	"wiek"	INTEGER,
	"staz"	INTEGER
);
INSERT INTO "uczniowie" VALUES ('Adam','Pączkowski',16,'A');
INSERT INTO "uczniowie" VALUES ('Genogefa','Widelec',15,'A');
INSERT INTO "uczniowie" VALUES ('Marcel','Pająk',16,'B');
INSERT INTO "uczniowie" VALUES ('Patryk','Fąk',15,'A');
INSERT INTO "uczniowie" VALUES ('Marcin','Kowalski',15,'A');
INSERT INTO "uczniowie" VALUES ('Piotr','Kowalski',16,'A');
INSERT INTO "uczniowie" VALUES ('Marcin','Grudzień',15,'A');
INSERT INTO "uczniowie" VALUES ('Stanisław','Piątek',17,'A');
INSERT INTO "uczniowie" VALUES ('Marcin','Ząb',15,'A');
INSERT INTO "uczniowie" VALUES ('Filip','Stępień',17,'B');
INSERT INTO "uczniowie" VALUES ('Miłosz','Ziółkowicz',16,'B');
INSERT INTO "uczniowie" VALUES ('Gabrysia','Bąk',15,'B');
INSERT INTO "uczniowie" VALUES ('Stanisław','Zipkowski',14,'B');
INSERT INTO "uczniowie" VALUES ('Mariusz','Przyczepny',16,'B');
INSERT INTO "uczniowie" VALUES ('Zuzia','Stępień',15,'B');
INSERT INTO "uczniowie" VALUES ('Agnieszka','Rożek',16,'B');
INSERT INTO "uczniowie" VALUES ('Krzysztof','Zalewski',16,'B');
INSERT INTO "uczniowie" VALUES ('Bartosz','Wał',15,'B');
INSERT INTO "uczniowie" VALUES ('Michał','Baran',15,'A');
INSERT INTO "uczniowie" VALUES ('Aleksandra','Zdrukowiak',15,'C');
INSERT INTO "uczniowie" VALUES ('Martyna','Zing',15,'C');
INSERT INTO "uczniowie" VALUES ('Kacper','Kasprowiak',16,'C');
INSERT INTO "uczniowie" VALUES ('Mirosław','Zakręt',15,'C');
INSERT INTO "uczniowie" VALUES ('Mariusz','Szybki',16,'C');
INSERT INTO "uczniowie" VALUES ('Zuzia','Śledź',15,'C');
INSERT INTO "uczniowie" VALUES ('Agnieszka','Lampa',16,'C');
INSERT INTO "uczniowie" VALUES ('Michał','Płaszcz',16,'C');
INSERT INTO "uczniowie" VALUES ('Mateusz','Jakubowski',15,'C');
INSERT INTO "uczniowie" VALUES ('Paweł','Kali',15,'C');
INSERT INTO "uczniowie" VALUES ('Filip','Krąg',14,'C');
INSERT INTO "nauczyciele" VALUES ('Jakub','Markiewicz',52,20);
INSERT INTO "nauczyciele" VALUES ('Jakub','Stańczyk',30,2);
INSERT INTO "nauczyciele" VALUES ('Marek','Słoik',40,5);
INSERT INTO "nauczyciele" VALUES ('Barbara','Markiewicz',65,30);
INSERT INTO "nauczyciele" VALUES ('Mariusz','Sagowski',32,3);
INSERT INTO "nauczyciele" VALUES ('Zbigniew','Szczupacki',29,1);
INSERT INTO "nauczyciele" VALUES ('Filip','Stożkowski',54,17);
INSERT INTO "nauczyciele" VALUES ('Mateusz','Jakubowski',56,20);
INSERT INTO "nauczyciele" VALUES ('Michał','Wacławski',57,19);
INSERT INTO "nauczyciele" VALUES ('Maksymilain','Markowski',60,32);
INSERT INTO "nauczyciele" VALUES ('Tymoteusz','Raczkowski',28,1);
INSERT INTO "nauczyciele" VALUES ('Stanisław','Pała',32,2);
INSERT INTO "nauczyciele" VALUES ('Anna','Szczepańska',42,7);
INSERT INTO "nauczyciele" VALUES ('Weronika','Walec',41,9);
INSERT INTO "nauczyciele" VALUES ('Ilona','Słomka',48,12);
INSERT INTO "nauczyciele" VALUES ('Barbara','Most',40,8);
COMMIT;
