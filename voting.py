'''
This script contains helper functions that will be implemented to
count votes in a variety of methods
'''

# Part 1.1
def readBallot(filename):
    ''' Takes as input a path to a csv file and returns a list
    of lists of strings
    >>> len(readBallot('data/simple.csv'))
    4
    >>> readBallot('data/characters.csv')[2][2]
    'Harry Potter'
    >>> readBallot('data/icecream.csv')[10][3]
    'Double Fudge Brownie'
    '''
    fileList = []
    with open(filename) as list:
        for item in list:
            fileList.append(item.strip().split(',')) #.strip and .split methods
            #format the csv so they can be used easier later
    return fileList

# Part 1.2
def firstChoiceVotes(ballots):
    ''' Takes as input a list of lists of strings, then creates
    and returns a new list of strings containing only the zeroith
    index of each internal list.

    >>> firstChoiceVotes(readBallot('data/simple.csv'))
    ['Aamir', 'Beth', 'Chris', 'Aamir']
    >>> firstChoiceVotes([['Abe', 'Betsy'], ['Eve'], ['Fred', 'Gina'], []])
    ['Abe', 'Eve', 'Fred']
    '''
    firstChoiceList = [choice[0] for choice in ballots if len(choice) > 0]
    #len function eliminates empty strings/lists
    return firstChoiceList

# Part 1.3
def mostVotes(votes):
    ''' Takes as input a list of strings of votes and returns a list of
    strings of voting choices that appear the most number of times
    in the original list of strings of votes.

    >>> mostVotes(['Aamir', 'Beth', 'Chris', 'Aamir'])
    ['Aamir']
    >>> mostVotes(firstChoiceVotes(readBallot('data/characters.csv')))
    ['Scarlett OHara', 'Samwise Gamgee']
    >>> mostVotes(['Greta', 'Greta', 'Carter', 'Charlie', 'Carter', 'Greta', 'Charlie', 'Charlie', 'Greta'])
    ['Greta']
    '''
    result = []
    max_so_far = 0
    for choice in votes:
        count = votes.count(choice)
        if count > max_so_far:
            max_so_far = count #Redefines count
            result = [choice]
        elif choice not in result and count == max_so_far:
            result.append(choice)
    return result

# Part 1.5
def candidates(ballots):
    ''' Takes as input a list of list of strings, then creates
    and returns a new list of strings containing each unique string
    in the order that they appear.

    >>> candidates(readBallot('data/icecream.csv'))
    ['Double Fudge Brownie', 'Peanut Butter Swirl', 'Purple Cow', 'Mint Chocolate Chip']
    >>> candidates([['Carter', 'Charlie'], ['Greta'], ['Greta', 'Charlie', 'Carter'], []])
    ['Carter', 'Charlie', 'Greta']
    '''
    result = []
    for item in ballots:
        for cand in item: #Goes into an internal list
            if cand not in result:
                result.append(cand)
    return result

# Part 2.1
def leastVotes(votes, candidates):
    ''' Takes as input a list of strings of votes and candidates, and returns a list
    of the names appearing the least number of times in the list votes, as well as
    takes into account if a candidate does not appear at all in the list votes.

    >>> leastVotes(['Fries', 'Fries', 'Popcorn'], ['Popcorn', 'Chips', 'Fries'])
    ['Chips']
    >>> leastVotes(['Greta', 'Carter', 'Carter'], ['Greta', 'Carter', 'Charlie'])
    ['Charlie']
    '''
    result = []
    noVotes = [] #Takes into consideration a candidate that got no votes
    min_so_far = 10000 #Sets the min high so there is no amount of votes higher
    for person in candidates:
        if person not in votes:
            noVotes.append(person)
        else:
            for choice in votes:
                count = votes.count(choice)
                if count < min_so_far:
                    min_so_far = count
                    result = [choice]
                elif choice not in result and count == min_so_far:
                    result.append(choice)
    if noVotes != []:
        result = noVotes #Replaces result if there is a candidate with no votes
    return result


# Part 2.2
def majority(votes):
    ''' Takes as input a list of stings votes, and returns the candidate that represents
    over half of the total votes. If there is no candidate that gets over half of the
    votes, the function returns an empty string.

    >>> majority(['Charlie', 'Charlie', 'Charlie', 'Greta', 'Hadassah', 'Carter', 'Charlie', 'Charlie', 'Hadassah'])
    'Charlie'
    >>> majority(['Charlie', 'Carter', 'Charlie', 'Greta', 'Hadassah'])
    ''
    '''
    n = len(votes)
    mostVote = mostVotes(votes)
    majorityList = [person for person in mostVote if votes.count(person) > n // 2]
    result = ''.join(majorityList)
    return result

# Part 2.3
def eliminateCandidates(candidates, ballots):
    ''' Takes as input a list of strings of a candidate or candidates and a list of
    lists of ballots representing a voter's list of choices. The function eliminates
    every instance of the candidate from the ballot list and returns a new list
    without that candidate.

    >>> eliminateCandidates(['Purple Cow'], readBallot('data/icecream.csv'))[0]
    ['Double Fudge Brownie', 'Peanut Butter Swirl', 'Mint Chocolate Chip']
    >>> eliminateCandidates(['Hadassah'], [['Hadassah', 'Greta'], ['Greta', 'Carter'], ['Charlie', 'Hadassah']])
    [['Greta'], ['Greta', 'Carter'], ['Charlie']]
    '''
    result = []
    for preferenceList in ballots: #for loop used so the list comprehension will only be
    #applied to the inner lists
        newList = [person for person in preferenceList if person not in candidates]
        result += [newList]
    return result


if __name__ == '__main__':
    # this allows us to run the doctests included in the functions above
    # when the file is run as a script
    from doctest import *
    testmod()
