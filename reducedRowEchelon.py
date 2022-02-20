def reducedRowEchelon(M):
    if not M: return
    lead = 0

    # Find number of rows and columns
    rowCount = len(M)
    columnCount = len(M[0])

    # determine the leading 1
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        # Row operation on each  element
        M[i], M[r] = M[r], M[i]
        lv = M[r][lead]
        M[r] = [mrx / float(lv) for mrx in M[r]]

        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [iv - lv * rv for rv, iv in zip(M[r], M[i])]
        lead += 1


mtx = [
    [4, 7, 3, 8],
    [8, 3, 8, 7],
    [2, 9, 5, 3], ]
reducedRowEchelon(mtx)

for rw in mtx:
    print(', '.join((str(rv) for rv in rw)))
