import sueca_cards

# import previous files
# when you import module it runs the module 
# any variables assigned within that module exist in the current modules namespace 

import os # allows us to operate on underlying operating system tasks 

from sueca_cards import parseCard

# 3.3 - TRICKS

class Trick:
    def __init__ (self,ts):
        self.trickstring = ts
        self.tricklist = list(ts.split())
    
    def points(self):
        trickscore=[]
        for i in self.tricklist:
            trickscore.append(sueca_cards.Card(i).points())
        return sum(trickscore)
    
    def trick_winner(self, t):
        trickleader = self.tricklist[0]
        s = self.tricklist[0][1]
        for i in self.tricklist:
            if sueca_cards.Card(i).higher_than(sueca_cards.Card(trickleader), s, t):
                trickleader = i
        return self.tricklist.index(trickleader) + 1

    def show(self):
        return self.trickstring

def parseTrick(ts):
    trickList = list(ts.split())
    if not len(trickList) == 4:
        raise ValueError("Trick", ts, " is invalid")
    else:
        for x in trickList:
            sueca_cards.parseCard(x)
        return Trick(ts)
    
def parseGameFile(fname):
    pass




#class Trick : 

# required constuctor 
   # def __init__ (self, trick):
       # self.trick = trick 

   # def points(self):
        #points = 0 
        # for loop, iterate through each card played
       # for i in range(points):  
            # create a variable to obtain points for the card played
            # call rank_points previous function from sueca suits ranks() 
           # points = sueca_suits_ranks.rank_points()
            #how many points the four cards add up to ( total )
           # total_points = points * 4
            # len 4 == 

    # def trick_winner(t):
    # yields winning player 

    #def show(self): #gives tricks string representation


# takes a trick represented as a string and returns an object of class Trick
#def parseTrick(ts):

 #   ts = "AH DF KS QS".split()
    # split on spaces 
  #  print(ts.str.split())

    # for loop defines card 
   # for card in ts:
      #  card = "KS"
    #    rank, suit = card
       # print(rank)
        #print(suit)
        # construct from class Card
        #new_card = sueca_cards.Card(rank, suit)

    #for card in new_card:
     #   list = []
      #  list.append(new_card)
    # return a Trick object
    # calling trick __init__
    #parseTrick needs to turn the given string into a list of Cards
    # parse single string
       # return(Trick(card))



        try: 
            print(parseCard)
        #except sueca_cards.(CardInvalid): 
            raise ValueError("A trick string must comprise four cards only; the given trick is: ")
        return 
        #else: 
            #raise ValueError("")
    


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#  join prepends working directory
# dirname file - absolute path
# getcwd() - dropped 
# real path solves - symbolic
fname = open(os.path.join(__location__, 'game1.sueca'))
def parseGameFile(fname):
  print(fname.read())
parseGameFile(fname)
