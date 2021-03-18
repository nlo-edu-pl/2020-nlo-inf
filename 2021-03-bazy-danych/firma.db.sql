BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "pracownicy" (
	"numer pracownika"	INTEGER,
	"nazwisko"	TEXT,
	"imie"	TEXT,
	"staz"	REAL,
	"pensja"	NUMERIC
);
CREATE TABLE IF NOT EXISTS "samochody" (
	"nr_s"	INTEGER,
	"tablica rejestracyjna"	TEXT UNIQUE,
	"marka"	TEXT,
	"model"	TEXT,
	"rocznik"	INTEGER,
	"kolor"	TEXT
);
INSERT INTO "pracownicy" ("numer pracownika","nazwisko","imie","staz","pensja") VALUES (736,'Smitko','Alan',10.0,2000);
INSERT INTO "pracownicy" ("numer pracownika","nazwisko","imie","staz","pensja") VALUES (7499,'Nowaczek','Kazik',15.0,3000);
INSERT INTO "pracownicy" ("numer pracownika","nazwisko","imie","staz","pensja") VALUES (7599,'Więcek','Mariusz',11.0,3500);
INSERT INTO "pracownicy" ("numer pracownika","nazwisko","imie","staz","pensja") VALUES (3000,'Nowak','Mariusz',6.0,3200);
INSERT INTO "pracownicy" ("numer pracownika","nazwisko","imie","staz","pensja") VALUES (5000,'Nowakowski','Marcin',5.0,9000);
INSERT INTO "samochody" ("nr_s","tablica rejestracyjna","marka","model","rocznik","kolor") VALUES (1,'WPI0001','Nissan','GTR',2015,'czarny');
INSERT INTO "samochody" ("nr_s","tablica rejestracyjna","marka","model","rocznik","kolor") VALUES (1,'WPI0003','Opel','Corsa',2002,'szary');
INSERT INTO "samochody" ("nr_s","tablica rejestracyjna","marka","model","rocznik","kolor") VALUES (4,'WPI99XX','Nissan','Micra',NULL,NULL);
INSERT INTO "samochody" ("nr_s","tablica rejestracyjna","marka","model","rocznik","kolor") VALUES (5,'WPI1234','Nissan','Qashqai',2019,'bialy');
INSERT INTO "samochody" ("nr_s","tablica rejestracyjna","marka","model","rocznik","kolor") VALUES (6,'WPI1236','Nissan','Qashqai',2017,'bialy');
INSERT INTO "samochody" ("nr_s","tablica rejestracyjna","marka","model","rocznik","kolor") VALUES (10,'WN12345','Fiat','Panda',2000,'niebieski');
COMMIT;
