def toJadenCase(string):
    return ' '.join(word.capitalize() for word in string.split())


print(toJadenCase('hi nice to meet you'))
