# Ch1 The Role of Algorithms in Computing

## 1.1 Algorithms

### Exercises

#### 1

- 성적 등수를 결정할 때 sorting을 사용할 수 있다.

- image processing에서 object의 경계를 결정할 때 convex hull을 사용할 수 있다.

#### 2

- memory 사용량

#### 3

- linked-list는 삽입, 삭제에 용이하지만 검색이 어렵다.

#### 4

- shortest-path와 traveling-salesman 모두 최소 비용을 갖는 길을 찾아야하는 문제이지만, shotest-path는 한 지점에서 다른 지점까지의 길에 대한 문제이고, traveling-salesman은 시작지점에서 여러 지점을 거친 후 다시 시작지점으로 돌아가는 길에 대한 문제이다.

#### 5

- sorting은 bast solution이 가능하다.

- traveling-salesman 문제는 NP-complete 문제이기 때문에 approximately best solution이면 충분하다. 

## 1.2 Algorithms as a technology

### Exercises

#### 1

- linux의 process를 보여주는 top command는 사용자가 설정한 값에 따라 process 정보를 정렬해준다. 

#### 2

$$
8n^2 < 64n\log_2n
$$

- $n > 0$

$$
n < 8\log_2n
$$

$$
2^n < n^8
$$

$$
2^n - n^8 < 0
$$

- $2 \le n \le 43$

#### 3

$$
100n^2 < 2^n
$$

$$
100n^2 - 2^n < 0
$$

- $n \ge 15$

### Problems

| |1<br>second|1<br>minute>|1<br>hour|1<br>day|1<br>month|1<br>year|1<br>century|
|-|-|-|-|-|-|-|-|
|$\lg n$|$2^{10^6}$|$2^{6 \times 10^7}$|$2^{3.6 \times 10^9}$|$2^{8.64 \times 10^{10}}$|$2^{2.59 \times 10^{12}}$|$2^{3.15 \times 10^{13}}$|$2^{3.15 \times 10^{15}}$|
|$\sqrt{n}$|$10^{12}$|$3.6 \times 10^{14}$|$1.30 \times 10^{19}$|$7.46 \times 10^{21}$|$6.72 \times 10^{24}$|$9.95 \times 10^{26}$|$9.95 \times 10^{30}$|
|$n$|$10^6$|$6 \times 10^7$|$3.6 \times 10^9$|$8.64 \times 10^{10}$|$2.59 \times 10^{12}$|$3.15 \times 10^{13}$|$3.15 \times 10^{15}$|
|$n\lg n$|$6.27 \times 10^4$|$2.80 \times 10^6$|$1.33 \times 10^8$|$2.75 \times 10^9$|$7.18 \times 10^{10}$|$7.97 \times 10^{11}$|$6.85 \times 10^{13}$|
|$n^2$|$1000$|$7746$|$60000$|$293939$|$1609969$|$5615692$|$56156923$|
|$n^3$|$100$|$391$|$1533$|$4420$|$13737$|$31594$|$146646$|
|$2^n$|$20$|$26$|$32$|$36$|$41$|$45$|$51$|
|$n!$|$9$|$11$|$13$|$14$|$15$|$16$|$18$|
