# 3.2 - CARDS

import sueca_suits_ranks # import previous files 

from sueca_suits_ranks import rank_points, rank_higher_than, valid_rank, valid_suit

class CardInvalid(Exception): # create custom exception using class 
    pass

class Card:
    # required constructor - (__init__) initialize objects member during creation time
    # executed when class is initiated 
    # self - refers to current instance
    # method takes two additional arguments : ranks / suits  ( intial values for instance attributes)
    
    def __init__(self, ranks, suits):
        # Initialization of the variables
        self.ranks = ranks
        self.suits = suits
        self = ranks, suits

    def points(self):
        cardscore=[]
        for i in self.ranks: 
            # call previous ranking point function to return points
            cardscore.append(sueca_suits_ranks.rank_points(i)) # what to put in here?
        return sum(cardscore)
    
    # AttributeError: 'Card' object has no attribute 'show'
    def show(self):
        return self.ranks + self.suits  # gives string representation of card 


    def higher_than(self,other,s,t):
        # s = leadsuit
        # t = trump 

        #can only concatenate str (not "Card") to str



        self = Card(self.ranks, self.suits)

        # ALL POSSIBLE OUTCOMES: 
        # NOTHING BEATS TRUMP --> RETURN FALSE
        
         # self card == trump, other card != trump
        if self == t and other != t:
            return False

         # self card != trump, other card = trump
        elif self != t and other == t:
            return False

        # self card == lead suit, other card != lead suit
        elif self == s and other != s:
            return False

        # self card != lead suit, other card == lead suit
        elif self != s and other == s:
            return False

        # both self/other have trump 
        elif self == t and other == t:
            sueca_suits_ranks.rank_higher_than(self, other)
            return True

        # both self/other have lead suit 
        elif self == s and other == s:
            sueca_suits_ranks.rank_higher_than(self, other)
            return True

        # both self / other card aren't trump
        elif self != t and other !=t:
            sueca_suits_ranks.rank_higher_than(self, other)
            return True




"""        # when the self card and the other card have the same suit
        if self[1] == other[1]: 
            sueca_suits_ranks.rank_higher_than(self, other, s, t)
        # when the self card and the other card have the same trump
        elif self[0] == [0]: 
            sueca_suits_ranks.rank_higher_than(self, other, s, t)
        else: # or neither are the trump
        
        # card instance responding to self is higher than card instance responding to other
        if s > t: 
        # call previous higher than function 
            return True  # return boolean value True or False
        else: # lead suit isn't greater than trump suit
            return False  # return boolean value true or false"""



# not a function of class card
def parseCard(cs):
    # check that the given string is a valid representation of a sueca card
    if len(cs) != 2:  # string must have exactly two characters
        raise CardInvalid("Given string (" + cs + ") is not a valid representation of seuca card")
    elif not sueca_suits_ranks.valid_rank(cs[0]):  # first character must be a valid rank
        raise CardInvalid("Given string (" + cs + ") is not a valid representation of seuca card")
    elif not sueca_suits_ranks.valid_suit(cs[1]):  # second character must be a valid suit
        raise CardInvalid("Given string (" + cs + ") is not a valid representation of seuca card")

    # parse cs string
    ranks = cs[0]
    suits = cs[1]
    return Card(ranks, suits)  # card is only created if it is a valid representation


"""
    cardList = list(cs.split())
    if not len(cardList) == 2:
        raise CardInvalid ("Given string (" + cs + ") is not a valid representation of seuca card")
    else:
        return cardList 

"""