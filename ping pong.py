import turtle
import pygame
#creating a screen
wind = turtle.Screen()
wind.title('ping pong game')
wind.bgcolor('black')
wind.setup(width=800, height=600)
wind.tracer(0)

# bar A
bar_A = turtle.Turtle()
bar_A.shape('square')
bar_A.color('white')
bar_A.shapesize(stretch_wid=5, stretch_len=1)
bar_A.penup()
bar_A.goto(-350,0)

#bar B
bar_B = turtle.Turtle()
bar_B.shape('square')
bar_B.color('white')
bar_B.shapesize(stretch_wid=5, stretch_len=1)
bar_B.penup()
bar_B.goto(350,0)

# Making a ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('Blue')
ball.penup()
ball.goto(0,0)
ball_x = 0.7
ball_y = 0.7

#score
sboard = turtle.Turtle()
sboard.shape('square')
sboard.color('white')
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)
sboard.write("Player A: 0 PLayer B: 0", align="center", font=("courier", 24, 'normal'))

score_a = 0
score_b = 0





# functions
def bar_A_up():
    y = bar_A.ycor()
    y += 30
    bar_A.sety(y)
    
def bar_A_down():
    y = bar_A.ycor()
    y -= 30
    bar_A.sety(y)

def bar_B_up():
    y = bar_B.ycor()
    y += 30
    bar_B.sety(y)

def bar_B_down():
    y = bar_B.ycor()
    y -= 30
    bar_B.sety(y)

# keyboard binding
wind.listen()
wind.onkeypress(bar_A_up, 'w')
wind.onkeypress(bar_A_down, 's')
wind.onkeypress(bar_B_up, 'p') 
wind.onkeypress(bar_B_down, 'l')






while True:
    wind.update()

    #ball movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)
    
    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1

    #score
    if ball.xcor() > 350:
        score_a += 1
        sboard.clear()
        sboard.write("PLayer A: {} Player B: {}".format(score_a, score_b), align='center', font=('courier', 24, 'normal'))
        ball.goto(0,0)
        ball_x *= -1
    elif ball.xcor() < -350:
        score_b += 1
        sboard.clear()
        sboard.write("PLayer A: {} Player B: {}".format(score_a, score_b), align='center', font=('courier', 24, 'normal'))
        ball.goto(0,0)
        ball_x *= -1



    #collision with bars

    if ball.xcor() < -340 and ball.ycor() < bar_A.ycor() + 50 and ball.ycor() > bar_A.ycor() -50:
        ball_x *= -1
    elif ball.xcor() > 340 and ball.ycor() < bar_B.ycor() + 50 and ball.ycor() > bar_B.ycor() -50:
        ball_x *= -1