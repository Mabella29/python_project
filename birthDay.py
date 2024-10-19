import turtle

# Setup the screen
bg = turtle.Screen()
bg.bgcolor("black")
turtle.hideturtle()

# Set the pen properties
turtle.pensize(3)


# Draw horizontal lines (as cake layers)
def draw_cake_layer(y_pos, width):
    turtle.penup()
    turtle.goto(-width // 2, y_pos)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(width)


draw_cake_layer(-180, 330)
draw_cake_layer(-150, 305)
draw_cake_layer(-120, 280)

# Draw the cake (pink rectangle)
turtle.penup()
turtle.goto(-95, -100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(190)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(190)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Draw candles
positions = [-75, -25, 25, 75]
colors = ["red", "blue", "yellow", "green"]

for i, pos in enumerate(positions):
    # Candle sticks
    turtle.penup()
    turtle.goto(pos, 20)
    turtle.color(colors[i])
    turtle.pendown()
    turtle.forward(20)

    # Candle flames
    turtle.penup()
    turtle.goto(pos, 30)
    turtle.color("red")
    turtle.pendown()
    turtle.forward(3)

# Draw circles around the cake
turtle.penup()
turtle.goto(10, -60)
turtle.pendown()

circle_colors = ["red", "orange", "brown", "green", "blue", "purple", "grey"]
for each_color in circle_colors:
    angle = 360 / len(circle_colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Add birthday message text
turtle.penup()
turtle.goto(-160, 50)
turtle.color("white")
turtle.pendown()

turtle.write("Happy birthday Love ❤️", font=("Poppins", 25, "normal"))

# Complete drawing
turtle.done()