'''
Here, every second/even element value gets doubled
'''
def double_every_other1(lst):
    lst[1::2] = [x * 2 for x in lst[1::2]]
    return lst

def double_every_other2(lst):
    return [x * (i % 2 + 1) for i, x in enumerate(lst)]

# print (double_every_other1([1,2,3,4,5,6])) --> [1, 4, 3, 8, 5, 12]
