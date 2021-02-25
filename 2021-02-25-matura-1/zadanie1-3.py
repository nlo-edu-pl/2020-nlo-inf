def czy_k_podobne(n, A, B, k):
    for i in range(0, n):
        print(f"Porównuję pozycję {i}: {A[i]} z {B[(n-k+i)%n]}")
        if A[i] != B[(n-k+i)%n]:
            return False
    return True

A = [4, 7, 8, 12, 13, 101, 2, 5]
B = [12, 13, 101, 2, 5, 4, 7, 8]

print(A)
print(B)
n=8
k=3
wynik = czy_k_podobne(n, A, B, k)
print(wynik)

def czy_podobne(n, A, B):
    for k in range(n):
        print(f"Sprawdzam k = {k}")
        if czy_k_podobne(n, A, B, k):
            return True
    return False

wynik = czy_podobne(n, A, B)
print(wynik)


