# Ch4 Divide-and-Conquer

## Contents

I Foundations

- Ch4 Divide-and-Conquer

    - Recurrences

    - Technicalities in recurrences

    - 4.1 The maximum-subarray problem

        - A brute-force solution

        - A transformation
        
        - A solution using divide-and-conquer

        - Analyzing the divide-and-conquer algorithm

    - 4.2 Starssen's algorithm for matrix multiplication

        - A simple divide-and-conquer algorithm

        - Strassen's method

    - 4.3 The substitution method for solving recurrences

        - Making a good guess

        - Subtleties

        - Avoiding pitfalls

        - Changing variables

    - 4.4 The recursion-tree mdthod for solving recurrence

    - 4.5 The master method for solving recurrences

        - The master theorem

        - Using the master method

## 4.1 The maximum-subarray problem

### Exercises

#### 1

- It returns the maximum subarray of length 1, which contains the largest element in $A$.

#### 2

- `FIND-MAXIMUM-SUBARRAY(A)` brute-force:

```c
max-sum = A[1]
max-left = 1
max-right = 1
for i = 1 to A.length
    sum = A[i]
    for j = i + 1 to A.length
        sum = sum + A[j]
        if sum > max-sum
            max-sum = sum
            max-left = i
            max-right = j
return (max-left, max-right, max-sum)
```

#### 3

- On my computer $n_0$ is about 29. Changing the base case of the recursive algorithm make $n_0$ almost 1.

#### 4

- Make the algorithms that do not allow empty subarrays to return an empty array when the algorithms return the subarray whose sum is negative.

#### 5

- `FIND-MAXIMUM-SUBARRAY(A)`:

```c
max-sum = A[1]
sum = 0
high = 1
low = 1
for j = 2 to A.length
    high = j
    if sum > 0
        sum = sum + A[j]
    else
        low = j
        sum = A[j]
    if sum > max-sum
        max-sum = sum
        max-low = low
        max-high = high
return (max-low, max-high, max-sum)
``` 

## 4.2 Strassen's algorithm for matrix multiplication

### Exercises

#### 1

$$
\begin{aligned}
&S_1 = 8 - 2 = 6 & &S_2 = 1 + 3 = 4 \\
&S_3 = 7 + 5 = 12 & &S_4 = 4 - 6 = -2 \\
&S_5 = 1 + 5 = 6 & &S_6 = 6 + 2 = 8 \\
&S_7 = 3 - 5 = -2 & &S_8 = 4 + 2 = 6 \\
&S_9 = 1 - 7 = -6 & &S_{10} = 6 + 8 = 14
\end{aligned}
$$

$$
\begin{aligned}
&P_1 = 1 \cdot 6 = 6 \\
&P_2 = 4 \cdot 2 = 8 \\
&P_3 = 12 \cdot 6 = 72 \\
&P_4 = 5 \cdot -2 = -10 \\
&P_5 = 6 \cdot 8 = 48 \\
&P_6 = -2 \cdot 6 = -12 \\
&P_7 = -6 \cdot 14 = -84
\end{aligned}
$$

$$
\begin{aligned}
&C_{11} = 48 + (-10) - 8 + (-12) = 18 \\
&C_{12} = 6 + 8 = 14 \\
&C_{21} = 72 + (-10) = 62 \\
&C_{22} = 48 + 6 - 72 - (-84) = 66
\end{aligned}
$$

$$
\left(\begin{matrix}1 & 3 \\ 7 & 5\end{matrix}\right) \cdot
\left(\begin{matrix}6 & 8 \\ 4 & 2\end{matrix}\right) =
\left(\begin{matrix}18 & 14 \\ 62 & 66\end{matrix}\right)
$$

#### 2

- `SQUARE-MATRIX-MULTIPLY-STRASSEN(A, B)`:

