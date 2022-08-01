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
my_label.grid(column=0,row=0)


# Button


button1 = tkinter.Button(text="button1", command=on_button_click)
button1.grid(column=1,row=1)


buttomn2=tkinter.Button(text="button2")
buttomn2.grid(column=2,row=0)
# Input
inp = tkinter.Entry()
inp.grid(column=4,row=3)


window.mainloop()
