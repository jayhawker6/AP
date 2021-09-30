import os

def cls(): #Generic cross-platform interpreter terminal clear function from stack-overflow. (does cls for linux and clear for windows and mac)
    os.system('cls' if os.name=='nt' else 'clear')
def bin2mod(list,index):
    testitem = list[index]
    if testitem == "000": return "---"
    if testitem == "001": return "--x"
    if testitem == "010": return "-w-"
    if testitem == "011": return "-wx"
    if testitem == "100": return "r--"
cls()
oct1 = []
bin1 = []
mod1 = []
oct1.append(int(input("Input first octal >> ")))
oct1.append(int(input("Input second octal >> ")))
oct1.append(int(input("Input third octal >> ")))

for item in range(len(oct1)): bin1.append(format(oct1[item], '03b'))