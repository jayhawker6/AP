import os

def cls(): #Generic cross-platform interpreter terminal clear function from stack-overflow. (does cls for linux and clear for windows and mac)
    os.system('cls' if os.name=='nt' else 'clear')
def bin2mod(fromlist,tolist):
    for item in range(len(fromlist)):
        testitem = fromlist[item]
        if testitem == "000": tolist.append("---")
        elif testitem == "001": tolist.append("--x")
        elif testitem == "010": tolist.append("-w-")
        elif testitem == "011": tolist.append("-wx")
        elif testitem == "100": tolist.append("r--")
        elif testitem == "101": tolist.append("r-x")
        elif testitem == "110": tolist.append("rw-")
        elif testitem == "111": tolist.append("rwx") # This method means that the further down the correct answer is, the longer it will take.
        else: tolist.append("You input something wrong here!")
def oct2bin(fromlist, tolist):
    for item in range(len(fromlist)): tolist.append(format(fromlist[item], '03b'))

cls()

oct1 = []
bin1 = []
mod1 = []
oct1.append(int(input("Input first octal >> ")))
oct1.append(int(input("Input second octal >> ")))
oct1.append(int(input("Input third octal >> ")))
oct2bin(oct1,bin1)
bin2mod(bin1,mod1)
print("Input 1 Octals: %s %s %s" % (oct1[0],oct1[1],oct1[2]))
print("Output 1 Binaries: %s %s %s" % (bin1[0],bin1[1],bin1[2]))
print("Output 1 CHMOD Values: %s %s %s" % (mod1[0],mod1[1],mod1[2]))