def sym(a, b):
    if a != 0:
        sym(a-1, b+1)
        print(a*b, end=" ")
        sym(a-1, b+1)

sym(3,1)
print()