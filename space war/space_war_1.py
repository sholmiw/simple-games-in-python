"""
Created on Tus May 26  2020

@author: shlomi
note: need to add sounds,background and gif's
https://www.youtube.com/watch?v=u5GT9nH95_A&list=PLlEgNdBJEO-muprNCDYiKLZ-Kc3-p8thS&index=9

"""
import os
import random
import turtle
import time

#turtle.fd(0) #needed for macOS in py 2.7
turtle.speed(0) #Set animations speed
turtle.bgcolor("black") #Set background color
turtle.bgpic("bg.gif") #Set background picture
turtle.title("space war") #Set title to screen
turtle.ht() #Hide the default turtle
turtle.setundobuffer(1) #This saves memory
turtle.tracer(2) #This speed up drawing


is_paused= False
def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused =True

def toggle_esc():
    global play
    play = False



class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, x, y):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.forward(0)
        self.goto(x,y)
        self.speed = 1
    
    def move(self):
        self.fd(self.speed)
        #Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
    
    def is_collisions(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, x, y):
        Sprite.__init__(self, spriteshape, color, x, y)
        #self.shape("player.gif")
        self.shapesize(stretch_wid=0.6, stretch_len=1.1,outline=None)
        self.speed = 4
        self.live = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)
    
    def accelerate(self):
        self.speed +=1

    def decelerate(self):
        self.speed -=1   

class Missile(Sprite):
    def __init__(self, spriteshape, color, x, y):
        Sprite.__init__(self, spriteshape, color, x, y)
        self.status = "ready"
        self.shapesize(stretch_wid=0.2,stretch_len=0.4,outline=None)
        self.speed = 20
        self.goto(-1000,-1000)
    
    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(),player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
    
    def move(self):
        if self.status == "ready":
            self.goto(-1000,1000)

        if self.status == "firing":
            self.fd(self.speed)

        #Border cheak
        if self.xcor() <-290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000,1000)
            self.status = "ready"



class Enemy(Sprite):
    def __init__(self, spriteshape, color, x, y):
        Sprite.__init__(self, spriteshape, color, x, y)
        self.speed = 6
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, x, y):
        Sprite.__init__(self, spriteshape, color, x, y)
        self.speed = 8
        self.setheading(random.randint(0,360))
    def move(self):
        self.fd(self.speed)
        #Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Particle(Sprite):
    def __init__(self, spriteshape, color, x, y):
        Sprite.__init__(self, spriteshape, color, x, y)
        self.shapesize(stretch_wid=0.1,stretch_len=0.1,outline=None)
        self.goto(-1000,-1000)
        self.prame = 0 

    def explode(self,x,y):
        self.goto(x,y)
        self.setheading(random.randint(0,360))
        self.prame = 1
        
    def move(self):
        if self.prame > 0:
            self.fd(10)
            self.prame +=1
        if self.prame > 12:
            self.goto(-1000,-1000)
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0 
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives= 3

    def draw_border(self):
        #draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range (4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg ="Score: %s ,Lives: %s" %(self.score,self.lives)
        self.pen.penup()
        self.pen.goto(-300,310)
        self.pen.write(msg,font=("Arial",16,"normal"))

    def game_over(self):
        self.pen.undo()
        msg ="game over, you are dead, your score = %s" %(self.score)
        self.pen.goto(-300,310)
        self.pen.write(msg,font=("Arial",16,"normal"))
        time.sleep(3)
        exit()
    # def play_sound(self, filename):
    #     windsound.PlaySound(filename , windsound.SND_ASYNC)

#create game object
game = Game()
#draw border
game.draw_border()
#show the game status
game.show_status()
#Create player
player = Player("triangle", "white", 0, 0)
#Create missile
missile = Missile("triangle", "yellow", 0, 0)

#Create ally
#ally = Ally("square","blue",0,0)
allies = []
for i in range(3):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    allies.append(Ally("square","blue",x,y))
#Create enemy
#enemy = Enemy("circle", "red", -100, 0)
enemies =[]
for i in range(6):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    enemies.append(Enemy("circle", "red", x, y))
particles =[]
for i in range(10):
    particles.append(Particle("circle", "orange", x, y))
#keyboard binding
#turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.decelerate,"Down")
turtle.onkey(missile.fire,"space")
turtle.onkey(toggle_pause,"p")
turtle.onkey(toggle_esc,"q")
turtle.listen()
#Main game loop
play = True
while play:
    turtle.update()
    if not is_paused:
        turtle.update()
        time.sleep(0.01)
        player.move()
        missile.move()
        for enemy in enemies:
            enemy.move()
            if player.is_collisions(enemy):
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                #update (Decreace) score
                game.score -= 100
                player.live -= 1
                game.lives -= 1
                if (player.live == 0):
                    game.game_over()
                game.show_status()
            #Check missile collision with enemy
            if missile.is_collisions(enemy):
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                missile.status == "ready"
                #update (Increace) score
                game.score +=100
                game.show_status()
                #add explose effect
                for particle in particles:
                    particle.explode(missile.xcor(),missile.ycor())
                    

        for ally in allies:
            ally.move()
            #check missile collision with ally
            if missile.is_collisions(ally):
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                ally.goto(x, y)
                missile.status == "ready"
                #update (Decreace) score
                game.score -=100
                game.show_status()
                #add explose effect
                for particle in particles:
                    particle.explode(missile.xcor(),missile.ycor())
                    
            #Check ally collision with enemy
            for enemy in enemies:
                if ally.is_collisions(enemy):
                    x = random.randint(-250, 250)
                    y = random.randint(-250, 250)
                    enemy.goto(x, y)
                    #game.play_sound("boom.wav")
                    x = random.randint(-250, 250)
                    y = random.randint(-250, 250)
                    ally.goto(x, y)
            
        for particle in particles:
            particle.move()
    else:
        #turtle.update()
        time.sleep(0.1)

delay = input("Press enter to finish")