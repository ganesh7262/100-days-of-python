from tkinter import *
import requests


def get_quote():
    response=requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    quote=response.json()['quote']
    canvas.itemconfig(quote_text,text=quote)
    



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\ISS overhead notifier\kanye_quotes_challenge\background.png')
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="click kanye to get quote....", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\ISS overhead notifier\kanye_quotes_challenge\kanye.png')
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()