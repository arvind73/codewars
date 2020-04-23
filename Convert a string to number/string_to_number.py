# first
def alphabet_position1(text):
    alphabet = {'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 10,
                'k': 11,
                'l': 12,
                'm': 13,
                'n': 14,
                'o': 15,
                'p': 16,
                'q': 17,
                'r': 18,
                's': 19,
                't': 20,
                'u': 21,
                'v': 22,
                'w': 23,
                'x': 24,
                'y': 25,
                'z': 26, }
    inds = []
    for x in text.lower():
        if x in alphabet:
            inds.append(alphabet[x])
    return ' '.join(([str(x) for x in inds]))
# second


def alphabet_position(text):

    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    l = []

    for i in text:
        if i in upper_alpha:
            index = upper_alpha.index(i) + 1
            l.append(str(index))
        elif i in lower_alpha:
            index = lower_alpha.index(i) + 1
            l.append(str(index))
    return " " .join(l)

# third


def alphabet_position2(text):
    al = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(al.index(l)+1) for l in text if l.isalpha()])
