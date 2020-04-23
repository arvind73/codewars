from collections import Counter
def find_it1(seq):
    counts = list(Counter(seq).items())
    for x in counts:
        if x[1] % 2 != 0:
            return x[0]
    return None


from functools import reduce
def find_it2(seq):
    return reduce(lambda x, y: x^y, seq)


def find_it3(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

import operator

def find_it4(xs):
    return reduce(operator.xor, xs)


def find_it5(seq):
    result = 0
    for x in seq:
        result ^= x
    return result


print(find_it2([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
