# Step 1 Set up turtle and time
import turtle
import time
turtle.title("Amol Blog Jai Shree Ram")
turtle.bgcolor('black')

# Step 2 create a Kalpavriksha branch function
def draw_branch(length, depth):
    if depth == 0:
        return

    # Draw the main branch
    turtle.forward(length)
    turtle.right(20)

    # Draw the right branch
    draw_branch(length * 0.8, depth - 1)
    turtle.left(40)

    # Draw the left branch
    draw_branch(length * 0.8, depth - 1)
    turtle.right(20)

    # Return to the starting position
    turtle.backward(length)

#Step 3 set turtle size, colour, speed and more
turtle.pensize(4)
turtle.color('gold')
turtle.left(90)
turtle.speed('fastest')
turtle.penup()
turtle.backward(200)
turtle.pendown()

# Step 4 Create 90c tall with 8 branch of Kalpavriksha
draw_branch(90, 8)

# Set up the screen
screen = turtle.Screen()

# Step 5 Draw the letters for "Jai Shree Ram"
text = turtle.Turtle()
text.speed(0)
text.color("gold")
text.pensize(5)

# Move to the starting position
text.penup()
text.goto(0, 200)
text.pendown()

# write "Jai Shree Ram"
text.write("जय श्री राम", align="center", font=("Arial", 50, "bold"))

# Hide the turtle cursor
text.hideturtle()

# Step 6 set turtle Background 6 colors
t = turtle.Turtle()
colors = ["purple", "light slate gray", "dim gray", "cornflower blue" , "orange red", "black"]

for color in colors:
    t.screen.bgcolor(color)
    time.sleep(1)


# Step 7 close the window after clicking
turtle.exitonclick()