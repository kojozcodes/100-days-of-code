from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def anti_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=anti_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
