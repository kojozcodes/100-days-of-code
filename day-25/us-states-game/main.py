import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    if len(guessed_states) > 0:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States Correct",
                                        prompt="What's another state's name")
    else:
        answer_state = screen.textinput(title="Guess the states", prompt="Write a state's name")

    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in guessed_states:
        answer_state_x = data[data.state == answer_state].x.item()
        answer_state_y = data[data.state == answer_state].y.item()
        timmy.goto(answer_state_x, answer_state_y)
        timmy.write(f"{answer_state}", align="center", font=("Courier", 10, "bold"))
        guessed_states.append(answer_state)

missing_states = {}
list_missing_states = [state for state in states if state not in guessed_states]
missing_states["Missing States"] = list_missing_states

missing_states_df = pandas.DataFrame(missing_states)
missing_states_df.to_csv("missing_states.csv")


