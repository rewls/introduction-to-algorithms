# Ch9 Medians and Order Statistics

## Contents

II Sorting and Order Statistics

- Ch9 Medians and Order Statistics

    - 9.1 Minimum and maximum

    - 9.2 Selection in expected linear time

    - 9.3 Selection in worst-case linear time

## 9.1 Minimum and maximum

### Exercises

#### 1

- Based on `MINIMUM` procedure, to find the second smallest of $n$ elements, first we keep track of the values that is assigned to `min` which takes $n - 1$ comparisons.

- And then we find the smallest value in them, which takes $\lceil \lg n\rceil - 1$.

- Summing both, the number of worst-case comparisons is $\lceil \lg n\rceil - 2$.

- We can also find the second smallest in $n - 1$ as follow.

- `MINIMUM2(A)`:

```c
min = A[1]
min2 = A[1]
for i = 2 to A.length
    if min > A[i]
        min2 = min
        min = A[i]
    else if min2 > A[i]
        min2 = A[i]
return min2
```

## 9.2 Selection in expected linear time

### Exercises

#### 1

- Making a recursive call to a $0$-length array is only when either in line 8 $p > q - 1$ or in line 9 $q+1 > r$.

- Since $p \le q \le r$, when $p = q$ or $q = r$ it is possible.

- But in that case lines 1-6 terminates the algorithm returning a proper value.

- Thus `RANDOMIZED-SELECT` naver makes a recursive call to a $0$-length array.

#### 2

- $X_k$ is not affected by $T(\text{max}(k-1, n-k))$.

#### 3

- `RANDOMIZED-SELECT(A, p, r, i)

```c
while true
    if p == r
        return A[p]
    q = RANDOMIZED-PARTITION(A, p, r)
    k = q - p + 1
    if i == k
        return A[q]
    elseif i < k
        r = q - 1
    else
        p = q + 1
        i = i - k
```

#### 4

- When every time the algorithm partitions it selects the largest value in given array as the pivot, which results in a worst-case performance.

## 9.3 Selection in worst-case linear time

### Exercises

#### 1

- If the input elements are divided into groups of $7$, the number of elements greater (or less) than the partitioning element $x$ is at least as follow.

$$
4\left(\left\lceil{1 \over 2}\left\lceil{n \over 7}\right\rceil\right\rceil - 2\right) \ge {2n \over 7} - 8
$$

- Thus the recurrence becomes as follow.

$$
T(n) \le T(\lceil n/7\rceil) + T(5n/7 + 8) + O(n)
$$

- We guess $T(n) \le cn$ and let $a$ the constant hidden in $O(n)$.

$$
\begin{aligned}
T(n)
&\le c\lceil n/7\rceil + c(5n/7 +  8) + an \\
&\le 6cn/7 + an + 8c \\
&= cn - cn/7 + an + 8c \\
&\le cn
\end{aligned}
$$

- where the last step holds for as follow.

$$
-cn/7 + an + 8c \le 0
$$

$$
(n/7 - 8)c \ge an
$$

- When $n \ge 56$

$$
c \ge 7a(n/(n - 56))
$$

- If we assume $n \ge 56\cdot 2$, $n/(n- 56) \le 2$ and $c \ge 14a$.

- Thus the worst-case running time of `SELECT` with each group of 7 elements is linear.

- Instead If the input elements are divided into groups of $3$, the number of elements greater (or less) than $x$ is at least as follow.

$$
2\left(\left\lceil{1 \over 2}\left\lceil{n \over 3}\right\rceil\right\rceil - 2\right) \ge {n \over 3} - 4
$$

- And the recurrence becomes as follow.

$$
T(n) \le T(\lceil n/3\rceil) + T(2n/3 + 4) + O(n)
$$

- We guess $T(n) \le cn$ and let $a$ the constant hidden in $O(n)$.

$$
\begin{aligned}
T(n)
&\le c\lceil n/3\rceil + c(2n/3 +  4) + an \\
&\le cn + an + 2c \\
&= cn + an + 2c \\
\end{aligned}
$$

- For the last exptression to be upper-bounded by $cn, it should be as follow.

$$
cn/6 + an + 2c \le 0
$$

- But since $c$ and $a$ must be the positive number, it is contradictory.

- Thus the worst-case running time of `SELECT` with each group of 3 elements is not linear.

- We can also see that $T(n)$ is nonlinear by noticing that each level of the recursion tree sums to $\Theta(n)$
