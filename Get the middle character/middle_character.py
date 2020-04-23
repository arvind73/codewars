def get_middle(s):
    if(len(s) % 2 == 0):  # if even, get middle two letters
        return "" + s[(int(len(s) / 2) - 1)] + s[(int(len(s) / 2))]
    else:
        return s[(int(len(s)/2))]  # inside the index, get middle letter


print(get_middle('america'))
