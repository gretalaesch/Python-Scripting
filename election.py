# Implements different voting algorithims

# import functions from voting module
from voting import *

# Part 1.4
def plurality(ballots):
    '''Takes as input ballot data as a list of lists of strings, and
    returns a list of strings of names of candidates who get the most votes.
    >>> plurality(readBallot('data/simple.csv'))
    ['Aamir']
    >>> plurality(readBallot('data/example.csv'))
    ['Ava']
    >>> plurality(readBallot('data/characters.csv'))
    ['Scarlett OHara', 'Samwise Gamgee']
    '''
    winners = mostVotes(firstChoiceVotes(ballots)) #Calls on two helper functions
    return winners


# Part 1.6

def bordaScore(item, ballots):
    '''Takes as input ballot data as a list of lists of strings,
    and assigns an interger score for the item
    >>> bordaScore('Ava',readBallot('data/example.csv'))
    37
    >>> bordaScore('Bob',readBallot('data/example.csv'))
    42
    '''
    votes = 0
    for ballot in ballots:
        if item in ballot:
            score = len(ballot) - ballot.index(item) #Gets the position as an
            #interger
            votes += score
    return votes

def borda(ballots):
    '''Takes as input ballot data as list of lists of strings, and
    returns a list of strings of the names of candidates with the
    maximum borda score.
    >>> borda(readBallot('data/simple.csv'))
    ['Aamir']
    >>> borda(readBallot('data/example.csv'))
    ['Cid']
    >>> borda(readBallot('data/characters.csv'))
    ['Harry Potter']
    '''
    result = []
    max_so_far = 0
    for ballot in candidates(ballots):
            count = bordaScore(ballot, ballots)
            if count > max_so_far:
                result = [ballot]
                max_so_far = count
            elif ballot not in result and count == max_so_far:
                result.append(ballot)
    return result


# Part 2.4
def rankedChoice(ballots):
    '''Takes as input ballot data as list of lists of strings, and
    returns the winner of the election based on ranked-choice
    voting as a list of strings of names.

    >>> rankedChoice(readBallot('data/simple.csv'))
    ['Aamir']
    >>> rankedChoice(readBallot('data/example.csv'))
    ['Bob']
    >>> rankedChoice(readBallot('data/characters.csv'))
    ['Scarlett OHara']
    >>> rankedChoice([['Abe', 'Betsy', 'Carmen'], ['Betsy', 'Abe', 'Carmen'], ['Carmen', 'Abe', 'Betsy']])
    ['Abe', 'Betsy', 'Carmen']
    >>> rankedChoice([['Sierra', 'Tao', 'Una'], ['Sierra', 'Tao', 'Una'], ['Tao', 'Sierra', 'Una'], ['Tao', 'Sierra', 'Una']])
    ['Sierra', 'Tao']
    '''
    while True:
        firstVotes = firstChoiceVotes(ballots)
        if majority(firstVotes) != '':
            return [majority(firstVotes)]
        if len(mostVotes(firstVotes)) == len(candidates(ballots)):
            return [candidates(firstVotes)]
        ballots = eliminateCandidates(leastVotes(firstVotes, candidates(ballots)), ballots)


# Part 2.5
def condorcet(ballots):
    '''EXTRA CREDIT: Takes as input ballot data as list of
    lists of strings, and returns the winner of the election
    as a string (or empty string if there is no winner).
    '''
    pass

if __name__ == '__main__':
    from doctest import *
    testmod()

    # Read in our ice cream ballots and run our election algorithms for Part 1.
    print('Ice-cream flavor class election results:')
    print('Plurality winner:', ", ".join(plurality(readBallot('data/icecream.csv'))))
    print('Borda winner:', ", ".join(borda(readBallot('data/icecream.csv'))))
    print('Ranked-choice winner:', ", ".join(rankedChoice(readBallot('data/icecream.csv'))))

    # # Uncomment the following line if you complete the extra credit
    # print('Condorcet winner:', condorcet(readBallot('data/icecream.csv')))
