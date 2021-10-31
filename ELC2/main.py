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
    
## BEGIN INTERFACE ##

cls()
input = input("Card values seperated by comma and space >> ")
enemyNumber = "K"
validNumbers = [1,2,3,4,5,6,7,8,9,"T","J","Q","K","A"]
while enemyNumber not in range(1, 10, 1):
    if enemyNumber not in validNumbers:
        raise Exception(f"{txtcolor.WARNING} CARD RANK NOT IDENTIFIED CORRECTLY!{txtcolor.ENDC}")