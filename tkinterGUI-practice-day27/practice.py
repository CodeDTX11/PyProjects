import tkinter

window = tkinter.Tk()
window.title("GUI Prog")
window.minsize(width=600, height=300)

#label

def add(*argies):
    num = 0
    for n in argies:
        num += n
    print(num)
# add(1,2,3)

def calculate(**kwargs):
    var1 = kwargs.get("var1")
    var2 = kwargs.get("var2")

calculate(var1="idk")

my_label = tkinter.Label(text="Label here", font=("Ariel", 24, "bold"))
my_label.pack()
# my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="Even newer text")

def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="Click here", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.insert(0, "idk")
input.pack()

window.mainloop()
