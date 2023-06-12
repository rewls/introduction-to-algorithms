def greedy_activity_selector(s, f, i):
    n = len(s)
    A = [i]
    k = i
    for m in range(i + 1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A


def interval_coloring(s, f):
    m = max(f)
    n = len(s)
    r = [-1 for _ in range(n)]
    k = 0
    color = 0
    while -1 in r[1:]:
        if -1 not in r[1:]:
            break
        if r[k] > -1:
            k += 1
            continue
        a = greedy_activity_selector(s, f, k)
        for j in a:
            s[j] = -1
            f[j] = -1
            r[j] = color
        color += 1
        k += 1
    return r

s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
print(interval_coloring(s, f))
