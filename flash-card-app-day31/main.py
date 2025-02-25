import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT_STYLE = ("Ariel", 40, "italic")
WORD_FONT_STYLE = ("Ariel", 60, "bold")

CSV_FILE = "./data/french_words.csv"

# --------------------------------------------------------------------------- #

def new_word():
    word = random.choice(french_english_dict)["French"]

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=word)
    # print(FRENCH_WORD)
# --------------------------------------------------------------------------- #

window = tkinter.Tk()
window.title("Flash!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

french_english_df = pandas.read_csv(CSV_FILE)
# print(type(french_english_df))

french_english_dict = french_english_df.to_dict('records')
# french_english_dict = french_english_df.to_dict()
print(french_english_dict)

canvas = tkinter.Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file="./images/card_front.png")

canvas.create_image(400, 270, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="title", font=TITLE_FONT_STYLE)

card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT_STYLE)

x_image = tkinter.PhotoImage(file="./images/wrong.png")
x_button = tkinter.Button(image=x_image, highlightthickness=0, command=new_word)
x_button.grid(row=1, column=0)

check_image = tkinter.PhotoImage(file="./images/right.png")
check_button = tkinter.Button(image=check_image, highlightthickness=0, command=new_word)
check_button.grid(row=1, column=1)

new_word()

window.mainloop()