from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # it's needed to remove right answer of the list

# when starts at the first time, data = 'french_words.csv', else data uses remained words "words_to_learn.csv"
try:
    data = pd.read_csv("data/words_to_learn.csv")  # read .csv with pandas
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")  # transform to dict
else:
    data_dict = data.to_dict(orient="records")  # transform to dict


# when click button, get next card
def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)  # to fix the bug, when click more than one time
    current_card = choice(data_dict)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    flip_timer = window.after(3000, english_answer, current_card)  # current_card is a parameter of english_answer


# remove the word when the user knows the answer, then it creates a .csv file to use when restart the game
def right_function():
    data_dict.remove(current_card)  # remove right answer

    data_df = pd.DataFrame(data=data_dict)  # create a dataframe
    data_df.to_csv("data/words_to_learn.csv", index=False)  # turn into .csv to use when restart the game

    next_card()  # call next card function


# after 3 seconds, flip the card and get the english answer
def english_answer(card):
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")


# ------------------------- WINDOW ------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, next_card)  # to fix the bug, when click more than one time

# defining front and back images
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# canvas configuration
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_img)  # set to a variable allows use into the function
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # set to a variable too
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))   # set to a variable too
canvas.grid(row=0, column=0, columnspan=2)

# ------------------------- BUTTONS ------------------------- #
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_function)
right_button.grid(row=1, column=1)

next_card()  # call the function to change the names before click either

window.mainloop()
