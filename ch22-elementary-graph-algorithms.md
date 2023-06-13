# Ch22 Elementary Graph Algorithms

## Contents

VI Graph Algorithms

- Ch22 Elementary Graph Algorithms 

    - 22.1 Representations of graphs

        - Representing attributes

    - 22.2 Breadth-first search

        - Analysis

        - Shortest paths

        - Breadth-first trees

    - 22.3 Depth-first search

        - Properties of depth-first search

        - Classification of edges

## 22.1 Representations of graphs

### Exercises

#### 22.1-1

- The time to compute the out-degree and the in-degree of every vertex is $O(|E|+ |V|)$.

#### 22.1-2

- adjacency-list

```
1 -> 2 -> 3
2 -> 1 -> 4 -> 5
3 -> 1 -> 6 -> 7
4 -> 2
5 -> 2
6 -> 3
7 -> 3
```

- adjacency-matrix

```
  1 2 3 4 5 6 7
1 0 1 1 0 0 0 0
2 1 0 0 1 1 0 0
3 1 0 0 0 0 1 1
4 0 1 0 0 0 0 0
5 0 1 0 0 0 0 0
6 0 0 1 0 0 0 0
7 0 0 1 0 0 0 0
```

#### 22.1-3

- For adjacency-list

```
for i = 1 to G.V.length
    for v in G.Adj[i] and j = 1 to G.Adj[i].length
        add G.V[i] to G.Adj[j]
        remove v from G.Adj[i]
```

- which takes $O(|V| + |E|)$.

- For adjacency-matrix

```c
for i = 1 to G.V.length
    for j = i + 1 to G.V.length
        t = a[i, j]
        a[i, j] = a[j, i]
        a[j, i] = t
```

- which takes $O(|V|^2)$.

#### 22.1-4

```
let Adj_prime[1..G.V.length] be a new array
for i = 1 to G.V.length
    for v in G.Adj[i] and j = 1 to G.Adj[i].length
        if v != G.V[i] and v not in Adj_prime[G.V[i]]
            Add v to Adj_prime[G.V[i]]
G.Adj = Adj_prime
```

#### 22.1-5

- For the adjacency-list

```c
for i = 1 to G.V.length
    for u in G.Adj[i] and j = 1 to G.Adj[i].length
        for v in G.Adj[j] and k = 1 to G.Adj[j].length
            if v not in G.Adj[i]
                add v to G.Adj[i]
```

- The loop of lines 1-4 iterates $|V|$ times, the total number of iterations of the loop of lines 2-4 is $|E|$ and the loop of lines 3-4 takes $O(|V|)$ in the loop of lines 2-4.

- The total running time is $O(|V| + |VE|) = O(|VE|)$

- For the adjacency-matrix

```c
for i = 1 to G.V.length
    for j = 1 to A.Adj[i].length
        for k = 1 to A.Adj[j].length
            if G.Adj[i][j] > 0 and G.Adj[j][k] > 0 and G.adj[i][k] <= 0
                G.Adj[i][k] = 1
```

- which takes $O(|V| + |VE|) = O(|VE|)$.

## 22.2 Breadth-first search

### Exercises

#### 22.2-1

|$v$|$v.d$|$v.\pi$|
|-|-|-|
|1|$\infty$|NIL|
|2|3|4|
|3|0|NIL|
|4|2|5|
|5|1|3|
|6|1|3|

#### 22.2-2

|$v$|$v.d$|$v.\pi$|
|-|-|-|
|r|4|s|
|s|3|w|
|t|1|u|
|u|0|NIL|
|v|5|r|
|w|2|t|
|x|1|u|
|y|1|u|

#### 22.2-3

- The introduction of colors is to distinguish whether a vertex is visited or not. Thus two colors suffice.

#### 22.2-4

- If we represent the input graph by an adjacency matrix, we have to modify the loop header of a line 12 to `for i = 1 to |V|`

