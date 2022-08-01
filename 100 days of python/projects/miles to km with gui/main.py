import tkinter


window=tkinter.Tk()
window.minsize(width=300,height=300)
window.title("Miles to KM convertor")
window.config(padx=100,pady=100)
# Conversion function

def convert():
    mile=inp.get()
    km=1.6*int(mile)
    l4.config(text=f"{km}")
    


# Input

inp=tkinter.Entry()
inp.grid(column=1,row=0)

# Labels

l1=tkinter.Label(text="Miles")
l1.grid(column=2,row=0)
l1.config(padx=20)

l2=tkinter.Label(text="is equal to")
l2.grid(column=0,row=1)

l3=tkinter.Label(text="Km")
l3.grid(column=2,row=1)

l4=tkinter.Label(text="0")
l4.grid(column=1,row=1)


# Button

button=tkinter.Button(text="Convert",command=convert)
button.grid(column=1,row=2)










window.mainloop()