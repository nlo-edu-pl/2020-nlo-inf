imie = "Mateusz"
nazwisko = "Adamowski"

x = imie, nazwisko

i, n = x

a = 100
b = 900

c,d = a,b

print(f"imie: {i}")
print(f"nazw: {n}")
print(f"c={c} d={d}")


def mniejsza_i_wieksza(n):
    mnie = n - 1
    wie = n + 1
    return mnie, wie

def mniejsza_i_wieksza2(n):
    return n-1, n+1

x,y = mniejsza_i_wieksza2(700)
xxx = mniejsza_i_wieksza(0)

print(f"x={x} y={y}")
print(xxx)


i,j = mniejsza_i_wieksza(100)

# jak zamienic miejscami wartosci i oraz j?

i,j = j,i


