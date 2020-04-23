def getCount(inputStr):
    num_vowels = 0
    vowel = set("a e i ou")
    for alphabet in vowel:
        if alphabet in vowel:
            num_vowels += 1
    return num_vowels

 # Second method


def getCount1(inputStr):

    num_vowels = 0
   # Creating a set of vowels
    s = "aeiou"
    v = set(s)

   # Loop to traverse the alphabet
   # in the given string
    for alpha in inputStr:
        # If alphabet is present
        # in set vowel
        if alpha in v:
            num_vowels += 1
    return(num_vowels)


print(getCount1("abracadabra"))
