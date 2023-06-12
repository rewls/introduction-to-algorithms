def activity_selector_value(s, f, v):
    n = len(s) - 2
    c = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    b = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n + 1):
        c[i][i] = 0
        c[i][i + 1] = 0
    c[n + 1][n + 1] = 0
    for l in range(2, n + 2):
        for i in range(n - l + 2):
            j = i + l
            c[i][j] = 0
            for k in range(i + 1, j):
                if s[k] >= f[i] and f[k] <= s[j] and \
                        c[i][j] < c[i][k] + v[k] + c[k][j]:
                    c[i][j] = c[i][k] + v[k] + c[k][j]
                    b[i][j] = k
    return c, b


def print_activity_set(c, b, i, j):
    if c[i][j] > 0:
        k = b[i][j]
        print_activity_set(c, b, i, k)
        print(f"a[{k}]", end=" ")
        print_activity_set(c, b, k, j)


s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12, 16]
f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16, 16]
v = [1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]
n = len(s) - 2
c, b = activity_selector_value(s, f, v)
print(c[0][n + 1])
print_activity_set(c, b, 0, n + 1)
print()
