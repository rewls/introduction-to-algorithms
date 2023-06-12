# Ch16 Greedy Algorithms

## Contents

IV Advanced Design and Analysis Techniques

- Ch16 Greedy Algorithms

    - 16.1 An activity-selection problem

        - The optimal substructure of the activity-selection problem

        - Making the greedy choice

        - A recursive greedy algorithm

        - An iterative greedy algorithm

    - 16.2 Elements of the greedy strategy

        - Greedy-choice property

        - Optimal substructure

        - Greedy vresus dynamic programming

    - 16.3 Huffman codes

        - Prefix codes

        - Constructing a Huffman code

        - Correctness of Huffman's algorithm

## 16.1 An activity-selection problem

### Exercises

#### 16.1-1

- `dp-activity-selector.py`

- The activity selector using dynamic programming takes $O(n^3)$, which is much slower than `GREEDY-ACTIVITY-SELECTOR` that takes $\Theta(n)$.

#### 16.1-2

- If we sort the activities in monotonically increasing order by start time, selecting the last activity to start that is compatible with all previously selected activities can be a greedy choice. Because that activity would leave the resource available for as many other activities as possible as we have seen above.

- Substituting the latest start time for the earliest finish time in Theorem 16.1, it means that selecting the last activity to start yields an optimal solution.

#### 16.1-3

- When we select the activity of least duration from amongthose that are compatible with previously selected activities

$$
s = \langle0, 2, 3, 5, 6\rangle,
f = \langle3, 4, 6, 7, 9\rangle
$$

- When we select the compatible activity that overlaps the fewest other remaining activities

$$
s = \langle0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6\rangle, 
f = \langle2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8\rangle
$$

- 시작 시간이 가장 빠른 호환 가능한 나머지 활동을 선택할 때

$$
s = \langle0, 1, 2,\rangle
f = \langle3, 2, 3\rangle
$$

#### 16.1-4

- `interval-graph-coloring-problem.py`

- `interval-graph-colornig-problem-activity-selector.py`

#### 16.1-5

- `activity-selector-value-n3.py`

- `activity-selector-value-nlogn.py`

## 16.2 Elements of the greedy strategy

### Exercises

#### 16.2-1

- Greedy-choice property: Let the $i$th item have the largest value per pounds. Then there is an optimal solution including the $i$th item as much as possible.

- Assume that there is an optimml solution in which we don't take as much of the $i$th item as possible, even take not at all.

- We suppose that the knapsack is full because if it is not full, just adding some more of the $i$th item make the better solution which is contradiction.

- Since there are items with values per pounds that are smaller than or equal to of the $i$th item, if we substitute the rest of the $i$th item for that of items with the smallest values per pounds, a better solution is made which is also contradiction.

- Thus an optimal solution includes as much of the $i$th item as possible.

#### 16.2-2

- `BINARY-KNAPSACK(w, v, W)`

```c
n = w.length
let r[1..n, 1..W] be a new table
for i = 0 to W
    r[0, i] = 0
for i = 1 to n
    for j = 1 to W
        if w[i] <= j
            r[i, j] = max(r[i - 1, j], r[i - 1, j - w[i]] + v[i])
        else
            r[i, j] = r[i - 1, j]
return r[n, W]
```

#### 16.2-3

- Greedy-choice property: Let the $i$th item have the largest value and the smallest weight. Then there is an optimal solution including the $i$th item.

- Suppose that there exists an optimal solution in which we don't take the $i$th item.

- If the knapsack is not full and has room for the the $i$th item, just adding the $i$th item make a better solution which is contradiction.

- Instead if the knapsack is full or there is no room for it, substituting the $i$th item for the smallest value make a better solution which is also contradiction. Since an item with smallest value has largest weigth, substituting is possible.

- Thus the $i$th item is included in some optimal solution.

#### 16.2-4

- If we choose the first water stop, the subproblem starting at that point remains.

- Combining optimal solution to a subproblem with first water stop makes an optimal solution to the original problem. Prove is as follow using cut-and-paste argument.

