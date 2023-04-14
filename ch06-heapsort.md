# Ch6 Heapsort

## 6.1 Heaps

### Exercises

#### 1

- The minimum numbers is $2^h$ and the maximum numbers is $2^{h+1} - 1$

#### 2

- At the above exercise, for an $n$-element heap that has height $h$, $2^h \le n \le 2^{h + 1} - 1 < 2^h$.

- Thus, $h \le \lg n < h + 1$, $h = \lceil\lg n\rceil$ since $h$ is an integer.

#### 3

- If the largest value is contained by some node other than the root of the subtree, it violates the max-heap property. Thus the root contains the largest value.

#### 4

- By the max heap property, the smallest element of a max-heap is in one of the leaf nodes.

#### 5

- Since the values of an array in sorted order satisfy the min-heap property, it is a min-heap.

#### 6

- Let the given array as `A`. Since `A[9] = 7` is larger than `A[PARENT(9)] = A[4] = 6`, which violates the max-heap property, `A` is not a max-heap.

#### 7

- Since a leaf is a node with no children, we show whether the node has children or not.

- First for the node indexed $\lfloor n/2 \rfloor + 1$,

$$
\begin{aligned}
LEFT(\lfloor n/2 \rfloor + 1)
&= 2(\lfloor n/2 \rfloor + 1) \\
&> 2(n/2 - 1) + 2 \\
&= n
\end{aligned}
$$

- Since the child node index of the node is larger than the number of nodes, the node doesn't have leaves. Thus the node are a leaf node.

- Similarly, other nodes are the leaves.

## 6.2 Maintaining the heap property

### Exercises

#### 1

```
27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0
```

```
27(1)
17(2) 3(3 = i)
16(4) 13(5) 10(6) 1(7)
5(8) 7(9) 12(10) 4(11) 8(12) 9(13) 0(14)

27(1)
17(2) 10(3)
16(4) 13(5) 3(6 = i) 1(7)
5(8) 7(9) 12(10) 4(11) 8(12) 9(13) 0(14)

27(1)
17(2) 10(3)
16(4) 13(5) 9(6) 1(7)
5(8) 7(9) 12(10) 4(11) 8(12) 3(13 = i) 0(14)
```

#### 2

- `MIN-HEAPIFY(A, i)`:

```c
l = LEFT(i)
r = RIGHT(i)
smallest = i
if l <= A.heap-size and A[l] < A[i]
    smallest = l
if r <= A.heap-size and A[r] < A[smallest]
    smallest = r
if smallest != i
    exchange A[i] with A[smallest]
    MIN-HEAPIFY(A, smallest)
```

- The running time of `MIN-HEAPIFY` is equal to that of `MAX-HEPIFY`

#### 3

- When the element `A[i]` is larger than its children, the algorithm is just done.

#### 4

- When `i > A.heap-size/2`, `l` and `r` is larger than `A.heap-size`. Thus two comparison is false then just done. 

#### 5

- `MAX-HEAPIFY(A, i)`:

```c
while true
    l = LEFT(i)
    r = RIGHT(i)
    largest = i
    if l <= A.heap-size and A[l] > A[i]
        largest = l
    if r <= A.heap-size and A[r] > A[smallest]
        largeset = r
    if largest == i
        return
    exchange A[i] and A[smallest]
    i = smallest
```

#### 6

- The worst-case is the array that is sorted in incresing order.

- The worst-case cause MAX-HEAPIFY to be called recursively at every node on a simple path from the root down to a leaf.

- Since the height of the array of n elements is $\lceil\lg n\rceil$, the worst-case running time is $\Omega(\lg n)$.

## 6.3 Building a heap

### Exercises

#### 1

```
5, 3, 17, 10, 84, 19, 6, 22, 9
```

