BACKGROUND_COLOR = "#B1DDC6"

from random import choice
import pandas as pd
import tkinter
cur_card={}
# --------------------Data-------------------#

data=pd.read_csv(filepath_or_buffer=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\capstone flash card\data\french_words.csv')
to_learn=data.to_dict(orient='records')

# ----------------functions------------#
def display_rand_frenchword():
    global flip_timer,cur_card
    window.after_cancel(flip_timer)
    cur_card=choice(to_learn)
    rand_french=cur_card["French"]
    canvas.itemconfig(front_img,image=card_front)
    canvas.itemconfig(Title,text="French",fill='black')
    canvas.itemconfig(word,text=rand_french,fill='black')
    flip_timer=canvas.after(3000,change_card)

def change_card():
    canvas.itemconfig(front_img,image=card_back)
    canvas.itemconfig(Title,text="English",fill='white')
    canvas.itemconfig(word,text=cur_card["English"],fill='white')

def is_know():
    to_learn.remove(cur_card)
    need_to_learn=pd.DataFrame(to_learn)
    try:
        need_to_learn.to_csv(path_or_buf=r"C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\capstone flash card\data\need_to_learn.csv")
    except FileNotFoundError:
        pass
    display_rand_frenchword()

# -----------------------UI-----------------------------#
window=tkinter.Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,change_card)

# ---images---#
card_back=tkinter.PhotoImage(file=r"C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\capstone flash card\images\card_back.png")
card_front=tkinter.PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\capstone flash card\images\card_front.png')
right_img=tkinter.PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\capstone flash card\images\right.png')
wrong_img=tkinter.PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\capstone flash card\images\wrong.png')

# --------canvas--#
canvas=tkinter.Canvas(width=800,height=526)
front_img=canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
Title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,260,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)




# ------Button-----#
wrong_button=tkinter.Button(image=wrong_img,highlightthickness=0,command=display_rand_frenchword)
wrong_button.grid(row=1,column=0)

right_button=tkinter.Button(image=right_img,highlightthickness=0,command=is_know)
right_button.grid(row=1,column=1)




display_rand_frenchword()







window.mainloop()