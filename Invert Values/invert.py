def invert(lst):
	while lst:
		x = lst[::-1]
		return x

lst = [1,2,3,4]
print(invert(lst))