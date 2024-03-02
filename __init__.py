import random


def factors(n: int):
    assert n > 0
    ret = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            if i * i != n:
                ret.append(n // i)
        i += 1
    return ret


def prime_factors(n):
    ret = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            ret.append([i, cnt])
    if n > 1:
        ret.append([n, 1])
    return ret


def qpow(a: int, b: int):
    if b < 0:
        raise ArithmeticError("The exponent must be nonnegative")
    ret = 1
    while b:
        if b & 1:
            ret = ret * a
        a = a * a
        b >>= 1
    return ret


class ArithmeticFunction:
    def set_function(self, func):
        self.func = func

    def __init__(self, func):
        self.set_function(func)

    def __call__(self, n: int):
        assert n > 0
        return self.func(n)

    def __add__(self, other):
        return ArithmeticFunction(lambda n: self(n) + other(n))

    def __mul__(self, other):
        def f(n: int):
            ret = 0
            for d in factors(n):
                ret += self(d) * other(n // d)
            return ret
        return ArithmeticFunction(f)

    def inv(self):
        def f(n: int):
            if self(1) == 0:
                raise ArithmeticError("f(1) must not be zero")
            if n == 1:
                return 1 / self(1)
            else:
                s = 0
                for d in factors(n):
                    if d != 1:
                        s += self(d) * f(n // d)
                return -s / self(1)
        return ArithmeticFunction(f)

    def test(self, n: int, end=", "):
        for i in range(1, n+1):
            if i == n:
                print(self(i))
            else:
                print(self(i), end=end)

    def __eq__(self, other):  # random
        lim = 1000000
        cnt = 100
        eps = 1e-6
        for _ in range(cnt):
            n = random.randint(1, lim)
            if abs(self(n) - other(n)) > eps:
                return False
        return True


def dot_product(f, g):
    return ArithmeticFunction(lambda n: f(n) * g(n))


class MultiplicativeFunction(ArithmeticFunction):
    def set_fpk(self, fpk):
        self.fpk = fpk

        def f(n: int):
            ret = 1
            for p, k in prime_factors(n):
                ret *= fpk(p, k)
            return ret
        self.set_function(f)

    def __init__(self, fpk):
        self.set_fpk(fpk)


epsilon = MultiplicativeFunction(lambda p, k: int(k == 0))
constant = MultiplicativeFunction(lambda p, k: 1)
mu = MultiplicativeFunction(lambda p, k: 1 if k == 0 else -1 if k == 1 else 0)
phi = MultiplicativeFunction(lambda p, k: qpow(p, k) - qpow(p, k-1))


class Id(MultiplicativeFunction):
    def __init__(self, e: int):
        MultiplicativeFunction.__init__(self, lambda p, k: qpow(p, k * e))


class Sigma(MultiplicativeFunction):
    def __init__(self, e: int):
        if e == 0:
            MultiplicativeFunction.__init__(self, lambda p, k: k+1)
        else:
            MultiplicativeFunction.__init__(self, lambda p, k: (
                qpow(p, (k + 1) * e) - 1) // (qpow(p, e) - 1))


class AdditiveFunction(ArithmeticFunction):
    def set_fpk(self, fpk):
        self.fpk = fpk

        def f(n: int):
            ret = 0
            for p, k in prime_factors(n):
                ret += fpk(p, k)
            return ret
        self.set_function(f)

    def __init__(self, fpk):
        self.set_fpk(fpk)


omega = AdditiveFunction(lambda p, k: 1)
bigomega = AdditiveFunction(lambda p, k: k)
