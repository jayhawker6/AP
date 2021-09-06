#   a115_robot_maze.py
import turtle

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = turtle.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "%/AP/1.1.5/! Robot/robot.gif"
wn.addshape(robot_image)

#----- init robot
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

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
'''
i = 0
while (i < 3): # forward 3
  move()
  i = i + 1 
'''

#---- end robot movement 

wn.mainloop()
