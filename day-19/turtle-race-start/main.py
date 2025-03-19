import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
is_race_on = False

starting_x = -230
starting_y = -100

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=starting_x, y=starting_y)
    starting_y += 40
    turtle_list.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            turtle.setheading(180)
        if turtle.xcor() < -230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