```c
n = A.rows
if n == 1
    return a11 * b11
let C be a new n * n matrix
partition A, B, and C as in equations (4.9)
S1 = B12 - B22
S2 = A11 + A12
S3 = A21 + A22
S4 = B21 - B11
S5 = A11 + A22
S6 = B11 + B22
S7 = A12 - A22
S8 = B21 + B22
S9 = A11 - A21
S10 = B11 + B12
P1 = SQUARE-MATRIX-MULTIPLY-STRASSEN(A11, S1)
P2 = SQUARE-MATRIX-MULTIPLY-STRASSEN(S2, B22)
P3 = SQUARE-MATRIX-MULTIPLY-STRASSEN(S3, B11)
P4 = SQUARE-MATRIX-MULTIPLY-STRASSEN(A22, S4)
P5 = SQUARE-MATRIX-MULTIPLY-STRASSEN(S5, S6)
P6 = SQUARE-MATRIX-MULTIPLY-STRASSEN(S7, S8)
P7 = SQUARE-MATRIX-MULTIPLY-STRASSEN(S9, S10)
C11 = P5 + P4 - P2 + P6
C12 = P1 + P2
C21 = P3 + P4
C22 = P5 + P1 - P3 - P7
return C
```

#### 6

- If we multiply a $kn \times n$ matrix by an $n \times kn$ matrix using Strassen's algorithm as a subroutine, we have to multiply the two square matrices $k^2$ times.

- With the order of input matrices reversed, we have to multiply and add the two square matrices multiply $k$ times.

#### 7

- If $A = (a + b)(c + d) = ac + ad + bc + bd$, $B = ac$ and $C = bd$, then $B - C = ac - bd$ and $A - B - C = ad + bc$.

## 4.3 The substitution method for solving recurrences

### Exercises

#### 1

- We guess $T(n) \le cn^2$.

$$
\begin{aligned}
T(n)
&\le c(n-1)^2 + n \\
&= cn^2 + (1 - 2c)n + c \\
&\le cn^2
\end{aligned}
$$

- where the last step holds as long as $c > {1 \over 2}$.

#### 2

- We guess $T(n) \le c\lg n$.

$$
\begin{aligned}
T(n)
&\le c\lg\lceil n/2\rceil + 1 \\
&\le c\lg((n+1)/2) + 1 \\
&= c(\lg(n+1) - 1) + 1 \\
&= c\lg(n+1) -c + 1 \\
&\le c\lg(n+1)
\end{aligned}
$$

- where the last step holds as long as $c \ge 1$.

- Since our geuss failed in substitution method, we guess $T(n) \le c\lg (n - d)$ instead.

$$
\begin{aligned}
T(n)
&\le c\lg(\lceil n/2 \rceil-d) + 1 \\
&\le c\lg((n+1)/2 -d) + 1 \\
&= c\lg((n + 1 - 2d)/2) + 1 \\
&= c(\lg(n+1-2d) - 1) + 1 \\
&= c\lg(n+1-2d) -c + 1 \\
&\le c\lg(n - d)
\end{aligned}
$$

- where the last step holds for $c \ge 1$ and $d \le 1$.

#### 3

- We guess $T(n) \ge cn\lg n$.

$$
\begin{aligned}
T(n)
&\ge 2\left(c\left\lfloor {n\over2} \right\rfloor \lg\left(\left\lfloor {n \over 2} \right\rfloor\right)\right) + n \\
&\ge 2c{n-1 \over 2}\lg\left({n - 1 \over2}\right) + n \\
&= c(n-1)(\lg (n-1) - 1) + n \\
&=c(n-1)\lg (n - 1) +(1 - c)n+c \\
&\ge c(n-1)\lg(n-1)
\end{aligned}
$$

- where the last step holds for $0 < c \le 1$

- Since our geuss failed in substitution method, we guess $T(n) \le c(n+d)\lg (n + d)$ instead.

$$
\begin{aligned}
T(n)
&\ge 2\left(c\left(\left\lfloor {n\over2} \right\rfloor + d\right) \lg\left(\left\lfloor {n \over 2} \right\rfloor + d\right)\right) + n \\
&\ge 2c\left({n-1 \over 2}+d\right)\lg\left({n - 1 \over2} + d\right) + n \\
&= c(n-1 + 2d)(\lg (n-1 +2d) - 1) + n \\
&=c(n-1 +2d)\lg (n - 1+2d) +(1 - c)n+(1-2d)c \\
&\ge c(n-d)\lg(n-d)
\end{aligned}
$$

- where the last step hods for $0<c\le1$ and $d \ge {1\over3}$.

#### 4

- We guess $T(n) \le n\lg n + 1$

