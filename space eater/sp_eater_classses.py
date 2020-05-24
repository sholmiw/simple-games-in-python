# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:55:42 2020

@author: shlomi
"""
import turtle
import math
import random
"""
import platform
for adding sounds to game
from sys import platform
if platform == "linux" or platform == "linux2":
    osflag = False
elif platform == "win32":
    osflag = True
else:
    print("dont like mac, dont spport it")
    exit()
    
if osflag:    
    import windsound # for playind sound in windows
else:
    import os 
     
#for adding picture to player/goals etc
images =["image1.gif","image2.gif","image3.gif"]
for image in images:
    turtle.register_shape(image)
    
#then add 
self.shape ("image")
to Player and Goal classes
"""
#Set Screen
wn= turtle.Screen()
wn.bgcolor("red")
wn.title("simple space eater with classes")
#for adding background
#wn.bgpic("background.gif")
#pause machanisem
is_paused= False

class Game(turtle.Turtl):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290,310)
        self.score = 0
    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False,align="left",font=("Ariel", 14, "normal"))
    def change_score(self,points):
        self.score +=points
        self.update_score()
    """
    def play_sound(self, filename): #background music
        if osflag:
            windsound.PlaySound(filename , windsound.SND_ASYNC)
        else:
            os.system("aplay {}&".format(filename))
    """
    
def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused =True

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)
    
    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0) #animation speed ( where 0 is the fastest)
        self.color("black","blue")
        self.shape("triangle") #always faceing right      
        self.speed = 1 #not animation speed ( where 0 is the fastest)
        
    def move(self):
        self.forward(self.speed)
        #border Checking
        if self.xcor() >290 or self.xcor() < -290:
            self.left(60)
            #game.play_sound("border collison_sound") mp3 for linux, wav for win
        if self.ycor() >290 or self.ycor() < -290:
            self.left(60)
            #game.play_sound("border collison_sound") mp3 for linux, wav for win
        
    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30)
    def increacespeed(self):
        self.speed +=1

class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0) #animation speed ( where 0 is the fastest)
        self.color("green")
        self.shape("circle") #always faceing right      
        self.speed = 3 
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random(0,360))
        
    def move(self):
        self.forward(self.speed)
        #border Checking
        if self.xcor() >290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() >290 or self.ycor() < -290:
            self.left(60)
            
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random(0,360))
        
def isCollision(t1,t2):
    a = t1.xcor() - t2.xcor()  
    b = t1.ycor() - t2.ycor()  
    distance = math.sqrt((a**2)+(b**2)) 
    if distance < 20:
        return True
    else:
        return False
    
    
def listionkey(player):
    wn.listen()
    wn.onkeypress(toggle_pause, "p")  #turtle <=> wn <=> self
    wn.onkeypress(player.turnleft, "Left")
    wn.onkeypress(player.turnright, "Right")
    wn.onkeypress(player.increacespeed, "Up")
   
def Main():
    wn.tracer(0)    
    player = Player()
    border = Border()
    game = Game()
    #draw the border
    border.draw_border()
    #Create multiple goals
    goals = []
    for count in range(6):
        goals.append(Goal())

    listionkey(player)
    
    while True:
        if not is_paused:
            wn.update()
            player.move()
            for goal in goals:
                goal.move()
            
            #Check for colisions
            for goal in goals:
                if isCollision(player, goal):
                    goal.jump()
                    game.change_score(10)
                    #game.play_sound("collison_sound") mp3 for linux, wav for win
        else:
            wn.update()
 
Main()       