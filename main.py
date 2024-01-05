import time
import turtle
import pandas as pd
import random
import numpy as np

df = pd.DataFrame(columns=["x_in", "y_in", "change", "x_fin"])

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


screen.tracer(1)

x_pos_in = 0
y_pos_in = 0

dictionary = {
    20 : 1,
    -20 : 2
}

for i in range(1000000):
    if ball.xcor() >= 240:
        x_change = -20;
        x_pos_in = ball.xcor()
        y_pos_in = ball.ycor()
    elif ball.xcor() <= -240:
        x_change = 20;
        x_pos_in = ball.xcor()
        y_pos_in = ball.ycor()
    if ball.ycor() >= 280:
        # Saving of the data happens here
        df.loc[df.size+1] = np.array([x_pos_in, y_pos_in, dictionary[x_change], ball.xcor()])
        y_change = -20;
        screen.tracer(0)
        ball.sety(-20)
        ball.setx(random.randint(-12, 12) * 20)
        screen.tracer(1)
    elif ball.ycor() <= -340:
        y_change = 20;
    screen.tracer(0)
    ball.setpos(ball.xcor()+x_change, ball.ycor() + y_change)
    screen.tracer(1)
df.to_csv("data.csv")