$$
\begin{aligned}
T(n)
&\le 2(c\lfloor n/2 \rfloor\lg(\lfloor n/2\rfloor)) + n \\
&\le cn\lg(n/2) + n \\
&= cn\lg n + (1 - c)n \\
&\le cn\lg n + 1
\end{aligned}
$$

- where the last step holds for $c \ge 1$

$$
T(1) = 1
$$

#### 5

- To show that $\Theta(n\lg n)$, we separately guess upper and loser bounds.

- First, we guess the upper bound $T(n) \le cn\lg n$.

$$
\begin{aligned}
T(n)
&\le c\left\lceil {n \over 2} \right\rceil\lg\left\lceil {n \over 2}\right\rceil + c\left\lfloor {n \over 2} \right\rfloor\lg\left\lfloor {n \over 2}\right\rfloor + \Theta(n) \\
&\le c(n+1)\lg\left({n+1 \over 2}\right) + \Theta(n) \\
&= c(n+1)\lg(n+1) - c(n+1) + \Theta(n) \\
&\le c(n+1)\lg(n+1)
\end{aligned}
$$

- where the last step holds for $c(n+1) \ge \Theta(n)$.

- Since our guess failed in substitution method, we guess $T(n) \le c(n-d)\lg(n-d)$.

$$
\begin{aligned}
T(n)
&\le c\left(\left\lceil {n \over 2} \right\rceil-d\right)\lg\left(\left\lceil {n \over 2}\right\rceil-d\right) + c\left(\left\lfloor {n \over 2} \right\rfloor-d\right)\lg\left(\left\lfloor {n \over 2}\right\rfloor-d\right) + \Theta(n) \\
&\le c(n+1-2d)\lg\left({n+1-2d \over 2}\right) + \Theta(n) \\
&= c(n+1-2d)\lg(n+1-2d) - c(n+1-2d) + \Theta(n) \\
&\le c(n - d)\lg(n-d)
\end{aligned}
$$

- where the last step holds for $c(n+1-2d) \ge \Theta(n)$ and $d \ge 1$

- Second, we guess the lower bound $T(n) \ge cn\lg n$.

$$
\begin{aligned}
T(n)
&\ge c\left\lceil {n \over 2} \right\rceil\lg\left\lceil {n \over 2}\right\rceil + c\left\lfloor {n \over 2} \right\rfloor\lg\left\lfloor {n \over 2}\right\rfloor + \Theta(n) \\
&\ge c(n-1)\lg\left({n-1 \over 2}\right) + \Theta(n) \\
&= c(n-1)\lg(n-1) - c(n-1) + \Theta(n) \\
&\ge c(n-1)\lg(n-1)
\end{aligned}
$$

- where the last step holds for $c(n-1) \le \Theta(n)$

- Since our guess failed in substitution method, we instead guess $T(n) \ge c(n-d)\lg(n-d)$.

$$
\begin{aligned}
T(n)
&\ge c\left\lceil {n-d \over 2} \right\rceil\lg\left\lceil {n-d \over 2}\right\rceil + c\left\lfloor {n-d \over 2} \right\rfloor\lg\left\lfloor {n-d \over 2}\right\rfloor + \Theta(n) \\
&\ge c(n-d-1)\lg\left({n-d-1 \over 2}\right) + \Theta(n) \\
&= c(n-d-1)\lg(n-d-1) - c(n-d-1) + \Theta(n) \\
&\ge c(n-d)\lg(n-d)
\end{aligned}
$$
$$
\begin{aligned}
T(n)
&\ge c\left(\left\lceil {n \over 2} \right\rceil-d\right)\lg\left(\left\lceil {n \over 2}\right\rceil-d\right) + c\left(\left\lfloor {n \over 2} \right\rfloor-d\right)\lg\left(\left\lfloor {n \over 2}\right\rfloor-d\right) + \Theta(n) \\
&\ge c(n-1-2d)\lg\left({n-1-2d \over 2}\right) + \Theta(n) \\
&= c(n-1-2d)\lg(n-1-2d) - c(n-1-2d) + \Theta(n) \\
&\ge c(n - d)\lg(n-d)
\end{aligned}
$$

- where the last step holds for $c(n+d-1) \le \Theta(n)$ and $d \le -1$

