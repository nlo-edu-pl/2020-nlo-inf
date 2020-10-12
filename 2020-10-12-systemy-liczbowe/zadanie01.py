liczba = "2bf541"

podstawa = 16
wynik = 0

for i in range( len(liczba) ):
  wynik *= podstawa
  # wynik = wynik * podstawa
  
  #cyfra = int( liczba[i] )

  cyfra = "0123456789abcdef".find( liczba[i] )

  # wynik = wynik + cyfra 
  wynik += cyfra # zapis skrócony

  print( f"{i}: {wynik}  {cyfra}" )

print(wynik)