- Thus since the loop iterates $|V|$ times the total running time becomes $O(|V|^2)$.

## 22.3 Depth-first search

### Exercises

#### 22.3-1

- For directed graph, we can determine edge types by thinking each case of two intervals in Theorem 22.7

    1. The intervals $[u.d, u.f]$ and $[v.d, v.f]$ are entirely disjoint, and neither $u$ nor $v$ is a descendant of the other in the depth-first forest.

    2. The interval $[u.d, u.f]$ is contained entirely within the interval $[v.d, v.f]$ , and $u$ is a descendant of $v$ in a depth-first tree.

    3. The interval $[v.d, v.f]$ is contained entirely within the interval $[u.d, u.f]$, and $v$ is a descendant of $u$ in a depth-first tree.

- (WHITE, WHITE)

    1. If two intervals are disjoint then the edge type is cross.

    2. If the former interval is contained within the letter then the edge type is back.

    3. If the latter interval is contained within the former then the edge type is tree or forward.

- (WHITE, GRAY): 1. Cross, 2. Back, 3. None

- (WHITE, BLACK): 1. Cross, 2. None 3. None

- (GRAY, WHITE): 1. None, 2. None, 3. Tree or forward

- etc.

| |WHITE|GRAY|BLACK|
|-|-|-|-|
|WHITE|All|B, C|C|
|GRAY|T, F|T, B, F|T, F, C|
|BLOCK|None|B|All|

- For undirected graph, according to Theorem 22.10 every edge is either a tree edge ora back edge which is depend on the order of discovery of $(u, v)$ and $(v, u)$.

| |WHITE|GRAY|BLACK|
|-|-|-|-|
|WHITE|T, B|T, B|None|
|GRAY|T, B|T, B|T, B|
|BLOCK|None|T, B|T, B|

#### 22.3-2

|$v$|$v.d$|$v.f$|
|-|-|-|
|q|1|16|
|r|17|20|
|s|2|7|
|t|8|15|
|u|18|19|
|v|3|6|
|w|4|5|
|x|9|12|
|y|13|14|
|z|10|11|

- Tree edges: (q, s), (s, v), (v, w), (q, t), (t, x), (x, z), (t, y), (r, u)

- Back edges: (w, s), (z, x), (y, q)

- A forward edge: (q, w)

- Cross edges: (r, y), (u, y)

#### 22.3-3

- (u (v (y (x x) y) v) u) (w (z z) w)

#### 22.3-4

- The introduction of colors is to distinguish whether a vertex is visited or not. Thus two colors suffice.

#### 22.3-5

- According to Theorem 22.7 given statements holds.

- Let (u, v) be a some edge.

1. A tree edge or forward edge if and only if $u.d < v.d < v.f < u.f$

    - A tree edge or forward edge (u, v) implies connecting a vertex u to a descendant v in a depth-first tree. If v is a descendant of u in a depth-first tree, [v.d, v.f] is contained within the [u.d, u.f].

    - If [v.d, v.f] is contained within the [u.d, u.f], v is a descendant of u in a depth-first tree in that (u, v) is a tree edge or forward edge.

2. A back edge if and only if $v.d \le u.d < u.f \le v.f$

    - A back edge (u, v) connects a vertex u to an ancestor v in a depth-first tree. If u is a descendant of v in a depth-first tree then [u.d, u.f] is contained within [v.d, v.f].

    - If [u.d, u.f] is contained within the [v.d, v.f], u is a descendant of v in a depth-first tree in that (u, v) is a back edge.

3. A cross edge if and only if $v.d < v.f < u.d < u.f$

    - A cross edge is a some edge that is not tree, back or forward edge. In other words neither u nor v is a descendant of the other in the depth-first forest. If so, [u.d, u.f] and [v.d, v.f] are disjoint.

    - If [u.d, u.f] and [v.d, v.f] are disjoint, neither u nor v is a descendant of the other in the depth-first forest which means (u, v) is a cross edge.
