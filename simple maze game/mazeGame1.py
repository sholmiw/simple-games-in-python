# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:35:06 2020
simple maze game.
Python 2 and Python3 Compatible
@author: shlomi
"""

import turtle
import math 
import random 
#Set map 
BASESIZE = 288
TILESIZE = 24

wn =turtle.Screen()
wn.bgcolor("black")
wn.title ("a maze game")
wn.setup(700,700)
#put it here for faster loeding
#wn.tracer(0)

#Register shapes

images =["player_right.gif","player_left.gif","enemy_right.gif","enemy_left.gif",
                             "treasure.gif","wall.gif"]
for image in images:
    turtle.register_shape(image)

#create Pen - the tilse
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Create Player class
class Player(turtle.Turtle):
       def __init__(self):
           turtle.Turtle.__init__(self)
           self.shape("player_right.gif") #player_right.gif
           self.color("blue")
           self.penup()
           self.speed(0)
           self.gold = 0 
#Adding mobility to the player, can do better then this
# second version with collision detection, sort of 
# collision with wall stop player from moving into the wall           
       def go_up(self):
           new_x = self.xcor()
           new_y = self.ycor() + TILESIZE
           #Cheak for collision
           if (new_x,new_y) not in walls:
               self.goto(new_x,new_y)
       def go_down(self):
           new_x = self.xcor()
           new_y = self.ycor() - TILESIZE 
           if (new_x,new_y) not in walls:
               self.goto(new_x,new_y)
       def go_left(self):
           new_x = self.xcor() - TILESIZE
           new_y = self.ycor()
           self.shape("player_left.gif")
           if (new_x,new_y) not in walls:
               self.goto(new_x,new_y)
       def go_right(self):
           new_x = self.xcor() + TILESIZE
           new_y = self.ycor()
           self.shape("player_right.gif")
           if (new_x,new_y) not in walls:
               self.goto(new_x,new_y)
       #collision detection with treasure or enemy
       def is_collision(self,other):
           a = self.xcor()-other.xcor()
           b = self.ycor()-other.ycor()
           distance = math.sqrt((a**2)+(b**2))
           if distance <5:
               return True
           else:
               return False
            
"""       
#my approch will by more like:
       def move(self,diraction):
           if diraction == "up":
               self.goto(self.xcor(), self.ycor() + TILESIZE)
           if diraction == "down":
               self.goto(self.xcor(), self.ycor() - TILESIZE) 
           if diraction == "left":
               self.goto(self.xcor() - TILESIZE, self.ycor())
           if diraction == "right":
               self.goto(self.xcor() + TILESIZE, self.ycor())
# funny thing, find out thet python dont have a swicth statment           
"""
class Treasure(turtle.Turtle):
    def __init__(self, x,y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif") #treasure.gif
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#Create enemy       
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemy_left.gif") #enemy_left.gif
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up","down","right","left"])
        
    def move(self):
        if self.direction =="up":
            dx = 0
            dy = TILESIZE
        elif self.direction == "down":
            dx = 0
            dy = -TILESIZE
        elif self.direction == "left":
            dx= -TILESIZE
            dy = 0
            self.shape("enemy_left.gif")
        elif self.direction == "right":
            dx = TILESIZE
            dy = 0
            self.shape("enemy_right.gif")
        else:
            dx = 0
            dy = 0
        
        #Add simple Ai,
        #if player close,try chase him
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction ="left"
            elif player.xcor() > self.xcor():
                self.direction ="right"
            elif player.ycor() > self.ycor():
                self.direction ="up"
            elif player.ycor() < self.ycor():
                self.direction ="down"
        #Calculate the spot to move to 
        move_to_x =self.xcor() + dx
        move_to_y =self.ycor() + dy
        #cheak if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #object got into wall
            self.direction =random.choice(["up","down","right","left"])
            
        #Set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))
    #Cheak if other(player) close
    def is_close(self, other):
         a = self.xcor()-other.xcor()
         b = self.ycor()-other.ycor()
         distance = math.sqrt((a**2)+(b**2))
         if distance < TILESIZE*3:
             return True
         else:
             return False
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
"""
#Create enamy
class Enamy(turtle.Turtle):
       def __init__(self):
           turtle.Turtle.__init__(self)
           self.shape("square")
           self.color("red")
           self.penup()
           self.speed(0) 

"""           
        
#create level list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                      X",
"XXXXXXXXXXXXXXXXXXXXX   X",
"XXXXXXXXXXXXXXXXXXX     X",
"XXXXXXXXXXXXXXXXX       X",
"XXXXXXXXXXXXXXXXX       X",
"XXXXXXXXXXXXXX          X",
"XXX E                    X",
"XXX                 XXXXX",
"XXX      XXXXXTXXXXXXXXX",
"XXXXXXXX XXXXXE      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX XXXX XXXXX",
"XXXX XXX XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
"XXXX     XXXXX      XXXXX",
]

#add a treasure list
treasures = []
#add enemis list
enemeis = []
#Add maze to the maze list
levels.append(level_1)



#Create level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get the character at each x,y coordinate
            #note the order of y and x in the next line
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = -BASESIZE + (x * TILESIZE)
            screen_y = BASESIZE - (y * TILESIZE)
            
            #Cheak if it is an X (x representing a wall)
            if character == "X":
                pen.goto(screen_x,screen_y)
                pen.shape("wall.gif") #wall.gif
                #note: we can make fake wall using 2 type of wall.
                pen.stamp()
                #Add coordinates to wall list (as a point)
                walls.append((screen_x,screen_y))
            #Cheak if it is an P (for Player position)
            if character == "P":
                player.goto(screen_x,screen_y)
                #player.stamp()
            #Cheak if it is an T (for treasure position)
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))
            #Cheak if it is an E (for enemy position)
            if character == "E":
                enemeis.append(Enemy(screen_x,screen_y))
#Create class instance
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []
#Set up the level
setup_maze(levels[1])
#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

#Turn off screen update , put it here for faster loeding
wn.tracer(0)
#Start moving enemeis
#set moving enemy after 250 mlisecond
ENEMY_START_MOVE = 250
for enemy in enemeis:
    turtle.ontimer(enemy.move, t = ENEMY_START_MOVE)

#Main Game Loop
while True:
    #Cheak for player collision with treasure
    #by uteratetion through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure gold to the player gold
            player.gold +=treasure.gold
            print("Player Gold: {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)
    #Iterate thriugh enemy list to see if player collided with enemy
    for enemy in enemeis:
        if player.is_collision(enemy):
            print("player dies!")
            exit()
            
    wn.update()
    #pass