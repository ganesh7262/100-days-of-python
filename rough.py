import tkinter


window=tkinter.Tk()
window.title("First GUI program")
window.minsize(width=600,height=600)

# Label
my_label=tkinter.Label(text="My first Tkinter Label",font=("Arial",20,"bold"))
my_label.pack(side="left")



window.mainloop()