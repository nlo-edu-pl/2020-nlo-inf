# print("\n".join( [" "*((17-n)//2) + "#"*n for n in list(range(1,16,2))+list(range(9,18,2))+5*[3]]))

#print("\n".join( [" "*((17-n)//2) + "#"*n for n in [1,3,5,7,9,11,13,15,9,11,13,15,17]+5*[3]]))

# print("\n".join([" "*(9-n)+"#"*(2*n+1) for n in list(range(8))+list(range(4,9))+5*[1]]))

print("\n".join([" "*(9-n)+"#"*(2*n+1) for x in [range(8), range(4,9), 5*[1]] for n in x]))
