try:
    from Classes.colors import txtcolor
except ImportError:
    raise Exception("#000 Connected Classes not found!")
try:
    import os
    import pyCardDeck as pcd
except ImportError:
    raise Exception(f"{txtcolor.FAIL}A dependancy could not be accessed! Refer to error code #001 for solution!{txtcolor.ENDC}")
def cls(): os.system('cls' if os.name=='nt' else 'clear')
def cardIn(setVar):
    setVar = input("Input cards >> ")
    
## BEGIN INTERFACE ##

cls()
allcards = []
while True:
    cardIn(allcards)