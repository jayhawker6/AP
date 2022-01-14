# Runtime Import
import turtle as trtl
import random as rand
import time

## Starting Variable Defs
shape = 'square'
shape_x_sz, shape_y_sz, shrink_x_sz, shrink_y_sz = 8,8,4,4

#colors
color_1 = '#c785ec'
color_2 = '#a86add'
color_3 = '#8549a7'
color_4 = '#634087'
color_bck = '#deb7ff'

#list for program
sequence_list = []
working_list = []


correct = True
pnt_up = 1
points = 0
txt_setup = ('arial', 30, 'normal')

points = 0
correct = True
sequence_time = .25
shrink_time = .10
#-------------Turtles-------


#Makes the screen turtle
screen = trtl.Screen()
screen.tracer(False)

#text rutles that displays the score
txt_trtl = trtl.Turtle()
txt_gme_ovr = trtl.Turtle()
#Makes the turtles for the game
shape_top_left = trtl.Turtle()
shape_top_right = trtl.Turtle()
shape_bottom_left = trtl.Turtle()
shape_bottom_right = trtl.Turtle()

#Turtles penup annd leave no shape
shape_top_left.penup(),shape_top_left.shape(shape),shape_top_left.shapesize(shape_x_sz,shape_y_sz)
shape_top_right.penup(),shape_top_right.shape(shape),shape_top_right.shapesize(shape_x_sz,shape_y_sz)
shape_bottom_left.penup(),shape_bottom_left.shape(shape),shape_bottom_left.shapesize(shape_x_sz,shape_y_sz)
shape_bottom_right.penup(),shape_bottom_right.shape(shape),shape_bottom_right.shapesize(shape_x_sz,shape_y_sz)


#sets color theme for the shape
shape_top_left.color(color_1)
shape_top_right.color(color_2)
shape_bottom_left.color(color_3)
shape_bottom_right.color(color_4)

screen.bgcolor(color_bck)



#Move the turtles
shape_top_left.goto(-80,80)
shape_top_right.goto(80,80)
shape_bottom_left.goto(-80,-80)
shape_bottom_right.goto(80,-80)
screen.tracer(True)



#text turtle setup
txt_gme_ovr.ht()
txt_gme_ovr.color('white')
txt_trtl.penup()
txt_trtl.goto(0, 175)
txt_trtl.color('white')
txt_trtl.write("Points: " + str(points), font=txt_setup, align='center')

#shrinks turtle on click
def shrink(turtle):
    turtle.shapesize(shrink_x_sz,shrink_y_sz)
    time.sleep(.2)
    turtle.shapesize(shape_x_sz,shape_y_sz)

#updates score
def txt_updt():
    global points
    txt_trtl.undo()
    txt_trtl.write("Points: " + str(points), font=txt_setup, align='center')

#The corresponding squares will lightup depending on the pattern
def follow_sequence():
    global correct
    global sequence_list
    global working_list

    if correct == True and len(working_list) == 0:
        rand_num = rand.randint(1,4)
        sequence_list.append(rand_num)
        working_list = sequence_list.copy()
        for num in sequence_list:
            if num == 1:
                shape_bottom_left.color('white')
                time.sleep(sequence_time)
                shape_bottom_left.color(color_3)
                time.sleep(sequence_time)
            elif num == 2:
                shape_top_left.color('white')
                time.sleep(sequence_time)
                shape_top_left.color(color_1)
                time.sleep(sequence_time)
            elif num == 3:
                shape_top_right.color('white')
                time.sleep(sequence_time)
                shape_top_right.color(color_2)
                time.sleep(sequence_time)
            else:
                shape_bottom_right.color('white')
                time.sleep(sequence_time)                
                shape_bottom_right.color(color_4)
                time.sleep(sequence_time)


#checks if the button pressed is in the working list
def check_button(color_pressed):
    global sequence_list
    global correct
    global points
    if len(sequence_list) > 0:
        
        check_list = working_list.pop(0)
        if str(color_pressed) in str(check_list):
            points += pnt_up
            txt_updt()
            correct = True
            
        else:
            correct = False
            sequence_list = []
            check_list = []
            end_game()

        print(correct)
    else:
        
        print("done")

#hides turtles


def end_game():
    txt_gme_ovr.st()
    shape_top_left.ht()
    shape_top_right.ht()
    shape_bottom_left.ht()
    shape_bottom_right.ht()
    txt_gme_ovr.write("Game_Over", font=txt_setup, align='center')



#calls the things needed after the button is pressed
def check_tp_lft(x,y):
    shrink(shape_top_left)
    check_button(2)
    follow_sequence()
def check_tp_rit(x,y):
    shrink(shape_top_right)
    check_button(3)
    follow_sequence()
def check_btm_lft(x,y):
    shrink(shape_bottom_left)
    check_button(1)
    follow_sequence()
def check_btm_rit(x,y):
    shrink(shape_bottom_right)
    check_button(4)
    follow_sequence()



follow_sequence()
#checks if the button is pressed
shape_top_left.onclick(check_tp_lft)
shape_top_right.onclick(check_tp_rit)
shape_bottom_left.onclick(check_btm_lft)
shape_bottom_right.onclick(check_btm_rit)


screen.mainloop()