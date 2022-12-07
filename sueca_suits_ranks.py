# 3.1 - SUITS AND RANKS
    
suits = {
    "H" : "Hearts",
    "C" : "Clubs",
    "S" : "Spades",
    "D" : "Diamonds"
}

ranks = {
    "2" : "Two", # lowest rank
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "Q" : "Queen",
    "J" : "Jack", # more valuable than queen 
    "K" : "King",
    "7" : "Seven", # second highest rank 
    "A" : "Ace" # highest rank
}


# TAKES STRING AND RETURNS CORRESPONDING BOOLEAN WHICH INDICATES IF IT EXISTS

# AssertionError: assert not True

def valid_suit(s):
    if (s == "H"):  # calling upon key 
        return True
    elif (s == "C"):
        return True
    elif (s == "S"):
        return True
    elif (s == "D"):
        return True
    else:
       return False


    
# TAKES STRING AND RETURNS CORRESPONDING BOOLEAN WHICH INDICATES IF IT EXISTS

def valid_rank(r):
    if r == "2":
        return True
    elif r == "3":
        return True
    elif r == "4":
        return True
    elif r == "5":
        return True
    elif r == "6":
        return True
    elif r == "Q":
        return True
    elif r == "J":
        return True
    elif r == "K":
        return True
    elif r == "7":
        return True
    elif r == "A":
        return True
    else:
        return False


# RETURNS STRING WITH THE GIVEN NAME IN FULL 
def suit_full_name(s): # can you have the same parameter as previous functions?
        if (s == "S"):
            return (suits["S"])
        elif (s == "D"):
            return (suits ["D"])
        elif (s == "H"):
            return (suits ["H"])
        elif (s == "C"):
            return (suits ["C"])
        else:
            raise ValueError("Invalid suit Symbol: " + s)
        


# RETURN POINTS ASSOCIATED WITH GIVEN RANK  - use dictoinary
def rank_points(r): 
    if (r == "2"): 
        return 0
    elif ( r == "3"):
        return 0 
    elif (r == "4"):
        return 0
    elif (r == "5"):
        return 0 
    elif (r == "6"):
        return 0 
    elif (r == "Q"):
        return 2
    elif (r == "J"):
        return 3
    elif (r == "K"):
        return 4
    elif (r == "7"):
        return 10
    elif (r == "A"):
        return 11
    else:
        raise ValueError("Invalid Rank Symbol" + r)

     
def rank_higher_than(r1, r2):
    if rank_points(r2)==0 and rank_points(r1)== 0:
        int(r1 and r2)
        return r1 > r2
    else:
        return rank_points(r1) > rank_points(r2)
        raise ValueError("Invalid Rank Symbol" + r1 + r2)


 
    



