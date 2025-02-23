from tkinter import *
from tkinter import messagebox
import random
#pyperclip used for clipboard interaction
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters = int(input("How many letters would you like in your password?\n"))
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # Hard level
    # for char in range(0, nr_letters):
    #     password_list.append(random.choice(letters))

    char_list = [random.choice(letters) for _ in range(random.randint(8, 10))]

    # for char in range(0, nr_symbols):
    #     password_list.append(random.choice(symbols))

    num_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    # for char in range(0, nr_numbers):
    #     password_list.append(random.choice(numbers))

    symb_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = char_list + num_list + symb_list

    # print(password_list)
    random.shuffle(password_list)
    # print(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_uname = email_uname_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure input is not empty")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"Ok to save info?\n"
                                                      f"{email_uname}\n"
                                                      f"{password}")
        if is_ok:
            with open(file="data.txt", mode="a") as data:
                data.write(f"{website} | {email_uname} | {password}\n")

            website_input.delete(0,END)
            password_input.delete(0,END)

            # messagebox.showinfo("Info", "Save successful")

# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_uname_label = Label(text="Email/Username:")
email_uname_label.grid(row=2, column=0)

email_uname_input = Entry(width=40)
email_uname_input.grid(row=2, column=1, columnspan=2)
email_uname_input.insert(0, "dummy@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=gen_password)
gen_password_button.grid(row=3, column=2, sticky="e", padx=0)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()