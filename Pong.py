#pong game in python
import turtle
import winsound
import sys

win = turtle.Screen()
win.title('pong gemaakt door mo7abouyi')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

#score
scoreA = 0
scoreB = 0

#stokA
stokA = turtle.Turtle()
stokA.speed(0)
stokA.shape('square')
stokA.color('white')
stokA.shapesize(stretch_wid=5, stretch_len=1)
stokA.penup()
stokA.goto(-350, 0)
#stokB
stokB = turtle.Turtle()
stokB.speed(0)
stokB.shape('square')
stokB.color('white')
stokB.shapesize(stretch_wid=5, stretch_len=1)
stokB.penup()
stokB.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0   Player B: 0', align='center', font=('Courier', 24, 'normal'))

#stokA boven
def stokA_up():
    y = stokA.ycor()
    y += 15
    stokA.sety(y)

def stokA_down():
    y = stokA.ycor()
    y -= 15
    stokA.sety(y)

#stokB boven
def stokB_up():
    y = stokB.ycor()
    y += 15
    stokB.sety(y)

def stokB_down():
    y = stokB.ycor()
    y -= 15
    stokB.sety(y)



#toetsenbord verbinding
win.listen()
win.onkeypress(stokA_up, 'w')
win.onkeypress(stokA_down, 's')
win.onkeypress(stokB_up, 'Up')
win.onkeypress(stokB_down, 'Down')




#game loop
while True:
    win.update()
    #ball bewegen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # grens check voor bal
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        #winsound.PlaySound("test.wav", winsound.SND_ASYNC)


    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        #winsound.PlaySound('test.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))
    
    #stok en ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < stokB.ycor() + 50 and ball.ycor() > stokB.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < stokA.ycor() + 50 and ball.ycor() > stokA.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1