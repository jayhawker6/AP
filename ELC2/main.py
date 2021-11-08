try:
    from Classes.colors import txtcolor
except ImportError:
    raise ImportError("#000 Connected Classes not found!")
try:
    import os
    import pyCardDeck as pcd
except ImportError:
    raise ImportError(f"{txtcolor.FAIL}#001 | A dependancy could not be accessed! Refer to error code for solution!{txtcolor.ENDC}")
def cls(): os.system('cls' if os.name=='nt' else 'clear')
def printWarn(warningText):
    if warningText == None: raise Exception("A warning was not defined in the code")
    print(f"{txtcolor.WARNING}%s{txtcolor.ENDC}" % (warningText)), os.system('Pause'), cls()
def translateRank(transvar):
    if transvar == "A": return 0
    if transvar == "T": return 10
    if transvar == "J": return 11
    if transvar == "Q": return 12
    if transvar == "K": return 13
    else: return "Fail!"
cls()
    
## BEGIN INTERFACE ##

print("""\nINFO:\n    The given input must be in the correct format,\n    Looking like this: (Excluding the parethacies)\n    #X, #X, #X, #X, #X, #X\n    It should have exactly 22 characters, the first\n    value given is the card of the opponent, and the\n    last 5 cards are the hand of the dealer. # represents\n    the rank and X represents the suit.\n    Valid ranks are in the following order:\n    A (Ace)\n    1\n    2\n    3\n    4\n    5\n    6\n    7\n    8\n    9\n    T (10)\n    J (Jack)\n    Q (Queen)\n    K (King)\n    \n    Valid suits:\n    D (Diamonds)\n    C (Clubs)\n    H (Hearts)\n    S (Spades)\n    \n""")
os.system('pause'), cls()
validRanks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
validSuits = ["D","H","C","S"]
while True:
    
    userinput = str(input("Card values seperated by one comma and one space >> "))
    if len(userinput) != 22: printWarn(" -=-  INPUT LENGTH IS INCORRECT!  -=- "); continue #We base things off of the character position, so we check the amount of characters
    
    enemyrank = translateRank(userinput[0]) #Take the input enemy rank and make a numerical variable for it
    enemysuit = userinput[1]
    
    if enemyrank not in validRanks or enemysuit not in validSuits: printWarn(" -=-  ENEMY CARD VALUE NOT IDENTIFIED!  -=- "); continue #Check that the translation output a correct numerical value
    
    print(f"{txtcolor.FAIL}Rank of enemy = %s{txtcolor.ENDC}" % (enemyrank)), os.system('pause')
    dealerhand = userinput[4:22].split(", ")
    dc1 = dealerhand[0]
    print(dealerhand)
    break

coss = [] #List containing cards in dealer's hand in the same suit of that of the opponents (Cards Of Same Suit)

for i in range(len(dealerhand)):
    card = dealerhand[i]
    if str(card[1]) == enemysuit: coss.append(dealerhand[i])
if not coss:
    

print(f"{txtcolor.OKGREEN}Program ENDED!{txtcolor.ENDC}")