from tkinter import *

# constant
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# countdown timer
timer = None


def count_down(count):
    global timer

    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)


def reset_timer():
    global timer

    if timer:
        window.after_cancel(timer)
        timer = None

    canvas.itemconfig(timer_text, text="00:00")


# ui setup
window = Tk()
window.title("Podomoro")
window.config(padx=100, pady=50, bg=YELLOW)

# add label
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

# add image to canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="python-lab/lessons/lesson10/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# add text to canvas
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=2, row=2)


# add buttons
button_start = Button(
    text="Start",
    font=(FONT_NAME, 18, "bold"),
    bg=YELLOW,
    fg=GREEN,
    highlightthickness=0,
    borderwidth=0,
    padx=10,
    pady=5,
    command=lambda: count_down(WORK_MIN * 60),
)
button_start.grid(column=1, row=3)

button_reset = Button(
    text="Reset",
    font=(FONT_NAME, 18, "bold"),
    bg=YELLOW,
    fg=RED,
    highlightthickness=0,
    borderwidth=0,
    padx=10,
    pady=5,
    command=reset_timer,
)
button_reset.grid(column=3, row=3)

# add check mark label
check_mark_label = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=2, row=4)

window.mainloop()