#### 6

- We guess $T(n) \le c(n - d)\lg (n - d)$.

$$
\begin{aligned}
T(n)
&\le 2c(\lfloor n/2\rfloor + 17 - d)\lg(\lfloor n/2\rfloor + 17 - d) + n \\
&\le c(n+34-2d)\lg((n+34-2d)/2) + n \\
&= c(n + 34 -2d)\lg(n+34-2d) -c(n+35-2d) +n \\
&\le c(n-d)\lg(n-d)
\end{aligned}
$$

- where the last step holds for $c \ge 1$ and $d \ge 34$

#### 7

- If we guess $T(n) \le cn^{\log_3 4}$,

$$
\begin{aligned}
T(n)
&\le 4c(n/3)^{\log_3 4} + n \\
&= cn^{\log_3 4} + n
\end{aligned}
$$

- We can guess $T(n) \le c\left(n^{\log_3 4} - n\right)$ instead. 

$$
\begin{aligned}
T(n)
&\le 4c\left((n/3)^{\log_3 4} - n/3\right) + n \\
&= cn^{\log_3 4} + (1 - 4/3c)n \\
&\le cn^{\log_3 4} - cn
\end{aligned}
$$

- where the last step holds for $c \ge 3$.

#### 8

- If we guess $T(n) \le cn^2$,

$$
\begin{aligned}
\end{aligned}
$$

#### 9

- Renaming $m = \lg n$ yields

$$
T(2^m) = 3T(2^{m/2}) + m
$$

- We can now rename $S(m) = T(2^m)$ to produce the new recurrence

$$
S(m) = 3S(m/2) + m
$$

## 4.4 The recursion-tree method for solving recurrences

### Exercises

#### 1

- The subproblem size for a node at depth $i$ is $n/2^i$.

- Since $n/2^i = 1$, or $i = \lg n$, the height of the tree is $\lg n$. Thus, the tree has $\lg n + 1$ levels (at depth 0, 1, 2, ..., $\lg n$).

- The number of nodes at depth $i$ is $3^i$ and each node at depth $i$, for $i = 0, 1, 2, ..., \lg n-1$, has a cost of $n/2^i$.

- Multiplying, the total cost over all nodes at depth $i$, for $i = 0, 1, 2, ..., \lg n-1$, is $(3/2)^in$.

- The bottom level, at depth $\lg n$, has $3^{\lg n} = n^{\lg 3}$ nodes, each contributing cost $T(1)$, for a total cost of $n^{\lg 3}T(1)$, which is $\Theta(n^{\lg 3})$.

$$
\begin{aligned}
T(n)
&= \sum_{i=0}^{\lg n - 1}\left({3 \over 2}\right)^in +\Theta\left(n^{\lg 3}\right) \\
&= {(3/2)^{\lg n} - 1\over (3/2) - 1}n + \Theta\left(n^{\lg 3}\right) \\
&= 2\left((3/2)^{\lg n}-1\right)n + \Theta\left(n^{\lg 3}\right) \\
&= 2n^{\lg3} - 2n + \Theta\left(n^{\lg 3}\right) \\
&= O\left(n^{\lg 3}\right)
\end{aligned}
$$

- We guess $T(n) \le cn^{\lg 3}$.

$$
\begin{aligned}
T(n)
&\le 3c\lfloor n/2\rfloor^{\lg 3} + n \\
&\le3c(n/2)^{\lg 3} +n \\
&= cn^{\lg 3} + n
\end{aligned}
$$

- Since our guess failed we guess $T(n) \le c(n^{\lg3} -n)$.

$$
\begin{aligned}
T(n)
&\le 3c(\lfloor n/2 \rfloor^{\lg 3} - n) + n \\
&\le 3c((n/2)^{\lg 3} -n) + n \\
&= cn^{\lg 3} + (1 - 3c)n \\
&\le c(n^{\lg 3} - n)
\end{aligned}
$$

- where the last step holds as long as $c \ge 1/2$.

#### 2

- The subproblem size for a node at depth $i$ is $n/2^i$.

- Since $n/2^i = 1$, or $i = \lg n$, the height of the tree is $\lg n$. Thus, the tree has $\lg n+ 1$ levels (at depth 0, 1, 2, ..., $\lg n$)

