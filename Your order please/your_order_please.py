# 1
'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
'''
import operator
def order(sentence):
    array = sentence.split()

    toReturn = ""

    new_dict = {"1":"NONE", "2":"NONE", "3":"NONE", "4":"NONE", "5":"NONE", "6":"NONE", "7":"NONE", "8":"NONE", "9":"NONE", }

    for word in array:
        for char in word:
            if(char.isdigit() and int(char) <= 9):
                new_dict[char] = word

    sorted_dict = sorted(new_dict.items())

    for s in sorted_dict:

        if(s[1] != "NONE"):
            toReturn = toReturn + s[1]+" "

    toReturn = toReturn[:-1]
    return toReturn

# 2


def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))




def order(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))
'''


def order(sentence):
    if not sentence:
        return ""
    result = []  # the list that will eventually become our sentence

    split_up = sentence.split()  # the original sentence turned into a list, splits sentence into list of words
    # list of words

    for i in range(1, 10): # 1-9 inside each word
        for item in split_up:
            if str(i) in item: # if number in word, converts number to string
                # adds them in numerical order since it cycles through i first
                result.append(item)

    return " ".join(result)
    # join() method takes all items in an iterable and joins them into one string.


print(order('is Thi1s T4est 3a'))
