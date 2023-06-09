# Ch15 Dynamic Programming

## Contents

IV Advanced Design and Analysis Techniques

- Ch15 Dynamic Programming

    - 15.1 Rod cutting

        - Recursive top-down implementation

        - Using dynamic programming for optimal rod cutting

        - Subproblem graphs

        - Recontstructing a solution

    - 15.2 Matrix-chain multiplication

        - Counting the number of parenthesizations

        - Applying dynamic programming

        - Step 1: The structure of an optimal parenthesization

        - Step 2: A recursive solution

        - Step 3: Computing the optimal costs

        - Step 4: Constructing an optimal solution

    - 15.3 Elements of dynamic programming

        - Optimal substructure

        - Overlapping subproblems

        - Reconstructing an optimal solution

        - Memoization

    - 15.4 Longest common subsequence

        - Step 1: Characterizing a longest common subsequence

        - Step 2: A recursive solution

        - Step 3: Computing lthe length of an LCS

        - Step 4: Constructing an LCS

        - Improving the code

    - 15.5 Optimal binary search trees

        - Step 1: The structure of an optimal binary search tree

        - Step 2: A recursive solution

        - Step 3: Computing the expected search cost of an optimal binary search tree

## 15.1 Rod cutting

### Exercises

#### 15.1-1

- Basis: $T(0) = 1 = 2^0$

- Inductive step: Suppose $T(k) = 2^k$ for $k$.

$$
\begin{aligned}
T(k+1)
&= 1 + \sum_{j=0}^kT(j) \\
&= 1 + \sum_{j=0}^k2^j \\
&= 1 + (2^{k+1} - 1) \\
&= 2^{k+1}
\end{aligned}
$$

- Thus, the following equation holds.

$$
T(n) = 2^n
$$

#### 15.1-2

- The following case is a counterexample for a rod of length 3. The given greedy strategy returns the cuts 2 and 6, but it is not optimal way.

|length $i$|1|2|3|
|price $p_i$|1|10|12|
|density $p_i/i$|1|5|4|

#### 15.1-3

- `BOTTOM-UP-CUT-ROD(p, c, n)`

```c
let r[0..n] be a new array
r[0] = 0
for j = 1 to n
    q = -1
    for i = 1 to j
        q = max(q, p[i] + r[j - i] - c)
    r[j] = q
return r[n]
```

#### 15.1-4

- `MEMOIZED-CUT-ROD(p, n)`:

```c
let r[0..n] and s[0..n] be a new array
for i = 0 to n
    r[i] = -1
(r, s) = MEMOIZED-CUT-ROT-AUX(p, n, r, s)
while n > 0
    print s[n]
    n = n - s[n]
```

- `MEMOIZED-CUT-ROD-AUX(p, n, r, s)`

```c
if r[n] >= 0
    return r[n] and 
if n == 0
    q = 0
else
    q = -1
    for i = 1 to n
        (m, s) = MEMOIZED-CUT-ROD-AUX(p, n - i, r, s)
        if q < p[i] + m
            q = p[i] + m
            s[n] = i
r[n] = q
return r[n] and s
```

#### 15.1-5

- `FIBONACCI(n)`:

```c
let r[0..n] be a new array
r[0] = 0
r[1] = 1
for i = 2 to n
    r[i] = r[i - 1] + r[i - 2]
return r[n]
```

```
   (0)
     ^
      \
   (1) |
    ^  |
    | /
   (2)
    ^^
    | \
   ...
   ^^  |
  / | /
 |(n-2)
 |  ^^
  \ | \
  (n-1)|
    ^  |
    | /
   (n)
```

- The number of vertices is $n$ and the number of edges is $2n - 2$.

## 15.2 Matrix-chain multiplication

### Exercises

#### 15.2-1

- $((A_1A_2)((A_3A_4)(A_5A_6)))$

#### 15.2-2

- `MATRIX-CHAIN-MULTIPLY(A, s, i, j)`

```c
let R[1..A[i].rows, 1..A[j].cols] be a new table
for k = 1 to R.rows
    for l = 1 to R.cols
        R[k, l] = 0
if i == j
    return A[i]
B = MATRIX-CHAIN-MULTIPLY(A, s, i, s[i, j])
C = MATRIX-CHAIN-MULTIPLY(A, s, s[i, j] + 1, j)
for k = 1 to R.rows
    for l = 1 to R.cols
        for m = 1 to B.cols
            R[k, l] += B[k, m] * C[m, l]
return R
```

#### 15.2-3

- We guess $P(n) \ge c2^n$.

$$
\begin{aligned}
P(n)
&\ge \sum_{k=1}^{n-1}P(k)P(n-k) \\
&\ge c^2\sum_{k=1}^{n-1}2^k2^{n-k} \\
&\ge c^2\sum_{k=1}^{n-1}2^n \\
&\ge c^2(n-1)2^n \\
&\ge c2^n
\end{aligned}
$$

