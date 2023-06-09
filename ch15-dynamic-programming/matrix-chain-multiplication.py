def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = m[i][i] + m[i + 1][j] + p[i]*p[i + 1]*p[j + 1]
            s[i][j] = i
            for k in range(i + 1, j):
                q = m[i][k] + m[k + 1][j] + p[i]*p[k + 1]*p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return s


def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A[{i}]", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


import sys


if len(sys.argv) < 2:
    print(f"usage: python {sys.argv[0]} <dimension list>")
    exit()

p = list(map(int, sys.argv[1:]))
s = matrix_chain_order(p)
print_optimal_parens(s, 0, len(p) - 2)
print()
