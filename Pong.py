import turtle
#import os # Linux and MAC # <os.system("afplay {name}&")> for MAC or <os.system("aplay{name}&")> for Linux
import winsound #windows # <winsound.PlaySound("{name}", winsound.SND_ASYNC)>

# Screen
xs = 800
ys = 600
wd = turtle.Screen()
wd.title("Atari Pong recriation by hss")
wd.bgcolor("black")
wd.setup(width = xs, height = ys)
wd.tracer(0)

# Scores
score1 = 0
score2 = 0
living = True

# Left
racket_left = turtle.Turtle()
racket_left.speed(0)
racket_left.shape("square")
racket_left.color("blue")
racket_left.shapesize(stretch_wid = 5, stretch_len = 1)
racket_left.penup()
racket_left.goto(-(xs / 2 - 50), 0)

# Right
racket_right = turtle.Turtle()
racket_right.speed(0)
racket_right.shape("square")
racket_right.color("blue")
racket_right.shapesize(stretch_wid = 5, stretch_len = 1)
racket_right.penup()
racket_right.goto((xs / 2 - 50), 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (ys / 4))
pen.write("{}             {}".format(score1, score2), align="center", font=("arialblack", 64, "bold"))

# Functions of rackets movements
## Left
def racket_left_up():
    y = racket_left.ycor()
    y += 20
    racket_left.sety(y)
    if y > (ys / 2 - 50):
        racket_left.sety(ys / 2 - 50)

def racket_left_down():
    y = racket_left.ycor()
    y -= 20
    racket_left.sety(y)
    if y < -(ys / 2 - 50):
        racket_left.sety(-ys / 2 + 50)

## Right

def racket_right_up():
    y = racket_right.ycor()
    y += 20
    racket_right.sety(y)
    if y > (ys / 2 - 50):
        racket_right.sety(ys / 2 - 50)

def racket_right_down():
    y = racket_right.ycor()
    y -= 20
    racket_right.sety(y)
    if y < -(ys / 2 - 50):
        racket_right.sety(-ys / 2 + 50)

# Binding
wd.listen()
wd.onkeypress(racket_left_up, "w")
wd.onkeypress(racket_left_down, "s")
wd.onkeypress(racket_right_up, "Up")
wd.onkeypress(racket_right_down, "Down")

# Main
while living != False:
    wd.update()

    # Square movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border limit check
    ## Y
    if ball.ycor() > (ys / 2 - 10):
        ball.sety((ys / 2 - 10))
        ball.dy *= -1
        winsound.PlaySound("Pong.wav", winsound.SND_ASYNC)

    if ball.ycor() < -(ys / 2 - 10):
        ball.sety(-(ys / 2 - 10))
        ball.dy *= -1
        winsound.PlaySound("Pong.wav", winsound.SND_ASYNC)

    ## X
    if ball.xcor() > (xs / 2 - 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("{}             {}".format(score1, score2), align="center", font=("arialblack", 64, "bold"))

    if ball.xcor() < -(xs / 2 - 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("{}             {}".format(score1, score2), align="center", font=("arialblack", 64, "bold"))

    # Collisions
    if (ball.xcor() > (xs / 2 - 60) and ball.xcor() < (xs / 2 - 50)) and (ball.ycor() < racket_right.ycor() + 50 and ball.ycor() > racket_right.ycor() - 50):
        ball.setx((xs / 2 - 60))
        ball.dx *= -1
        winsound.PlaySound("Pong.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -(xs / 2 - 60) and ball.xcor() > -(xs / 2 - 50)) and (ball.ycor() > racket_left.ycor() - 50 and ball.ycor() < racket_left.ycor() + 50):
        ball.setx(-(xs / 2 - 60))
        ball.dx *= -1
        winsound.PlaySound("Pong.wav", winsound.SND_ASYNC)


    # END
    if score1 == 10 or score2 == 10:
        check = turtle.textinput("Continue...","Play again? \n1 = yes\n 0 = no")
        if check == '1':
            score1 = 0
            score2 = 0
            pen.clear()
            pen.write("{}             {}".format(score1, score2), align="center", font=("arialblack", 64, "bold"))
        else:
            living = False