```
5(1)
3(2) 17(3)
10(4 = i) 84(5) 19(6) 6(7) 
22(8) 9(9)

5(1)
3(2) 17(3 = i)
22(4) 84(5) 19(6) 6(7) 
10(8) 9(9)

5(1)
3(2 = i) 19(3)
22(4) 84(5) 17(6) 6(7) 
10(8) 9(9)

5(1 = i)
84(2) 19(3)
22(4) 3(5) 17(6) 6(7) 
10(8) 9(9)

84(1)
22(2) 19(3)
10(4) 3(5) 17(6) 6(7) 
5(8) 9(9)
```

#### 2

- When we call `MAX-HEAPIFY`, the condition that each node of index i + 1, i + 2, ..., n is the root of a max-heap must be satisfied to ensure the array of index i..n is a max-heap.

- If we increase from 1, there is no guarantee that each node following the node of index i are root of max-heap.

#### 3

- Base case

    - We have seen the number of the leaves of n-element max-heap is $\lceil n/2 \rceil$ in Exercise 6.1-7, which is the base case for the induction.

- Inductive step

    - Assume that the max number of the nodes of height $h$ is $\lceil n/2^{h+1}\rceil$.

    - Each node of height $h + 1$ has exactly two children for the complete binary. Thus the max number of nodes of height $h + 1$ is $\lceil n/2^{h+1}\rceil / 2 \le \lceil n/2^{h+2}\rceil$

- Thus there are at most $\lceil n/2^{h+1}\rceil$ nodes of height $h$ in any $n$-element heap.

## 6.4 The heapsort algorithm

### Exercises

#### 1

```
5, 13, 2, 25, 7, 17, 20, 8, 4
```

```
25
13 20
8 7 17 2
5 4

20
13 17
8 7 4 2
5 25(i)

17
13 5
8 7 4 2
20(i) 25

13
8 5
2 7 4 17(i)
20 25

8
7 5
2 4 13(i) 17
20 25

7
4 5
2 8(i) 13 17
20 25

5
4 2
7(i) 8 13 17
20 25

4
2 5(i) 
7 8 13 17
20 25

2
4(i) 5
7 8 13 17
20 25
```

```
2 4 5 7 8 13 17 20 25
```

#### 2

- Initialization: At the start of the first loop iteration, `i = A.length = n`, the subarray `A[1..n]` is a max-heap containing the `i` smallest elements of `A[1..n]` since after the call of `BUILD-MAX-HEAP`, and the subarray `A[n+1..n]`, an empty array, contains the `n - n = 0` largest element of `A[1..n]`, sorted.

- Maintenance: `A[1]` is the largest element in `A[1..i]`. Since the subarray `A[i+1..n]` contains the `n-i` largest elements of `A[1..n]`, sorted, placing `A[1]` in `A[i]` make `A[i..n]` contains the `n-i+1` largest elements of `A[1..n]`, sorted. Decrementing `i` by 1 preserves the loop invariant.

- Termination: The loop terminates when $i = 1$. the subarray `A[1..1]` is a max-heap trivially containing the 1 smallest element of `A[1..n]`, and the subarray `A[1+1..n] = A[2..n]` contains the `n-1` largest elements of `A[1..n]`, sorted. Thus combining those make the entire array sorted.

#### 3

- For both the running time is $O(n\lg n)$

#### 4

- The worst-case is tha array that is sorted in decreasing order.

- The call to `BUILD-MAX-HEAP` takes time $O(n)$. Since each of the $n-1$ calls to `MAX-HEAPIFY` takes time $O(\lg n)$ for the worst case, overall calls takes time as follow.

$$
\begin{aligned}
\sum_{i = 1}^{n-1} \lg i 
&= \lg ((n-1)!) \\
&\le \lg ((n-1)^{n-1}) \\
&= n-1\lg (n-1) \\
&= \Omega(n\lg n)
\end{aligned}
$$

- Thus the worst-case running time of `HEAPSORT` is $\Omega(n \lg n)$
