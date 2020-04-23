def find_short1(s):
    words = s.split(' ')
    words.sort(key=len)
    return len(words[0])

def find_short2(s):
    return min(map(len, s.split(' ')))

def find_short3(s): # small prob
    find_short = lambda s: min(len(e) for e in s.split())

print(find_short2('Hello this is mee'))
