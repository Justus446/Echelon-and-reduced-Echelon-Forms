def vector_solution(matrx1, matrx2):
    matrx1 = np.array(matrx1, dtype='float')
    matrx2 = np.array(matrx2, dtype='float')

    def isSquare(m):
        return all(len(row) == len(m) for row in m)

    # matrx2 = np.reshape(matrx2, (r, 1))
    print(isSquare(matrx1))

    def equalizer1(matrx, matri):
        r, c = matrx.shape
        z = max(r, c) - min(r, c)

        for x in range(z):
            matri = np.append(matri, 0)

        return matri

    def equalizer(matrx):
        r, c = matrx.shape

        if r == c:
            pass

        elif c > r:

            diff = c - r
            col = [0] * c

            for x in range(diff):
                matrx = np.append(matrx, [col], axis=0)

        else:

            diff = r - c
            row = [0] * r
            print(row, "yes")

            for x in range(diff):
                matrx = np.append(matrx, [row], axis=1)

        return matrx

    mat = equalizer(matrx1)
    mat1 = equalizer1(matrx1, matrx2)

    return np.linalg.lstsq(mat, mat1, rcond=None)


A = np.matrix([[-1, 1, 2, -8, 16, 30],
               [4, -4, -8, 28, -60, -108],
               [1, -1, -2, 0, -12, -10],
               [4, -4, -8, 24, -60, -100]])

b = np.matrix([-89, 328, 49, 316])

print(vector_solution(A, b))
