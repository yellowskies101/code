import sueca_games #  import previous files 


# 3.5 - COMMAND LINE INTERFACE AND OUTPUTS

# main controller file, deals with cmd  


class GameFileCouldNotBeFound(Exception):
    pass

class SuecaGameIncomplete(Exception):
    pass

def runGame(fname, showCards, showGame):
    if fname != :
    raise GameFileCouldNotBeFound("This file does not exist")

raise SuecaGameIncomplete

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
#  join prepends working directory
# dirname file - absolute path
# getcwd() - dropped 
# real path solves - symbolic
fname = open(os.path.join(__location__, 'game1.sueca'))
def runGame(fname, showCards, showGame):
  print(fname.read())
parseGameFile(fname)
