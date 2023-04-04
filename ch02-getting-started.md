# Ch2 Getting Started

## 2.1 Insertion sort

### Exercises

#### 1

```
a. |31|41|59|26|41|58|
        ^
b. |31|41|59|26|41|58|
           ^
     -->-->-->
c. |31|41|59|26|41|58|
     <--------
              -->
d. |26|31|41|59|41|58|
              <--
                 -->
e. |26|31|41|41|59|58|
                 <--
f. |26|31|41|41|58|59|
```

#### 2

- `INSERTION-SORT(A)`:

```c
for j = 2 to A.length
    key = A[j]
    i = j - 1
    while i > 0 and A[i] < key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
```

#### 3

- `LINEAR-SEARCH(A, ν)`:

```c
for i = 1 to A.length
    if A[i] == ν
        return i
return NIL
```

- Loop invariant: At the start of each iteration of the `for` loop of lines 1-4, the subarray `A[1..i-1]` consists of the elements not equal to `ν`.

- Initialization: Before the first loop interation, when `i = 1`, `A[1..i-1]` is the empty array, thus loop variant is preserved.

- Maintenance: Incrementing `i` for the next iteration of the `for` loop, when `A[i] != ν`, thus after incrementing the elements in `A[1..i]` is different than `ν`.

- Termination: The condition for the `for` loop to terminate is `i > A.length` or `A[i] == ν`. Incrementing `j` by 1 at each loop iteration, when `i = A.length + 1`, the `for` loop terminates and NIL is returned. Second, the `for` loop terminates when `A[i] != ν`, and the index, `i` is returned. For both cases, `A[1..i-1]` does not contain `ν`.

- Hence, the algorithm is correct.

#### 4

- Input: Two n-bit binary integers, stored in two n-element arrays A and B

- Output: The sum of the two integers should be stored in binar form in an (n + 1)-element array C.

- `ADD-BINARY(A, B)`:

```c
for i = 1 to A.length
    sum = A[i] + B[i] + C[i]
    C[i] = sum % 2
    C[i + 1] = sum / 2
return C
```

## 2.2 Analyzing algorithms

### Exercises

#### 1

$$
n^3/1000 - 100n^2 - 100n + 3 = \Theta(n^3)
$$

#### 2

- `SELECTION-SORT(A)`:

```c
for i = 1 to A.length - 1
    min_i = i
    for j = 1 + 1 to A.length
        if A[j] < A[min_i]
            min_i = j
    exchange A[i] with A[min_i]
```

- Loop invariant: At the start of each iteration of the `for` loop of lines 1-6, the subarray `A[1..i-1]` consists of the smallest `i - 1` elements in sorted order and the elements is in `A`.
        
- Initialization: Starting at `i = 1`, the subarray `A[1..i-1]` consists of zero elements, which preserves the loop invariant.

- Maintenance: The body of the `for` loop (lines 3-7) find the min value in `A[i..A.length]`. Then, the body of the `for` loop (lines 2-7) locate the min value to `A[i]`. Thus, `A[1..i]` consists of the smallest `i - 1` elements in sorted order.

- Termination: The condition causing the `for` loop to terminate is that `i > A.length - 1`. Each loop iteration increasing `i` by 1, we must have `i = A.length` at that time and `A[1..A.length - 1]` consists of the smallest `A.length - 1` elements in sorted order. Because `A[A.length]` is largest number in `A`, `A[1..A.length]` consists of the smallest `A.length` elements in sorted order, which is the entire array.

- Hence, the algorithm is correct.

- best-case and worst-case running times of the algorithm is $\Theta(n^2)$.

#### 3

- On average, half the elements in `A` are compared, thus $n/2 = \Theta(n)$. In the worst case, all the elements in `A` are compared, thus $n = \Theta(n)$.

#### 4

- We can put the condition for the best case and thus process it, which takes less time.

- For example, the best-case for the problem to sort the given array is for the array already sorted. Modify the algorithm so that it checks whether the array of length $n$ is sorted, which takes $\Theta(n)$. If it is, the algorithm terminates.

## 2.3 Designing algorithms

### Exercises

#### 1

```
 3 9 26 38 41 49 52 57
      /         \
3 26 41 52  9 38 49 57
  /    \        /   \
3 41  26 52  38 57  9 49
/ \    / \    / \   / \ 
3 41  52 26  38 57  9 49
```

#### 2

- `MERGE(A, p, q, r)`:

```c
n1 = q - p + 1
n2 = r - q
let L[1..n1+1] and R[1..n2+1] be new arrays
for i = 1 to n1
    L[i] = A[p+i-1]
for j = 2 to n2
    R[j] = A[q+j]
i = 1
j = 1
k = p
while i <= n1 and j <= n2
    if L[i] < R[j]
        A[k] = L[i]
        i = i + 1
    else
        A[k] = R[j]
        j = j + 1
    k = k + 1
while i <= n1
    A[k] = L[i]
    i = i + 1
    k = k + 1
while j <= n2
    A[k] = R[j]
    j = j + 1
    k = k + 1
```

