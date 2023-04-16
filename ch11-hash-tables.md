# Ch11 Hash Tables

## 11.1 Direct-address tables

### Exercises

#### 1

- Looping from $i = m$ to $1$, we examine that the element with index $i$ exists. If it does, the maximum element of $S$ is that element.

- The worst-case performance is $\Theta(m)$.

#### 2

- A bit vector can be used for representing whether the key exists or not. Each bit matches a key.

- Dictionary operations runs in $O(1)$ time as follow.

- `DIRECT-ADDRESS-SEARCH(T, k)`:

```c
if T[k] == 1
    return k
else
    return NIL
```

- `DIRECT-ADDRESS-INSERT(T, k)`:

```c
T[k] = 1
```

- `DIRECT-ADDRESS-DELETE(T, k)`:

```c
T[k] = NIL
```

#### 3

- We can modify slots of the direct-address table to point doubly linked lists.

## 11.2 Hash tables

### Exercises

#### 1

- Let us define the indicator random variable $X_{kl} = I\{h(k) = h(l)\}$ for some key $k$ and $l$ in which $k \ne l$.

- Since simple uniform hashing, $E[X_{kl}] = 1/m$.

- Then we define random variable $Y$ the number of collisions.

$$
\begin{aligned}
E[Y]
&= E\left[\sum_{k \ne l} X_{kl}\right] \\
&= \sum_{k \ne l}E[X_{kl}]
&= {n \choose 2}{1 \over m} \\
&= {n(n-1) \over 2}\cdot {1 \over m} \\
&= {n(n-1) \over 2m}
\end{aligned}
$$

#### 2

- For convienience, we assume using singly linked list.

```
   T
0  |/|
1  |-|->|28|-|->|19|-|->|10|/|
2  |-|->|20|/|
3  |-|->|12|/|
4  |/|
5  |-|->|5|-|->|33|/|
6  |-|->|15|/|
7  |/|
8  |-|->|17|/|
```

#### 3

- Searches remain to take the linear time.

- To keep each list in sorted order, insertions become to take the linear time since it has to be placed in the right place.

- If we take the pointer as the argument, deletions take the constant time.

## 11.3 Hash functions

### Exercises

#### 1

- To search a linked list, we need to compare the element.

- Since comparing two long character string is expensive, we instead compare the hash value to save the cost.

#### 2

- Modular arithmetic can be distributed.

- Since the result of the modular arithmetic is in between 0 and modulus, distributing of modular arithemetic to each characters saves the cost.

- For example, suppose $x$ is string of length $n$ and each character is denoted by $x_i$ for $i = 1, 2, \dots, n$.

$$
\begin{aligned}
k
&= \left(\sum_{i = 1}^n x_i2^{7i}\right) \,\bmod\, m \\
&= \left(\sum_{i=1}^n ((x_i2^{7i}) \,\bmod\, m)\right) \,\bmod\, m \\
&= \left(\sum_{i=0}^n(((x_i \,\bmod m)(2^{7i} \,\bmod\, m))\,\bmod\,m)\right)\,\bmod\,m \\
&= \left(\sum_{i=0}^n\left((x_i \,\bmod\, m)\left(\left(\prod_1^i(2^7\,\bmod\, m)\right)\,\bmod\,m\right)\right) \,\bmod\, m\right) \,\bmod\, m
\end{aligned}
$$

#### 3

$$
k = \sum_{i=0}^n(x_i2^{ip})
$$

$$
\begin{aligned}
k\,\bmod\,m
&= \left(\sum_{i=0}^n(x_i2^{ip})\right)\,\bmod\, (2^p - 1) \\
&= \left(\sum_{i=0}^n((x_i2^{ip}) \,\bmod\, (2^p - 1))\right) \,\bmod\,(2^p-1) \\
&= \sum_{i=0}^nx_i \,\bmod\,(2^p-1) 
\end{aligned}
$$

- Thus any string obtained by permuting same characters hash to the same value.

The value h2.k/ must be relatively prime to the hash-table size m for the entire
hash table to be searched

## 11.4 Open addressing

### Exercises

#### 1

$$
h^\prime(k) = k
$$

- The result using linear probing is as follow.

$$
h(k, i) = (k + i) \,\bmod\, 11
$$

```
0  22(0)
1  88(1)
2
3
4   4(0)
5  15(1)
6  28(0)
7  17(1)
8  59(4)
9  31(0)
10 10(0)
```

- The result using quadratic probing with $c_1 = 1$ and $c_2 = 3$ is as follow.

$$
h(k, i) = (k + i + 3i^2) \,\bmod\, 11
$$

```
0  22(0)
1  
2  88(8)
3  17(3)
4   4(0)
5
6  28(0)
7  59(2)
8  15(1)
9  31(0)
10 10(0)
```

- The result using double hashing with $h_1(k) = k$ and $h_2(k) = 1 + (k \,\bmod\,(m-1))$ is as follow.

$$
h(k, i) = (k + i(1 + (k \,\bmod\,10)))\,\bmod\,11
$$

```
0  22(0)  
1
2  59(2)
3  17(1)
4   4(0)
5  15(2)
6  28(0)
7  88(2)
8
9  31(0)
10 10(0)
```

#### 2

- `HASH-DELETE(T, k)`:

```c
i = 0
repeat
    j = h(k, i)
    if T[j] == k
        T[j] = DELETED
        return j;
    else
        i = i + 1
until T[j] == NIL or i = m
error "no such key"
```

- `HASH-INSERT(T, k)`:

```c
i = 0
repeat
    j = h(k, i)
    if T[j] == NIL or T[j] == DELETED
        T[j] = k
        return j
    else
        i = i + 1
until i == m
error "hash table overflow"
```

#### 3

- When the load factor is $3/4$, upper bounds on  the expected  number of probes in an unsuccessful search is $1/(1-3/4) = 4$ and on the expected number of probes in a successful search is $1/(3/4)\ln(1/(1-3/4)) = 4\ln4/3$.

- When the load factor is $7/8$, the former is $1/(1-7/8) = 8$ and the latter is $1/(7/8)\ln(1/(1-7/8)) = 8\ln8/7$
