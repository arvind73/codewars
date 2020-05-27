def namelist(names):
    #your code here
    Returnto = ''
    if(len(names) == 1):
        return names[0]['name']
    elif(len(names) == 2):
        Returnto = Returnto + names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for i in range(0, len(names)-1):
            Returnto = Returnto + names[i]['name'] + ", "
        Returnto = Returnto[:-2] + " & " + names[len(names)-1]['name']
    return Returnto

print(namelist('Bart', 'Lisa','Maggie'))