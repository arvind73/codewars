def accum(s):
    c = 1
    string = ''
    for letter in s:
        temp = (c * s[c-1])
        temp = temp.capitalize()
        temp = temp + '-' #append hyphen
        string = string + temp   #append mini string to another string
        c+= 1
    string = string[:-1] #remove last hyphen
    return string

print(accum('abcdef'))