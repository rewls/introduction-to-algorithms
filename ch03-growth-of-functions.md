# Ch3 Growth of Functions

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