#### 3

- Base case: When $n = 2$, $T(2) = 2\lg 2 = 2$

- Inductive step: Assume that $T(n) = 2T(n/2) + n = n\lg n$ for $k > 1$ when $n = 2^k$. When $n = 2^{k+1}$:
$$
\begin{aligned}
T(2^{k+1})
&= 2T(2^{k+1}/2) + 2^{k+1} \\
&= 2T(2^k) + 2^{k+1} \\
&= 2k \cdot 2^k + 2^{k+1} \\
&= (k + 1)2^{k+1} = 2^{k+1} \lg 2^{k+1}
\end{aligned}
$$

- Thus $T(n) = n \lg n$.

#### 4

- `INSERTION-SORT(A)`:

```c
INSERTION-SORT(A[1..n-1])
key = A[j]
i = n - 1
while i > 0 and A[i] > key
    A[i + 1 = A[i]
    i = i - 1
A[i + 1] = key
```

$$
T(n) = \begin{cases}
\Theta(1) & \text{if }n = 1 \\
T(n-1) + \Theta(n) & \text{if }n > 1
\end{cases}
$$

#### 5

- `ITERATIVE-BINARY-SEARCH(A, v)`:
 
```c
start = 1
end = A.length
while start <= end
    mid = floor((start + end) / 2)
    if A[mid] == v
        return mid
    if A[mid] > v
        end = mid - 1
    else
        start = mid + 1
return NIL
```    

- $T(n) = \lg n$

- `RECURSIVE-BINARY-SEARCH(A, v, start, end)`:

```c
if start > end
    return NIL
mid = floor((start + end) / 2)
if A[mid] == v
    return mid
if (A[mid] > val)
    return BINARY-SEARCH(A, v, low, mid-1)
else
    return BINARY-SEARCH(A, v, mid+1, high)
```

$$
T(n) =
\begin{cases}
\Theta(1) & \text{if } n = 1 \\
T(n/2) + \Theta(1)& \text{if } n > 1
\end{cases}
$$

- $T(n) = \lg n$

#### 6

- To insert the element, we must shift right the elements to the right of the index to be inserted, which takes $\Theta(n)$, even though find the index using binary search which takes $\Theta(\lg n)$.

- Thus, we can't improve the overall worst-case running time of insertion sort to $\Theta(n \lg n)$ using binary search in the while loop of lines 5-7 of the `INSERTION-SORT`.

#### 7

- First, sort the set S using merge sort, which takes $\Theta(n \lg n)$

- Second, for each element $a$ search $b$ such that $a + b = x$ using binary search, which takes $\Theta(\lg n)$

- $\Theta(n \lg n) + n \cdot \Theta(\lg n) = \Theta(n \lg n)$

## Problems

### 1 Insertion sort on small arrays in merge sort

#### a

- For each sublist, the time taken to be sorted is $\Theta(k^2)$, Thus $n / k \cdot \Theta(k^2) = \Theta(nk)$.

#### b

- Because merge function makes only two sorted sublists to a single uniformed and sorted sublists, to merge $n/k$ sorted sublists we should take two sublists and then merge them to finally become a single sorted list of length $n$.

- In the tournament way, the number of merging is $\lg n/k$. Merging takes $\Theta(n)$ time.

- Thus, merging the $n/k$ sublists takes $\lg n/k \cdot \Theta(n) = \Theta(n \lg n/k)$ worst-case time

#### c

$$
T(n) = \begin{cases}
\Theta(1) & \text{if }n = 1 \\
n/k \cdot T(k) + \Theta(n) & \text{if }n > 1
\end{cases}
$$

$$
\begin{aligned}
nk + n\lg(n/k) 
&= nk + n(\lg n - \lg k) \\
&= n\lg n + n(k - \lg k)
\end{aligned}
$$

- Because $n\lg n + n(k - \lg k) = \Theta(n\lg n)$, $k = \lg n$

#### d

- Choose largest k for which insertion sort is faster than merge sort.

### 2 Correctness of bubblesort

#### a

- At the start of each iteration of the `for` loop of lines 1-4, the subarray`A[1..i-1]` consists of the elements originally in `A`, but the smallest `i - 1` elements in sorted order.

#### b

- Loop invariant: At the start of each iteration of the `for` loop of lines 2-4, `A[j]` is the smallest element in `A[j..A.length]` originated in `A[j..A.length]`.

