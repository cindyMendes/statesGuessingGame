import turtle
import pandas

# Alabama,139,-77
# California,-297,13
# Florida,220,-145
# Arkansas,57,-53


screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # get the coordinates of a click on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # so the screen doesnt close


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                     prompt="What's another state's name? ").title()

    if answer_states == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # The line above replace the code below
        # missing_states = []
        #   for state in all_states:
        #       if state not in guessed_states:
        #           missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_states in all_states:
        guessed_states.append(answer_states)
        answer_states_row = data[data.state == answer_states]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(answer_states_row.x), int(answer_states_row.y))
        t.write(answer_states)
        # t.write(answer_states_row.state.item())
    else:
        print(f"{answer_states} is not a state.")


