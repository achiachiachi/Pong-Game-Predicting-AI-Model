import time
import turtle
import pandas as pd
import numpy as np
import joblib
import random

loaded_model = joblib.load("model.pkl")

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.setup(500, 700)
screen.tracer(0)
ball = turtle.Turtle(shape="square")
ball.color("#ffffff")
ball.shapesize(2, 2)
ball.penup()
ball.setpos(0, -60)
x_change = 20
y_change = -20

square1 = turtle.Turtle(shape="square")
square1.penup()
square1.color("#ffffff")
square1.shapesize(2,2)
square1.setpos(-60, 320)
square2 = turtle.Turtle(shape="square")
square2.penup()
square2.color("#ffffff")
square2.shapesize(2,2)
square2.setpos(-20, 320)
square3 = turtle.Turtle(shape="square")
square3.penup()
square3.color("#ffffff")
square3.shapesize(2,2)
square3.setpos(20, 320)
square4 = turtle.Turtle(shape="square")
square4.penup()
square4.color("#ffffff")
square4.shapesize(2,2)
square4.setpos(60, 320)


dictionary = {
    20: 1,
    -20: 2
}
screen.tracer(1)
while True:
    #"Ball_x_pos","Square2", "Square3", "Dir" ,"Move","Score"
    if (ball.xcor() >= square1.xcor()-20 and ball.xcor() <= square4.xcor()+20 and ball.ycor() >= 280):
        y_change = -20

    if ball.xcor() >= 240:
        x_change = -20;
        turtle.tracer(0)
        center = loaded_model.predict(pd.DataFrame(np.array([ball.xcor(), ball.ycor(), dictionary[x_change]])).T)
        square1.setx(center[0]-60)
        square2.setx(center[0]-20)
        square3.setx(center[0]+20)
        square4.setx(center[0]+60)

        turtle.tracer(1)
    elif ball.xcor() <= -240:
        x_change = 20;
        turtle.tracer(0)
        center = loaded_model.predict(pd.DataFrame(np.array([ball.xcor(), ball.ycor(), dictionary[x_change]])).T)
        square1.setx(center[0]-60)
        square2.setx(center[0]-20)
        square3.setx(center[0]+20)
        square4.setx(center[0]+60)
        turtle.tracer(1)
    if ball.ycor() >= 340:
        screen.bgcolor("red")
        y_change = -20;
        screen.tracer(0)
        ball.sety(-20)
        ball.setx(random.randint(-12, 12) * 20)
        screen.tracer(1)
        screen.bgcolor("black")
    elif ball.ycor() <= -340:
        y_change = 20;
    screen.tracer(0)
    ball.setpos(ball.xcor()+x_change, ball.ycor()+y_change)
    screen.tracer(1)
    time.sleep(0.01)
