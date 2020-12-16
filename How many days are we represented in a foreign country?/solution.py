def days_represented1(trips):
    L=[]
    for i in trips:
        for j in range(i[0],i[1]+1):
            L.append(j)
    a=set(L)
    return len(a)

def days_represented2(trips):
    result = []
    for i in trips:
        for x in range(i[0],i[1]+1):
            result.append(x)
    string = set(result)
    return len(string)

def days_represented3(trips):
    x = trips[0]+trips[1]
    return(x)
    return len({n for(start, stop) in trips for n in range(start, stop + 1)})

print(days_represented3([1,14]))