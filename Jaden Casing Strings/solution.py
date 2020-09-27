def toJadenCase(string):
    return ' '.join(word.capitalize() for word in string.split())


print(toJadenCase('Hi i am an apple'))