- Denote by $S_i$ the set of water stops that are further from starting point than water stop $i$. Let $s_i$ be an minimum set of warter stops in which he doesn't run out of water. If we can find a set that has less water stops than $s_i$, substituting it for $s_i$ we make a better solution which is contradiction. Thus this algorithm yeilds an optimal solution and this problem exhibits optimal substructure.

- Greedy-choice property: Let water stop $i$ be the furthest point from starting point that is $m$ miles or less away. Then there is an optimal solution including water stop $i$.

- Suppose that there exists an optimal solution $s_k$ including such water stop $j$($j \ne i$). If we denote by $s_k^\prime$ a solution including water stop $i$ instead of water stop $j$, $s_k^\prime$ is also optimal solution because in $s_k^\prime he doesn't run out of water. Since $|s_k| = |s_k^\prime|$, we conclude that $s_k^\prime$ is an optimal solution including water stop $i$.

- Assume that the array of water stop places is sorted by the distances between its places and starting poni. Since to take a greedy-choice we search the water stops sequentially, this algorithm takes $O(n)$

#### 16.2-5

- Since the interval to be included in the set we need to determine is closed, given points can be located in a boundary of an interval.

- Thus to include as much of given points as possible we determine leftmost point in the given set as an left boundary of the first interval.

- If we choose the first interval, the subproblem that determines the smallest set of intervals that contains the given points excluding points in the first interval remains.

- We can make an optimal solution to the original problem by combining an optimal solution to a subproblem and the first interval. It is proven using cut-and-paste arrgument. Thus this problem exhibits optimal substructure.

- Greedy-choice property: The closed interval using leftmost point as a left boundary is included in some optimal solution.

- Suppose that there exists an optimal solution in which we don't take the leftmost point as a left boundary of an interval.

- If not every points that was in an interval using the leftmost point as a boundary are fit in an interval with a left boundary that is not the leftmost point, it doesn't guarantee that it makes an optimal solution not to use leftmost point as a left boundary of an interval which is contradiction.

- Thus this greedy choice is correct.

#### 16.2-7

- If we choose first elements in a and b respectively that maximize $a_1^{b_1}$ a subproblem for a and b excluding selected elements remains.

- Combining an optimal solution to a subproblem and first elements, an optimal solution to the original problem is made. Thus this problem exhibits optimal substructure.

- Greedy-choice property: Denote by $A^\prime$ and $B^\prime$ respectively sorted $A$ and sorted $B$. Elements with a same index in $A^\prime$ and $B^\prime$ is located in a same index in some optimal reordered $A$ and $B$.

- Assume that there is an optimal solution in which we place elements with different indices in $A^\prime$ and $B^\prime$ in a same index. In other words, assume that there is some $i < j$ for which $a_i < a_j$ $b_i > b_j$. 

- Focusing on these two, the payoff is $a_i^{b_j}a_j^{b_i}$. Swapping either $a_i$ and $a_j$ or $b_i$ and $b_j$, the payoff is $a_i^{b_i}a_j^{b_j}$ that is larger than the former as seen below which is contradiction.

$$
{a_i^{b_j}a_j^{b_i} \over a_i^{b_i}a_j^{b_j}} = a_i^{b_j - b_i}a_j^{b_i - b_j} = \left({a_j \over a_i}\right)^{b_i - b_j} > 1
$$

- Thus greedy choice is correct.

