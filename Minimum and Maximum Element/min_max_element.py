#1
def min_max(lst):
  return [min(lst), max(lst)]

#2
def mm2(lst):
    min_max = lambda l: [min(l), max(l)]

#4
def min_max3(lst):
  min, max = lst[0], lst[0]

  for x in lst:
    if x > max:
      max = x
    elif x < min:
      min = x

  return [min, max]

#4
def min_max4(lst):
    lis=[]
    lst.sort()
    lis.append(lst[0])
    lis.append(lst[-1])
    return lis

print(min_max4([1,3,5,7]))
