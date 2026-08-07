import tkinter

# creating window
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=700, height=500)


def calculate():
    miles_values = miles.get()
    km = float(miles_values) * 1.60934
    result_label.config(text=f"{km:.2f}")


miles = tkinter.Entry(width=10)
miles.pack()

label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
label.pack()

button = tkinter.Button(text="Calculate", command=calculate)
button.pack()

result_label = tkinter.Label(text="0", font=("Arial", 24))
result_label.pack()

window.mainloop()
