import tkinter


window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=600, height=600)
# Functions


def button_test():
    my_label.config(text="button works,challenge complete")


def on_button_click():
    my_label.config(text=inp.get())


# Label
my_label = tkinter.Label(text="New Text", font=("Arial", 20, "bold"))
my_label.pack()


# Button


button = tkinter.Button(text="click me", command=on_button_click)
button.pack()


inp = tkinter.Entry()
inp.pack()

window.mainloop()
