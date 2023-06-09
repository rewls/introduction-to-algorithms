def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n+1)] for i in range(2)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[1][j] = c[0][j-1] + 1
            elif c[0][j] >= c[1][j-1]:
                c[1][j] = c[0][j]
            else:
                c[1][j] = c[1][j-1]
        for j in range(1, n+1):
            c[0][j] = c[1][j]
    return c[0][j]


import sys


if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} <sequence1> <sequence2>")
    exit()

X = sys.argv[1]
Y = sys.argv[2]
print(lcs_length(X, Y))
