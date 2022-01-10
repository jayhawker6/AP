import turtle as trtl
import random


wn = trtl.Screen()
TLbutt = trtl.Turtle("square",0,True)
TLbutt.penup(),TLbutt.color("green"),TLbutt.goto(-50,50),TLbutt.turtlesize(4.5)

TRbutt = trtl.Turtle("square",0,True)
TRbutt.penup(),TRbutt.color("blue"),TRbutt.goto(50,50),TRbutt.turtlesize(4.5)

BLbutt = trtl.Turtle("square",0,True)
BLbutt.penup(),BLbutt.color("magenta"),BLbutt.goto(-50,-50),BLbutt.turtlesize(4.5)

BRbutt = trtl.Turtle("square",0,True)
BRbutt.penup(),BRbutt.color("brown"),BRbutt.goto(50,-50),BRbutt.turtlesize(4.5)

order = []

while True:
    input()
    order.append(random.randrange(4))
    for i in len(order):
        if order[i] == 0:
            TLbutt.hideturtle()
        elif order[i] == 1:
            TRbutt.hideturtle()
        elif order[i] == 2:
            BLbutt.hideturtle()
        elif order[i] == 3:
            BRbutt.hideturtle()
            

wn.mainloop()