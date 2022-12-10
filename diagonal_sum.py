def diagSum(mat):
    summ = 0
    for i in range(len(mat)):
        summ += mat[i][i]
        if i != len(mat) - (i + 1):
            summ += mat[i][len(mat) - (i + 1)]
    return summ 
