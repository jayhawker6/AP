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
validnumbers
enemynumber = None
while enemynumber not in range(1, 10, 1):
    if (enemynumber == "K" or enemynumber == "Q") or (enemynumber == "")