- The total cost at depth $i$, for $i = 0, 1, 2, ..., \lg n-1$, is $(n/2^i)^2 = 1/4^in^2$.

- The bottom level, at depth $\lg n$, has a node, whose cost is $T(1)$, which is $\Theta(1)$.

$$
\begin{aligned}
T(n)
&= \sum_{i=0}^{\lg n - 1}1/4^in^2 + \Theta(1) \\
&\le \sum_{i=0}^{\infty}1/4^in^2 + \Theta(1) \\
&= {1 \over 1 - (1/4)}n^2 + \Theta(1) \\
&= 4/3n^2 + \Theta(1) \\
&= O(n^2)
\end{aligned}
$$

- We guess $T(n) \le cn^2$.

$$
\begin{aligned}
T(n)
&\le c(n/2)^2 + n^2 \\
&= (c/4 + 1)n^2 \\
&\le cn^2
\end{aligned}
$$

- where the last step holds as long as $c \ge 4/3$

#### 3

- The subproblem size for a node at depth $i$ is $n/2^i + \alpha$, but we assume $n/2^i$ becasue it is tolerable sloppiness.

- Since $n/2^i = 1$, or $i = \lg n$, the height of the tree is $\lg n$. Thus the tree has $\lg n + 1$ levels.

- The number of nodes at dapth $i$ is $4^i$ and each node at dapth $i$, for $i = 0, 1, 2, ..., \lg n-1$, has a cost of $n/2^i$.

- Multiplying, the total cost over all nodes at depth $i$, for $i = 0, 1, 2, ..., \lg n$, is $2^in$.

- The bottom level, at depth $\lg n$, has $4^{\lg n} = n^2$ nodes, each contributing cost $T(1)$ which is $\Theta(n^2)$.

$$
\begin{aligned}
T(n)
&= \sum_{i=0}^{\lg n - 1} 2^in + \Theta(n^2) \\
&= {2^{\lg n} - 1 \over 2 - 1}n + \Theta(n^2) \\
&= (n - 1)n  + \Theta(n^2) \\
&= O(n^2)
\end{aligned}
$$

- We guess $T(n) \le cn^2$.

$$
\begin{aligned}
T(n)
&\le 4c(n/2 + 2)^2 + n \\
&= 4c(n^2/4 +2n  + 4) + n \\
&= cn^2 + (8c + 1)n + 16c \\
\end{aligned}
$$

- Since our guess failed, we guess $T(n) \le c(n^2 - dn)$ instead.

$$
\begin{aligned}
T(n)
&\le 4c\left((n/2 + 2)^2 -d(n/2 + 2)\right) \\
&= 4c(n^2/4 + (2-d/2)n + 4 - 2d) + n \\
&= cn^2 + (8c -2cd + 1)n + (16-4d)c \\
&\le c(n^2 - dn)
\end{aligned}
$$

- where the last step holds as long as $cd - 8c - 1 \ge 0$

#### 4

- The subproblem size for a node at depth $i$ is $n-i$. Thus the tree has $n$ levels.

- The number of nodes at depth $i$ is $2^i$ and each node at depth $i$ has a cost of 1.

- Multiplying, the total cost over all nodes at depth $i$ is $2^i$.

$$
\begin{aligned}
T(n)
&= \sum_{i=0}^{n-1} 2^i \\
&= {2^n - 1 \over 2 - 1} \\
&= 2^n - 1 \\
&= O(2^n)
\end{aligned}
$$

- We guess $T(n) \le c2^n$.

$$
\begin{aligned}
T(n)
&\le 2c2^{n-1} + 1 \\
&=c2^n + 1
\end{aligned}
$$

- Since our guess failed, we guess $T(n) \le c(2^n - 1)$ instead.

$$
\begin{aligned}
T(n)
&\le 2c(2^{n-1} - 1) + 1 \\
&= c2^n -2c +1 \\
&\le c(2^n - 1)
\end{aligned}
$$

- where the last step holds as long as $c \ge 1$

## 4.5 The master method for solving recurrences

### Exercises

#### 1

##### a

- $a = 2$, $b = 4$, $f(n) = 1$

- Since $n^{\log_4 2} = n^{1/2}$, $f(n) = O(n^{1/2 - \epsilon})$ for $\epsilon = 1/2$.

