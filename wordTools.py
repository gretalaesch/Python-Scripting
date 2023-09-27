"""
This lab contains six functions that manipulates string and lists
for some result.
"""

def letters(phrase):
    """Takes as input a string phrase and returns a string
    that contains just the letters from phrase (in order).

    >>> letters('superb: owl!')
    'superbowl'
    >>> letters('')
    ''
    >>> letters('#@$%')
    ''
    """
    result = ''
    for char in phrase:
        if char.isalpha():  # if char is a letter
            result += char  # concatenate to result
    return result

def canon(word):
    """Takes as input a string word and returns a "canonical" version
    of word: just the letters, in lower case, and in alphabetical order
    (as a string). Supports anagram testing.

    >>> canon('fix me') #Fixed this doctest
    'efimx'
    >>> canon('Mamma Mia!')
    'aaaimmmm'
    >>> canon('iAm')
    'aim'
    >>> canon('a lot')
    'alot'
    """
    word = letters(word)      # drop anything that's not a letter (e.g. spaces)
    lowerWord = word.lower()  # to ensure Carol == carol
    orderedWord = sorted(lowerWord) # ie.  a *list* of letters, in alpha order
    result = ''.join(orderedWord) # converts list of letters to a single string
    return result

def uniques(word):
    """Takes as input string word and return a string consisting of the unique
    characters in word.

    >>> uniques('abracadabra')
    'abrcd'
    >>> uniques('Connecticut')
    'Conectiu'
    >>> uniques('colorado') #added docstrings
    'colrad'
    >>> uniques('banana')
    'ban'
    """
    result = ''
    for char in word:
        if char not in result:
            result += char
    return result

def isIsogram(word):
    """Takes as input a string word and returns True only if the
    characters in word are unique (i.e., there are no repeated characters).

    >>> isIsogram('tagaloog')
    False
    >>> isIsogram('skateboard')
    False
    >>> isIsogram('updog')
    True
    """
    isogram = uniques(word)
    if isogram.lower() == word.lower():
        return True
    else:
        return False

def sized(n, wordList):
    """ Takes as input an integer and list of words and returns a
    concatenated list that has the amount of characters n

    >>> sized(5, ['greta', 'charlie', 'katie'])
    ['greta', 'katie']
    >>> sized(3, ['happy', 'sad', 'mad', 'glad'])
    ['sad', 'mad']
    """
    result = []
    for word in wordList:
        if len(word) == int(n):
            result += [word]
    return result

def readWords(filename):
    """Takes as input the path to a file filename, opens and reads the words
    (one per line) in that file, and returns a list containing those words.

    >>> len(readWords('words/firstNames.txt'))
    5166
    >>> readWords('words/bodyparts.txt')[14]
    'belly button'
    >>> sized(8, readWords('words/italianCities.txt'))
    ['Cagliari', 'Florence', 'Siracusa']
    """
    results = []
    with open(filename) as wordFile:
        for line in wordFile:
            word = line.strip()   # removes any spaces or specified characters at the start and end of a string
            results.append(word)  # The append() method in python adds a single item to the existing list
    return results

if __name__ == '__main__':
    # the following code tests the tests in the docstrings ('doctests').
    # as you add tests, re-run this as a script to test your work
    from doctest import testmod  # this import is necessary when testing
    testmod()                    # test this module, according to the doctests
