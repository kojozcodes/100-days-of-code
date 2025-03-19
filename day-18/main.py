import turtle
import random

colours = [
    "CornflowerBlue", "DarkOrchid",
    "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat",
    "SlateGray", "SeaGreen"
]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('red')
# timmy.forward(100)
# timmy.right(90)


# Draw a Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


# draw multiple shapes
# def draw_shapes(num_of_sides):
#     for side in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(360/num_of_sides)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shapes(shape_side_n)

# Generate a random walk
# directions = [0, 90, 180, 270]
# timmy.pensize(20)
timmy.speed(0)
# for _ in range(100):
#     timmy.color(random_color())
#     timmy.forward(50)
#     timmy.setheading(random.choice(directions))


# Draw a spirograph
def draw_spirograph(number_of_circles):
    timmy.hideturtle()
    current_heading = timmy.heading()
    for _ in range(number_of_circles):
        timmy.color(random_color())
        current_heading += 360 / number_of_circles
        timmy.circle(100)
        timmy.setheading(current_heading)


draw_spirograph(50)
screen = turtle.Screen()
screen.exitonclick()
