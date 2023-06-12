def interval_coloring(s, f):
    n = len(s)
    a = [[s[i], -1 - i] for i in range(n)] + \
            [[-1 - i, f[i]] for i in range(n)]
    a.sort(key = lambda x: x[0] if x[0] >= 0 else x[1])
    r = [0 for i in range(n)]
    free = [i for i in range(n - 1, -1, -1)]
    use = []
    for i in range(2 * n):
        if a[i][0] >= 0:
            j = -1 - a[i][1]
            r[j] = free.pop()
            use.append(r[j])
        else:
            j = -1 - a[i][0]
            use.remove(r[j])
            free.append(r[j])
    return r
            
s = [0, 1, 2, 3, 3, 5, 5, 6, 8, 8, 12]
f = [6, 4, 14, 5, 9, 7, 9, 10, 11, 12, 16]
print(interval_coloring(s, f))
