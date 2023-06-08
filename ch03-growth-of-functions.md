# Ch3 Growth of Functions

## Contents

I Foundations

- Ch3 Growth of Functions

    - 3.1 Asymptotic notation

        - Asymptotic notation, funnctions, and running times

        - $\Theta$-notation

        - $O$-notation

        - $\Omega$-notation

        - Asymptotic notation in equations and inequalities

        - $o$-notation

        - $\omega$-notation

        - Comparing functions

    - 3.2 Standard notations and common functions

        - Monotonicity

        - Floors and ceilings

        - Modular arithmetic

        - Polynomials

        - Exponentials

        - Logarithms

        - Factorials

        - Functional iteration

        - The iterated logarithm function

        - Fibonacci numbers

## 3.1 Asymptotic notation

### Exercises

#### 1

- To prove that $\text{max}(f(n), g(n)) = \Theta(f(n) + g(n))$, we have to find positive constants $c_1$, $c_2$ and $n_0$ sush that

$$
0 \le c_1(f(n) + g(n)) \le \text{max}(f(n), g(n)) \le c_2(f(n) + g(n)
$$

- for all $n \ge n_0$.

$$
\text{max}(f(n), g(n)) \le f(n) + g(n)
$$

$$
f(x) \le \text{max}(f(n), g(n))
$$

$$
g(n) \le \text{max}(f(n), g(n))
$$

$$
{f(x) + g(n) \over 2} \le \text{max}(f(n), g(n))
$$

$$
0 \le {f(x) + g(n) \over 2} \le \text{max}(f(n), g(n)) \le f(n) + g(n)
$$

- As above, $c_1 = {1 \over 2}$ and $c_2 = 1$ for all sufficiently large because of $f(n)$ and $g(n)$ is asymptotically nonnegative function.

- Thus, $\text{max}(f(n), g(n)) = \Theta(f(n) + g(n))$.

#### 2

- To prove that $(n + a)^b = \Theta(n^b)$, we should determine positive constants $c_1$, $c_2$ and $n_0$ such that $0 \le c_1n^b \le (n + a)^b \le c_2n^b$ for all $n \ge n_0$.

- If positive constants $d_1, d_2$ and $n_0$ such that $0 \le d_1n \le (n + a) \le d_2n$ for all $n \ge n_0$ is exist, above $c_1$ and $c_2$ also exist because $b > 0$.

- $n + a \ge n - |a| \ge{1 \over 2}n$ for all $|a| \le {1 \over 2}n$, $n \ge 2|a|$

- $n + a \le n + |a| \le 2n$ for all $|a| \le n$, $n \ge |a|$

- As above, $d_1 = {1 \over 2}$, $d_2 = 2$, $m_0 = 2|a|$, thus $c_1 = \left({1 \over 2}\right)^b$, $c_2 = 2^b$, $n_0 = 2|a|$

#### 3

- $O(n^2)$ is the set of functions $f(n)$ with positive constants $c$ and $n_0$ such that $0 \le f(n) \le cg(n)$ for all $n \le n_0$.

- According to the definition, $O(n^2)$ contains $f(n) = 0$ for all $n$.

- Assuming $T(n)$ is the running time of algorithm A, $T(n) \ge O(n^2)$ is actually $T(n) \ge 0$.

- Thus given statement is meaningless.

#### 4

- Since $0 \ge 2^{n+1} \ge 2 \cdot 2^n$ for all $n$, $2^{n+1} = O(2^n)$.

- Assuming there exist positive constants $c$ and $n_0$ such that $0 \le 2^{2n} \le c \cdot 2^n, $c$ must greater than or equal to $2^n$.

- No constant is greater than $2^n$, thus the assumption has a contradiction.

#### 5

- First, assume $f(n) = \Theta(g(n))$. Then there exist positive constants $c_1$, $c_2$, and $n_0$ such that $0 \le c_1g(n) \le f(n) \le c_2g(n)$ for all $n \ge n_0$.

- Since $0 \le f(n) \le c_2g(n)$ for all $n \ge n_0$, $f(n) = O(g(n))$.

- Since $0 \le c_1g(n) \le f(n)$ for all $n \ge n_0$, $f(n) = \Omega(g(n))$.

- Second, assume $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$. Then there exist positive constants $c_O$, $c_\Omega$, and $n_O$, $n_\Omega$ such that $0 \le c_\Omega g(n) \le f(n)$ for all $n \ge n_O$ and $0 \le f(n) \le c_Og(n)$ for all $n \ge n_\Omega$.

- Combining two inequalities, $0 \le c_\Omega g(n) \le f(n) \le c_Og(n)$ for all $n \ge \text{max}(n_O, n_\Omega)$, $f(n) = \Theta(g(n))$

#### 6

- Assume the running time of an algorithm is $T(n)$ and its worst-case running time is $T_w(n)$ and its best-case running time is $T_b(n)$.

- First, assume $T(n) = \Theta(g(n))$. Then there exist positive constants $c_1$, $c_2$, and $n_0$ such that $0 \le c_1g(n) \le T_b(n) \le T(n) \le T_w(n) \le c_2g(n)$ for all $n \ge n_0$.

- Since $0 \le T_w(n) \le c_2g(n)$ for all $n \ge n_0$, $T_w(n) = O(g(n))$.

- Since $0 \le c_1g(n) \le T_b(n)$ for all $n \ge n_0$, $T_b(n) = \Omega(g(n))$.

- Second, assume $T_w(n) = O(g(n))$ and $T_b(n) = \Omega(g(n))$. Then there exist positive constants $c_O$, $c_\Omega$, $n_O$, and $n_\Omega$ such that $0 \le T_w(n) \le c_Og(n)$ for all $n \ge n_O$ and $0 \le c_\Omega g(n) \le T_b(n)$ for all $n \ge n_\Omega$.

- Combining two inequalities, $0 \le c_\Omega g(n) \le T_b(n) \le T(n) \le T_w(n) \le c_Og(n)$ for all $n \ge \text{max}(n_O, n_\Omega)$, $T(n) = \Theta(g(n))$

#### 7

- Assume $o(g(n)) \cap \omega(g(n))$ is not empty.

- $o(g(n))$ is the set of functions such that for any positive constant $c$, there exists a positive constant $n_o$ such that $0 \le f(n) < cg(n)$ for all $n \ge n_o$.

- $\omega(g(n))$ is the set of functions such that for any positive constant $c$, there exists a constant $n_\omega$ such that $0 \le c g(n) < f(n)$ for all $n \ge n_\omega$

- Combining two inequalities, $0 \le c g(n) < f(n) < cg(n)$ for all $n \ge \text{max}(n_o, n_\omega)$. $f(n)$ that satisfy the inequality does not exists.

- Since the assumption leads to a contradiction, $o(g(n)) \cap \omega(g(n))$ is the empty set.

#### 8

$$
\begin{aligned}
\Omega(g(n,m)) = \{f(n, m):\; &\text{there exist positive constants } c, n_0, \text{and }m_0 \\
&\text{such that }0 \le cg(n, m) \le f(n, m) \\
&\text{for all }n \ge n_0 \text{ or } m \ge m_0\}
\end{aligned}
$$

$$
\begin{aligned}
\Theta(g(n,m)) = \{f(n, m):\; &\text{there exist positive constants } c_1, c_2, n_0, \text{and }m_0 \\
&\text{such that }0 \le c_1g(n, m) \le f(n, m) \le c_2g(n,m) \\
&\text{for all }n \ge n_0 \text{ or } m \ge m_0\}
\end{aligned}
$$

## 3.2 Standard notations and common functions

### Exercises

#### 1

- First, assume $f(n)$ and $g(n)$ are monotonically increasing functions. It means for $m \le n$ $f(m) \le f(n)$ and $g(m) \le g(n)$.

- Combining two inequalities, $f(m) + g(m) \le f(n) + g(n)$ for $m \le n$. Thus $f(n) + g(n)$ is a monotonically increasing functions.

- Since $m \le n$ implies $g(m) \le g(n)$, for $m \le n$ $f(g(m)) \le f(g(n))$. Thus $f(g(n))$ is a monotonically increasing functions.

- Second, assume $f(n)$ and $g(n)$ are nonnegative.

- Multiplying two inequalities, $f(m)g(m) \le f(n)g(n)$. Thus $f(n)g(n)$ is monotonically increasing.

#### 2

$$
a^{\log_bc} = a^{\log_a c \over \log_a b} = \left(a^{\log_a c}\right)^{1 \over \log_a b} = c^{\log_b a}
$$

#### 3

- According to Stirling's approximation, $n! = \sqrt{2\pi n}\left({n \over e}\right)^n \left(1 + \Theta\left({1 \over n}\right)\right)$.

$$
\begin{aligned}
\lg n! &= \lg\sqrt{2\pi n}\left({n \over e}\right)^n \left(1 + \Theta\left({1 \over n}\right)\right) \\
&= n\lg{n \over e} + \lg\sqrt{2\pi n} + \lg\left(1 + \Theta\left({1 \over n}\right)\right) \\
&= \Theta(n\lg n) + \Theta(\lg n) + \Theta(1) \\
&= \Theta(n \lg n)
\end{aligned}
$$

- $n! = \omega(2^n)$ is proved by:

$$
\begin{aligned}
\lim_{n \to\infty}{2^n \over n!} 
&= \lim_{n \to \infty}{2^n \over \sqrt{2\pi n}\left({n \over e}\right)^n \left(1 + \Theta\left({1 \over n}\right)\right)} \\
&= \lim_{n \to \infty} {1 \over \sqrt{2\pi n} \left(1 + \Theta\left({1 \over n}\right)\right)}\left({2e \over n}\right)^n \\
&= \lim_{n \to \infty} {1 \over \sqrt{2\pi n} \Theta(1)} \left({2e \over n}\right)^n \\
&\le \lim_{n \to \infty} \left({2e \over n}\right)^n = 0
\end{aligned}
$$

- $n! = o(n^n)$ is proved by:

$$
\lim_{n \to \infty} {n! \over n^n} = 0
$$

#### 4

- Proving that a function $f(n)$ is polynomially bounded is equivalent to proving that $\lg(f(n)) = O(\lg n)$.

    - If $f(n)$ is polynomially bounded, there exist constants $c$, $k$ and $n_0$ such that $f(n) \le cn^k$ for all $n \ge n_0$. Then, $\lg(f(n)) \le ck\lg n$, which means $\lg(f(n)) = O(\lg n)$.

    - Similarly, if $\lg(f(n)) = O(\lg n)$, then $f$ is polynomially bounded.

- $\lg(n!) = \Theta(n\lg n)$

- $\lceil\lg n\rceil = \Theta(\lg n)$

    - $\lceil \lg n \rceil \ge \lg n$

    - $\lceil \lg n\rceil < \lg n + 1 \le 2\lg n$ for all $n \ge 2$

$$
\begin{aligned}
\lg(\lceil\lg  n\rceil !)
&= \Theta(\lceil\lg n\rceil \lg\lceil\lg n\rceil) \\
&= \Theta(\lg n \lg \lg n) \\
&= \omega(\lg n)
\end{aligned}
$$

- Since $\lg(\lceil\lg n\rceil!) \ne O(\lg n)$, $\lceil\lg n\rceil!$ is not polynomially bounded.

- Note that $lg^b n = o(n^a)$ for any constant $a > 0$.

$$
\begin{aligned}
\lg(\lceil\lg\lg n\rceil!)
&= \Theta(\lceil\lg\lg n\rceil\lg\lceil\lg \lg n\rceil) \\
&= \Theta(\lg\lg n\lg \lg \lg n) \\
&= o((\lg \lg n)^2) \\
&= o(\lg n) = O(\lg n)
\end{aligned}
$$

- Since $\lg(elceil\lg \lg n\rceil!) = o(\lg n)$, $\lceil\lg\lg n\rceil!$ is polynomially bounded.

#### 5

- Note that $\lg^*2^n = \lg^*n + 1$

$$
\begin{aligned}
\lim_{n \to \infty}{\lg(\lg^* n) \over \lg^*(\lg n)}
&= \lim_{n \to \infty}{\lg(\lg^* 2^n) \over \lg^*(\lg 2^n)} \\
&= \lim_{n \to \infty}{\lg(1 + \lg^* n) \over \lg^* n}
\end{aligned}
$$

- Substituting $t = \lg^* n$, When $n \to \infty$, $\lg^* n \to \infty$. Thus $t \to \infty$.

$$
\lim_{t \to \infty}{\lg(1 + t) \over t} = 0
$$

- Thus, $\lg^*(\lg n)$ is asymptotically larger than $\lg(\lg^*n)$.

#### 6

- According to the root formula, the solution of $x^2 = x + 1$, $x^2 - x - 1 = 0$ is:

$$
x = {1 \pm \sqrt{1 + 4} \over 2} = {1 \pm \sqrt{5} \over 2}
$$

#### 7

- Base case

    - When $i = 0$, $F_0 = {\phi^0 - \hat{\phi}^0 \over \sqrt{5}} = 0$

    - When $i = 1$, $F_1 = {\phi^1 - \hat{\phi}^1 \over \sqrt{5}} = 1$

- Inductive step

    - Assume $F_k = {\phi^k - \hat{\phi}^k \over \sqrt{5}}$ and $F_{k + 1} = {\phi^{k + 1} - \hat{\phi}^{k + 1} \over \sqrt{g}}$ for a constant $k$.

    $$
    \begin{aligned}
    F_{k + 2}
    &= F_k + F_{k + 1} \\
    &= {\phi^k - \hat{\phi}^k \over \sqrt{5}} + {\phi^{k + 1} - \hat{\phi}^{k + 1} \over \sqrt{5}} \\
    &= {(1 + \phi)\phi^k - (1 + \hat{\phi})\hat{\phi}^k \over \sqrt{5}} \\
    &= {\phi^2\phi^k - \hat{\phi}^2\hat{\phi}^k \over \sqrt{5}} \\
    &= {\phi^{k+2} - \hat{\phi^{k+2}} \over \sqrt{5}}
    \end{aligned}
    $$

    - Thus, the equality holds for some $k+1$.

- Conclusion: Since both the base case and inductive step have been proved as true, by mathematical induction the equality holds for every natural number $n$.

#### 8

- Accorting to symmetry of $\Theta$, $k \ln k = \Theta(n)$ if and only if $n = \Theta(k\ln k)$.

- $f(n) = \Theta(g(n))$ if and only if $\ln f(n) = \Theta(\ln g(n))$. Because if there exist constants $c_1$, $c_2$ and $n_0$ such that $0 \le c_1g(n) \le f(n) \le c_2g(n)$, $0 \le c_1\ln g(n) \le \ln f(n) \le c_2\ln g(n)$, which means $\ln f(n) = \Theta(\ln g(n))$

$$
\ln n = \Theta(\ln(k \ln k)) = \Theta(\ln k + \ln\ln k) = \Theta(\ln k)
$$

$$
{n \over \ln n} = {\Theta(k\ln k) \over \Theta(\ln k)} = \Theta\left({k\ln k \over \ln k}\right) = \Theta(k)
$$

- Therefore $k = \Theta({n \over \ln n})$

## Problems

### 1 Asymptotic behavior of polynomials

#### a

- To prove that $p(d) = O(n^k)$ for $k \ge d$, we have to find positive constants $c$ and $n_0$ such that

$$
0 \le \sum_{i=0}^ka_in^i \le cn^k
$$

- When $c \ge \sum_{i=0}^ka_i$, the above inequality is true. Thus $p(d) = O(n^k)$

#### b

- To prove that $p(d) = \Omega(n^k)$ for $k \ge d$, we have to find positive constants $c$ and $n_0$ such that

$$
0 \le cn^k \le \sum_{i=0}^ka_in^i
$$

- When $c \le \sum_{i=0}^ka_i$, the above inequality is true. Thus $p(d) = \Omega(n^k)$

#### c

- To prove that $p(d) = \Theta(n^k)$ for $k \ge d$, we have to find positive constants $c_1$, $c_2$ and $n_0$ such that

$$
0 \le c_1n^k \le \sum_{i=0}^ka_in^i \le c_2n^k
$$

- When $c_1 \le \sum_{i=0}^ka_i$ and $c_2 \ge \sum_{i=0}^ka_i$, the above inequality is true. Thus $p(d) = \Theta(n^k)$

#### d

- To prove that $p(d) = O(n^k)$ for $k \ge d$, we have to find positive constants $c$ and $n_0$ such that

$$
0 \le \sum_{i=0}^ka_in^i < cn^k
$$

- When $c > \sum_{i=0}^ka_i$, the above inequality is true. Thus $p(d) = o(n^k)$

#### e

- To prove that $p(d) = \Omega(n^k)$ for $k \ge d$, we have to find positive constants $c$ and $n_0$ such that

$$
0 \le cn^k < \sum_{i=0}^ka_in^i
$$

- When $c < \sum_{i=0}^ka_i$, the above inequality is true. Thus $p(d) = \omega(n^k)$

### 2 Relative asymptotic growths

|A|B|$O$|$o$|$\Omega$|$\omega$|$\Theta$|
|-|-|-|-|-|-|-|
|$\lg^kn$|$n^\epsilon$|yes|yes|no|no|no
|$n^k$|$c^n$|yes|yes|no|no|no|
|$\sqrt{n}$|$n^{\sin n}$|no|no|no|no|no|no|
|$2^n$|$2^{n/2}$|no|no|yes|yes|no|
|$n^{\lg c}$|$c^{\lg n}$|yes|no|yes|no|yes|
|$\lg(n!)$|$\lg(n^n)$|yes|yes|no|no|no|

### 3 Ordering by asymptotic growth rates

#### a

$$
\begin{matrix}
2^{2^{n+1}} &|& 2^{2^n} &|& (n + 1)! &|& n!&|& e^n &|& \\
n\cdot 2^n &|& 2^n &|& (3/2)^n &|& (\lg n)^{\lg n} &|& (\lg n)! &|& \\
n^3 &|& n^2 &|& n\lg n, \lg(n!) &|& n &|& 2^{\sqrt{2\lg n}} &|& \\
\lg^2 n &|& \ln n &|& \sqrt{\lg n} &|& \ln\ln n &|& 2^{\lg^* n} &|& \\
\lg^* n, \lg^* (\lg n) &|& \lg(\lg^* n) &|& n^{1/\lg n} 1
\end{matrix}
$$

- $(\lg n)^{\lg n} = n^{\lg \lg n}$

- $n = 2^{\lg n}$

- $(\sqrt{2})^{\lg n} = \sqrt{n}$

- $n^{1 / \lg n} = 2$

#### b

- Ocillate between $2^{2^{n+2}}$ and ${1 \over n}$ because $g_i(n) = o(2^{2^{n+2}})$ and $g_i(n) = \omega({1 \over n})$.

$$
f(n) = \begin{cases}
2^{2^{n+2}} & \text{if } n \text{ is even} \\
{1 \over n} & \text{if } n \text{ is odd} \\
\end{cases}
$$

### 4

#### a

- A counterexample is $f(n) = n$ and $g(n) = n^2$.

#### b

- A counterexample is $f(n) = n$ and $g(n) = n^2$.

#### c

- if $(n) = O(g(n))$, there exist constants $c$ and $n_0$ such that $0 \le f(n) \le cg(n)$ for $n \gen_0$. Hence, $0 \le \lg f(n) \le c\lg g(n)$, which means that $\lg f(n) = O(\lg g(n)$.

#### d

- A counterexample is $f(n) = 2n$ and $g(n) = n$.

#### e

- A counterexample is $f(n) = {1 \over n}$.

#### f

- If $(n) = O(g(n))$, there exist constants $c$ and $n_0$ such that $0 \le f(n) \le cg(n)$. Hence, $0 \le cf(n) \le g(n)$, which means $\Theta(g(n)) = f(n)$.

#### g

- A counterexample is $f(n) = 2^n$

#### h

- Suppose $o(f(n)) = g(n)$. Then there exist constants $c$ and $n_0$ such that $0 \le g(n) < cf(n) for $n \ge n_0$.

- Hence, $0 \le c_1f(n) \le f(n) + g(n) \le c_2f(n)$ for $c_1 = 1$ and $c_2 = 1 + c$, which means $f(n) + o(f(n)) = \Theta(f(n))$.

### 5

#### c

- For any two functions $f(n)$ and $g(n)$, we have $f(n) = \Theta(g(n))$ then $f(n) = O^\prime(g(n))$ and $f(n) = \Omega(g(n))$.

    - If $f(n) = \Theta(g(n))$, there exist positive constants $c_1$, $c_2$ and $n_0$ such that $0 \le c_1g(n) \le f(n) \le c_2g(n)$ for all $n \ge n_0$. Hence $0 \le f(n) \le cg(n)\lg^k(n)$ for any $k$, which means $f(n) = \tilde{O}(g(n))$

- For any two functions $f(n)$ and $g(n)$, we have $f(n) = O^\prime(g(n))$ and $f(n) = \Omega(g(n))$ then $f(n) = \Theta(g(n))$.

    - A counterexample is $f(n) = \lg n$ and $g(n) = 1$. 

#### d

$$
\begin{aligned}
\tilde{\Omega}(g(n)) = \{f(n) :\; &\text{there exist positive constants }c, k, \text{and } n_0 \text{ such that } \\
&0 \le cg(n)\lg^k(n) \le f(n) \text{ for all }n \ge n_0\}
\end{aligned}
$$

$$
\begin{aligned}
\tilde{\Theta}(g(n)) = \{f(n) :\; &\text{there exist positive constants }c_1, c_2, k_1, k_2, \text{and } n_0 \text{ such that } \\
&0 \le c_1g(n)\lg^k_1(n) \le f(n) \le c_2g(n)\lg^{k_2}(n) \text{ for all }n \ge n_0\}
\end{aligned}
$$
