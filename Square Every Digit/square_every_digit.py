# 1
def sq(num):
    z = ''.join(str(int(i)**2) for i in str(num))
    return int(z)

# 2


def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)
