def LCS_LENGTH(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n+1)] for i in range(m+1)]
    b = [[0 for i in range(n)] for i in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "A"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "T"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "L"
    return c, b


def print_lcs(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == "A":
        print_lcs(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == "T":
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)
    return

Y = "BDCABA"
X = "ABCBDAB"
c, b = LCS_LENGTH(X, Y)
print_lcs(b, X, len(X)-1, len(Y)-1)