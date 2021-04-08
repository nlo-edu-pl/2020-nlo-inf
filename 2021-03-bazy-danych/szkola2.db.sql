BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "nauczyciele" (
	"id"	INTEGER NOT NULL,
	"imie"	TEXT NOT NULL,
	"nazwisko"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "uczniowie" (
	"id"	INTEGER NOT NULL,
	"imie"	TEXT NOT NULL,
	"nazwisko"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"id_klasy"	INTEGER NOT NULL,
	"skreslony"	INTEGER NOT NULL DEFAULT 0,
	"plec"	TEXT NOT NULL CHECK("plec" IN ('M', 'K')),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "klasy" (
	"id"	INTEGER NOT NULL,
	"nazwa"	TEXT NOT NULL UNIQUE,
	"id_wychowawcy"	INTEGER NOT NULL,
	"profil"	TEXT NOT NULL DEFAULT 'ogólny',
	"sala"	TEXT,
	PRIMARY KEY("id")
);
INSERT INTO "nauczyciele" ("id","imie","nazwisko") VALUES (1,'Roman','Romanowski');
INSERT INTO "nauczyciele" ("id","imie","nazwisko") VALUES (2,'Zdzisław','Zdzichowski');
INSERT INTO "nauczyciele" ("id","imie","nazwisko") VALUES (3,'Karol','Karolak');
INSERT INTO "nauczyciele" ("id","imie","nazwisko") VALUES (4,'Bogdan','Bogdański');
INSERT INTO "uczniowie" ("id","imie","nazwisko","email","id_klasy","skreslony","plec") VALUES (1,'Jan','Kowalski','jan.kowalski@szkola.abc',1,0,'M');
INSERT INTO "uczniowie" ("id","imie","nazwisko","email","id_klasy","skreslony","plec") VALUES (2,'Jan','Kowalczyk','jan.kowalczyk@szkola.abc',1,0,'M');
INSERT INTO "uczniowie" ("id","imie","nazwisko","email","id_klasy","skreslony","plec") VALUES (3,'Jan','Nowak','jan.nowak@szkola.abc',1,0,'M');
INSERT INTO "uczniowie" ("id","imie","nazwisko","email","id_klasy","skreslony","plec") VALUES (4,'Antoni','Nowakowski','antoni.nowakowski@szkola.abc',2,0,'M');
INSERT INTO "uczniowie" ("id","imie","nazwisko","email","id_klasy","skreslony","plec") VALUES (5,'Michał','Michałowski','michal.michalowski@szkola.abc',2,0,'M');
INSERT INTO "uczniowie" ("id","imie","nazwisko","email","id_klasy","skreslony","plec") VALUES (6,'Piotr','Piotrowski','piotr.piotrowski@szkola.abc',2,0,'M');
INSERT INTO "klasy" ("id","nazwa","id_wychowawcy","profil","sala") VALUES (1,'1C',2,'ogólny',NULL);
INSERT INTO "klasy" ("id","nazwa","id_wychowawcy","profil","sala") VALUES (2,'3E',4,'ogólny',NULL);
INSERT INTO "klasy" ("id","nazwa","id_wychowawcy","profil","sala") VALUES (3,'4F',13,'ogólny',NULL);
COMMIT;
