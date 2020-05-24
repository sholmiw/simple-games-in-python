# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:08:58 2020
simpale spaceship eating game.
v 0.99 
need to clean code!!!!
@author: shlomi
"""
import turtle
import math
import random
#import os # for geting sound in linuxs or mac
#import winsound # for geting sound in windows

#Set Screen
wn= turtle.Screen()
wn.bgcolor("lightgreen")
#wn.bgpic("some_pic_for_background.gif") 600x600 will be on borders and we can delate drowing them
wn.tracer(3) #skip some prame to make drowing faster
#Drew border , we use a simple drowing of border 
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range (4):
    mypen.forward(600) # stright line
    mypen.left(90) # make a corner
mypen.hideturtle()

#Creeate player turtle - make it class later
player = turtle.Turtle()
player.color("black","blue")
player.shape("triangle") #always faceing right
player.penup()
player.speed(0) # animation speed (0 is the fastest)


#Create score
score = 0 
#Create goals -we can make a goal class later
maxGoals = 4
goals = []

for count in range (maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].speed(0)
    goals[count].penup()
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300)) 



#Set speed varibale
speed = 1

#Define functions
def increasespeed():
    global speed
    speed += 1

def turnleft():
    player.left(30)
   
def turnright():
    player.right(30)

#Collision detaction using distance
def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d <20:
        return True
    else:
        return False


#Set keyboard binding
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")

while True:
    player.forward(speed)
    
    #Boundry Cheaking ,shold put it in a sepret function?
    if player.xcor() >300 or player.xcor() <-300:
        player.right(180) #we can add a slop to the engle for more intrasting play
        #windsound.PlaySound("sound_for_bowncing.wav",winsound.SND_ASYNC)# for windows
        #os.system( "afplay sound_for_bowncing.mp3&") #for linux and mac
    if player.ycor() >300 or player.ycor() <-300:
        player.right(180)
        #windsound.PlaySound("sound_for_bowncing.wav",winsound.SND_ASYNC) for windows
        #os.system("afplay sound_for_bowncing.mp3&") #for linux and mac (afplay and namefile.mp3&)
    
    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(3)
    
        #Boundry Cheaking ,shold put it in a sepret function?
        if goals[count].xcor() >290 or goals[count].xcor() <-290:
            goals[count].right(180) #we can add a slop to the engle for more intrasting play
        if goals[count].ycor() >290 or goals[count].ycor() <-290:
            goals[count].right(180)
        #Collision detaction 
        if isCollision(player,goals[count]):
            #windsound.PlaySound("sound_for_Collision.wav",winsound.SND_ASYNC) for windows
            #os.system("afplay sound_for_Collision.mp3&") #for linux and mac
            goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            score +=1
            #print(score)
            #Wrow the score on screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            score_string ="Score: %s" %score
            mypen.write(score_string, False, align = "left", font=("Ariel",14,"normal"))


delay = input("Press Enter to finish")