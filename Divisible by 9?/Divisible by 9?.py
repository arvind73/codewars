def div_by_9(ns):       #First solution
    return True if int(ns)%9==0 else False

def div_by_9(ns):     #Second solution
    while ns>=0:
        if ns%9==0:
            return True
        return False
    else:
        return False

print(div_by_9(810000))