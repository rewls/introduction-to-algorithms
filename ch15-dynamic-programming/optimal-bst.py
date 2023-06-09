def optimal_bst(p, q, n):
    e = [[0 for j in range(n + 1)] for i in range(n + 2)]
    w = [[0 for j in range(n + 1)] for i in range(n + 2)]
    root = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for l in range(1, n + 1):
        for i in range(n - l + 2):
            j = i + l - 1
            e[i][j] = n
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root


def construct_optimal_bst(root):
    r = root[1][len(root) - 1]
    print(f"k[{r}] is the root")
    construct_optimal_bst_aux(root, 1, r - 1, r)
    construct_optimal_bst_aux(root, r + 1, len(root) - 1, r)


def construct_optimal_bst_aux(root, i, j, parent):
    if i == parent:
        print(f"d[{parent - 1}] is the left child of k[{parent}]")
        return
    if j == parent:
        print(f"d[{parent}] is the right child of k[{parent}]")
        return
    r = root[i][j]
    if j < parent:
        print(f"k[{r}] is the left child of k[{parent}]")
    else:
        print(f"k[{r}] is the right child of k[{parent}]")
    construct_optimal_bst_aux(root, i, r - 1, r)
    construct_optimal_bst_aux(root, r + 1, j, r)
    

n = 7
p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
e, root = optimal_bst(p, q, n)
print("Cost:", e[1][n])
print("Structure:")
construct_optimal_bst(root)
