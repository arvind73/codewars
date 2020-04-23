def stock_list0(listOfArt, listOfCat):
    if len(listOfCat) == 0 or len(listOfCat) == 0:
        return ''
    ans = [int(i) for i in list(str(0)*len(listOfCat))]
    for i in listOfArt:
        i = i.split()
        if i[0][0] in listOfCat:
            ans[listOfCat.index(i[0][0])] += int(i[1])
    if ans.count(0) == len(ans):
        return ''
    ans_arr = []
    i = 0
    while i < len(listOfCat):
        ans_arr.append('(' + listOfCat[i] + ' : ' + str(ans[i]) + ')')
        i += 1
    return ' - '.join(ans_arr)

#2
def stock_list1(listOfArt, listOfCat):
    if listOfArt and listOfCat:
        return " - ".join(['(%s : %d)' % (c, sum([int(i.split(" ")[1]) for i in listOfArt if c==i[0]])) for c in listOfCat])
    else:
        return ""
