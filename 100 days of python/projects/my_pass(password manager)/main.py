from random import choice
import tkinter
import string
from tkinter import END, Button, messagebox
import json

FONT=("Ariel",10,"bold")
global rand_pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    
    set_of_char=string.ascii_letters + string.digits
    global rand_pass
    rand_pass=''.join([choice(set_of_char) for i in range(9)])
    password_inp.insert(0,rand_pass)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_values():
    return website_inp.get(),email_username_inp.get(),rand_pass

def add():
    web,email_u,pas=get_values()

    new_data={
        web:{
            'email':email_u,
            'password':pas
        }
    }

    if len(web)==0 or len(pas)==0:
        messagebox.showinfo(title='Oops',message='Please make sure you havent left any fields emmpty')
    else:
        try:
            with open('data.json','r') as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open('data.json','w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_inp.delete(0,END)
            password_inp.delete(0,END)
        
def search_pass():
    req_web=website_inp.get()
    with open('data.json') as data_file:
        data=json.load(data_file)
        if req_web in data.keys():
            password_inp.insert(0,data[req_web]["password"])
        else:
            messagebox.showinfo(title='Oops',message="No data of given website availabe")

# ---------------------------- UI SETUP ------------------------------- #

window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)

logo_img=tkinter.PhotoImage(file=r"C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\my_pass(password manager)\logo.png")
canvas=tkinter.Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=tkinter.Label(text="Website: ",font=FONT)
website_label.grid(row=1,column=0)

website_inp=tkinter.Entry(width=30)
website_inp.grid(row=1,column=1)
website_label.config(pady=5)
website_inp.focus()

email_username_label=tkinter.Label(text="Email/Username: ", font=FONT)
email_username_label.grid(row=3,column=0,pady=5)

email_username_inp=tkinter.Entry(width=40)
email_username_inp.insert(0,"ganeshshinde@gmail.com")
email_username_inp.grid(row=3,column=1,columnspan=2)

password_label=tkinter.Label(text="Password: ",font=FONT)
password_label.grid(row=4,column=0,pady=5)

password_inp=tkinter.Entry(width=30)
password_inp.grid(row=4,column=1)


generate_button=tkinter.Button(text="Generate",command=password_gen)
generate_button.grid(row=4,column=2)

search_button=Button(text='Search',command=search_pass)
search_button.grid(row=1,column=2)

add_button=tkinter.Button(text='Add',width=35,command=add)
add_button.grid(row=5,column=1,columnspan=2)

window.mainloop()