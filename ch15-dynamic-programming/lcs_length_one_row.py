def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [0 for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j == 1:
                c[n] = c[0]
                c[0] = 0
            else:
                c[j-1] = c[0]
            if X[i-1] == Y[j-1]:
                v = c[j-1] + 1
            elif c[j] >= c[0]:
                v = c[j]
            else:
                v = c[0]
            c[0] = v
    return v


import sys


if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} <sequence1> <sequence2>")
    exit()
    
X = sys.argv[1]
Y = sys.argv[2]
print(lcs_length(X, Y))
