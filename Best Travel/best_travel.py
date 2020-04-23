from itertools import combinations
def choose_best_sum1(max_miles, max_towns, lst):
    highest = 0
    for a in combinations(lst, max_towns):
        total_distance = sum(a)
        if max_miles >= total_distance > highest:
            highest = total_distance
    return highest or None

def recurse(sum, ls, level):
  if level == 1:
        return [(x+sum) for x in ls]
  ary = list(ls)
  totals = []
  for x in ls:
    ary.remove(x)
    if len(ary) >= level - 1:
      totals += recurse(sum+x, ary, level - 1)
  return totals

def choose_best_sum2(t, k, ls):
    if len(ls) < k:
      return None
    totals = recurse(0, ls, k)
    sum = 0
    for x in totals:
      if x > sum and x <= t:
        sum = x
    if sum == 0:
      return None
    return sum


def choose_best_sum3(t, k, ls):
    import itertools
    values = list(itertools.combinations(ls,k))
    distances = [sum(row) for row in values]
    
    for distance in reversed(sorted(distances)):
        if distance <= t:
            return distance

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]    
print(choose_best_sum3(230, 4, xs), 229)
