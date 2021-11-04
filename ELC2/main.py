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
def cardIn(setVar):
    setVar = input("Input cards >> ")
def printWarn(warningText):
    if warningText == None: raise Exception("A warning was not defined in the code")
    print(f"{txtcolor.WARNING}%s{txtcolor.ENDC}" % (warningText)), os.system('Pause'), cls()
def translateRank(transvar,tolist):
    if transvar == "T": tolist = [10,tolist]
    if transvar == "J": tolist = [11,tolist]
    if transvar == "Q": tolist = [12,tolist]
    if transvar == "Q": tolist = [12,tolist]

    
    
cls()
    
## BEGIN INTERFACE ##

print("""\nINFO:\n    The given input must be in the correct format,\n    Looking like this: (Excluding the parethacies)\n    #X, #X, #X, #X, #X, #X\n    It should have exactly 22 characters, the first\n    value given is the card of the opponent, and the\n    last 5 cards are the hand of the dealer. # represents\n    the rank and X represents the suit.\n    Valid ranks are in the following order:\n    A (Ace)\n    1\n    2\n    3\n    4\n    5\n    6\n    7\n    8\n    9\n    T (10)\n    J (Jack)\n    Q (Queen)\n    K (King)\n    \n    Valid suits:\n    D (Diamonds)\n    C (Clubs)\n    H (Hearts)\n    S (Spades)\n    \n""")
os.system('pause'), cls()
validRanks = [1,2,3,4,5,6,7,8,9,"T","J","Q","K","A"]
validSuits = ["D","H","C","S"]
while True:
    userinput = str(input("Card values seperated by one comma and one space >> "))
    if len(userinput) != 22: printWarn(" -=-  INPUT LENGTH IS INCORRECT!  -=- "); continue
    if userinput[0] == "T": enemyCard = [10,userinput[1]]
    if userinput[0] == "J": enemyCard = [11,userinput[1]]
    if userinput[0] == "Q": enemyCard = [12,userinput[1]]
    if int(userinput[1]) not in validRanks: printWarn(" -=-  CARD VALUE NOT IDENTIFIED!  -=- "); continue
    else: break
print(f"{txtcolor.OKGREEN}Program ENDED!{txtcolor.ENDC}")