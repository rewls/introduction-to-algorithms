def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for i in range(n+1)] for j in range(m+1)]
    c = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "←"
    return b


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "↖":
        print_lcs(b, X, i-1, j-1)
        print(X[i-1], end=' ')
    elif b[i][j] == "↑":
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)


import sys


if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} <sequence1> <sequence2>")
    exit()

X = sys.argv[1]
Y = sys.argv[2]
b = lcs_length(X, Y)
print_lcs(b, X, len(X), len(Y))
print()
