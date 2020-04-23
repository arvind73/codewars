#1
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum

#2
def series_sum(n):
    return '%.2f' % sum(1.0 / i for i in xrange(1, 3 * n, 3))

#3
def series_sum(n):
    seriesSum = 0.0
    for x in range(n):
        seriesSum += 1 / (1 + x * 3)
    return '%.2f' % seriesSum
