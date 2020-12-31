def print_nums(*args):
    return '\n'.join(['0'*(len(str(max(args)))-len(str(x)))+str(x) for x in args])

def print_nums(*x):
    return '\n'.join(str(0)*(len(str(max(list(x))))-len(str(i)))+str(i) for i in list(x))

print(print_nums([1,20,406]))