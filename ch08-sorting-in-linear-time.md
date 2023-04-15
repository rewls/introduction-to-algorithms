# Ch8 Sorting in Linear Time

## 8.1 Lower bounds for sorting

### Exercises

#### 1

- Since sorting the input array of length $n$ using comparison sort requires $n-1$ comparisons, the smallest possible depth is $n-1$.

#### 2

- We have upper bound as follow.

$$
\lg(n!) \le \lg (n^n) = n\lg n
$$

- We should show we have also lower bound.

- Assume that $n$ is the power of 2.

$$
\begin{aligned}
\lg(n!)
&= \sum_{k = 1}^n \lg k \\
&= \sum_{k=1}^{n/2}\lg k + \sum_{k=n/2 + 1}^n \lg k \\
&\ge \sum_{k=1}^{n/2}1 + \sum_{k=n/2 + 1}^n\lg (n/2) \\
&= n/2 + n/2\lg(n/2) \\
&= n/2\lg n
\end{aligned}
$$

#### 3

- Consider a decision tree of height $h$ with $l$ reachble leaves corresponding to a comparison sort on $n$ elements

- In the case of half of the $n!$ inputs of length $n$, because each of the $n!/2$ permutations of the input appears as some leaf, we have $n!/2 \le l$.

- Since a binary tree of height $h$ has no more than $2^h$ leaves, we have the following.

$$
n!/2 \le l \le 2^h
$$

- which, by taking logarithms, implies

$$
h \ge \lg(n!/2) = \lg(n!) - 1 = \Omega(n \lg n)
$$

- In the case of a fraction of $1/n$ of the inputs of length $n$, because each of the $1/n\cdot n!$ permutations of the input appears as some leaf, we have $1/n\cdot n! \le l$.

$$
n/1\cdot n! \le l \le 2^h
$$

- which, by taking logarithms, implies

$$
h \ge \lg (n/1\cdot n!) = \lg((n-1)!) = \Omega(n \lg n)
$$

- In the case of a fraction $1/2^n$, becasue each of the $1/2^n\cdot n!$ permutations of the input appears as some leaf, we have $1/2^n\cdot n! \le l$

$$
1/2^n\cdot n! \le l  \le 2^h
$$

- which, by taking logarithms, implies

$$
h \ge \lg(1/2^n\cdot n!) = \lg (n!)- n = \Omega(n \lg n)
$$

- Thus there is no comparison sort whose running time is linear for each numbers of inputs.

#### 4

- The running time of sorting $k$ elements is $\Omega(k\lg k)$.

- Since we repeat this sorting $n/k$ times, multiplying, the total running time is $\Omega(n/k\cdot k\lg k) =  \Omega(n\lg k)$

## 8.2 Counting sort

### Exercises

#### 1

```
6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2
```

```
    1 2 3 4 5 6 7 8 9 1011
A: |6|0|2|0|1|3|4|6|1|3|2|
    0 1 2 3 4 5 6
C: |2|2|2|2|1|0|2|

    0 1 2 3 4 5 6
C: |2|4|6|8|9|9|11|

    1 2 3 4 5 6 7 8 9 1011
B: | | | | | |2| | | | | |
    0 1 2 3 4 5 6
C: |2|4|5|8|9|9|11|

    1 2 3 4 5 6 7 8 9 1011
B: | | | | | |2| |3| | | |
    0 1 2 3 4 5 6
C: |2|4|5|7|9|9|11|

    1 2 3 4 5 6 7 8 9 1011
B: | | | |1| |2| |3| | | |
    0 1 2 3 4 5 6
C: |2|3|5|7|9|9|11|

B: |0|0|1|1|2|2|3|3|4|6|
```

#### 2

- Consider the index $i$ and $j$ ($i < j$) containing the same element $k$.

- Since the for loop of lines 10-12 starts from $j = A.length$, processing for $j$ runs before for $i$.

- Decrementing $C[k]$ guarantees the element with index $j$ in $A$ is placed after one with index $i$

- Thus numbers with the same value appear in the output array in the same order as they do in the input array, in that counting sort is stable.

#### 3

- Since the algorithm is not affected by the order in which the A is processed, it is correct.

- In the modified algorithm, numbers with the same value appear in the output array in the reverse order. Thus It is not stable.

#### 4

- In the preprocessing, since the first for loop takes time $\Theta(k)$, the second for loop takes time $\Theta(n)$ and the third for loop takes time $\Theta(k), the totall time is $\Theta(n + k)$

- How many of the $n$ integers fall into a range $[a..b]$ can be computed by summing values in $C[a..b]$, which takes $O(1)$ time.

## 8.3 Radix sort

### Exercises

#### 1

```
COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX
```

```
COW     SEA     TAB     BAR
DOG     TEA     BAR     BIG
SEA     MOB     EAR     BOX
RUG     TAB     TAR     COW
ROW     DOG     SEA     DIG
MOB     RUG     TEA     DOG
BOX     DIG     DIG     EAR
TAB --> BIG --> BIG --> FOX
BAR     BAR     MOB     MOB
EAR     EAR     DOG     NOW
TAR     TAR     COW     ROW
DIG     COW     ROW     RUG
BIG     ROW     NOW     SEA
TEA     NOW     BOX     TAB
NOW     BOX     FOX     TAR
FOX     FOX     RUG     TEA
```

#### 2

- Insertion sort and merge sort are stable but heapsort and quicksort are not stable.

- To make any sorting algorithm stable, we can add index information to each element, in other words, the element in given array becomes the data structure that contains value and index such as (value, index).

- In the array preprocessed, $(i, a) < (j, b)$ if $i < j$ or if $i == j$ and $a < b$.

- Additional time is a constant and additional space is twice as large as B.

#### 3

- Loop invariant: At the start of each iteration of the for loop, the given array is sorted on the last $i-1$ digits

- Initialization: Before the first loop iteration, when $i = 1$, the given array is sorted on the last 0 digits trivially.

- Maintenance: Assume that the given array is sorted on the last $i-1$ digits. The body of the for loop sorts the given array by digit $i$, which results in the array sorted on the last $i$ digits. Incrementing $i$ by 1, the loop invariant preserves.

- Termination: The algorithm terminates when $i = d + 1$. The given array have been sorted on the last $d$ digits, which means the entire array is sorted.

#### 4

- If we view integers as number whose base is $n$, an integer in the range $0$ to $n^3 - 1$ becomes a $\log_n (n^3) = 3$-digit number whose base is $n$.

- Then We use radix sort in which $d = 3$ and $k = n$, which takes $\Theta(d(n+k)) = \Theta(3(n+n)) = \Theta(n)$.

## 8.4 Bucket sort

### Exercises

#### 1

```
.79, .13, .16, .64, .39, .20, .89, .53, .71, .42
```

```
    A   B
1  .79
2  .13
3  .16
4  .64
5  .39
6  .20
7  .89
8  .53
9  .71
10 .42 

```

#### 2

- The worst-case is that all elements in the given array falls into a bucket in reverse order, in which the running time is$\Theta(n^2)$ because bucket sort sorts elements in a bucket using insertion sort whose the worst-case running time is $O(n^2)$.

- If we modify the method to sort elements in a bucket from insertion sort to the algorithm whose worst-case running time is $O(n\lg n)$ such as merge sort, the worst-case running time becomes $O(n \lg n)$.

#### 3

$$
E[X^2] = E^2[X]
$$

$$
E[X] = 2 \cdot {1 \over 4} + 1 \cdot {1 \over 2} + 0 \cdot {1 \over 4} = 1
$$

$$
E[X^2] = E^2[X] = 1
$$
