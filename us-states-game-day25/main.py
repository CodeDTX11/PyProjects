import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE = "blank_states_img.gif"
CSV_FILE = "50_states.csv"

screen.addshape(IMAGE)
turtle.shape(IMAGE)

# used to get coordinates of the states on the map
# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_data = pandas.read_csv(CSV_FILE)

state_names = state_data.state.to_list()

cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()

correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in state_names:
        #     if state not in correct_guesses:
        #         missing_states.append(state)

        # alternate way using list comprehension
        missing_states = [item for item in state_names if item not in correct_guesses]

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")

        break

    item = state_data[state_data.state == answer_state]

    if len(item) != 0:
        # print(item.state)
        if answer_state not in correct_guesses:
            coordinates = (item.x.item() , item.y.item())
            cursor.goto(coordinates)
            correct_guesses.append(answer_state)

            cursor.write(item.state.item())
        else:
            print(f"{answer_state} already guessed")
    else:
        print("wrong")


# screen.exitonclick()