import os

def cls(): os.system('cls' if os.name=='nt' else 'clear')
def cardIn(setVar):
    setVar = input("Input cards >> ")
    
## BEGIN INTERFACE ##

cls()
allcards = []
while True:
    
    cardIn(allcards)