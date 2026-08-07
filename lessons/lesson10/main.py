import tkinter

# creating window
window = tkinter.Tk()
# add a title to window
window.title("My First GUI Program")
# sizing window
window.minsize(width=500, height=300)


def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")


def get_input_value():
    input_value = input.get()
    my_label.config(text=f"{input_value}")


# label component
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# button component
button = tkinter.Button(text="Click Me", command=get_input_value)
button.grid(column=1, row=1)

# entry component
input = tkinter.Entry(width=10)
input.grid(column=2, row=2)


window.mainloop()
