# Ch12 Binary Search Trees

## 12.1 What is a binary search tree?

### Exercises

#### 1

- The binary search tree of height 2 is as follow.

```
   10
   /\
  4  17
 /\  /\
1 5 16 21
```

- The binary search tree of height 3 is as follow.

```
   10
   /\
  5  17
  /  /\
 4  16 21
 /
1
```

- The binary search tree of height 4 is as follow.

```
    16
    /\
   10 21
   /  /
  5  17
  /
 4
 /
1
```

- The binary search tree of height 5 is as follow.

```
     17
     /\
   16 21
   /
  10
  /
  5
  /
 4
 /
1
```

- The binary search tree of height 6 is as follow.

```
       21
      /
     17
     /
    16
    /
   10
   /
   5
  /
  4
 /
1
```

#### 2

- Although in min-heap a node's key is greater than or equal to its children's keys, in binary-search-tree a nodes's key is greater than or equal to its left child's key and less than or equal to its right child's key.

- Since the min-heap property doesn't separate the left and right node in the relationship, we can't know where is the next element needed to print. Actually, it could be in either subtree.

- Thus, if we use the min-heap we can't print the keys of a tree in sorted order in linear time.

#### 3

- `INORDER-TREE-WALK(x)`:

```c
let S be an empty stack
current = T.root
while current != NIL or !S.EMPTY()
    if current != NIL
        push(S, current)
        current = current.left
    else
        current = pop(S, current)
        print current.key
        current = current.right
```

#### 4

- `PREORDER-TREE-WALK(x)`:

```c
if x != NIL
    print x.key
    PREORDER-TREE-WALK(x.left)
    PREORDER-TREE-WALK(x.right)
```

- `POSTORDER-TREE-WALK(x)`:

```c
if x != NIL
    POSTORDER-TREE-WALK(x.left)
    POSTORDER-TREE-WALK(x.right)
    print x.key
```

#### 5

- Assume that some comparison-based algorithm for constructing a binary search tree from an arbitrary list of $n$ elements takes $o(n\lg n)$ time.

- If we use it to create a binary search tree of $n$ nodes and use an inorder walk, we sort the list in $o(n\lg n)$ time.

- Since sorting $n$ elements takes $\Omega(n\lg n)$ time in the worst case in the comparison model but it is done in $o(n\lg n)$, a contradiction is occured.

- Thus any comparison-based algorithm for constructing a binary search tree takes $\Omega(n\lg n) time in the worst case.

## 12.2 Querying a binary search tree

### Exercises

#### 1

- In c the elements examined after 911 is examined must be smaller than 911 since the search key is smaller than 911. But there is 912 thus it could not be the sequence of nodes examined.

- In d the elements examined after 347 is examined must be larger than 347 since the search key is larger than 347. But there is 299 thus it could not be the sequence of nodes examined.

#### 2

- `TREE-MINIMUM(x)`:

```c
if x.left == NIL
    return x
return TREE-MINIMUM(x.left)
```

- `TREE-MAXIMUM(x)`:

```c
if x.right == NIL
    return x
return TREE-MAXIMUM(x.right)
```

#### 3

- `TREE-PREDECESSOR(x)`:

```c
if x.left != NIL
    TREE-MAXIMUM(x.left)
y = x.p
while y != NIL nad x != y.right
    x = p
    y = y.p
return y
```

#### 4

```
  7
 /
 5
/\
1 6
 \
 3
 /\
 2 4
```

- In the above tree, $A = \{2\}$, $B = \{7, 5, 1, 3, 4\}$ and $C = \{6}$.

- When $a = 2$ and $b = 1$, $a \ge b$.

- When $b = 7$ and $c = 6$, $b \ge c$

## 12.3 Insertion and deletion

### Exercises

#### 1

- `TREE-INSERT(x, y, z)`:

```c
x = T.root
y = NIL
while x != NIL
    y = x
    if x.key > z.key
        x = x.left
    else
        x = x.right
z.p = y
if y == NIL
    T.root = z
else if y.key > z.key
    y.right = z
else
    y.left = z 
```

```c
if X == NIL
    z.p = y
    if y == NIL
        T.root = z
    else if y.key > z.key
        y.right = z
    else
        y.left = z
else
    if x.key < z.key
        TREE-INSERT(x.right, z)
    else
        TREE-INSERT(x.left, z)
```

#### 2

- Since inserting is ocurred at a leaf node, the number of nodes examined in searching for a value in the tree is one plus the number of nodes examined when the value was first inserted into the tree to count the inserted node as an examined node.

#### 3

- The worst case is when the result of building a binary search tree is a skewed tree, in which sorting takes $\Theta(n^2)$.

- The best case is when the building a binary search tree result in a complete tree, in which sorting takes $\Theta(n\lg n)$.

### Lab exercises

#### 1

Show that if a node has two children in a binary search tree, the successor of the node doesn't have a left child and the predeccessor of the node doesn't have a right child.

- Suppose the node with two children in the binary search.

- Then the successor of the node is the leftmost node with the smallest value in the right subtree.

- The leftmost node implies that the node doesn't have a left child node.

- Thus the successor of the node with two children doesn't have a left child.

- Similarly, the predeccessor doesn't have a right child.

#### 2

Write pseudocode for counting the number of nodes in a given binary search tree and computing the height of a given binary search tree.

- `COUNT-NODE(x)`:

```c
if x == NIL
    return 0
return 1 + COUNT-NODE(x.left) + COUNT-NODE(x.right)
```

- `COMPUTE-HEIGHT(x)`:

```c
if x == NIL
    return 0
left-height = COMPUTE-HEIGHT(x.left)
right-height = COMPUTE-HEIGHT(x.right)
if left-height > right-height
    return left-height
else
    return right-height
```
