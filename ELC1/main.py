import os, time

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
        else: tolist.append("Incorrect Input! ")
def oct2bin(fromlist, tolist):
    for item in range(len(fromlist)): tolist.append(format(fromlist[item], '03b'))
def bin2oct(fromlist, tolist):
    for item in range(len(fromlist)):
        testitem = fromlist[item]
        if testitem == "000": tolist.append("0")
        elif testitem == "001": tolist.append("1")
        elif testitem == "010": tolist.append("2")
        elif testitem == "011": tolist.append("3")
        elif testitem == "100": tolist.append("4")
        elif testitem == "101": tolist.append("5")
        elif testitem == "110": tolist.append("6")
        elif testitem == "111": tolist.append("7") # This method means that the further down the correct answer is, the longer it will take.
        else: tolist.append("Incorrect Input! ")
def mod2bin(fromlist,tolist):
    for item in range(len(fromlist)):
        testitem = fromlist[item]
        if testitem == "---": tolist.append("000")
        elif testitem == "--x": tolist.append("001")
        elif testitem == "-w-": tolist.append("010")
        elif testitem == "-wx": tolist.append("011")
        elif testitem == "r--": tolist.append("100")
        elif testitem == "r-x": tolist.append("101")
        elif testitem == "rw-": tolist.append("110")
        elif testitem == "rwx": tolist.append("111") # This method means that the further down the correct answer is, the longer it will take.
        else: tolist.append(" Wrong Input! ")
cls()
## First Input ##
oct1 = []
bin1 = []
mod1 = []
oct1.append(int(input("Input first octal >> ")))
oct1.append(int(input("Input second octal >> ")))
oct1.append(int(input("Input third octal >> ")))
oct2bin(oct1,bin1)
bin2mod(bin1,mod1)
print("Input 1 Input: %s %s %s" % (oct1[0],oct1[1],oct1[2]))
input("Output 1: %s %s %s and %s %s %s" % (bin1[0],bin1[1],bin1[2],mod1[0],mod1[1],mod1[2]))
## Second Input ##
oct2 = []
bin2 = []
mod2 = []
oct2.append(int(input("Input first octal >> ")))
oct2.append(int(input("Input second octal >> ")))
oct2.append(int(input("Input third octal >> ")))
oct2bin(oct2,bin2)
bin2mod(bin2,mod2)
print("Input 2: %s %s %s" % (oct2[0],oct2[1],oct2[2]))
input("Output 2: %s %s %s and %s %s %s" % (bin2[0],bin2[1],bin2[2],mod2[0],mod2[1],mod2[2]))
## Third input ##
bin3 = []
oct3 = []
mod3 = []
bin3.append(input("Input first binary >> "))
bin3.append(input("Input second binary >> "))
bin3.append(input("Input third binary >> "))
bin2oct(bin3,oct3)
bin2mod(bin3,mod3)
print("Input 3: %s %s %s" % (bin3[0],bin3[1],bin3[2]))
input("Output 3: %s %s %s and %s %s %s" % (oct3[0],oct3[1],oct3[2],mod3[0],mod3[1],mod3[2]))
## Fourth input ##
bin4 = []
oct4 = []
mod4 = []
bin4.append(input("Input first binary >> "))
bin4.append(input("Input second binary >> "))
bin4.append(input("Input third binary >> "))
bin2oct(bin4,oct4)
bin2mod(bin4,mod4)
print("Input 4: %s %s %s" % (bin4[0],bin4[1],bin4[2]))
input("Output 4: %s %s %s and %s %s %s" % (oct4[0],oct4[1],oct4[2],mod4[0],mod4[1],mod4[2]))
## Fifth input ##
oct5, bin5, mod5 = [], [], []
mod5.append(input("Input first CHMOD value >> "))
mod5.append(input("Input second CHMOD value >> "))
mod5.append(input("Input third CHMOD value >> "))
mod2bin(mod5,bin5)
bin2oct(bin5,oct5)
print("Input 5: %s %s %s" % (mod5[0],mod5[1],mod5[2]))
input("Output 5: %s %s %s and %s %s %s" % (bin5[0],bin5[1],bin5[2],oct5[0],oct5[1],oct5[2]))
cls()
print("Hey so... This was the end of the assignment. I've got nothing left. Soooooo. Yeah bye.")
time.sleep(5) # Exactly 100 lines of code. Very ugly code yes, but you only have to look at 100 lines of it, so things could be much worse.
cls()         # Enjoy the compacted if and for statements ;) (I would also like to thank my BFF's, Ctrl+C and Ctrl+V)