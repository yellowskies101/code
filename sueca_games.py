import sueca_tricks #  import previous files 

# 3.4 - GAMES

# the winner of the last trick is the first one to go in the next one
#so you have to increment the starting player by 1


# return value must be identical for codegrade to work

class CardAlreadyPlayed(Exception):
    pass

class DealerDoesNotHoldTrumpCard(Exception):
    pass

class IllegalCardPlayed(Exception):
    pass

class Game: 

    # required instructor
    def __init__(self, ):
    

    def gameTrump(self): # returns game trump's card, an instance of class Card above
    
    def score(self): # returns a pair with the points won by each pair in the current game
    
    
    def playTrick(self, t):

    raise CardAlreadyPlayed 
    # trick contains a card played in a previous round of the game

    raise DealerDoesNotHoldTrumpCard 
    # dealer did not actually hold game's trump card

    raise IllegalCardPlayed 
    # card played in some round is illegal with respect to the lead suit 

    def cardsOf(self,p): 
    # returns list of cards ( instances of class Card above) held by the player p ( a number from 1 to 4) in the current game
        raise ValueError # given player number is invalid 

    def gameTricks(self): 
    # returns a list with the tricks ( instances of class Trick above ) played in the game