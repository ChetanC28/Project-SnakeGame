import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
gm = turtle.Screen()
gm.title("Snake Game by @TokyoEdTech")
gm.bgcolor("black")
gm.setup(width=600, height=600)
gm.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

def write():
    pen.clear()
    pen.goto(0, 260)
    if high_score == 0:
        pen.write("Score: 0 | High Score: 0", align="center", font=("Courier", 24, "normal"))
    else:
        pen.write("Score: {} | High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    pen.goto(0,220)
    pen.write("---------------------------", align="center", font=("Courier",45,"bold"))
write()



# Functions
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
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
gm.listen()
gm.onkeypress(go_up, "Up")
gm.onkeypress(go_down, "Down")
gm.onkeypress(go_left, "Left")
gm.onkeypress(go_right, "Right")

# Main game loop
while True:
    gm.update()

    # Check for a collision with the border
    if head.xcor()>260 or head.xcor()<-270 or head.ycor()>200 or head.ycor()<-270:
        time.sleep(0.25)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        
        write()


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-270, 260)
        y = random.randint(-270, 200)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        
        write()

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            write()
    time.sleep(delay)