- Initialization: Starting at `j = A.length`, `A[j]` is the smallest element in `A[j..A.length]`, or `A[A.length..A.length]` originated in `A[A.length..A.length]`, thus the loop invariant preserved.

- Maintenance: The body of the `for` loop (lines 2-4) exchange `A[j]` with `A[j-1]` if `A[j] < A[j-1]`. Thus `A[j-1]` is the smallest element in `A[j-1..A.length]` originated in `A[j-1..A.length]`, preparing the loop invariant for the next iteration.

- Termination: The condition causing the `for` loop to terminate is that `j < i + 1`. Each loop iteration decreasing `j` by 1, we must have `j = i` at that time. `A[j]` is the smallest element in `A[j..A.length]` and substituting `i` for `j`, `A[i]` is the smallest element in `A[i..A.length]` originated in `A[i..A.length]`.

#### c

- Loop invariant: At the start of each iteration of the `for` loop of lines 1-4, the sublist `A[1..i-1]` consists of the elements originally in `A`, but the smallest `i - 1` elements in sorted order.

- Initialization: Starting at `i = 1`, `A[1..i-1]`, or `A[1..0]` contains zero element. Thus `A[1..i-1]` consists of the smallest `i - 1`, or 0 elements originated in `A`.

- Maintenance: The body of the `for` loop (lines 1-4), second `for` loop (lines 2-4) terminates to make `A[i]` the smallest element in `A[i..A.length]` originated in `A[i..A.length]`. Thus `A[i]` is `i`th smallest element in `A`, and `A[1..i]` consists of the elements originally in `A`, but the smallest `i` elements in sorted order.

- Termination: the condition for `for` loop to terminate is that `i > A.length - 1`. Incresing `i` by 1, `i` becomes `A.length` at that time. `A[1..1-1]`, in that, replacing `i` to `A.length`, `A[1..A.length-1]` is sorted and the smallest elements originated in `A`. Because `A[1..A.length-1]` consists of the smallest `A.length - 1` elements, `A[A.length]` is the largest element in `A`. Thus `A[1..A.length]`, the entire array consists of the elements originally in `A` but in sorted order.

#### d

- The number of first `for` loop of lines 1-4 iterations is $n$ and for each the number of second `for` loop of lines 2-4 is $n - i$. Because the body of two `for` loop takes constant time, we can ignore them. Thus, the worst time for bubble sort is $n \cdot (n-i) = \Theta(n^2)$, equal to for insertion sort.

### 3 Correctness of Horner's rule

#### a

- $\Theta(n)$

#### b

```c
y = 0
for i = 0 to n
    t = a_i
    for j = 0 to i
        t = t * x
    y += t
```

- This takes $n \cdot i$ time, and the worst time is $\Theta(n^2)$, which is longer than for Horner's rule.

#### c

- Initialization Starting at `i = n`, $\sum_{k=0}^{n-(n+1)} a_{k+i+1}x^k$ is a summation with no terms, 0.

- Maintenance: In the body of the `for` loop of lines 2-4, `y` is the product of itself and `x` plus `a_i`. In other words, $\sum_{k=0}^{n-(i+1)}a_{k+i+1}x^k$ is multiplied by $x$ and added to $a_{i+1}$, thus $\sum_{k=0}^{n-i}a_{k+i}x^k$, preparing the loop invariant for the next iteration.

- At the start of the each iteration of the `for` loop (lines 2-4), $y = \sum_{k=0}^{n-(i+1)}a_{k+i+1}x^k$. In the body of the `for` loop, `y` is the product of itself and `x` plus `a_i`. In other words, $\sum_{k=0}^{n-(i+1)}a_{k+i+1}x^k$ is multiplied by $x$ and added to $a_{i+1}$, thus $\sum_{k=0}^{n-i}a_{k+i}x^k$, preparing the loop invariant for the next iteration. The computation is as follow:

$$
\begin{aligned}
a_i + x\sum_{k=0}^{n-(i+1)}a_{k+i+1}x^k
&= a_i + \sum_{k=0}^{n-(i+1)}a_{k+i+1}x^{k+1} \\
&= \sum_{k=0}^{n-i}a_{k+i}x^k
\end{aligned}
$$

- Termination: The `for` loop of lines 2-4 terminates when `i = -1`. Substituting $i$ to -1 in $\sum_{k=0}^{n-(i+1)}a_{k+i+1}x^k$, $\sum_{k=0}^na_kx^k$.

#### d

- At the end of the `for` loop, The loop invariant implies `y` is the evaluation of a polynomial with the given coefficients.

### 4 Inversions

#### a

- $(3, 4), (1, 5), (2, 5), (3, 5), (4, 5)$

#### b

- The array [n, n-1, ..., 1] has the most inversions. It has an inversion $(i, j)$ for all $1 \le i \le n$. the number of inversions is ${n \choose 2} = {(n-1)n \over 2}$.

