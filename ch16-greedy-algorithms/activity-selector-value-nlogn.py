def activity_selector_value(s, f, v):
    n = len(s)
    c = v.copy()
    c.append(0)
    b = [[] for _ in range(n)]
    c[0] = v[0]
    b[0] = [True, -1]
    for i in range(1, n):
        start = 0
        end = i - 1
        while start <= end:
            mid = (start + end) // 2
            if f[mid] == s[i]:
                break
            elif f[mid] < s[i]:
                start = mid + 1
            else:
                end = mid - 1
        j = mid if start <= end else end
        if v[i] + c[j] > c[i - 1]:
            c[i] = v[i] + c[j]
            b[i] = [True, j]
        else:
            c[i] = c[i - 1]
            b[i] = [False, i - 1]
    return c, b
            

def print_activity_set(b, i):
    if b[i][0] == True and b[i][1] < 0:
        print(f"a[{i + 1}]", end=" ")
        return
    if b[i][0] == True:
        print_activity_set(b, b[i][1])
        print(f"a[{i + 1}]", end=" ")
    else:
        print_activity_set(b, b[i][1])


s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
v = [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1]
n = len(s)
c, b = activity_selector_value(s, f, v)
print(c[n - 1])
print_activity_set(b, len(b) - 1)
print()