- where the last step holds as long as $c \ge 1$ and $n \ge 1$.

#### 15.2-4

- If $i = j$, the vertex $v_{i, j}$ has only input edges.

- If $i < j$, there are $(v_{i, j}, v_{i, k})$ and $(v_{i, j}, v_{k+1, j})$ edges for $i \le k < j$

- The number of vertices is 

$$
\begin{aligned}
\sum_{i=1}^ni = {n(n+1) \over 1}
\end{aligned}
$$

- The number of edges is 

$$
\begin{aligned}
\sum_{i=1}^{n-1}\sum_{j=i+1}^n2(j-i)
&= \sum_{i=1}^{n-1}\sum_{j=1}^{n-i}2j \\
&=\sum_{i=1}^{n-1}(n-i)(n-i+1) \\
&=\sum_{i=1}^{n-1}i(i+1) \\
&={(n-1)n(2n-1) \over 6} + {(n-1)n \over 2} \\
&={(n-1)n(n+1) \over 3} \\
&={n^3 - n \over 3}
\end{aligned}
$$

#### 15.2-5

- The total number of references for the entire table is equal to the number of edges of the subproblem graph. As seen in 15.2-4, the number of edges is $(n^3 - n)/3$

##### 15.2-6

- Basis: A full parenthesization of an $1$-element expression has trivially 0 pairs of parentheses.

- Inductive step

    - Suppose that a full parenthesizations of a $k$-element expression has $k-1$ pairs of parentheses. 

    - Adding an element to a $k$-element expression make one more operation, that is one more parenthesis. Thus the number of pairs of parentheses in $(k+1)$-element expression is $k$, because in a full parenthesizations the number of operations is the same.

## 15.3 Elements of dynamic programming

### Exercises

#### 15.3-1

- Running `RECURSIVE-MATRIX-CHAIN` is more efficient than enumerating all the ways of parenthesizing the product and computing the number of multiplications for each.

- Recursive calls of `RECURSIVE-MATRIX-CHAIN` returns the minimum number of scalar multiplications need to compute the left-chain product $A_{i..k}$ and the right-chain product $A{k+1..j}$. `RECURSIVE-MATRIX-CHAIN` saves some of the cost of enumerating all the ways of parenthesizing the product and computing the number of multiplication for each.

#### 15.3-2

```
                                                   [1..16]
                        [1..8]                                                       [9..16]
          [1..4]                      [5..8]                       [9..12]                             [13..16]
   [1..2]        [3..4]        [5..6]        [7..8]        [9..10]          [11..12]          [13..14]          [15..16]
[1..1] [2..2] [3..3] [4..4] [5..5] [6..6] [7..7] [8..8] [9..9] [10..10] [11..11] [12..12] [13..13] [14..14] [15..15] [16..16]
```

- Since there are no overlapping subproblems in `MERGE-SORT`, memoization fails to speed up the algorithms.

#### 15.3-3

- Unlike longest simple path, matrix-chain multication problem to maximize the cost  exhibit optimal substructure.

- The recursive definition for the maximum cost of parenthesizing is as follow.

$$
m[i, j] = \begin{cases}
0 & \text{if }i = j\\
\text{min}_{i\le k<j} \{m[i, k] + m[k+1, j] + p_{i-1}p_kp_j\} & \text{if }i < j
\end{cases}
$$

#### 15.3-4

$$
p = \langle p_0, p_1, p_2, p_3, p_4\rangle = \langle4, 3, 2, 1, 4 \rangle
$$

- When $k = 3$ $p_0p_kp_4$ becomes minimum.

- In $A_{1..3}$ $p_0p_kp_3$ is minimized when $k = 2$.

- Her argument makes parenthesization $(((A_1A_2)A_3)A_4)$, and the number of scalar multiplication is as follow.

$$
4\cdot3\cdot2 + 4\cdot2\cdot1 + 4\cdot1\cdot4 = 40
$$

- An optimal solution is $((A_1(A_2A_3))A_4)$, and the number of scalar multiplication is as follow.

$$
3\cdot2\cdot1 + 4\cdot3\cdot1 + 4\cdot1\cdot4 = 34
$$

- which is less than that of her method.

- Thus her greedy approach yields a suboptimal solution.

#### 15.3-5

- When the number of pieces of length $i$ is limited, previous cuts affect subsequent cuts. Thus optimal solutions to subproblems may not be incorperated an optimal solution to the original problem.

#### 15.3-6

- Suppose $c_k = 0$ for all $k = 1, 2, \dots, n$.

    - Let $s_{i..j}$ denote the best sequence of exchanges from currency $i$ to currency $j$ consisting of some of currencies numbered between $i$ and $j$.

    - We decompose $s_{i..j}$ to $s_{i..k}$ and $s_{k+1..j}$ for a currency $k$ that is in $s_{i..j}$.

    - If $s_{i..k}$ and $s_{k+1..j}$ is not optimal sequences and $s_{i..k}^\prime$ and $s_{k+1..j}^\prime$ is optimal sequences, $s_{i..k}^\prime s_{k+1..j}^\prime$ is a better solution than $s_{i..j}$, which contradicts our assumption.

