def gausselim(A, B):
    # Normalize row 1
    for k in range(len(A)):
        norm = A[k][k]
        for i in range(len(A[k])): A[k][i] /= norm
        B[k] = B[k]/norm

        # Eliminate row 2 - A[1]
        for j in set(range(len(A)))-{k}:
            norm = A[j][k] / A[k][k]

            for i in range(len(A[j])): A[j][i] = A[j][i] - A[k][i] * norm
            B[j] = B[j] - B[k] * norm

    # Normalize row 2 - B[1] will now contain the solution for x2
    # norm = A[len(A)-1][len(A)-1]
    # for i in range(len(A[len(A)-1])): A[len(A)-1][i] = A[len(A)-1][i] / norm
    # B[len(A)-1] = B[len(A)-1] / norm

    # Sub back and solve for B[0] <-> x1
    # This can be seen as eliminating A[0][1]
    # norm = A[0][1] / A[0][0]
    # note that len(A) will give number of rows
    # for i in range(len(A)):
    #     A[i][1] = A[i][1] - A[i][0] * norm
    #     B[i] = B[i] - A[i][0] * norm

    return B

print(gausselim([[2, 3],[1, -1]],[6, 1/2]))