- Thus case 1 applies, and we have the solution $T(n) = \Theta(n^{1/2}))$

##### b

- Since $f(n) = \Theta(n^{1/2})$ case 2 applies so that $T(n) = \Theta(\sqrt{n}\lg n)$

##### c

- Since $f(n) = \Omega(n^{1/2+\epsilon})$ for $\epsilon = 1/2$ and for sufficiently large $n$ $2f(n/4) = 2(n/4) \le (1/2)n = cf(n)$ for $c = 1/2$, case 3 applies and thus $T(n) = \Theta(n)$.

##### d

- Since $f(n) = \Omega(n^{1/2+\epsilon})$ for $\epsilon = 3/2$ and for sufficiently large $n$ $2f(n/4) = 2(n/4)^2 \le (1/8)n^2 = cf(n)$ for $c = 1/8$, case 3 applies and thus $f(n) = \Theta(n^2)$.

#### 2

- Since Starssen's algorithm take $\Theta(n^{\lg 7})$, the largest integer value of a is 48.

## Lecture exercises

### 1 Master method

Use the master method to give tight asymptotic bounds for the following recurrences.

#### a

> $T(n) = 5T(n/2) + \Theta(n^2)$

- $a = 5$, $b = 2$, $f(n) = \Theta(n^2)$

- Since $f(n) = O(n^{\lg 5 - \epsilon})$ for $\epsilon = \lg 5 - 2$, case 1 applies, and we have the solution $T(n) = \Theta(n^{\lg 5})$.

#### b

> $T(n) = 27T(n/3) + \Theta(n^3\lg n)$

- $a = 27$, $b = 3$, $f(n) = \Theta(n^3\lg n)$

- Since $\Theta(n^3\lg n)$ is not polynomially larger than $n^{\log_3 27} = n^3$, we can't use master method.

#### c

> $T(n) = 5T(n/2) + \Theta(n^3)$

- $a = 5$, $b = 2$, $f(n) = \Theta(n^3)$

- Since $f(n) = \Omega(n^{\lg 5 + \epsilon})$ for $\epsilon = 3 - \lg 5$ and for sufficiently large $n$ $5f(n/2) = 5(n/2)^3 \le (5/8)n^3 = cf(n)$ for $c = 5/8$, case 3 applies and we have the solution $T(n) = \Theta(n^3)$.

### 2 K-selection

The below pseudocode represents K-selection algorithm.

- `SELECT(A, k)`:

```c
// If A.length = O(1), then any sorting algorithm runs in time O(1).
if A.length  <= 25:
    A = INSERTION-SORT(A)
    return A[k]
pivot = getPivot(A)
L, pivot, R = PARTITION(A, pivot)
if L.length == k
    return pivot
else if L.length > k
    return SELECT(L, k)
else
    return SELECT(R, k - L.length)
```

Assume that above the algorithm has the following recurrence.

$$
T(n) = \begin{cases}
T(L.length) + O(n) & \text{if }L.length > k - 1 \\
T(R.length) + O(n) & \text{if }L.length < k - 1 \\
O(n) & \text{if }L.length = k - 1
\end{cases}
$$

#### a

Use a recursion tree to determine a good asymptotic upper bound on the given recurrence for the best pivot value. Use the substitution method to verify your answer.

- The best pivot value is the value that can exactly divide the given array. Thus given recurrence changes to:

$$
T(n) = \begin{cases}
O(n) & \text{if } L.length = k - 1 \\
2T(n/2) + O(n) & \text{elsewhere}
\end{cases}
$$

- The subproblem size for a node at depth $i$ is $n/2^i$.

- Since $n/2^i = 1$, or $i = \lg n$, the height of the tree is $\lg n$. Thus, the tree has $\lg n + 1$ levels.

- The number of nodes at depth $i$ is $2^i$ and each node at depth $i$ has a cost of $cn/2^i$, in which $c$ represents the constant factor in the $O(n)$ term.

- Multiplying, the total cost over all nodes at depth $i$ is $cn$

$$
\begin{aligned}
T(n)
&= \sum_{i=0}^{\lg n}cn \\
&= c{n(n-1) \over 2} \\
&= O(n^2)
\end{aligned}
$$

