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

```
INSERTION-SORT(A)
    for j = 2 to A.length
        key = A[j]
        i = j - 1
        while i > 0 and A[i] < key
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
```

#### 3

```
LINEAR-SEARCH(A, ν)
    for i = 1 to A.length
        if A[i] == ν
            return i
        return NIL
```

- Initialization: Befor the first loop interation, When `i = 1`, the elements in `A[1..i-1]` are not `ν`.

- Maintenance: When `A[i] != ν`, incrementing `i` for the next iteration of the for loop then preserves the loop invariant.

- Termination: The for loop terminates at the time, `A[i] == ν` or `i = A.length + 1`. When `A[i] == ν`, the elements in `A[1..i-1]` are not `ν`. When `i = A.length + 1`, the elements in `A[1..A.length + 1 - 1]`, `A[1..A.length]` are not `ν` because only when `A[i] != ν` incrementing `j` by 1 to become `A.length + 1`.

- Hence, the algorithm is correct.

#### 4

- Input: Two n-bit binary integers, stored in two n-element arrays A and B

- Output: The sum of the two integers should be stored in binar form in an (n + 1)-element array C.

```
ADD-BINARY(A, B)
    for i = 1 to A.length
        sum = A[i] + B[i] + C[i]
        C[i] = sum % 2
        C[i + 1] = sum / 2
        return C
```
