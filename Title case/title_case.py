def title_case(title, minor_words = ''):
    new_title = []
    new_minor_words = [word.lower() for word in minor_words.split(' ')]

    if not len(title):
        return title

    for index, word in enumerate(title.split(' ')):
        if index == 0:
            new_title.append(word.title())
            continue

        if word.lower() in new_minor_words:
            new_title.append(word.lower())
            continue

        new_title.append(word.title())

    return ' '.join(new_title)

#2
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

#3
def title_case(title, minor_words=''):
    return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))



print(title_case('a clash of KINGS', 'a an the of'))
