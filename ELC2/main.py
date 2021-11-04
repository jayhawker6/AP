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
    
    
cls()
    
## BEGIN INTERFACE ##

print("""
INFO:
    The given input must be in the correct format,
    Looking like this: (Excluding the parethacies)
                      #X, #X, #X, #X, #X, #X
    It should have exactly 22 characters, the first
    value given is the card of the opponent, and the
    last 5 cards are the hand of the dealer. # represents
    the rank and X represents the suit.
    Valid ranks are in the following order:
    A (Ace)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    T (10)
    J (Jack)
    Q (Queen)
    K (King)
    
    Valid suits:
    D (Diamonds)
    C (Clubs)
    H (Hearts)
    S (Spades)
    
""")
os.system('pause'), cls()
validRanks = [1,2,3,4,5,6,7,8,9,"T","J","Q","K","A"]
validSuits = ["D","H","C","S"]
while True:
    userinput = str(input("Card values seperated by one comma and one space >> "))
    if len(userinput) != 22:
        printWarn(" -=-  INPUT LENGTH IS INCORRECT!  -=- ")
        continue
    elif userinput[0] not in validRanks or userinput[1] not in validSuits:
        printWarn(" -=-  CARD VALUE NOT IDENTIFIED!  -=- ")
        continue
    else:
        enemyCard = userinput[0]
    