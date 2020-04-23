#1
def list_squared1(m, n):
    result = []
    for i in range(m, n + 1):
        b = 0
        a = sum(let * let + (i / let) * (i / let) for let in range(1, int(i ** 0.5) + 1) if i % let == 0)
        if (i ** 0.5) % 1 == 0:
            a = a - (i ** 0.5) * (i ** 0.5)
        if (a ** 0.5) % 1 == 0:
            result.append([i, int(a)])
    return result

from math import floor, sqrt, pow

#2
def sum_squared_factors2(n):
    s, res, i = 0, [], 1
    while (i <= floor(sqrt(n))):
        if (n % i == 0):
            s += i * i
            nf = n // i
            if (nf != i):
                s += nf * nf
        i += 1
    if (pow(int(sqrt(s)), 2) == s):
        res.append(n)
        res.append(s)
        return res
    else:
        return None

def list_squared3(m, n):
    res, i = [], m
    while (i <= n):
        r = sum_squared_factors2(i)
        if (r != None):
            res.append(r)
        i += 1
    return res


#3
from itertools import chain
from functools import reduce


def factors(n):
    return set(chain.from_iterable(
        [d, n // d] for d in range(1, int(n**0.5) + 1) if n % d == 0))


def square_factors(n):
    return reduce(lambda s, d: s + d**2, factors(n), 0)


def list_squared5(m, n):
    l = []
    for x in range(m, n + 1):
        s = square_factors(x)
        if (s**0.5).is_integer():
            l.append([x, s])
    return l

#4
def list_squared4(m, n):
    list=[]
    for i in range(m,n+1):
        sum=0
        s_list=[]
        for j in range(1,int(i**.5)+1):
            if i%j==0:
                div=i//j
                sum+=j**2
                if j!=div:
                    sum+=div**2
        sqt=sum**.5
        if int(sqt)==sqt:
            s_list=[i,sum]
            list.append(s_list)
    return list
#Test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
