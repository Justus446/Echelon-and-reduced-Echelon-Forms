def row_echelon_form(matrx1, matrx2):
    matrx1 = np.array(matrx1, dtype='float')
    matrx2 = np.array(matrx2, dtype='float')
    r, c = matrx1.shape

    matrx2 = np.reshape(matrx2, (r, 1))
    A = np.concatenate((matrx1, matrx2), axis=1)

    print("ok")

    def row_echelon(A):
        # if matrix A has no columns or rows,
        # it is already in REF, so we return itself
        r, c = A.shape
        if r == 0 or c == 0:
            return A

        # we search for non-zero element in the first column
        for i in range(len(A)):
            if A[i, 0] != 0:
                break
        else:
            # if all elements in the first column is zero,
            # we perform REF on matrix from second column
            B = row_echelon(A[:, 1:])
            # and then add the first zero-column back
            return np.hstack([A[:, :1], B])

        # if non-zero element happens not in the first row,
        # we switch rows
        if i > 0:
            ith_row = A[i].copy()
            A[i] = A[0]
            A[0] = ith_row

        # we divide first row by first element in it
        A[0] = A[0] / A[0, 0]
        # we subtract all subsequent rows with first row (it has 1 now as first element)
        # multiplied by the corresponding element in the first column
        A[1:] -= A[0] * A[1:, 0:1]

        # we perform REF on matrix from second row, from second column
        B = row_echelon(A[1:, 1:])

        # we add first row and first (zero) column, and return
        return np.vstack([A[:1], np.hstack([A[1:, :1], B])])

    return row_echelon(A)

#sample vectors for value A
A = np.matrix([[-1, 1, 2, -8, 16, 30],
               [4, -4, -8, 28, -60, -108],
               [1, -1, -2, 0, -12, -10],
               [4, -4, -8, 24, -60, -100]])
a = np.matrix([[1, 2], [3, 5]])


#sample vectors for value b
B = np.matrix([-89, 328, 49, 316])

b = np.matrix([1, 2])


print(row_echelon_form(a, b))
