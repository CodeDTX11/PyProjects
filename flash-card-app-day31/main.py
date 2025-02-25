import tkinter
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT_STYLE = ("Ariel", 40, "italic")
WORD_FONT_STYLE = ("Ariel", 60, "bold")

START_CSV_FILE = "./data/french_words.csv"
UPDATED_CSV_FILE = "./data/words_to_learn.csv"

current_card = {}

learned_words = []

# --------------------------------------------------------------------------- #

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(flash_words_list)
    dict_keys = list(current_card.keys())

    # print(dict_keys)
    # print(dict_keys[0])
    canvas.itemconfig(card_title, text=dict_keys[0], fill="black")
    canvas.itemconfig(card_word, text=current_card[dict_keys[0]], fill="black")

    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(2000, flip_card)

def flip_card():

    dict_keys = list(current_card.keys())

    canvas.itemconfig(canvas_image, image=card_back_img)
    # canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_title, text=list(current_card.keys())[1], fill="white")
    # canvas.itemconfig(card_word, text=current_card["English"] , fill="white")
    canvas.itemconfig(card_word, text=current_card[list(current_card.keys())[1]] , fill="white")

def save_card():
    flash_words_list.remove(current_card)
    learned_words.append(current_card)
    # print(len(flash_words_dict))

    if len(flash_words_list) > 0:
        next_card()
    else:
        print("Word list is empty")
# --------------------------------------------------------------------------- #

window = tkinter.Tk()
window.title("Flash!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    flash_words_df = pandas.read_csv(UPDATED_CSV_FILE)
except FileNotFoundError:
    flash_words_df = pandas.read_csv(START_CSV_FILE)

# print(flash_words_df)

flash_words_list = flash_words_df.to_dict('records')
# french_english_dict = french_english_df.to_dict()
# print(flash_words_list)

canvas = tkinter.Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 270, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="title", font=TITLE_FONT_STYLE)

card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT_STYLE)

x_image = tkinter.PhotoImage(file="./images/wrong.png")
x_button = tkinter.Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

check_image = tkinter.PhotoImage(file="./images/right.png")
check_button = tkinter.Button(image=check_image, highlightthickness=0, command=save_card)
check_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()

words_to_learn = pandas.DataFrame(flash_words_list)
words_to_learn.to_csv("./data/words_to_learn.csv", index=False)