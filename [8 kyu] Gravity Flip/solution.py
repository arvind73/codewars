def flip1(d, a):
    if d == 'R':
        a.sort()
    else:
        a.sort()
        a.reverse()
    return a


def flip(d, a):
    # Do some magic
    if d == 'R':
        return sorted(a)
    if d == 'L':
        return sorted(a, reverse = True)
    return 'error'

print(flip('L',[1,3,446,543,27]))