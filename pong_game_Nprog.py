import turtle

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("red")
wn.setup(width=1000, height=650)
wn.tracer(0)
Paddle1 = turtle.Turtle()
Paddle1.speed(0)
Paddle1.shape("square")
Paddle1.color("black")
Paddle1.penup()
Paddle1.goto(-400, 0)
Paddle1.shapesize(stretch_wid=7, stretch_len=2)

Paddle2 = turtle.Turtle()
Paddle2.speed(0)
Paddle2.shape("square")
Paddle2.color("black")
Paddle2.penup()
Paddle2.goto(400, 0)
Paddle2.shapesize(stretch_wid=7, stretch_len=2)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.goto(0, 0)
ball.dx = .4
ball.dy = .3


# P1motion
def up1():
    y = Paddle1.ycor()
    y += 20
    Paddle1.sety(y)


def dw1():
    y = Paddle1.ycor()
    y -= 20
    Paddle1.sety(y)


# p2motion
def up2():
    y = Paddle2.ycor()
    y += 20
    Paddle2.sety(y)


def dw2():
    y = Paddle2.ycor()
    y -= 20
    Paddle2.sety(y)


# p2key
wn.listen()
wn.onkeypress(up1, "w")
wn.onkeypress(dw1, "s")

# p2key
wn.listen()
wn.onkeypress(up2, "Up")
wn.onkeypress(dw2, "Down")
while True:
    wn.update()

#ballmotion
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 320:
        ball.sety(320)
        ball.dy *= -1
    if ball.ycor() < -320:
        ball.sety(-320)
        ball.dy *= -1
    if ball.xcor() > 440:
        ball.goto(0, 0)

