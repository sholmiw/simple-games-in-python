# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:57:32 2020
simpale spaceship eating game.

verion base. v0.7 need to clean code!!!!
-use this later to creat diffrant games in same idea
@author: shlomi
"""
"""
improv idea:
  -make the borders Move from the border to the opposite\random border 
  -incrase speed of player (one goal to take each time,goal give point and speed)
  -we can make enemy that build same as player. 
  -we can make a multy players option (each playr need 2 -3 buttom)
  -set a timer to collect all goals (goals = points)
  or 
  -make the goals resource like a fuel to collect (for changing dirction)
   or wepean 
  -battle royel: cople of enemy (build like player):
      eat other ships and get point / bigger:
            set life for each object. on colliding make demage intil break.                          
"""
import turtle
import math
import random
#Set Screen
wn= turtle.Screen()
wn.bgcolor("lightgreen")

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
player.color("blue")
player.shape("triangle") #always faceing right
player.penup()
player.speed(0) # animation speed (0 is the fastest)
 
#we can make enemy that build same as player.

#Create goal - make it class later
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.speed(0)
goal.penup()
goal.setposition(random.randint(-300,300),random.randint(-300,300)) 

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
    #here we can make more staff like 
    
    #Boundry Cheaking ,shold put it in a sepret function?
    if player.xcor() >300 or player.xcor() <-300:
        player.right(180) #we can add a slop to the engle for more intrasting play
    if player.ycor() >300 or player.ycor() <-300:
        player.right(180)
    
    #Collision detaction 
    if isCollision(player,goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))

    #here we can make more staff like  
delay = input("Press Enter to finish")


########################################################
########################################################
"""
v0.6
import turtle
import math
import random
#Set Screen
wn= turtle.Screen()
wn.bgcolor("lightgreen")

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
player.color("blue")
player.shape("triangle") #always faceing right
player.penup()
player.speed(0) # animation speed (0 is the fastest)
 
#we can make enemy that build same as player.

#Create goal - make it class later
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.speed(0)
goal.penup()
goal.setposition(random.randint(-300,300),random.randint(-300,300)) 

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
    if player.ycor() >300 or player.ycor() <-300:
        player.right(180)
    
    #Collision detaction 
    if isCollision(player,goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        goal.right(random.randint(0,360)) 
    #Move the goal 
    goal.forward(3)

    #Boundry Cheaking ,shold put it in a sepret function?
    if goal.xcor() >290 or goal.xcor() <-290:
        goal.right(180) #we can add a slop to the engle for more intrasting play
    if goal.ycor() >290 or goal.ycor() <-290:
        goal.right(180)

delay = raw_input("Press Enter to finish")
"""