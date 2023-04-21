def get_factors(n: int, sort_flg: bool = False):
    assert n > 0
    ret = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            if i * i != n:
                ret.append(n // i)
        i += 1
    if sort_flg:
        ret.sort()
    return ret


def qpow(a: int, b: int):
    assert b >= 0
    ret = 1
    while b:
        if b & 1:
            ret = ret * a
        a = a * a
        b >>= 1
    return ret


#============================================================================


class ArithmeticFunction:
    def __init__(self, function):
        self.function = function

    def __call__(self, n: int):
        return self.function(n)

    def __add__(self, other):
        def h(n: int):
            assert n > 0
            return self.function(n) + other.function(n)
        return h

    def __mul__(self, other):
        def h(n: int):
            assert n > 0
            ret = 0
            factors = get_factors(n)
            for d in factors:
                ret += self(d) * other(n // d)
            return ret
        return h

    def inv(self, n: int):
        if n == 1:
            return 1 / n
        else:
            return (
                -1 / self(1)
                * sum([self(d) * self.inv(n // d) for d in get_factors(n) if d != 1])
            )


#============================================================================


class IdentityFunction(ArithmeticFunction):
    def f(self, n: int):
        assert n > 0
        return int(n == 1)

    def __init__(self):
        self.function = self.f

    def __repr__(self):
        return "epsilon(x)"


epsilon = IdentityFunction()


#============================================================================


class Sigma0Function(ArithmeticFunction):
    def f(self, n: int):
        assert n > 0
        return len(get_factors(n))

    def __init__(self):
        self.function = self.f

    def __repr__(self):
        return "sigma0(x), or d(x)"


d = Sigma0Function()


#============================================================================


class TotientFunction(ArithmeticFunction):
    def f(self, n: int):
        assert n > 0
        ret = n
        i = 2
        while i * i <= n:
            if n % i == 0:
                ret = ret // i * (i - 1)
                while n % i == 0:
                    n //= i
            i += 1
        if n != 1:
            ret = ret // n * (n - 1)
        return ret

    def __init__(self):
        self.function = self.f

    def __repr__(self):
        return "phi(x)"


phi = TotientFunction()


#============================================================================


class ConstantFunction(ArithmeticFunction):
    def f(self, n: int):
        assert n > 0
        return 1

    def __init__(self):
        self.function = self.f

    def __repr__(self):
        return "1(x)"


one = ConstantFunction()


#============================================================================


class PowerFunction(ArithmeticFunction):
    def f(self, n: int):
        assert n > 0
        return qpow(n, self.k)

    def __init__(self, k: int = 1):
        assert k >= 0
        self.k = k
        self.function = self.f

    def __repr__(self):
        return f"id_k(x), k={self.k}"


Id = PowerFunction()


#============================================================================


class MobiusFunction(ArithmeticFunction):
    def f(self, n: int):
        assert n > 0
        ret = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                n //= i
                ret *= -1
            if n % i == 0:
                return 0
            i += 1
        if n != 1:
            ret *= -1
        return ret


    def __init__(self, k: int = 1):
        assert k >= 0
        self.k = k
        self.function = self.f

    def __repr__(self):
        return "mu(x)"


mu = MobiusFunction()


#============================================================================