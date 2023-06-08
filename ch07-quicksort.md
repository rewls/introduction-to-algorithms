# Ch7 Quicksort

## Contents

II Sorting and Order Statistics

- Ch7 Quicksort

    - 7.1 Description of quickwort

        - Partitioning the array

    - 7.2 Performance of quicksort

        - Worst-case partitioning

        - Best-case partitioning

        - Balanced partitioning

        - Intuition for the average case

    - 7.3 A randomized version of quicksort

    - 7.4 Analysis of quicksort

        - 7.4.1 Worst-case analysis

        - 7.4.2 Expected running time

            - Running time and comparisons

## 7.1 Description of quicksort

### Exercises

#### 1

```
13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11
```

```
 i pj                                r
  |13 19  9  5 12  8  7  4 21  2  6|11

 i  p  j                             r
  |13|19  9  5 12  8  7  4 21  2  6|11

 i  p    j                           r
  |13 19| 9  5 12  8  7  4 21  2  6|11

   ip        j                       r
    9|19 13| 5 12  8  7  4 21  2  6|11

    p  i        j                    r
    9  5|13 19|12  8  7  4 21  2  6|11

    p  i           j                 r
    9  5|13 19 12| 8  7  4 21  2  6|11

    p     i           j              r
    9  5  8|19 12 13| 7  4 21  2  6|11

    p        i           j           r
    9  5  8  7|12 13 19| 4 21  2  6|11

    p           i           j        r
    9  5  8  7  4|13 19 12|21  2  6|11

    p           i              j     r
    9  5  8  7  4|13 19 12 21| 2  6|11

    p              i              j  r
    9  5  8  7  4  2|19 12 21 13| 6|11

    p                 i              r
    9  5  8  7  4  2  6|12 21 13 19|11

    p                 i              r
    9  5  8  7  4  2  6|11|21 13 19 12|
```

#### 2

- It returns `r`.

- `PARTITION(A, p, r)`:

```c
x = A[r]
i = p - 1
count = 0
for j = p to r - 1
    if A[j] <= x
        i = i + 1
        exchange A[i] with A[j]
    if A[j] == x
        count = count + 1
if count == p - r
    return floor((p+r)/2)
exchange A[i+1] with A[r]
return i + 1
```

#### 3

- Since there is the for loop whose body is executed $\Theta(n)$ times for any case, the running time is $\Theta(n)$

#### 4

- In `PARTION`, modify the if condition `A[j] <= x` to `A[j] >= x`.

## 7.2 Performance of quicksort

### Exercises

#### 1

- First, we guess a upper bound $T(n) \le cn^2$. Let $d$ the constant hidden in $\Theta(n)$.

$$
\begin{aligned}
T(n)
&\le c(n - 1)^2 + dn \\
&= cn^2 + (d - 2c)n + c
&\le cn^2
\end{aligned}
$$

- where the last step holds for $c >= d/2$ and $n \le c/(d - 2c)$.

- Second, we guess a lower bound $T(n) \ge cn^2$.

$$
\begin{aligned}
T(n)
&\ge c(n - 1)^2 + dn \\
&= cn^2 + (d - 2c)n + c
&\ge cn^2
\end{aligned}
$$

- where the last step holds for $c \le d/2$.

- Thus the solution is $T(n) = \Theta(n^2)$.

#### 2

- Since `PARTITION` produces one subproblem with $n-1$ elements and one with 0 elements, the running time is $\Theta(n^2)$.

#### 3

- If the array is sorted in decreasing order, the pivot is always smaller than other elements.

- Then since `PARTITION` produces one subproblem with $n-1$ elements and on with 0 elements, the running time is $\Theta(n^2)$

#### 4

- If the input array is almost-sorted, insertion sort algorithm takes nearly linear time.

- In the almost-sorted array, `PARTITION` of quicksort is likely to produce one subproblem with $n-1$ elements and one with 0 elements because the pivot is likely to be larger than other elements. Thus it is likely to take $\Theta(n^2)$ time.

- Thus, the procedure `INSERTION-SORT` would tend to beat the procedure `QUICKSORT` on this problem.

#### 5

- The node that has the shortest path from root has a cost of $n\alpha^i$. In other words, it is leftmost element.

- Since $n\alpha^i = 1$, or $i = \log_\alpha n/1$, the height of the tree is $\log_\alpha n/1 = - \lg n / \lg \alpha$

- Similarly, the node that has the longest path, that is right most elemnt has a cost of $n(1 - \alpha)^i$.

- Since $n(1 - \alpha)^i = 1$, or $i = \log_{1 - \alpha} 1/n$, the height of the tree is $- \lg n /\lg (1 - \alpha)$

#### 6

- Only when `PARTITION` produces one subproblem with less elements than $\alpha n$, a worse split than $1 - \alpha$ to \alpha$ is produced.

- That happens either when the left split has less elements than $\alpha n$ or the right split does.

- The probability of each situation is approximately $\alpha n / n = \alpha$.

- The complement of a sum of each probability is $1 - 2\alpha$, in which `PARTITION` produces a split more balanced than $1 - \alpha$ to \alpha$.
