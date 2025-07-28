def matrix_multiply(matrix1, matrix2):
    """
    Multiply two matrices.

    Parameters:
    matrix1 (List(List[float])) : A 2 dimensional matrix
    matrix2 (List(List[float])) : A 2 dimensional matrix

    Returns:
    solution (List(List[float])) : A 2 dimensional matrix which is the result of multiplying the above two matrices.

    The following function first validates if the inputs are valid or not, if not valid then it throws errors, and then it multiuplies the two
    matrices.
    """

    # This is to check if a matrix is Empty or not.
    if (
        len(matrix1) == 0
        or len(matrix2) == 0
        or len(matrix1[0]) == 0
        or len(matrix2[0]) == 0
    ):
        raise ValueError("Empty Matrix or Matrices")

    # This is to check the dimensionality of the matrix(it might happen that a list of numbers was inputted).
    if type(matrix1[0]) is not list or type(matrix2[0]) is not list:
        raise ValueError("Given matrix is NOT a matrix!")

    # This is to check if the dimensions of matrices, do not allow their multiplication
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Incompatible Dimensions")

    # This is to check that each element of the matrix is either a float or an integer.
    for m in matrix1:
        for item in m:
            count = 0
            if not (isinstance(item, float) or isinstance(item, int)):
                count += 1
            if count > 0:
                raise TypeError("Wrong Datatype in list")
    for m in matrix2:
        for item in m:
            count = 0
            if not (isinstance(item, float) or isinstance(item, int)):
                count += 1
            if count > 0:
                raise TypeError("Wrong Datatype in list")

    # This is to check that the length of all the rows of the matrices are uniform.
    for m in matrix1:
        if len(m) != len(matrix1[0]):
            raise ValueError("The length of rows are not the same")

    for m in matrix2:
        if len(m) != len(matrix2[0]):
            raise ValueError("The length of rows are not the same")

    # The solution matrix
    solution = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(0)
            # Performing multiplication and then adding it to the right element in the result
            for k in range(len(matrix1[0])):
                row[j] += matrix1[i][k] * matrix2[k][j]
        solution.append(row)
    # This refers to the solution matrix
    return solution
