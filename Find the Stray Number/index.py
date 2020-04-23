# 1
from collections import Counter
# Counter is faster than count()


def stray1(arr):
    return (list(Counter(arr).most_common(2)[1]))[0]

# 2


def stray2(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

# 3


def stray3(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i


print(stray3([1, 1, 1, 1, 2]))