- Suppose commissions $c_k$ are arbitrary values.

    - Commissions affect the subproblem

    - Since previous trades affect subsequent trades because of commisions based on the number of trades, optimal solutions to subproblems may not be incorperated an optimal solution to the original problem.

## 15.4 Longest common subsequence

### Exercises

#### 15.4-1

- 0, 0, 1, 0, 0, 1

#### 15.4-2

- `PRINT-LCS(c, X, i, j)`:

```c
if i == 0 or j == 0
    return
if c[i, j] == c[i-1, j-1] + 1
    PRINT-LCS(c, X, i-1, j-1)
    print X[i]
elif c[i, j] == c[i-1, j]
    PRINT-LCS(c, X, i-1, j)
else
    PRINT-Longest(c, X, i, j-1)
```

#### 15.4-3

- `LCS-LENGTH(X, Y, c, i, j)`:

```c
if i == 0 or j == 0
    return c[i, j] = 0
if c[i, j] >= 0
    return c[i, j]
if X[i] == Y[j]
    return c[i, j] = LCS-LENGTH(X, Y, c, i-1, j-1) + 1
return max(LCS-LENGTH(X, Y, c, i-1, j), LCS-LENGTH(X, Y, c, i, j-1))
```

- All elements of `c` should be set to -1 before running `LCS-LENGTH`.

#### 15.4-4

- `LCS-LENGTH(X, Y)` usnig $2\cdot\text{min}(m,n) + O(1)$ additional space:

```c
m = X.length
n = Y.length
let c[0..1, 0..n] be new tables
c[1, 0] = 0
for j = 0 to n
    c[0, j] = 0
for i = 1 to m
    for j = 1 to n
        if X[i] == Y[j]
            c[1, j] = c[0, j-1] + 1
        elseif c[0, j] >= c[1, j-1]
            c[1, j] = c[0, j]
        else
            c[1, j] = c[1, j-1]
    for j = 1 to n
        c[0, j] = c[1, j]
return c[0, j]
```

- `LCS-LENGTH(X, Y)` using $\text{min}(m, n) + O(1)$ additional space:

```c
m = X.length
n = Y.length
let c[0..n] be new tables
for i = 0 to n
    c[i] = 0
for i = 1 to m
    for j = 1 to n
        if X[i] == Y[j]
            if j == 1
                v = 0 + 1
            else 
                v = c[j-1] + 1
        elseif c[j] >= c[0]
            v = c[j]
        else
            v = c[0]
    c[j-1] = c[0]
    c[0] = v
return v
```

#### 15.4-5

- `LMIS-LENGTH(X)`:

```c
n = X.length
let Y[1..n] be a copy of X
sort Y in ascending order 
return LCS-LENGTH(X, Y)
```

## 15.5 Optimal binary search trees

### Exercises

#### 15.5-1

- `CONSTRUCT-OPTIMAL-BST(root)`:

```c
r = root[1, root.length - 1]
print k[r] is the root
CONSTRUCT-OPTIMAL-BST-AUX(root, 1, r - 1,r)
CONSTRUCT-OPTIMAL-BST-AUX(root, r + 1, len(root) - 1, r)
```

- `CONSTRUCT-OPTIMAL-BST-AUX(root, i, j, parent)`:

```c
if i == parent
    print d[parent-1] is the left child of k[i]
    return
if j == parent
    print d[parent] is the right child of k[i]
    return
r = root[i, j]
if j < parent
    print k[r] is the left child of k[parent]
else
    print k[r] is the right child of k[parent]
CONSTRUCT-OPTIMAL-BST-AUX(root, i, r - 1, r)
CONSTRUCT-OPTIMAL-BST-AUX(root, r + 1, j, r)
```

#### 15.5-2

```sh
$ python optimal-bst.py
Cost: 3.12
Structure:
k[5] is the root
k[2] is the left child of k[5]
k[1] is the left child of k[2]
d[0] is the left child of k[1]
d[1] is the right child of k[1]
k[3] is the right child of k[2]
d[2] is the left child of k[3]
k[4] is the right child of k[3]
d[3] is the left child of k[4]
d[4] is the right child of k[4]
k[7] is the right child of k[5]
k[6] is the left child of k[7]
d[5] is the left child of k[6]
d[6] is the right child of k[6]
d[7] is the right child of k[7]
```

#### 15.5-3

- The asymptotic running time of `OBTIMAL-BST` will remain the same $\Theta(n^3)$ because the computation of $w(i, j)$ takes $\Theta(j - i)$ and the loop for computing it is located at the same level as loop 10-14.
