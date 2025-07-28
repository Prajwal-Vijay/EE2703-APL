def subsetsum(L, S):
    for i in range(0, len(L)):
        for j in range(i, len(L)+1):
            if sum(L[i:j]) == S:
                return (i,j-1)
    return (-1,-1)

print(subsetsum([1, 2, 3], 6))