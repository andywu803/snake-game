# imports
import turtle
import random
import time

# Create the game screen
screen = turtle.Screen()
screen.title('Snake Game')
screen.setup(width = 800, height = 800)
screen.tracer(0)
screen.bgcolor('black')

# create score variables
delay = 0.1
score = 0
high_score = 0

# create the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('orange')
snake.penup()
snake.goto(0,0)
snake.direction = 'Stop'

body = []

# create the fruits
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(0, 100)

# display the scores
scoring = turtle.Turtle()
scoring.speed(0)
scoring.shape('square')
scoring.color('white')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 250)
scoring.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

# keys for snake movement
def up():
    if snake.direction != "down":
        snake.direction = "up"

def down():
    if snake.direction != "up":
        snake.direction = "down"

def left():
    if snake.direction != "right":
        snake.direction = "left"

def right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "s")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "a")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "d")
screen.onkeypress(right, "Right")

# Gameplay Mechanics
while True:
    screen.update()
    # snake death
    if snake.xcor() > 380 or snake.xcor() < -380 or snake.ycor() > 380 or snake.ycor() < -380:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "Stop"
        for segment in body:
            segment.goto(1000, 1000)
        body.clear()
        score = 0
        delay = 0.1
        scoring.clear()
        scoring.write("Score: {}  High Score: {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    if snake.distance(fruit) < 20:
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        fruit.goto(x, y)
        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        body.append(new_segment)
        delay = delay - 0.001
        score = score + 1
        if score > high_score:
            high_score = score
        scoring.clear()
        scoring.write("Score: {}  High Score: {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    # check collision between head and body
    for i in range(len(body)-1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)
    move()
    for segment in body:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "Stop"
            for segment in body:
                segment.goto(1000, 1000)
            body.clear()
            score = 0
            delay = 0.1
            scoring.clear()
            scoring.write("Score: {}  High Score: {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

screen.mainloop()