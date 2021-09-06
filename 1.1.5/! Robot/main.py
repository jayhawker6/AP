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
robot_image = "robot.gif"
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
wn.bgpic("maze1.png")  # other file names should be maze2.png, maze3.png

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
if wn.bgpic() == "maze1.png":
    solveOne()

# ---- end robot movement

wn.mainloop()
