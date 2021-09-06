import os
clearcon = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearcon()
while True:
    clearcon()
    try:
        usera = int(input("Input first number: "))
    except ValueError:
        continue
    try:
        userb = int(input("Input second number: "))
    except ValueError:
        continue
    if usera == 0 or userb == 0:
        input("Nice try.")
        continue
    elif usera % userb != 0:
        input("That does not divide evenly!")
    else:
        break
input("That divides evenly!")
clearcon()