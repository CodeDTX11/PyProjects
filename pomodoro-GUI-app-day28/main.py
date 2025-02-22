from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

CHECK_MARK = "✔"
timer = None
reps = 0
chk_marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    wrk = WORK_MIN * 60
    s_brk = SHORT_BREAK_MIN * 60
    l_brk = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(7)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(3)
    else:
        # print("here")
        count_down(5)
        # print("after")
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    min = count // 60
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        # print("a")
        global timer
        timer = window.after(1000, count_down, count - 1)
        # print("b")
    else:
        start_timer()
        marks = ""

        for _ in range(math.floor(reps/2)):
            marks += CHECK_MARK
        # print("adfasfd")
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()