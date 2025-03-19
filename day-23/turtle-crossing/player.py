from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_DIRECTION = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line_y = FINISH_LINE_Y
        self.shape('turtle')
        self.penup()
        self.setheading(PLAYER_DIRECTION)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
