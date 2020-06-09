# -*- coding: utf-8 -*-
"""
Created on Mon Jun 9 2020
snake game
Python3 

v 1.0
@author: shlomi
"""
import turtle
import time
import random


#Set Screen
wn= turtle.Screen()
wn.bgcolor("green")
wn.title("snake game")
wn.setup(width = 600, height = 600)
wn.tracer(0)

# Set a delay
delay = 0.1

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction ="stop"
#snake body
segments =[]
#score
score = 0 
high_score = 0 

#pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,269)
pen.write("Score: 0 , High Score: 0",align="center",font=("Courier",24,"normal"))


#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor() + 20
        head.sety(y)
    if head.direction == "down":
        y = head.ycor() - 20
        head.sety(y)
    if head.direction == "right":
        x = head.xcor() + 20
        head.setx(x)
    if head.direction == "left":
        x = head.xcor() - 20
        head.setx(x)



#keyboard binding
wn.listen()
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_up,"Up")
#for wsad
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_up,"w")

#main game loop
while True:
    wn.update()

    #Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"
        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)
            #clear segments list
        segments.clear()
        #reset score and delay
        delay = 0.1
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    #Check for a collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay 
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    # move body 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to head last position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #Check for a head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear segments list
            segments.clear()
            #reset score and delay
            delay = 0.1
            score = 0
            pen.clear()
            pen.write("Score: {} Higt Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))


    time.sleep(delay)

wn.mainloop()
