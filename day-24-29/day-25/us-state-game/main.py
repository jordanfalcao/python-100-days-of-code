import turtle
from write_names import WriteNames
import pandas as pd

# import Turtle

screen = turtle.Screen()
screen.title("U.S. States Games")

# add the image as shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # how to get the coordinates from each state by clicking on the image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# # every click on the image prints the coordinates
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# write_names = WriteNames()

db = pd.read_csv("50_states.csv")
state_list = db.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in state_list:
        guessed_states.append(answer_state)
        line = db[db.state == answer_state]
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.up()
        t1.goto(int(line.x), int(line.y))
        t1.write(answer_state, align="center", font=("Courier", 7, "normal"))

    # if user type "Exit", create a .csv file with all missing States
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("states_to_learn.csv")
        break


