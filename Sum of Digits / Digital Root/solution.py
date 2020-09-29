def digital_root1(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root

def digital_root2(n):
    return n if n < 10 else digital_root2(sum([int(c) for c in str(n)]))

print(digital_root2(518))
#Solution -> 5