#### c

- The running time of insertion sort is $\Theta(n^2)$, and the max number of inversions is ${(n-1)n \over 2} = \Theta(n^2)$. Both values in $\Theta$-notation are equal.

- In insersion sort pseudocode, adding counting code to the body of the `for` loop, the number of inversions is computed as below.

- `COUNT-INVERSION(A)`:

```c
n = 0
for j = 2 to A.length
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key 
    n = n + (j - 1) - i
```

- The loop invariant for this algorithm is simillar to for insertion sort, except for someting added as the below. We would show correctness only about inversion because we've already seen about insertion sort in the book.

- Loop invariant: At the start of each iteration, the variable `n` is the number of inversions in which the right index is `k` for all `1 <= k <= j - 1`. `A[1..j-1]` consists of the elements originally in `A[1..j-1]`, but in sorted order.

    - The reason for sorting is that by sorting, we can specify the boundary of elements greater than `A[j]` without checking all elements in `A[1..j-1]`

- Initializatoin: When `j = 2`, `n` is 0, the number of inversions in which the right index is `j - 1 = 1`.

- Maintenance: After lines 3-8 which is part of the insertion sort code, the number of indexs passed in the `while` loop of lines 5-7 is the number of inversions in which the right index is `j` because `A[1..j-1]` is sorted. It is added to `n`, thus `n` is the number of inversions in which the right index is `k` for all `1 <= k <= j`, preserving the loop invariant for the next iteration.

- Termination: When `j = A.length + 1`, the loop terminates. `n` is the number of inversions in which the right index is `k` for all `1 <= k <= j - 1`, `1 <= k <= A.length`. Thus `n` is the number of inversions for `A`.

- Since we have added a constant amount of additional work to each iteration, running time of counting the number of inversions is proportional to of insertion sort.

#### d

- Divide: Divide the $n$-element in which we count inversions into two subsequences of $n/2$ elements each.

- Conquer: Count inversions in two subsequences recursively.

which right index is in one subsequence and left one is in another recursively, sorting the two subsequences.

- Combine: Add the number of inversions in which the right index is in one subsequence and the left one is in other to produce the entire number of inversions, merging the two sorted subsequences to eliminating the inversions in that to avoid double counting.

- `MERGE-COUNT-INVERSION(A, p, r)`:

```c
if p >= r
    return 0
n = 0
q = floor((p + r) / 2)
n = n + MERGE-INVERSION(A, p, q)
n = n + MERGE-INVERSION(A, q + 1, r)
n = n + MERGE(A, p, q, r)
return n
```

- `MERGE(A, p, q, r)`:

```c
n1 = q - p + 1
n2 = r - q
let L[1..n1+1] and R[1..n2+1] be new arrays
for i = 1 to n1
    L[i] = A[p+i-1]
for j = 2 to n2
    R[j] = A[q+j]
n = 0
i = 1
j = 1
k = p
while i <= n1 and j <= n2
    if L[i] <= R[j]
        A[k] = L[i]
        i = i + 1
    else
        A[k] = R[j]
        j = j + 1
        n = n + n1 - i + 1
while i <= n1
    A[k] = L[i]
    i = i + 1
    k = k + 1
while i <= n2
    A[k] = R[j]
    j = j + 1
    K = k + 1
return n;
```

- The loop invariant for this algorithm is simillar to for merge, except for someting added as the below. We would show correctness only about inversion because we've already seen about merge in the book.

- Loop invariant: At the start of each iteration, the variable `n` is the number of inversions in which the left index is in `L[1..n1]` and the right index is in `R[1..j-1]`. `A[p..k-1]` consists of the element in `L[1..i-1]` and `R[1..j-1]`, but in sorted order.

- Initialization: When `i = 1`, `j = 1`, and `k = p`, `n` is 0, the number of inversions in which the left index is in `L[1..n1]` and the right one is in `R[1..j-1]`, the empty array `R[1..0]`.

- Maintenance: Let us suppose that `L[i] <= R[j]`. Because `(i, j)` is not an inversion, incrementing `i` and `k` prepares the loop invariant for the next iteration. If `L[i] > R[j]`, `(i, j)` is an inversion. Because `L` is sorted, `(x, j)` for all `x` in `L[i..n1]` is an inversion. Thus adding the number of the inversions for the right index `j` and incrementing `j`, `n` is the number of inversions in which the left index is in `L[1..n]` and the right one is in `R[1..j-1]`.

- Termination: When `i = n1 + 1` or `j = n2 + 1`, the loop terminates. `n` is the number of inversions in which the left index is in `L[1..n1]` and the right on is in `R[1..j-1]`, in that `R[1..n2]`, the entire number of inversions.
