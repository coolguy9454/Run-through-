import turtle
import random
import time

# Create window
wn = turtle.Screen()
wn.setup(500, 600)
wn.title("Super Run Through!")
wn.bgcolor("khaki")
wn.tracer(0)

# Water
water = turtle.Turtle()
water.penup()
water.color("skyblue")
water.shape("square")
water.shapesize(30, 30)
water.goto(0, -150)

# Map
road = turtle.Turtle()
road.penup()
road.color("saddlebrown")
road.shape("square")
road.shapesize(22, 15)
road.goto(0, -20)

# Player
player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("sandybrown")
player.shape("circle")
player.shapesize(1, 1)
player.goto(0, -200)
player.direction = "front"

# Turtle
turtles = []

for _ in range(120):
    tur = turtle.Turtle()
    tur.penup()
    tur.color("green")
    tur.shape("turtle")
    tur.right(90)
    tur.goto(0, -300)

    turtles.append(tur)

# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 200)
pen.pendown()
pen.write("0", align = "center", font = ("Impact", 40, "normal"))

# Pen die
pen_die = turtle.Turtle()
pen_die.hideturtle()
pen_die.penup()
pen_die.color("red")
pen_die.goto(0, 0)
pen_die.pendown()

# Virable
score = 0

# Player turns

def turn_front():
    player.direction = "front"

def turn_back():
    player.direction = "back"

def turn_left():
    player.direction = "left"

def turn_right():
    player.direction = "right"

# Keyboard blinding
wn.listen()
wn.onkeypress(turn_front, "Up")
wn.onkeypress(turn_back, "Down")
wn.onkeypress(turn_left, "Left")
wn.onkeypress(turn_right, "Right")

# Main game loop
while True:
    wn.update()

    # Player moves
    if player.direction == "front":
        player.sety(player.ycor() + 1)

    if player.direction == "back":
        player.sety(player.ycor() - 2.5)
        
    if player.direction == "left":
        player.setx(player.xcor() - 2)

    if player.direction == "right":
        player.setx(player.xcor() + 2)

    # Off boundary checking
    if player.ycor() > 190:
        player.sety(190)

    if player.xcor() > 160 or player.xcor() < -160 or player.ycor() < -250:
        pen_die.write("Game over!", align = "center", font = ("Impact", 50, "normal"))
        time.sleep(3)
        player.goto(0, -200)
        player.direction = "front"
        score = 0
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))

        for tur in turtles:
            tur.goto(0, -300)

    # tur setup
    for tur in turtles:
        tur.forward(1.5)

        # Tur position
        if tur.ycor() < -300:
            tur.goto(random.randint(-140, 140), random.randint(300, 1200))
            tur.color("green")
                
        # Player with tur collision
        if player.distance(tur) < 20 and player.ycor() < tur.ycor():
            player.sety(player.ycor() - 3)

        if player.distance(tur) < 20 and player.ycor() > tur.ycor():
            player.sety(player.ycor() + 3)

        # Tur with water collision
        if tur.ycor() < -250:
            tur.color("mediumturquoise")

        # Score
        if tur.ycor() < -299:    
            pen.clear()
            score = score + 1
            pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))