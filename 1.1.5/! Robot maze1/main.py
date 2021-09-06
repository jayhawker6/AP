# a115_robot_maze.py
import turtle

# ----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

# ------ robot commands


def move(x=1):
    for i in range(x):
        robot.dot(10)
        robot.fd(50)


def turn_left():
    robot.speed(0)
    robot.lt(90)
    robot.speed(2)


def turn_right():
    robot.speed(0)
    robot.lt(-90)
    robot.speed(2)

# ----- init screen
wn = turtle.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "assets/robot.gif"
wn.addshape(robot_image)

# ----- init robot
robot = turtle.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

# ---- TODO: change maze here
wn.bgpic("assets/maze2.png")  # other file names should be maze2.png, maze3.png

# ---- TODO: begin robot movement here
def solveOne():
    w1 = 0
    while w1 < 2:
        move()
        w1 += 1
    turn_right()
    w1 = 0
    while w1 < 2:
        move()
        w1 += 1
    w1 = 0
    while w1 < 2:
        move()
        turn_left()
        move()
        turn_right()
        w1 += 1
def solveTwo():
    w2 = 0
    while w2 < 3:
        move()
        w2 += 1
    turn_right()
    w2 = 0
    while w2 < 2:
        move()
        w2 += 1
    w2 = 0
    robot.goto(startx,starty)
    while w2 < 3:
        move() #The move function IS a nested loop. I changed it to have a for loop and a variable to decide how many times to run.
        w2 += 1
    w2 = 0
    turn_left()
    while w2 < 3:
        move()
        w2 += 1
    w2 = 0
    while w2 < 1:
        turn_left()
        move()
        w2+=1
        

if wn.bgpic() == "assets/maze1.png":
    solveOne()
elif wn.bgpic() == "assets/maze2.png":
    solveTwo()

# ---- end robot movement

wn.mainloop()
