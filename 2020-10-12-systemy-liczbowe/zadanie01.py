podstawa = int(input("Podaj podstawę: "))

liczba = input(f"Podaj liczbę o podstawie {podstawa}: ")

wynik = 0

for i in range( len(liczba) ):
  wynik *= podstawa
  # wynik = wynik * podstawa
  
  #cyfra = int( liczba[i] )

  cyfra = "0123456789abcdef".find( liczba[i] )

  # wynik = wynik + cyfra 
  wynik += cyfra # zapis skrócony

  #print( f"{i}: {wynik}  {cyfra}" )

print(f"Liczba {liczba} o podstawie {podstawa}: na wartość: {wynik}")

