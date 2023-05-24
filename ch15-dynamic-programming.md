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
