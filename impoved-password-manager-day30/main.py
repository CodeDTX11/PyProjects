from tkinter import *
from tkinter import messagebox
import random
#pyperclip used for clipboard interaction
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [random.choice(letters) for _ in range(random.randint(8, 10))]

    num_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    symb_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = char_list + num_list + symb_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_uname = email_uname_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email_uname,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure input is not empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Ok to save info?\n"
                                                      f"{email_uname}\n"
                                                      f"{password}")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as data_file:
                    #reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #updatating data
                data.update(new_data)

                with open(file="data.json", mode="w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0,END)
                password_input.delete(0,END)

            # messagebox.showinfo("Info", "Save successful")
# ---------------------------- SEARCH --------------------------------------- #
def search():
    website = website_input.get()
    if len(website) > 0:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        else:
            try:
                found_entry = data[website]
            except KeyError:
                messagebox.showinfo(title="Sorry", message=f'The website "{website}" was not found')
            else:
                messagebox.showinfo(title=f"{website}", message=f"Email: {found_entry["email"]}\n"
                                                                f"Password: {found_entry["password"]}")

# ---------------------------- UI SETUP ------------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, sticky=EW)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=W)

website_input = Entry(width=32)
website_input.grid(row=1, column=1, columnspan=2, sticky=W)
website_input.focus()

search_button = Button(text="Search", command=search, bg="lightblue")
search_button.grid(row=1, column=2, stick=EW)

email_uname_label = Label(text="Email/Username: ")
email_uname_label.grid(row=2, column=0, sticky=W)

email_uname_input = Entry()
email_uname_input.grid(row=2, column=1, columnspan=2, sticky=EW)
email_uname_input.insert(0, "dummy@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=W)

password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky=W)

gen_password_button = Button(text="Generate Password", command=gen_password)
gen_password_button.grid(row=3, column=2, sticky=EW)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()