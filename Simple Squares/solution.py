def solve1(n):
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0 and n ** 0.5 != i:
            if (i + n // i) % 2 == 0:
                return ((n // i - i) // 2) ** 2
    return -1


def solve2(n):
    arr = []
    for n1 in range(1, int(n ** 0.5) + 1):
        if n % n1 != 0:
            continue
        n2 = n // n1
        if n1 == n2 or (n1 + n2) % 2:
            continue
        a = (n1 + n2) // 2
        b = (n2 - n1) // 2
        if a ** 2 - b ** 2 == n:
            arr.append(b ** 2)
    return min(arr, default = -1)   


def solve3(n):
    for i in range(int(n**0.5), 0, -1):
        x = n - i**2
        if x > 0 and x % (2*i) == 0:
            return ((n - i ** 2) // (2 * i)) ** 2
    return -1

print(solve3(32))

    