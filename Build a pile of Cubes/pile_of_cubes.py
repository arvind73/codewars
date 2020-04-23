import math as math

def find_nb(m):
    # your code
    my = math.sqrt(m)
    print(m,my)
    if m%(int(my)) != 0:
        return -1
    i=1
    n=0
    while n<=my:
        n+=i
        if n==my:
            return i
        i+=1
    return -1

def findNB(m):
    if 1 ** 3 == m:
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume = volume + n ** 3
            if volume == m:
                return n
            else:
                n = n + 1
                continue
        return -1

def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

def find_nb(m):
    i,sum = 1,1
    while sum < m:
        i+=1
        sum+=i**3
    return i if m==sum else -1


#test.assert_equals(find_nb(24723578342962), -1)
#est.assert_equals(find_nb(4183059834009), 2022)