- We geuss $T(n) \le cn^2$.

$$
\begin{aligned}
T(n)
&\le 2c(n/2)^2 + O(n) \\
&= cn^2/2 + O(n) \\
&\le cn^2
\end{aligned}
$$

- Since our guess failed, we guess $T(n) \le c(n^2 - n)$ instead.

$$
\begin{aligned}
T(n)
&\le 2c((n/2)^2 - (n/2)) + O(n) \\
&= cn^2/2 - cn + O(n) \\
&\le cn^2
\end{aligned}
$$

- where the last step holds for $cn >= O(n)$.

#### b

Use the master method to give tight asymptotic bounds for the recurrence for the best pivot value in the above.

- $a = 2$, $b = 2$, $f(n) = O(n)$.

- Since $log_a b = \lg 2 = 1$, $f(n) = \Theta(n^{\log_b a})$.

- Thus $T(n) = \Theta(n\lg n)$.

#### c

Use a recursion tree to determine a good asymptotic upper bound on the given recurrence for the worst pivot value. Use the substitution method to verify your answer.

- The worst pivot value is the smallest value in the given array. Thus given recurrence changes to:

$$
T(n) = \begin{cases}
O(n) & \text{if } L.length = k - 1 \\
T(n - 1) + O(n) & \text{elsewhere}
\end{cases}
$$

- Since the subproblem size for a node at depth $i$ is $n - i$, the tree has $n$ levels.

- The number of nodes at depth $i$ is 1 and each node at depth $i$ has a cost of $c(n - i)$, in which $c$ represents the constant factor of the $O(n)$ term.

- Multiplying, the total cost over all nodes at depth $i$, except for $i = n - 1$ is $cn(n-i) \le cn^2$

- The bottom level, at depth $n - 1$, has a node contributing cost $T(1) = O(n)$.

$$
\begin{aligned}
T(n)
&= \sum_{i=0}^{n-2} cn^2 + O(n)\\
&= c{(n-2)(n-1)(2n-3) \over 6} + O(n) \\
&= O(n^3)
\end{aligned}
$$

- We guess $T(n) \le cn^3$.

$$
\begin{aligned}
T(n)
&\le c(n-1)^3 + O(n) \\
&\le cn^3
\end{aligned}
$$

- where the last step holds for $cn \le O(n)$.

### 3 Tower of hanoi

#### a

Write pseudocode for solution of tower of hanoi problem using divide-and-conquer.

- `MOVE-TOWER(n, departure, arrival, auxiliary)`:

```c
if n == 1
    move 1 disk from departure to arrival
MOVE-TOWER(n-1, departure, auxiliary, arrival)
move 1 disk from departure to arrival
MOVE-TOWER(n-1, auxiliary, arrival, departure)
```

#### b

Make recurrence for your solution in tower of hanoi problem.

$$
T(n) = \begin{cases}
\Theta(1) & \text{if }n=1 \\
2T(n-1) + \Theta(1) & \text{if }n > 1
\end{cases}
$$

#### c

Use a recursion tree to determine a good asymptotic upper bound on the your recurrence. Use the substitution method to verify your answer.

- The subproblem size for a node at depth $i$ is $n - i$. Thus the tree has $n$ levels.

- The number of nodes at depth $i$ is $2^i$ and each node at depth $i$ has a cost of 1.

- Multiplying, the total cost over all nodes at depth $i$ is $2^i$.

$$
\begin{aligned}
T(n) 
&= \sum_{i=0}^{n-1} 2^i \\
&= {2^n - 1 \over 2 - 1} \\
&= 2^n - 1 \\
&= O(2^n)
\end{aligned}
$$

- We guess $T(n) \le c2^n$.

$$
\begin{aligned}
T(n)
&\le 2c2^{n-1} + \Theta(1) \\
&= c2^n + \Theta(1)
\end{aligned}
$$

- Since our guess failed, we guess $T(n) \le c(2^n - 1)$ instead.

$$
\begin{aligned}
T(n)
&\le 2c(2^{n-1} - 1) + \Theta(1) \\
&= c2^n -2c + \Theta(1) \\
&\le c(2^n - 1)
\end{aligned}
$$

- where the last step holds as long as $c \ge \Theta(1)$