- First we have to sort $A$ and $B$ then take a greedy choice over and over until we arrive at the arrival poin. Sorting may take $\Theta(n\log n)$. Each iteration may take $O(1)$ because we can just choose an index in order algorithm take $O(n)$ then the total iterations take $O(n)$. Thus this algorithm takes $O(n\log n$.

## 16.3 Huffman codes

### Exercises

#### 16.3-1

- Since $a.freq \le b.freq$ and $a.freq \ge x.freq$ if $x.freq = b.freq$ then $a.freq \le x.freq$ in that $x.freq = a.freq$

- Since $x.freq \le y.freq$ and $y.freq \le b.freq$ if $x.freq = b.freq$ then $b.freq \le y.freq$ in that $y.freq = b.freq$

- Thus $a.freq = b.freq = x.freq = y.freq$

#### 16.3-2

- Assume that there is an optimal prefix code corresponding to a binary tree that is not full.

- In other words there is at least one node whose degree is one in that optimal prefix code.

- Denote by $n_i$ that node. If $n_i$ is the root, just removing it makes the lower cost which is contradiction.

- If $n_i$ is an internal node that is not the root, removing $n_i$ and placing the child subtree in the position of $n_i$ makes the lower cost which is also contradiction.

- Thus a binary tree that is not full cannot correspond to an optimal prefix code.

#### 16.3-3

```
    (54)
   /    \
[h:21] (33)
      /    \
   [g:13] (20)
         /    \
       [f:8] (12)
            /    \
          [e:5] (7)
               /   \
            [d:3] (4)
                 /   \
              [c:2] (2)
                   /   \
                [a:1] [b:1]
```

|Character|Huffman code|
|-|-|
|a|1111110|
|b|1111111|
|c|111110|
|d|11110|
|e|1110|
|f|110|
|g|10|
|h|0|

- Except for the deepest level and the root, nodes at each level in an binary tree corresponding to an optimal prefix code is generalized as follow.

$$
\text{left node: }fib(i), \text{right node: }\sum_{j = 1}^{\lfloor i/2 \rfloor}fib(2j) \text{ if } i \text{ is even}
$$

$$
\text{left node: }fib(i), \text{right node: }\sum_{j = 1}^{\lfloor i/2 \rfloor}fib(2j) + fib(i - 1) \text{ if } i \text{ is odd}
$$

- Our answer can be generalized as follow.

- A codeword for the character of first Fibonacci number frequency is $n + 1$ 1s.

- A codeword for the character of $i$th Fibonacci number frequency in which $n \ge i > 1$ is $n - i$ 1s and a zero. 

#### 16.3-4

- The cost of the tree $T$ is defined as follow.

$$
B(T) = \sum_{c\in C}c.freq\cdot d_T(c)
$$

- The costs of nodes at lower level is cumulative to the costs of merger nodes at higher level.

- Each frequency of the leaf nodes is accumulated its depth times in ths sum of the costs of all merger nodes. It means the total cost of the tree.

#### 16.3-5

빈도가 단조롭게 감소하도록 문자를 알파벳으로 정렬하면 코드워드 길이가 단조롭게 증가하는 최적의 코드가 있음을 증명하십시오.

- Assume that there exists an optimal code whose codeword lengths are monotonically increasing for ndk

- Let $A$ be $C$ sorted by frequency in monotonically decreasing.

- Assume that there exists an optimal code whose codeword lengths are not monotonically increasing.

- Then there is some $i$ and $j$($i < j$) for which the length of the codeword of $a_j$ is larger than those of $a_i$.

- That implies that the frequency of $a_j$ is larger than those of $a_i$ which is contradiction.

- Thus if we order the characters in an alphabet so that their frequencies are monotonically decreasing, then there exists an optimal code whose codeword lengths are monotonically increasing.

#### 16.3-6

- The number of nodes of a full binary tree is $2n - 1$

- To make receiver determine the structure of the tree we set 1 bit per the node that represents whether the node has the child nodes.

- The total size of codewords is $n\lceil \lg n\rceil$.

- Thus we can represent any optimal prefix code on $C $ using only $2n - 1 + n\lceil \lg n\rceil$ bits.

#### 16.3-7

- Merge the three least-frequent objects instead of two.

- We can prove that by substituting the three least-frequent objects for the two in Lemmas 16.2 and 16.3.

#### 16.3-8

- If the maximum character frequency is less than twice the minimum character frequency, the cost of merger nodes always larger than the maximum character frequency.

- This makes the binary tree of a code represent a complete tree which also occurs in a fixed-length code.

- Thus in this case Huffman coding is no more efficient than using an ordinary 8-bit fixed-length code.

#### 16.3-9

- As seen in 16.3-8, for a file of randomly chosen 8-bit characters the cost of merger nodes always larger than the maximum character frequency. Thus the binary tree of a code becomes a complete binary tree in which Huffman codding is no more efficient than using an ordinary 8-bit fixed-length code.
