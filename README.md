# NTFuncs

Tags：OI（信息学竞赛）、数论。

这个 Repo 名字暂定为 NTFuncs，之后如果加了更多功能可能还会改。

NTFuncs 是指 Number Theoretic Functions。

```python
# 使用例

from NTFuncs import *

print(prime_factors(40)) # 对 40 分解质因数
print(qpow(5, 3)) # 快速幂求 5 的 3 次方

print("================================================")

mu.test(20) # 输出莫比乌斯函数的前 20 项

print("================================================")

# 判断两个函数是否相等
print(phi * constant == Id(1))
print(constant.inv() == mu)
print(dot_product(mu, mu).inv() == liouville_lambda)
print(Id(0) == Id(1))

print("================================================")

# 自己定义一个数论函数
f = ArithmeticFunction(lambda n: n*2)
f.test(20)
```

## 内置数论函数

- `epsilon`：$\varepsilon(x) = [x = 1]$。
- `constant`：$1(x) = 1$。
- `mu`：$\mu(x)$ 为莫比乌斯函数（[A008683](https://oeis.org/A008683)）。
- `phi`：$\varphi(x)$ 为欧拉函数（[A000010](https://oeis.org/A000010)）。
- `liouville_lambda`：$\lambda(x)$ 为刘维尔函数（[A008836](https://oeis.org/A008836)）。
  - 为什么不用 `lambda` 这个名字：`lambda` 是 Python 关键字。
- `Id(k)`：$\text{Id}_k(x) = x^k$。
- `Sigma(k)`：$\sigma_k(x) = \sum\limits_{d|x} x^k$。
- `omega`：$\omega(x)$ 为 $x$ 的不同质因子个数（[A001221](https://oeis.org/A001221)）。
- `big_omega`：$\Omega(x)$ 为 $x$ 的质因子个数（可重复）（[A001222](https://oeis.org/A001222)）。
- `sum_of_pow1`：$f(n) = \sum\limits_{i=1}^n i$。
- `sum_of_pow2`：$f(n) = \sum\limits_{i=1}^n i^2$。
- `sum_of_pow3`：$f(n) = \sum\limits_{i=1}^n i^3$。

## 关于数论函数的操作

- `+` 运算符返回两个函数的和。
- `-` 运算符返回两个函数的差。
- `*` 运算符返回两个函数的狄利克雷卷积。
- `==` 运算符返回两个函数是否相等。
  - 请注意这是**随机化**实现的，所以**不保证正确性**。
  - 运算时间较长，可能有几秒钟。
- `inv` 方法返回该数论函数的狄利克雷逆元。
- `test(n)` 方法会打印该数论函数的前 $n$ 项。
- `dot_product` 函数返回两个数论函数的点积。
- `composition` 函数返回两个数论函数的复合。
- `partial_sum` 函数返回一个数论函数的前缀和函数。

## 有用的函数

- `factors`：返回一个数的所有因数（未排序）。
- `prime_factors`：对一个数做质因数分解。
  - 格式：例如 `prime_factors(40)` 返回 `[[2, 3], [5, 1]]`。
- `qpow`：快速幂。