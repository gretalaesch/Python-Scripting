"""Start by solving spelling-bee puzzle B1.

   Next, you may solve either the NPR puzzle P1 or P2.  You must solve at
   least one of these! If you want extra practice, try solving both.

   Extra Credit: If you would like a challenge, check out problems B2 and P3.
   These are not required! A small amount of extra credit will be given if you
   solve one or both of them.
"""

from wordTools import * #Imports all modules from wordTools.py

def b1():
    """How many lowercase 7-letter isograms are in words/dict.txt?

    This function returns an int representing the number of 7-letter isograms
    that are the answer.
    """
    count = 0 #Initializes counter
    sevLetter = sized(7, readWords('words/dict.txt')) #Makes a new list with all the seven-letter words in words/dict.txt
    for word in sevLetter:
        if isIsogram(word) and word.islower(): #Calls isIsogram from wordTools.py and only includes words with all lower letters
            count += 1
    return int(count)

def p1():
    """Name part of the human body in six letters. Add an 'r' and rearrange
    the result to name another part of the body in seven letters.

    This function returns a string representing the concatenation of the
    two body parts (eg, 'part1 part2' or 'part2 part1').
    """
    result = '' #Initializes the accumulation variable as a string
    sixLetters = sized(6, readWords('words/bodyParts.txt')) #Makes a new list with all the six-letter words in words/bodyParts.txt
    otherWords = sized(7, readWords('words/bodyParts.txt')) #Makes a new list with all the seven-letter words in words/bodyParts.txt
    for words in sixLetters:
        cWord = canon(words + 'r') #Calls canon from wordTools.py which puts the word in alphabetical order, so cWord can be compared to the new word
        for phrase in otherWords:
            if canon(phrase) == cWord: #Looks for the word in otherWords that fufills the request
                result += words + " " + phrase #Concatinates the two words into a string
    return(result)

def p2():
    """Think of a major city in France whose name is an anagram of a major city
    in Italy.

    This function returns a string representing the concatenation of
    the cities (eg, 'frenchCity italianCity' or 'italianCity frenchCity').
    """
    result = '' #Initializes the accumulation variable as a string
    frenchCity = readWords('words/frenchCities.txt') #Assigns frenchCity to be the list frenchCities.txt
    italianCity = readWords('words/italianCities.txt') #Assigns italianCity to be the list italianCities.txt
    for cities1 in frenchCity:
        frenchC = canon(cities1) #Outer loop canonicalizes each word in the frenchCity list
        for cities2 in italianCity:
            if frenchC == canon(cities2): #Checks relation between each word in frenchC and a canonical version of each word in italianCity
                result += cities1 + " " + cities2 #Concatinates the two words into a string
    return(result)

def b2():
    """Extra credit: Suppose you have a seven letter hive, 'mixcent'. How many
    4-letter lowercase words in words/dict.txt (1) include 'm' and (2) are
    spelled only using (possibly repeated) letters from the hive string?

    This function returns an int representing the number of words.
    """
    hiveWords = [] #Initializes the accumulation variable as a list
    hive = 'mixcent'
    words4 = sized(4, readWords('words/dict.txt')) #Calls sized() from wordTools, and creates a new list with all 4 letter strings in words/dict.txt
    for word in words4:
        if 'm' in word and word.islower():
                if word[0] in hive:
                    if word[1] in hive:
                        if word[2] in hive:
                            if word[3] in hive: #Checks to see if each letter in hive is in a word in the word4 list
                                hiveWords += [word] #Concatinates the words into a list
    return len(hiveWords) #Returns the length of the list hiveWords

def p3():
    """Extra credit: Think of a disease in five letters. Shift each letter three
    spaces later in the alphabet---for example, 'a' would become 'd', 'b' would
    become 'e', etc. The result will be a prominent name from the Bible.

    This function returns a string that is a concatenation of the illness and
    the name (eg, 'illness name' or 'name illness').
    """
    pass

if __name__ == '__main__':
    # call puzzle functions
    print("b1(): " + str(b1()))
    print("p1(): " + str(p1()))
    print("p2(): " + str(p2()))
    print("b2(): " + str(b2()))
    print("p3(): " + str(p3()))
